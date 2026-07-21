#!/usr/bin/env python3
"""Build NFHS district-explorer assets: projected SVG geometry + district data.
Sources (cloned in scratchpad/nfhs-src):
  saik/India.csv                 IIPS NFHS-4/5 district factsheet compilation
  maps/geojson/india.geojson     2011-census district boundaries (udit-001/india-maps-data)
Outputs -> repo data/nfhs/
"""
import json, csv, collections, re, difflib, sys, os

SRC = "/tmp/claude-0/-home-user-ImpactMojo/ca887b3f-2cee-5895-ae94-988cdf63214a/scratchpad/nfhs-src"
OUT = "/home/user/ImpactMojo/data/nfhs"
os.makedirs(OUT, exist_ok=True)

SYN = [('pashchimi','west'),('pashchim','west'),('paschim','west'),('purba','east'),('purbi','east'),
       ('uttar','north'),('dakshin','south'),('madhya','central'),('purvi','east'),('poorvi','east')]
def nrm(s):
    s=(s or '').lower(); s=re.sub(r'\(.*?\)','',s); s=s.replace('&','and')
    s=re.sub(r'[^a-z0-9]','',s); s=s.replace('district','')
    for a,b in SYN: s=s.replace(a,b)
    return s
def nstate(s):
    # NOTE: state names must NOT go through the district SYN table (which maps
    # uttar->north, madhya->central etc.) or "Uttar Pradesh" -> "northpradesh".
    s=(s or '').lower(); s=re.sub(r'\(.*?\)','',s); s=s.replace('&','and'); s=re.sub(r'[^a-z0-9]','',s)
    s=s.replace('nctof','').replace('nct','').replace('islands','island').replace('orissa','odisha')
    s=s.replace('uttaranchal','uttarakhand').replace('pondicherry','puducherry')
    # merge the two NFHS UTs onto the combined geometry state
    if s in ('damananddiu','dadraandnagarhaveli'): s='dadraandnagarhavelianddamananddiu'
    return s

