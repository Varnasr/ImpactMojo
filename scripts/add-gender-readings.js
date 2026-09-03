#!/usr/bin/env node
/**
 * Add "Further Reading" sections to gender course modules in Supabase.
 * Appends a styled reading list to each module's content_html.
 *
 * Usage: SUPABASE_SERVICE_KEY=... node scripts/add-gender-readings.js
 */

const SERVICE_KEY = process.env.SUPABASE_SERVICE_KEY || process.env.SUPABASE_PAT;
if (!SERVICE_KEY) { console.error('Set SUPABASE_SERVICE_KEY'); process.exit(1); }

const SUPABASE_URL = 'https://ddyszmfffyedolkcugld.supabase.co';

const READINGS = {
  1: [
    { author: 'Oakley, Ann', year: 1972, title: 'Sex, Gender and Society', pub: 'Temple Smith / Routledge', access: '' },
    { author: 'Butler, Judith', year: 1990, title: 'Gender Trouble: Feminism and the Subversion of Identity', pub: 'Routledge', access: '' },
    { author: 'Connell, R.W.', year: 1995, title: 'Masculinities', pub: 'Polity Press', note: 'Chapter 3: The Body and Social Practice' },
    { author: 'Connell, R.W. & Messerschmidt, James W.', year: 2005, title: 'Hegemonic Masculinity: Rethinking the Concept', pub: 'Gender & Society, 19(6), 829\u2013859', access: 'https://www.jstor.org/stable/27640853' },
  ],
  2: [
    { author: 'Federici, Silvia', year: 2004, title: 'Caliban and the Witch: Women, the Body and Primitive Accumulation', pub: 'Autonomedia', access: '', note: 'Open Access PDF available' },
    { author: 'hooks, bell', year: 1984, title: 'Feminist Theory: From Margin to Center', pub: 'South End Press' },
    { author: 'Mohanty, Chandra Talpade', year: 1988, title: 'Under Western Eyes: Feminist Scholarship and Colonial Discourses', pub: 'Feminist Review, 30, 61\u201388', access: 'https://www.jstor.org/stable/1395054' },
    { author: 'Crenshaw, Kimberl\u00e9', year: 1989, title: 'Demarginalizing the Intersection of Race and Sex', pub: 'University of Chicago Legal Forum, 1989(1)', access: 'https://chicagounbound.uchicago.edu/uclf/vol1989/iss1/8/' },
  ],
  3: [
    { author: 'Crenshaw, Kimberl\u00e9', year: 1991, title: 'Mapping the Margins: Intersectionality, Identity Politics, and Violence Against Women of Color', pub: 'Stanford Law Review, 43(6), 1241\u20131299', access: 'https://www.jstor.org/stable/1229039' },
    { author: 'Rege, Sharmila', year: 1998, title: 'Dalit Women Talk Differently: A Critique of \u2018Difference\u2019 and Towards a Dalit Feminist Standpoint Position', pub: 'Economic and Political Weekly, 33(44), WS39\u2013WS46', access: 'https://www.jstor.org/stable/4407323' },
    { author: 'Guru, Gopal', year: 1995, title: 'Dalit Women Talk Differently', pub: 'Economic and Political Weekly, 30(41/42), 2548\u20132550', access: 'https://www.jstor.org/stable/4403327' },
  ],
  4: [
    { author: 'Agarwal, Bina', year: 1994, title: 'A Field of One\u2019s Own: Gender and Land Rights in South Asia', pub: 'Cambridge University Press' },
    { author: 'Kabeer, Naila', year: 1999, title: 'Resources, Agency, Achievements: Reflections on the Measurement of Women\u2019s Empowerment', pub: 'Development and Change, 30(3), 435\u2013464' },
    { author: 'Agarwal, Bina', year: 1997, title: '\u2018Bargaining\u2019 and Gender Relations: Within and Beyond the Household', pub: 'Feminist Economics, 3(1), 1\u201351' },
    { author: 'Kabeer, Naila', year: 1994, title: 'Reversed Realities: Gender Hierarchies in Development Thought', pub: 'Verso' },
  ],
  5: [
    { author: 'Federici, Silvia', year: 2012, title: 'Revolution at Point Zero: Housework, Reproduction, and Feminist Struggle', pub: 'PM Press' },
    { author: 'Razavi, Shahra', year: 2007, title: 'The Political and Social Economy of Care in a Development Context', pub: 'UNRISD Gender and Development Programme Paper No. 3', note: 'Open Access' },
    { author: 'Bhattacharya, Tithi (ed.)', year: 2017, title: 'Social Reproduction Theory: Remapping Class, Recentering Oppression', pub: 'Pluto Press' },
  ],
  6: [
    { author: 'Chatterjee, Urmila, Murgai, Rinku & Rama, Martin', year: 2015, title: 'Job Opportunities along the Rural-Urban Gradation and Female Labor Force Participation in India', pub: 'World Bank Policy Research WP 7412', note: 'Open Access' },
    { author: 'Klasen, Stephan & Pieters, Janneke', year: 2015, title: 'What Explains the Stagnation of Female Labor Force Participation in Urban India?', pub: 'World Bank Economic Review, 29(3), 449\u2013478' },
    { author: 'ILO', year: 2018, title: 'India Wage Report: Wage Policies for Decent Work and Inclusive Growth', pub: 'International Labour Organization', note: 'Open Access' },
  ],
  7: [
    { author: 'Agnes, Flavia', year: 1999, title: 'Law and Gender Inequality: The Politics of Women\u2019s Rights in India', pub: 'Oxford University Press' },
    { author: 'Agnes, Flavia', year: 2011, title: 'Family Law I: Family Laws and Constitutional Claims', pub: 'Oxford University Press' },
    { author: 'Parashar, Archana', year: 1992, title: 'Women and Family Law Reform in India: Uniform Civil Code and Gender Equality', pub: 'Sage Publications' },
  ],
  8: [
    { author: 'Baxi, Pratiksha', year: 2014, title: 'Public Secrets of Law: Rape Trials in India', pub: 'Oxford University Press' },
    { author: 'Supreme Court of India', year: 1997, title: 'Vishaka v. State of Rajasthan, AIR 1997 SC 3011', pub: '', access: 'https://indiankanoon.org/doc/1031794/', note: 'Full text' },
    { author: 'Patel, Vibhuti', year: 2013, title: 'Campaign Against Sexual Harassment at the Workplace', pub: 'Economic and Political Weekly, 48(10)' },
  ],
  9: [
    { author: 'Chattopadhyay, Raghabendra & Duflo, Esther', year: 2004, title: 'Women as Policy Makers: Evidence from a Randomized Policy Experiment in India', pub: 'Econometrica, 72(5), 1409\u20131443', access: 'https://economics.mit.edu/files/792', note: 'Open Access via MIT' },
    { author: 'Rai, Shirin M.', year: 2002, title: 'Class, Caste and Gender \u2014 Women in Parliament in India', pub: 'International IDEA', note: 'Open Access' },
    { author: 'Kudva, Neema', year: 2003, title: 'Engineering Elections: The Experiences of Women in Panchayati Raj in Karnataka', pub: 'International Journal of Politics, Culture, and Society, 16(3), 445\u2013463' },
  ],
  10: [
    { author: 'Kumar, Radha', year: 1993, title: 'The History of Doing: An Illustrated Account of Movements for Women\u2019s Rights and Feminism in India, 1800\u20131990', pub: 'Kali for Women / Zubaan' },
    { author: 'Menon, Nivedita', year: 2004, title: 'Recovering Subversion: Feminist Politics Beyond the Law', pub: 'Permanent Black' },
    { author: 'Basu, Amrita (ed.)', year: 2010, title: 'Women\u2019s Movements in the Global Era: The Power of Local Feminisms', pub: 'Westview Press' },
  ],
  11: [
    { author: 'Chakravarti, Uma', year: 1993, title: 'Conceptualising Brahmanical Patriarchy in Early India: Gender, Caste, Class and State', pub: 'Economic and Political Weekly, 28(14), 579\u2013585', access: 'https://www.jstor.org/stable/4399556' },
    { author: 'Rege, Sharmila', year: 2006, title: 'Writing Caste/Writing Gender: Narrating Dalit Women\u2019s Testimonios', pub: 'Zubaan' },
    { author: 'Ambedkar, B.R.', year: 1916, title: 'Castes in India: Their Mechanism, Genesis and Development', pub: 'Paper, Columbia University', access: 'https://www.columbia.edu/itc/mealac/pritchett/00ambedkar/txt_ambedkar_castes.html', note: 'Open Access' },
  ],
  12: [
    { author: 'Connell, R.W.', year: 1995, title: 'Masculinities', pub: 'Polity Press' },
    { author: 'Supreme Court of India', year: 2014, title: 'NALSA v. Union of India, (2014) 5 SCC 438', pub: '', access: 'https://indiankanoon.org/doc/193543132/', note: 'Full text' },
    { author: 'Reddy, Gayatri', year: 2005, title: 'With Respect to Sex: Negotiating Hijra Identity in South India', pub: 'University of Chicago Press' },
  ],
  13: [
    { author: 'Moser, Caroline O.N.', year: 1993, title: 'Gender Planning and Development: Theory, Practice and Training', pub: 'Routledge' },
    { author: 'Razavi, Shahra & Miller, Carol', year: 1995, title: 'From WID to GAD: Conceptual Shifts in the Women and Development Discourse', pub: 'UNRISD Occasional Paper No. 1', note: 'Open Access' },
    { author: 'Kabeer, Naila', year: 2005, title: 'Gender Equality and Women\u2019s Empowerment: A Critical Analysis of the Third MDG', pub: 'Gender & Development, 13(1), 13\u201324' },
  ],
  14: [
    { author: 'Gurumurthy, Anita & Chami, Nandini', year: 2014, title: 'Gender Equality in the Information Society', pub: 'IT for Change', note: 'Open Access' },
    { author: 'Kovacs, Anja, Padte, Richa & Shobha SV', year: 2013, title: 'Don\u2019t Let It Stand! An Exploratory Study of Women and Verbal Online Abuse in India', pub: 'Internet Democracy Project', note: 'Open Access' },
  ],
  15: [
    { author: 'Kabeer, Naila', year: 2000, title: 'The Power to Choose: Bangladeshi Women and Labour Market Decisions in London and Dhaka', pub: 'Verso' },
    { author: 'Mumtaz, Khawar & Shaheed, Farida', year: 1987, title: 'Women of Pakistan: Two Steps Forward, One Step Back?', pub: 'Zed Books' },
    { author: 'Jayawardena, Kumari', year: 1986, title: 'Feminism and Nationalism in the Third World', pub: 'Zed Books' },
  ],
  16: [
    { author: 'Menon, Nivedita', year: 2012, title: 'Seeing Like a Feminist', pub: 'Zubaan / Penguin India' },
    { author: 'John, Mary E. (ed.)', year: 2008, title: 'Women\u2019s Studies in India: A Reader', pub: 'Penguin India' },
    { author: 'Batliwala, Srilatha', year: 1994, title: 'The Meaning of Women\u2019s Empowerment: New Concepts from Action', pub: 'In Sen, Germain & Chen (eds.), Population Policies Reconsidered, Harvard', note: 'Open Access via Harvard' },
  ],
};

