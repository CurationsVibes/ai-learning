# Algolia DocSearch - Complete Setup

**Status**: ✅ **CONFIGURED AND READY**

**Date**: 2025-11-16
**MCP Server**: `bunker-docs-search`
**Index**: `ai-indexing`

---

## 🔑 Credentials (ACTIVE)

```bash
Application ID: U5EA7WSUAC
Search API Key: c34b4ee5045520f0135795c2ab09b574
Index Name: ai-indexing
MCP Server URL: https://mcp.us.algolia.com/1/CzV1dTQPDw51dLZONjZJMklNNTUwMTU1MkgzMDQ2Nbc0TTZKTDKwTDI1N7FOzNTNzEtJrcjMS7c2NDczNjI3M7e0BAA/mcp
```

**Security**:
- ✅ Search API Key is read-only (safe for client-side use)
- ✅ Already added to `.env` (git-ignored)
- ✅ Never commit Admin API Key to git

---

## 📦 Files Created

**Environment Configuration**:
- `.env` - Contains your actual credentials (git-ignored)

**Algolia Component**:
- `src/components/AlgoliaSearch.astro` - Ready-to-use search component

**Documentation**:
- This file (complete setup guide)

---

## 🎯 For Michael (Stage 2 Integration)

### **Step 1: Verify Environment Variables**

The `.env` file is already created with your credentials. Verify it exists:

```bash
cat .env
```

Should show:
```bash
PUBLIC_ALGOLIA_APP_ID=U5EA7WSUAC
PUBLIC_ALGOLIA_API_KEY=c34b4ee5045520f0135795c2ab09b574
PUBLIC_ALGOLIA_INDEX_NAME=ai-indexing
```

### **Step 2: Use the AlgoliaSearch Component**

**Component location**: `src/components/AlgoliaSearch.astro`

**Usage in your layout/header**:

```astro
---
import AlgoliaSearch from '../components/AlgoliaSearch.astro';
---

<!-- In your header or navigation -->
<AlgoliaSearch />
```

**The component**:
- ✅ Loads DocSearch from CDN (no npm install needed initially)
- ✅ Styled to match BUNKER branding
- ✅ Keyboard shortcuts work (Cmd+K / Ctrl+K)
- ✅ Mobile responsive
- ✅ Reads credentials from environment variables

### **Step 3: Alternative - NPM Installation** (Optional)

If you prefer local dependencies instead of CDN:

```bash
npm install @docsearch/js @docsearch/css
```

Then update `AlgoliaSearch.astro` to use local imports instead of CDN.

### **Step 4: Test Locally**

```bash
# Start dev server
npm run dev

# Open browser to http://localhost:4321
# Click search or press Cmd+K / Ctrl+K
# Search should work if index is populated
```

### **Step 5: Populate Index** (If Empty)

**Check if index has records**:
1. Go to Algolia Dashboard → Search → Index → `ai-indexing`
2. Check "Records" count

**If empty, use Algolia Crawler**:
1. Go to **Data Sources** → **Crawler**
2. Click **New Crawler**
3. Configure:
   ```
   Name: BUNKER Docs Crawler
   Start URL: https://curationsla.github.io/ai-learning/
   Sitemap URL: https://curationsla.github.io/ai-learning/sitemap-index.xml
   ```
4. Click **Create Crawler**
5. Click **Run Crawler** (takes ~2-5 minutes)

**Crawler Configuration** (if needed):

```json
{
  "appId": "U5EA7WSUAC",
  "apiKey": "[ADMIN_API_KEY_FROM_DASHBOARD]",
  "indexName": "ai-indexing",
  "startUrls": ["https://curationsla.github.io/ai-learning/"],
  "sitemaps": ["https://curationsla.github.io/ai-learning/sitemap-index.xml"],
  "exclusionPatterns": [],
  "selectors": {
    "lvl0": {
      "selector": ".sl-markdown-content h1",
      "global": false
    },
    "lvl1": ".sl-markdown-content h2",
    "lvl2": ".sl-markdown-content h3",
    "lvl3": ".sl-markdown-content h4",
    "lvl4": ".sl-markdown-content h5",
    "text": ".sl-markdown-content p, .sl-markdown-content li"
  }
}
```

---

## 🧪 Testing Checklist

**After Integration**:
- [ ] Search modal opens (click search button or Cmd+K)
- [ ] Results appear as you type
- [ ] Click result navigates to correct page
- [ ] Keyboard navigation works (arrows, Enter, Esc)
- [ ] Mobile search works (responsive)
- [ ] Styling matches BUNKER theme
- [ ] No console errors
- [ ] Performance acceptable (Lighthouse ≥90)