# --- explicit renamings a fuzzy matcher gets wrong (NFHS name -> geometry name), by norm(state) ---
ALIAS = {
 'uttarpradesh': {'faizabad':'Ayodhya','jyotibaphulenagar':'Amroha','kanshiramnagar':'Kasganj',
    'mahamayanagar':'Hathras','santravidasnagar':'Bhadohi','kheri':'Lakhimpur Kheri','mahrajganj':'Maharajganj'},
 'karnataka': {'bangalore':'Bengaluru Urban','bangalorerural':'Bengaluru Rural','gulbarga':'Kalaburagi',
    'mysore':'Mysuru','bellary':'Ballari','bijapur':'Vijayapura','belgaum':'Belagavi','shimoga':'Shivamogga',
    'tumkur':'Tumakuru','bagalkot':'Bagalkote','chikmagalur':'Chikkamagaluru','chamarajanagar':'Chamarajanagara'},
 'haryana': {'mewat':'Nuh','gurgaon':'Gurugram','dadri':'Charkhi Dadri'},
 'westbengal': {'haora':'Howrah','hugli':'Hooghly','kochbihar':'Cooch Behar','maldah':'Malda',
    'northtwentyfourparganas':'North 24 Parganas','southtwentyfourparganas':'South 24 Parganas',
    'puruliya':'Purulia','paschimbarddhaman':'Paschim Bardhaman'},
 'odisha': {'anugul':'Angul','baleshwar':'Balasore','baudh':'Boudh','debagarh':'Deogarh',
    'jagatsinghapur':'Jagatsinghpur','jajapur':'Jajpur'},
 'gujarat': {'aravali':'Aravalli','kachchh':'Kutch','mahesana':'Mehsana','thedangs':'Dang'},
 'punjab': {'firozpur':'Ferozepur','gurudaspur':'Gurdaspur','muktsar':'Sri Muktsar Sahib',
    'sahibzadaajitsinghnagar':'S.A.S. Nagar'},  # SAS Nagar = Mohali (kept distinct from Nawanshahr)
 'rajasthan': {'chittaurgarh':'Chittorgarh','dhaulpur':'Dholpur','jalor':'Jalore'},
 'maharashtra': {'bid':'Beed','buldana':'Buldhana','gondiya':'Gondia','raigarh':'Raigad'},
 'jammuandkashmir': {'badgam':'Budgam','bandipore':'Bandipora','baramula':'Baramulla','shupiyan':'Shopiyan'},
 'himachalpradesh': {'lahulandspiti':'Lahaul and Spiti'},
 'jharkhand': {'kodarma':'Koderma'},
 'madhyapradesh': {'narsimhapur':'Narsinghpur'},
 'chhattisgarh': {'dantewada':'Dakshin Bastar Dantewada'},
 'tamilnadu': {'kanniyakumari':'Kanyakumari','thenilgiris':'Nilgiris'},
 'sikkim': {'east':'East Sikkim','north':'North Sikkim','south':'South Sikkim','west':'West Sikkim'},
 'telangana': {'jangoan':'Jangaon','komarambheemasifabad':'Komaram Bheem'},
 'tripura': {'unakoti':'Unokoti'},
 'andamanandnicobarisland': {'nicobar':'Nicobars'},
 'arunachalpradesh': {'dibangvalley':'Lower Dibang Valley'},  # NFHS old undivided ~ lower valley bulk
 'andhrapradesh': {'sripottisriramulunellore':'S.P.S. Nellore','ysr':'Y.S.R. Kadapa'},
 'dadraandnagarhavelianddamananddiu': {'dadraandnagarhaveli':'Dadra and Nagar Haveli','daman':'Daman','diu':'Diu'},
}
DROP = {('jammuandkashmir','datanotavailable')}          # junk row
# districts with no separate polygon in this boundary set -> data views only, not the map
NO_POLYGON_NOTE = {('maharashtra','mumbaisuburban')}

# ---------- load geometry ----------
geo = json.load(open(f"{SRC}/maps/geojson/india.geojson"))
gidx = {}                       # (nstate, ndist) -> feature
gnames = collections.defaultdict(list)
for f in geo['features']:
    p=f['properties']
    if not p.get('district') or not p.get('st_nm'): continue
    st=nstate(p['st_nm']); dn=nrm(p['district'])
    gidx[(st,dn)] = f; gnames[st].append(p['district'])

# ---------- load NFHS ----------
with open(f"{SRC}/saik/India.csv",encoding='utf-8',errors='replace') as fh:
    rows=list(csv.DictReader(fh))
def gv(r,k): return (r.get(k) or r.get('﻿'+k) or '').strip()

# district registry + long values
districts=collections.OrderedDict()   # dkey -> {state,district,geokey or None}
IND=collections.OrderedDict()         # indicator name -> {cat}
vals=collections.defaultdict(dict)    # dkey -> {ind: [n5,n4]}
def num(x):
    x=(x or '').strip()
    if x in ('','NA','na','*','-','('): return None
    try: return float(x)
    except:
        m=re.match(r'-?\d+(\.\d+)?', x);
        return float(m.group()) if m else None

for r in rows:
    st_raw=gv(r,'State'); d_raw=gv(r,'District')
    dkey=(st_raw, d_raw)
    if dkey not in districts:
        districts[dkey]={'state':st_raw,'district':d_raw}
    cat=gv(r,'Category'); ind=gv(r,'Indicator')
    if ind and ind not in IND: IND[ind]={'cat':cat}
    n5=num(gv(r,'NFHS 5')); n4=num(gv(r,'NFHS 4'))
    vals[dkey][ind]=[n5,n4]

