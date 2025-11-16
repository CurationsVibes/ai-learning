# Algolia DocSearch Application Guide

**Date**: 2025-11-16
**For**: BUNKER Documentation Site
**Repository**: CurationsLA/ai-learning
**Site**: https://curationsla.github.io/ai-learning

---

## 📋 Application Status

**Status**: ⏳ **READY TO APPLY**

**Decision Date**: November 15, 2025
**Decided By**: Michael (VS Code Copilot)
**Rationale**: Better search experience, free for open-source, industry standard with instant results
**Documented**: `docs/planning/gitbook-hybrid/99-decisions-needed.md` (lines 34-36)

---

## 🎯 Why Algolia DocSearch?

**Current Search**: Pagefind (Starlight default)
- ✅ Works perfectly
- ✅ 6,763 words indexed
- ✅ 40 pages searchable
- ❌ No instant search
- ❌ No keyboard shortcuts (Cmd+K)
- ❌ Limited result previews

**Algolia DocSearch Benefits**:
- ✅ Instant search results (as you type)
- ✅ Keyboard shortcuts (Cmd+K / Ctrl+K)
- ✅ Rich result previews
- ✅ Recent searches
- ✅ Mobile-optimized
- ✅ **Free for open-source projects**
- ✅ Industry standard (used by React, Vue, etc.)

---

## 📝 How to Apply

### **Option A: Online Application** (Recommended)

**URL**: https://docsearch.algolia.com/apply/

**Form Fields**:
```
Website URL: https://curationsla.github.io/ai-learning

Email: [YOUR EMAIL - provide this to Stanley]

Repository URL: https://github.com/CurationsLA/ai-learning

Documentation Type: Open Source Project

Project Description:
BUNKER is a Human × AI Creative Agency providing open-source frameworks,
guides, and resources for AI development, collaboration, and creativity.
Our documentation includes comprehensive AI × Human Cookbooks covering
RAG, agents, MCP/A2A protocols, advanced prompting, and business applications.
We promote "greater good creativity" and provide free learning resources
for developers, creators, and communities.

Public Documentation: ✅ Yes (publicly accessible)

Open Source: ✅ Yes (MIT License - see repository)

Technical Owner: ✅ Yes (you are the maintainer)

Commit to keeping up to date: ✅ Yes
```

**Verification**:
- They may ask you to add a meta tag to prove ownership
- Follow email instructions if requested

**Timeline**: 1-3 business days for response

---

### **Option B: Email Application**

If online form doesn't work, email: docsearch@algolia.com

**Subject**: DocSearch Application - BUNKER Documentation

**Body**:
```
Hello Algolia Team,

I'd like to apply for Algolia DocSearch for our open-source project.

Project: BUNKER (Human × AI Creative Agency)
Website: https://curationsla.github.io/ai-learning
Repository: https://github.com/CurationsLA/ai-learning
License: MIT (open source)

BUNKER provides open-source frameworks, guides, and resources for AI
development and Human × AI collaboration. Our documentation includes
comprehensive cookbooks on RAG, agents, MCP/A2A protocols, advanced
prompting, and business applications.

Our documentation is:
- Publicly accessible (no login required)
- Open source (GitHub repository linked above)
- Regularly updated
- Community-focused (serves developers, creators, educators)

We currently use Pagefind for search, but would like to upgrade to
Algolia DocSearch for better user experience (instant search, keyboard
shortcuts, rich previews).

Technical contact: [YOUR EMAIL]
GitHub username: [YOUR GITHUB USERNAME]

Thank you for considering our application.

Best regards,
[YOUR NAME]
BUNKER / CurationsLA
```

---

## 🔑 After Approval

**You'll receive**:
1. **Application ID**: `APP_ID`
2. **API Key**: `SEARCH_API_KEY` (public, read-only)
3. **Index Name**: Usually `curationsla_ai-learning`