function buildReadingHTML(moduleNum) {
  const refs = READINGS[moduleNum];
  if (!refs || refs.length === 0) return '';

  let html = `
            <div class="reading-list-section" style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-secondary, rgba(99,102,241,0.05)); border-radius: 12px; border: 1px solid var(--border-color, rgba(99,102,241,0.15));">
                <h4 style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem; font-family: 'Inter', sans-serif; color: var(--text-primary);">
                    <img src="https://cdn.jsdelivr.net/npm/sargam-icons@1.6.7/Icons/Line/si_Book.svg" alt="" style="width: 20px; height: 20px; opacity: 0.7;">
                    Further Reading
                </h4>
                <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.75rem;">`;

  for (const ref of refs) {
    const titlePart = ref.access
      ? `<a href="${ref.access}" target="_blank" rel="noopener" style="color: var(--accent, #7C3AED); text-decoration: none;">${ref.title}</a>`
      : `<em>${ref.title}</em>`;
    const notePart = ref.note ? ` <span style="font-size: 0.75rem; color: var(--text-muted, #94A3B8); background: rgba(99,102,241,0.08); padding: 0.1rem 0.4rem; border-radius: 4px;">${ref.note}</span>` : '';
    const pubPart = ref.pub ? ` ${ref.pub}.` : '';

    html += `
                    <li style="font-size: 0.9rem; line-height: 1.6; color: var(--text-secondary, #94A3B8); padding-left: 0;">
                        ${ref.author} (${ref.year}). ${titlePart}.${pubPart}${notePart}
                    </li>`;
  }

  html += `
                </ul>
            </div>`;
  return html;
}