**Test Queries** (try these):
- "RAG" → Should find RAG cookbook pages
- "agent" → Should find agent guides
- "MCP" → Should find MCP documentation
- "prompt" → Should find prompting guides

---

## 🔧 Troubleshooting

### **Search Not Working**

**1. Check Environment Variables**:
```bash
# In your Astro dev server console, you should see:
# ✅ Algolia DocSearch initialized

# If you see error, check .env file exists and is correct
```

**2. Check Index Has Records**:
- Dashboard → Search → Index → `ai-indexing`
- Should show record count > 0
- If 0, run crawler (see Step 5 above)

**3. Check Browser Console**:
```javascript
// Should NOT see errors like:
// "Algolia configuration missing"
// "Failed to load DocSearch"
```

**4. Verify Search API Key Permissions**:
- Should be "Search-Only API Key" (read-only)
- Should have access to `ai-indexing` index

### **Crawler Not Finding Content**

**Check**:
- Sitemap exists: `https://curationsla.github.io/ai-learning/sitemap-index.xml`
- Site is publicly accessible (no login required)
- robots.txt doesn't block Algolia bot
- HTML selectors match your page structure

**Adjust Selectors**:
If crawler runs but finds 0 records, selectors might be wrong. Check:
```bash
# Inspect your HTML
# Find the actual classes/tags for headings and content
# Update selectors in crawler config
```

### **Styling Doesn't Match BUNKER**

**Update CSS Variables** in `AlgoliaSearch.astro`:
```css
:root {
  --docsearch-primary-color: #YOUR_COLOR;
  --docsearch-text-color: #YOUR_COLOR;
}
```

---

## 📊 Analytics & Monitoring

**View Search Analytics**:
1. Algolia Dashboard → Analytics
2. See:
   - Popular search queries
   - Click-through rates
   - Searches with no results
   - User engagement

**Use Insights to Improve**:
- Add synonyms for common misspellings
- Create redirects for popular queries
- Improve content based on searches with no results

---

## 🤖 MCP Integration (Advanced)

**Your MCP Server**: `bunker-docs-search`

**Connect in Claude Desktop**:

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "algolia-bunker": {
      "command": "node",
      "args": [
        "/path/to/mcp-algolia-bridge.js",
        "https://mcp.us.algolia.com/1/CzV1dTQPDw51dLZONjZJMklNNTUwMTU1MkgzMDQ2Nbc0TTZKTDKwTDI1N7FOzNTNzEtJrcjMS7c2NDczNjI3M7e0BAA/mcp"
      ]
    }
  }
}
```

**Then you can**:
- Ask Claude to search BUNKER docs
- Get programmatic access to your knowledge base
- Automate content discovery

**Future**: Create GitHub Action to auto-index via MCP on every deploy.

---

## 🚀 Future Enhancements

**Stage 3+**:
1. **Auto-indexing**: GitHub Action that runs crawler on every deploy
2. **Search Analytics Dashboard**: Show popular content
3. **Synonym Configuration**: Handle common misspellings
4. **Faceted Search**: Filter by cookbook category, difficulty level
5. **Related Content**: Show similar pages based on search
6. **MCP Automation**: Auto-index new content via MCP on git push

**Documentation as Code**:
Write a cookbook: "How We Use MCP to Auto-Index Our Documentation" 📚

---

## ✅ Integration Checklist (Michael)

**Stage 2 - Algolia Integration**:
- [ ] Verify `.env` file exists with credentials
- [ ] Use `AlgoliaSearch.astro` component in header/nav
- [ ] Test search locally (Cmd+K works)
- [ ] Check index has records (run crawler if needed)
- [ ] Test on mobile (responsive)
- [ ] Verify keyboard shortcuts work
- [ ] Check BUNKER styling applied
- [ ] Test production build
- [ ] Deploy and verify search works live
- [ ] Monitor analytics for first week

**Estimated Time**: 2-3 hours (including testing)

---

## 📞 Support

**If Issues Arise**:
- Check Algolia Dashboard → Logs → Search Logs (see actual queries)
- Check crawler runs → Crawls → Recent runs
- Tag Stanley for MCP or infrastructure questions
- Tag user for design/UX decisions

**Algolia Support**:
- Docs: https://www.algolia.com/doc/
- Community: https://discourse.algolia.com/
- Email: support@algolia.com (if critical)

---

## 🎉 You're Ready!

**Everything is configured**:
- ✅ Credentials in `.env`
- ✅ Component ready to use
- ✅ MCP server active
- ✅ Instructions complete

**Michael can integrate Algolia search in Stage 2** (~2-3 hours) and users will have instant, powerful search! ⚡

---

**Next**: Check if `ai-indexing` index has records. If empty, run crawler once and you're done! 🚀
