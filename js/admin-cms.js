/**
 * ImpactMojo Admin CMS
 * Version: 1.0.0
 * Date: March 16, 2026
 *
 * JSON-based CMS that reads/writes to the Supabase `site_content` table.
 * Each row represents a named content section (e.g. "hero", "courses",
 * "testimonials") with a JSON `content` column.
 *
 * TABLE SCHEMA (create in Supabase SQL editor):
 *
 *   CREATE TABLE IF NOT EXISTS site_content (
 *       id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
 *       section_key TEXT UNIQUE NOT NULL,
 *       label TEXT NOT NULL,
 *       content JSONB NOT NULL DEFAULT '{}',
 *       schema JSONB DEFAULT NULL,
 *       updated_at TIMESTAMPTZ DEFAULT now(),
 *       updated_by UUID REFERENCES auth.users(id)
 *   );
 *
 *   -- RLS: anyone can read, only admins can write
 *   ALTER TABLE site_content ENABLE ROW LEVEL SECURITY;
 *
 *   CREATE POLICY "Public read" ON site_content
 *       FOR SELECT USING (true);
 *
 *   CREATE POLICY "Admin write" ON site_content
 *       FOR ALL USING (
 *           EXISTS (
 *               SELECT 1 FROM profiles
 *               WHERE profiles.id = auth.uid()
 *               AND profiles.role = 'admin'
 *           )
 *       );
 *
 *   -- Add role column to profiles if not exists
 *   ALTER TABLE profiles ADD COLUMN IF NOT EXISTS role TEXT DEFAULT 'user';
 *
 * PREREQUISITES:
 *   <script src="js/config.js"></script>
 *   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
 *   <script src="js/auth.js"></script>
 *   <script src="js/admin-gate.js"></script>
 *   <script src="js/admin-cms.js"></script>
 */