# ---------- resolve each NFHS district to geometry ----------
report=[]; matched=0; nogeo=[]
for dkey,meta in districts.items():
    st=nstate(meta['state']); dn=nrm(meta['district'])
    if (st,dn) in DROP:
        meta['geokey']='__DROP__'; continue
    gk=None; how=''
    if (st,dn) in gidx: gk=(st,dn); how='exact'
    elif st in ALIAS and dn in ALIAS[st]:
        cand=nrm(ALIAS[st][dn])
        if (st,cand) in gidx: gk=(st,cand); how='alias'
        else: how='ALIAS-BROKEN:'+ALIAS[st][dn]
    if gk is None and (st,dn) not in NO_POLYGON_NOTE:
        # high-threshold fuzzy for safe spelling variants only
        cands=[nrm(x) for x in gnames.get(st,[])]
        best=difflib.get_close_matches(dn,cands,n=1,cutoff=0.86)
        if best: gk=(st,best[0]); how='fuzzy'
    if gk:
        meta['geokey']=gk; matched+=1
        if how!='exact': report.append(f"  [{how}] {meta['state'][:14]:14} {meta['district'][:24]:24} -> {gidx[gk]['properties']['district']}")
    else:
        meta['geokey']=None; nogeo.append((meta['state'],meta['district']))

print("NON-EXACT MATCHES (verify each):")
print("\n".join(report))
print(f"\nTOTAL NFHS districts: {len(districts)} | mapped to polygon: {matched} | no-polygon (table-only): {len(nogeo)}")
print("NO-POLYGON districts:", "; ".join(f"{s}/{d}" for s,d in nogeo))

# stop here for review unless --emit given
if '--emit' not in sys.argv:
    print("\n(dry run — pass --emit to write assets)"); sys.exit(0)

import math
# ---------- indicator direction / headline classification ----------
LOWER_BETTER = ['stunted','wasted','underweight','overweight','anaemi','anemia','mortality','died',
  'married before age 18','who were already mothers','teenage','tobacco','alcohol','blood sugar','hypertension',
  'below age 15','unmet need','diarrhoea','symptoms of ari','high or very high','total unmet']
HIGHER_BETTER = ['literate','schooling','ever attended school','institutional','delivery in','immuniz','vaccinat',
  'received','electricity','improved drinking','improved sanitation','clean fuel','iodized','health insurance',
  'registered','breastfed','antenatal','folic','skilled','bank','money that they themselves','hygienic method',
  'preprimary','protecting against','four or more antenatal','postnatal','deworming','vitamin a','iron']
def direction(name):
    n=name.lower()
    for k in LOWER_BETTER:
        if k in n: return -1
    for k in HIGHER_BETTER:
        if k in n: return 1
    return 0
HEADLINE = [   # ordered hero set for the "change since NFHS-4" story (substring match, first hit wins)
  'children under 5 years who are stunted',
  'children under 5 years who are wasted (weight for height)',
  'children under 5 years who are underweight',
  'children age 6-59 months who are anaemic',
  'all women age 15-49 years who are anaemic',
  'institutional births',
  'children age 12-23 months fully vaccinated based on information from either',
  'women who are literate',
  'women age 2024 years married before age 18 years',
  'population living in households that use an improved sanitation facili',
  'households using clean fuel for cooking',
  'households with any usual member covered under a health insurance',
]
def unit_of(name):
    n=name.lower()
    if 'per 1,000' in n or 'sex ratio' in n or 'females per' in n: return 'ratio'
    if '%' in name: return '%'
    return ''

catalog=[]
name2id={}
for i,(nm,meta) in enumerate(IND.items()):
    name2id[nm]=i
    catalog.append({'id':i,'name':nm,'cat':meta['cat'],'dir':direction(nm),'unit':unit_of(nm)})
# mark headline + order
hero=[]
for h in HEADLINE:
    for nm,i in name2id.items():
        if h in nm.lower(): hero.append(i); catalog[i]['hero']=1; break
print("hero indicators resolved:",len(hero),"/",len(HEADLINE))