async function main() {
  // Get service role key if SUPABASE_PAT was provided
  let serviceKey = SERVICE_KEY;

  // First, fetch all gender modules
  const listRes = await fetch(
    `${SUPABASE_URL}/rest/v1/course_content?course_id=eq.gender&select=id,module_number,content_html&order=module_number`,
    { headers: { 'apikey': serviceKey, 'Authorization': `Bearer ${serviceKey}` } }
  );
  const modules = await listRes.json();

  if (!Array.isArray(modules)) {
    console.error('Failed to fetch modules:', modules);
    process.exit(1);
  }

  console.log(`Found ${modules.length} gender modules`);

  for (const mod of modules) {
    const readingHTML = buildReadingHTML(mod.module_number);
    if (!readingHTML) {
      console.log(`  M${mod.module_number}: no readings defined, skipping`);
      continue;
    }

    // Check if already has Further Reading
    if (mod.content_html && mod.content_html.includes('Further Reading')) {
      console.log(`  M${mod.module_number}: already has Further Reading, skipping`);
      continue;
    }

    const newContent = (mod.content_html || '') + readingHTML;

    const updateRes = await fetch(
      `${SUPABASE_URL}/rest/v1/course_content?id=eq.${mod.id}`,
      {
        method: 'PATCH',
        headers: {
          'apikey': serviceKey,
          'Authorization': `Bearer ${serviceKey}`,
          'Content-Type': 'application/json',
          'Prefer': 'return=minimal',
        },
        body: JSON.stringify({ content_html: newContent }),
      }
    );

    if (updateRes.ok) {
      console.log(`  M${mod.module_number}: added ${READINGS[mod.module_number].length} readings`);
    } else {
      const err = await updateRes.text();
      console.error(`  M${mod.module_number}: ERROR ${updateRes.status} - ${err}`);
    }
  }

  console.log('\nDone!');
}

main().catch(console.error);