(function () {
  'use strict';

  // =========================================================================
  // DEFAULT SECTION DEFINITIONS
  // These define which sections are manageable and their JSON schemas
  // =========================================================================

  var SECTIONS = [
    {
      key: 'hero',
      label: 'Homepage Hero',
      description: 'Main hero section on the homepage — headline, subtext, CTA buttons.',
      defaultContent: {
        headline: 'Learn Impact. Build Change.',
        subtext: 'Free courses, tools, and resources for monitoring, evaluation, and learning professionals.',
        cta_primary: { text: 'Explore Courses', link: '/catalog.html' },
        cta_secondary: { text: 'Browse Tools', link: '/dataverse.html' }
      },
      fields: [
        { key: 'headline', label: 'Headline', type: 'text' },
        { key: 'subtext', label: 'Subtext', type: 'textarea' },
        { key: 'cta_primary.text', label: 'Primary CTA Text', type: 'text' },
        { key: 'cta_primary.link', label: 'Primary CTA Link', type: 'text' },
        { key: 'cta_secondary.text', label: 'Secondary CTA Text', type: 'text' },
        { key: 'cta_secondary.link', label: 'Secondary CTA Link', type: 'text' }
      ]
    },
    {
      key: 'courses',
      label: 'Course Catalog',
      description: 'All courses displayed on the catalog page. Each entry has title, type, track, level, and link.',
      defaultContent: { DATA: [] },
      fields: null, // Array editor — uses JSON mode
      isArray: true,
      arrayKey: 'DATA',
      arrayFields: [
        { key: 'title', label: 'Title', type: 'text' },
        { key: 'type', label: 'Type', type: 'select', options: ['Flagship', 'Core', 'Supplementary', 'Elective'] },
        { key: 'track', label: 'Track', type: 'text' },
        { key: 'level', label: 'Level', type: 'select', options: ['Beginner', 'Intermediate', 'Advanced'] },
        { key: 'link', label: 'Link', type: 'text' }
      ]
    },
    {
      key: 'games',
      label: 'Games & Simulations',
      description: 'Interactive games and simulations listed on the platform.',
      defaultContent: { DATA: [] },
      isArray: true,
      arrayKey: 'DATA',
      arrayFields: [
        { key: 'title', label: 'Title', type: 'text' },
        { key: 'description', label: 'Description', type: 'textarea' },
        { key: 'category', label: 'Category', type: 'text' },
        { key: 'link', label: 'Link', type: 'text' }
      ]
    },
    {
      key: 'tools',
      label: 'Tools & Labs',
      description: 'Premium and free tools, labs, and workbenches.',
      defaultContent: { DATA: [] },
      isArray: true,
      arrayKey: 'DATA',
      arrayFields: [
        { key: 'title', label: 'Title', type: 'text' },
        { key: 'description', label: 'Description', type: 'textarea' },
        { key: 'category', label: 'Category', type: 'text' },
        { key: 'type', label: 'Type', type: 'select', options: ['Free', 'Premium'] },
        { key: 'link', label: 'Link', type: 'text' }
      ]
    },
    {
      key: 'testimonials',
      label: 'Testimonials',
      description: 'User testimonials displayed on the testimonials page and homepage.',
      defaultContent: { DATA: [] },
      isArray: true,
      arrayKey: 'DATA',
      arrayFields: [
        { key: 'name', label: 'Name', type: 'text' },
        { key: 'role', label: 'Role / Title', type: 'text' },
        { key: 'organization', label: 'Organization', type: 'text' },
        { key: 'quote', label: 'Quote', type: 'textarea' },
        { key: 'rating', label: 'Rating (1-5)', type: 'number' }
      ]
    },
    {
      key: 'team',
      label: 'Team Members',
      description: 'Team members displayed on the About page.',
      defaultContent: { DATA: [] },
      isArray: true,
      arrayKey: 'DATA',
      arrayFields: [
        { key: 'name', label: 'Name', type: 'text' },
        { key: 'role', label: 'Role', type: 'text' },
        { key: 'bio', label: 'Bio', type: 'textarea' },
        { key: 'image', label: 'Image URL', type: 'text' },
        { key: 'linkedin', label: 'LinkedIn URL', type: 'text' }
      ]
    },
    {
      key: 'footer',
      label: 'Footer Links',
      description: 'Footer navigation sections and links displayed across all pages.',
      defaultContent: {
        sections: [
          { title: 'About', links: [] },
          { title: 'Legal & IT Act', links: [] },
          { title: 'Resources', links: [] }
        ]
      },
      fields: null,
      isArray: false
    },
    {
      key: 'announcements',
      label: 'Announcements',
      description: 'Site-wide announcements or banners shown to users.',
      defaultContent: {
        active: false,
        text: '',
        link: '',
        type: 'info'
      },
      fields: [
        { key: 'active', label: 'Active', type: 'checkbox' },
        { key: 'text', label: 'Announcement Text', type: 'textarea' },
        { key: 'link', label: 'Link (optional)', type: 'text' },
        { key: 'type', label: 'Type', type: 'select', options: ['info', 'warning', 'success'] }
      ]
    }
  ];

  // =========================================================================
  // CMS ENGINE
  // =========================================================================

  var AdminCMS = {

    sections: SECTIONS,
    _cache: {},

    /**
     * Fetch all sections from site_content table.
     * @returns {Promise<Object>} Map of section_key → content
     */
    async fetchAll() {
      var result = await supabaseClient
        .from('site_content')
        .select('*')
        .order('label');

      if (result.error) {
        console.error('[CMS] Fetch error:', result.error);
        throw result.error;
      }

      var map = {};
      (result.data || []).forEach(function (row) {
        map[row.section_key] = row;
      });
      this._cache = map;
      return map;
    },

    /**
     * Fetch a single section by key.
     * @param {string} key
     * @returns {Promise<Object|null>}
     */
    async fetchSection(key) {
      var result = await supabaseClient
        .from('site_content')
        .select('*')
        .eq('section_key', key)
        .single();

      if (result.error && result.error.code !== 'PGRST116') {
        console.error('[CMS] Fetch section error:', result.error);
        throw result.error;
      }

      return result.data || null;
    },

    /**
     * Save (upsert) a section's content.
     * @param {string} key - section_key
     * @param {string} label - display label
     * @param {Object} content - JSON content
     * @returns {Promise<Object>}
     */
    async saveSection(key, label, content) {
      var userId = ImpactMojoAuth.user ? ImpactMojoAuth.user.id : null;

      var result = await supabaseClient
        .from('site_content')
        .upsert({
          section_key: key,
          label: label,
          content: content,
          updated_at: new Date().toISOString(),
          updated_by: userId
        }, { onConflict: 'section_key' })
        .select()
        .single();

      if (result.error) {
        console.error('[CMS] Save error:', result.error);
        throw result.error;
      }

      this._cache[key] = result.data;
      return result.data;
    },

    /**
     * Seed all default sections into the database (only inserts if not exists).
     * @returns {Promise<number>} count of sections seeded
     */
    async seedDefaults() {
      var existing = await this.fetchAll();
      var seeded = 0;

      for (var i = 0; i < SECTIONS.length; i++) {
        var sec = SECTIONS[i];
        if (!existing[sec.key]) {
          await this.saveSection(sec.key, sec.label, sec.defaultContent);
          seeded++;
        }
      }

      return seeded;
    },

    /**
     * Get nested value from an object using dot-notation key.
     * @param {Object} obj
     * @param {string} path - e.g. "cta_primary.text"
     * @returns {*}
     */
    getNestedValue: function (obj, path) {
      return path.split('.').reduce(function (o, k) {
        return o && o[k] !== undefined ? o[k] : '';
      }, obj);
    },

    /**
     * Set nested value on an object using dot-notation key.
     * @param {Object} obj
     * @param {string} path
     * @param {*} value
     */
    setNestedValue: function (obj, path, value) {
      var keys = path.split('.');
      var current = obj;
      for (var i = 0; i < keys.length - 1; i++) {
        if (current[keys[i]] === undefined) current[keys[i]] = {};
        current = current[keys[i]];
      }
      current[keys[keys.length - 1]] = value;
    },

    // =====================================================
    // UI RENDERING HELPERS
    // =====================================================

    /**
     * Render a form field HTML string.
     * @param {Object} field - { key, label, type, options? }
     * @param {*} value - current value
     * @param {string} prefix - id prefix for form elements
     * @returns {string} HTML
     */
    renderField: function (field, value, prefix) {
      var id = prefix + '_' + field.key.replace(/\./g, '_');
      var html = '<div class="cms-field">';
      html += '<label class="cms-label" for="' + id + '">' + field.label + '</label>';

      if (field.type === 'textarea') {
        html += '<textarea class="cms-input cms-textarea" id="' + id + '" data-key="' + field.key + '">' + (value || '') + '</textarea>';
      } else if (field.type === 'select') {
        html += '<select class="cms-input cms-select" id="' + id + '" data-key="' + field.key + '">';
        (field.options || []).forEach(function (opt) {
          var selected = opt === value ? ' selected' : '';
          html += '<option value="' + opt + '"' + selected + '>' + opt + '</option>';
        });
        html += '</select>';
      } else if (field.type === 'checkbox') {
        var checked = value ? ' checked' : '';
        html += '<input type="checkbox" class="cms-checkbox" id="' + id + '" data-key="' + field.key + '"' + checked + '>';
      } else if (field.type === 'number') {
        html += '<input type="number" class="cms-input" id="' + id + '" data-key="' + field.key + '" value="' + (value || '') + '">';
      } else {
        html += '<input type="text" class="cms-input" id="' + id + '" data-key="' + field.key + '" value="' + (value || '').toString().replace(/"/g, '&quot;') + '">';
      }

      html += '</div>';
      return html;
    },

    /**
     * Collect form values from rendered fields.
     * @param {Object} content - existing content object
     * @param {Array} fields - field definitions
     * @param {string} prefix - id prefix
     * @returns {Object} updated content
     */
    collectFieldValues: function (content, fields, prefix) {
      var updated = JSON.parse(JSON.stringify(content));
      var self = this;

      fields.forEach(function (field) {
        var id = prefix + '_' + field.key.replace(/\./g, '_');
        var el = document.getElementById(id);
        if (!el) return;

        var val;
        if (field.type === 'checkbox') {
          val = el.checked;
        } else if (field.type === 'number') {
          val = el.value ? parseFloat(el.value) : null;
        } else {
          val = el.value;
        }

        self.setNestedValue(updated, field.key, val);
      });

      return updated;
    }
  };

  window.AdminCMS = AdminCMS;
})();