# ---------- projection ----------
def coords_iter(geom):
    t=geom['type']; c=geom['coordinates']
    if t=='Polygon': return [c]
    if t=='MultiPolygon': return c
    return []
# bbox over matched polygons
minx=miny=1e9; maxx=maxy=-1e9
usedfeat={}
for dkey,meta in districts.items():
    gk=meta.get('geokey')
    if not gk or gk=='__DROP__' or gk not in gidx: continue
    usedfeat[gk]=gidx[gk]
for f in usedfeat.values():
    for poly in coords_iter(f['geometry']):
        for ring in poly:
            for x,y in ring:
                minx=min(minx,x);maxx=max(maxx,x);miny=min(miny,y);maxy=max(maxy,y)
midlat=math.radians((miny+maxy)/2); kx=math.cos(midlat)
W=1000.0
sx=W/((maxx-minx)*kx);
H=(maxy-miny)*sx
def proj(x,y): return ((x-minx)*kx*sx, (maxy-y)*sx)
def dp(points,tol):
    if len(points)<3: return points
    dmax=0;idx=0;a=points[0];b=points[-1]
    for i in range(1,len(points)-1):
        px,py=points[i];x1,y1=a;x2,y2=b
        dx,dy=x2-x1,y2-y1;den=dx*dx+dy*dy
        if den==0: d=math.hypot(px-x1,py-y1)
        else:
            t=((px-x1)*dx+(py-y1)*dy)/den;t=max(0,min(1,t))
            d=math.hypot(px-(x1+t*dx),py-(y1+t*dy))
        if d>dmax: dmax=d;idx=i
    if dmax>tol:
        return dp(points[:idx+1],tol)[:-1]+dp(points[idx:],tol)
    return [a,b]
def ring_path(ring):
    pts=[proj(x,y) for x,y in ring]
    pts=dp(pts,0.6)
    if len(pts)<3: return ''
    out=['M%.1f %.1f'%pts[0]]
    for p in pts[1:]: out.append('L%.1f %.1f'%p)
    out.append('Z');return ''.join(out)
geo_out={}
for gk,f in usedfeat.items():
    parts=[]
    for poly in coords_iter(f['geometry']):
        for ring in poly:
            p=ring_path(ring)
            if p: parts.append(p)
    geo_out['%s|%s'%gk]=''.join(parts)

# ---------- data ----------
def r1(v): return None if v is None else round(v,1)
data_out={}
for dkey,meta in districts.items():
    gk=meta.get('geokey')
    if gk=='__DROP__': continue
    mapkey=('%s|%s'%gk) if (gk and gk in usedfeat) else None
    v=[]
    for c in catalog:
        pair=vals[dkey].get(c['name'],[None,None])
        v.append([r1(pair[0]),r1(pair[1])])
    data_out['%s||%s'%(meta['state'],meta['district'])]={'s':meta['state'],'d':meta['district'],'m':mapkey,'v':v}

geojson={'vb':[round(W,1),round(H,1)],'d':geo_out}
payload={'meta':{'source':'IIPS/MoHFW NFHS-4 (2015-16) & NFHS-5 (2019-21) district fact sheets, rchiips.org',
                 'geometry':'2011 Census district boundaries (udit-001/india-maps-data, CC-BY)',
                 'districts':len(data_out),'mapped':len(geo_out),'indicators':len(catalog)},
         'catalog':catalog,'hero':hero,'data':data_out}
json.dump(geojson,open(f"{OUT}/india-districts-geo.json",'w'),separators=(',',':'))
json.dump(payload,open(f"{OUT}/nfhs-districts.json",'w'),separators=(',',':'))
print("viewBox: %.0f x %.0f"%(W,H))
for fn in ['india-districts-geo.json','nfhs-districts.json']:
    print("  %s : %.0f KB"%(fn, os.path.getsize(f"{OUT}/{fn}")/1024))