**Example credentials** (you'll get actual values):
```javascript
{
  "appId": "XXXXXXXXXX",
  "apiKey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "indexName": "curationsla_ai-learning"
}
```

---

## 🔧 Integration (For Michael - Stage 2)

**Once credentials are received**:

### **Step 1: Install Dependencies**
```bash
npm install @docsearch/js @docsearch/css
```

### **Step 2: Create DocSearch Component**

**Create**: `src/components/AlgoliaSearch.astro`

```astro
---
// AlgoliaSearch.astro
interface Props {
  appId: string;
  apiKey: string;
  indexName: string;
}

const { appId, apiKey, indexName } = Astro.props;
---

<div id="docsearch"></div>

<script
  is:inline
  define:vars={{ appId, apiKey, indexName }}
>
  import docsearch from '@docsearch/js';
  import '@docsearch/css';

  docsearch({
    appId: appId,
    apiKey: apiKey,
    indexName: indexName,
    container: '#docsearch',
    placeholder: 'Search BUNKER docs...',
    searchParameters: {
      facetFilters: ['language:en'],
    },
    insights: true,
  });
</script>

<style>
  /* Override DocSearch theme to match BUNKER branding */
  :root {
    --docsearch-primary-color: #667eea; /* BUNKER purple */
    --docsearch-text-color: #2c3e50;    /* BUNKER dark blue-gray */
  }
</style>
```

### **Step 3: Add to Site Header**

**Edit**: `astro.config.mjs` or your header component

```astro
---
import AlgoliaSearch from '../components/AlgoliaSearch.astro';
---

<!-- In your header -->
<AlgoliaSearch
  appId={import.meta.env.PUBLIC_ALGOLIA_APP_ID}
  apiKey={import.meta.env.PUBLIC_ALGOLIA_API_KEY}
  indexName={import.meta.env.PUBLIC_ALGOLIA_INDEX_NAME}
/>
```

### **Step 4: Add Environment Variables**

**Create/Edit**: `.env`

```bash
PUBLIC_ALGOLIA_APP_ID=your_app_id_here
PUBLIC_ALGOLIA_API_KEY=your_api_key_here
PUBLIC_ALGOLIA_INDEX_NAME=curationsla_ai-learning
```

**Update**: `.env.example`

```bash
# Algolia DocSearch Configuration
PUBLIC_ALGOLIA_APP_ID=
PUBLIC_ALGOLIA_API_KEY=
PUBLIC_ALGOLIA_INDEX_NAME=
```

**Add to**: `.gitignore` (if not already present)

```
.env
.env.local
```

### **Step 5: Configure Crawler**

**Algolia will provide**: `docsearch.json` config file

**Customize for BUNKER** (if needed):

```json
{
  "index_name": "curationsla_ai-learning",
  "start_urls": ["https://curationsla.github.io/ai-learning/"],
  "sitemap_urls": ["https://curationsla.github.io/ai-learning/sitemap-index.xml"],
  "selectors": {
    "lvl0": {
      "selector": ".sl-markdown-content h1"
    },
    "lvl1": ".sl-markdown-content h2",
    "lvl2": ".sl-markdown-content h3",
    "lvl3": ".sl-markdown-content h4",
    "text": ".sl-markdown-content p, .sl-markdown-content li"
  }
}
```

---

## 🧪 Testing After Integration

**Test Checklist**:
- [ ] Search modal opens (Cmd+K / Ctrl+K)
- [ ] Results appear as you type
- [ ] Results are accurate (try known terms)
- [ ] Click result navigates to correct page
- [ ] Mobile search works (responsive)
- [ ] Keyboard navigation works (arrow keys, Enter, Esc)
- [ ] Styling matches BUNKER theme
- [ ] No console errors
- [ ] Performance acceptable (Lighthouse still ≥90)

**Fallback Plan**:
- If Algolia has issues, keep Pagefind as backup
- Can run both simultaneously during testing
- Switch between them via environment variable

---

## 📊 Monitoring & Maintenance

**Crawler Frequency**:
- Algolia crawls your site automatically (weekly by default)
- You can request manual crawls: https://crawler.algolia.com/

**Analytics**:
- View search analytics in Algolia Dashboard
- Track popular queries, click-through rates, etc.

**Updates Needed When**:
- Site structure changes (update `docsearch.json`)
- Domain changes (update crawler config)
- New content sections added (may need selector updates)

---

## ❓ Troubleshooting

**Application Rejected?**
- Ensure site is publicly accessible (no login required)
- Confirm repository is truly open source (public, with license)
- Add CONTRIBUTING.md or CODE_OF_CONDUCT.md (shows active project)
- Try email application if form doesn't work

**Crawler Not Finding Content?**
- Check `sitemap-index.xml` exists and is correct
- Verify selectors match your HTML structure
- Request manual crawl to test
- Check robots.txt doesn't block Algolia bot

**Search Not Working?**
- Verify credentials in `.env` are correct
- Check browser console for errors
- Ensure API key has correct permissions (public read-only)
- Test with Algolia's DocSearch playground

---

## 📞 Contact

**Algolia Support**:
- Email: docsearch@algolia.com
- Docs: https://docsearch.algolia.com/docs/what-is-docsearch
- Community: https://discourse.algolia.com/

**Internal**:
- Questions about integration: Ask Stanley
- Questions about UI/UX: Ask Michael
- Questions about deployment: Check deployment docs

---

## ✅ Next Steps

**Immediate** (Stanley/User):
1. [ ] Decide who submits application (Stanley or User)
2. [ ] Provide email for application
3. [ ] Submit application (Option A or B above)
4. [ ] Wait 1-3 business days

**After Approval** (Michael - Stage 2):
5. [ ] Receive credentials from Algolia
6. [ ] Install dependencies (`@docsearch/js`)
7. [ ] Create AlgoliaSearch component
8. [ ] Add environment variables
9. [ ] Test integration
10. [ ] Deploy to production

**Timeline**:
- Application: Today (2025-11-16)
- Approval: 1-3 days (2025-11-17 to 2025-11-19)
- Integration: 2-3 hours (Michael, Stage 2)
- Testing: 1-2 hours
- Live: By end of Stage 2

---

## 📋 Application Checklist

**Ready to Apply**:
- [x] Site is publicly accessible
- [x] Repository is open source (public)
- [x] Documentation is substantial (40+ pages, 6,763 words)
- [x] Project is active (recent commits)
- [x] Community-focused (educational, open resources)
- [x] Commit to maintaining (yes)
- [ ] Email address provided
- [ ] Application submitted

**Status**: Waiting for user to provide email, then Stanley submits application.

---

**Stanley ready to submit application as soon as you provide the email address.** 📧
