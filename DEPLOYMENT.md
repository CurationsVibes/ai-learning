# Deployment Guide

This guide provides step-by-step instructions for setting up and maintaining the automated deployment pipeline for the BUNKER documentation site.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Initial Setup](#initial-setup)
- [Automated Deployment](#automated-deployment)
- [Custom Domain Setup](#custom-domain-setup)
- [Monitoring & Troubleshooting](#monitoring--troubleshooting)
- [Advanced Configuration](#advanced-configuration)

---

## Overview

The BUNKER documentation site is built with **Astro + Starlight** and automatically deployed to **GitHub Pages** using **GitHub Actions**.

### Technology Stack

- **Static Site Generator**: Astro v4.16.17
- **Documentation Theme**: Starlight v0.28.4
- **Build Tool**: Node.js 20.x + npm
- **Hosting**: GitHub Pages
- **CI/CD**: GitHub Actions

### Deployment Architecture

```
┌─────────────────┐
│  Push to main   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ GitHub Actions  │
│   Workflow      │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌────────┐ ┌────────┐
│ Build  │ │ Deploy │
│  Job   │ │  Job   │
└────┬───┘ └───┬────┘
     │         │
     └────┬────┘
          │
          ▼
    ┌──────────┐
    │  GitHub  │
    │  Pages   │
    └──────────┘
```

---

## Prerequisites

Before setting up deployment, ensure you have:

1. **Repository Access**
   - Admin access to the `CurationsLA/ai-learning` repository
   - Ability to modify repository settings

2. **GitHub Features Enabled**
   - GitHub Pages (usually enabled by default)
   - GitHub Actions (usually enabled by default)

3. **Local Development Environment** (for testing)
   - Node.js 20.x or later
   - npm 9.x or later
   - Git

---

## Initial Setup

### Step 1: Enable GitHub Pages

1. Navigate to your repository on GitHub: https://github.com/CurationsLA/ai-learning
2. Click **Settings** (gear icon in the top menu)
3. In the left sidebar, scroll down and click **Pages** (under "Code and automation")
4. Under **"Build and deployment"** section:
   - **Source**: Select **"GitHub Actions"** from the dropdown
   - This allows the workflow in `.github/workflows/deploy-pages.yml` to deploy automatically

![GitHub Pages Settings](https://docs.github.com/assets/cb-49851/mw-1440/images/help/pages/create-page-choose-source.webp)

### Step 2: Configure Workflow Permissions

1. While in Settings, click on **Actions** > **General** in the left sidebar
2. Scroll down to **"Workflow permissions"**
3. Ensure the following are selected:
   - ✅ **"Read and write permissions"**
   - ✅ **"Allow GitHub Actions to create and approve pull requests"**
4. Click **Save** if you made changes

### Step 3: Verify Workflow File

The workflow file should already exist at `.github/workflows/deploy-pages.yml`. Verify it contains:

```yaml
name: Deploy Astro site to GitHub Pages

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write
```

If the file is missing or outdated, refer to the repository's latest version.

### Step 4: Trigger First Deployment

You have three options:

**Option A: Push to Main Branch**
```bash
git checkout main
git pull
# Make any change (e.g., update README)
git add .
git commit -m "Trigger initial deployment"
git push
```

**Option B: Manual Workflow Trigger**
1. Go to the **Actions** tab in your repository
2. Click on **"Deploy Astro site to GitHub Pages"** workflow
3. Click **"Run workflow"** button (top right)
4. Select `main` branch
5. Click **"Run workflow"**

**Option C: Create a Pull Request**
1. Create a new branch with changes
2. Open a pull request to `main`
3. Once merged, deployment triggers automatically

---

## Automated Deployment

Once set up, deployment is fully automated:

### Trigger Events

The workflow automatically runs when:

1. **Code is pushed to main branch**
   - Any changes to `src/content/docs/` (documentation)
   - Changes to `astro.config.mjs` (configuration)
   - Changes to `package.json` (dependencies)
   - Changes to styling or components

2. **Manual trigger from Actions tab**
   - Useful for re-deploying without code changes
   - Good for testing or fixing failed deployments

### What Happens During Deployment

1. **Validation Phase** (~10 seconds)
   - Validates configuration files exist
   - Checks content directory structure
   - Ensures package.json is valid

2. **Build Phase** (~2 minutes)
   - Installs Node.js 20.x
   - Installs npm dependencies (with caching)
   - Runs TypeScript type checking
   - Builds Astro site (generates HTML, CSS, JS)
   - Indexes content for search (Pagefind)
   - Generates sitemap

3. **Verification Phase** (~5 seconds)
   - Verifies dist/ directory exists
   - Checks for index.html
   - Reports build statistics

4. **Deployment Phase** (~30 seconds)
   - Uploads build artifacts to GitHub Pages
   - Deploys to production environment
   - Updates live site

**Total Time**: Approximately 2-3 minutes from push to live.

### Monitoring Deployments

1. Go to the **Actions** tab in your repository
2. Click on the most recent workflow run
3. View logs for each step
4. Look for ✅ (success) or ❌ (failure) indicators

Example successful output:
```
✓ Validating Astro configuration...
✓ Validating package.json...
✓ Checking content directory...
✅ All configuration files validated successfully
📦 Installing npm dependencies...
✅ Dependencies installed successfully
🚀 Building Astro site...
✅ Build completed successfully
📊 Build statistics:
  Total files: 247
  HTML files: 41
  Size: 4.2M
✅ Build output verified successfully
✅ Deployment completed successfully
🌐 Site URL: https://curationsla.github.io/ai-learning/
```

---

## Custom Domain Setup

If you want to use a custom domain (e.g., `docs.bunker.curations.org`):

### Step 1: Add CNAME File

Create a file named `CNAME` in the `public/` directory:

```bash
# Create public directory if it doesn't exist
mkdir -p public

# Add your domain to CNAME file
echo "docs.bunker.curations.org" > public/CNAME

# Commit and push
git add public/CNAME
git commit -m "Add custom domain"
git push
```

### Step 2: Configure DNS

#### For Subdomain (e.g., docs.bunker.curations.org)

Add a **CNAME record** with your DNS provider:

| Type  | Name | Value                    | TTL  |
|-------|------|--------------------------|------|
| CNAME | docs | curationsla.github.io    | 3600 |

#### For Apex Domain (e.g., bunker.curations.org)

Add **A records** with your DNS provider pointing to GitHub Pages IPs:

| Type | Name | Value            | TTL  |
|------|------|------------------|------|
| A    | @    | 185.199.108.153  | 3600 |
| A    | @    | 185.199.109.153  | 3600 |
| A    | @    | 185.199.110.153  | 3600 |
| A    | @    | 185.199.111.153  | 3600 |

### Step 3: Enable Custom Domain in GitHub

1. Go to **Settings** > **Pages**
2. Under **"Custom domain"**, enter your domain
3. Click **Save**
4. Wait for DNS propagation (can take 24-48 hours)
5. Once DNS is verified, check **"Enforce HTTPS"** (recommended)

### Step 4: Update Astro Configuration

Edit `astro.config.mjs` to use your custom domain:

```javascript
export default defineConfig({
  site: 'https://docs.bunker.curations.org',
  base: '/',  // Change to '/' for custom domain
  // ... rest of config
});
```

### Verifying DNS Propagation

Use `dig` or online tools to check DNS:

```bash
# Check CNAME record
dig docs.bunker.curations.org

# Check A records
dig bunker.curations.org
```

---

## Monitoring & Troubleshooting

### Build Status Badge

Add a status badge to your README to monitor deployment health:

```markdown
[![Deploy Status](https://github.com/CurationsLA/ai-learning/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/CurationsLA/ai-learning/actions/workflows/deploy-pages.yml)
```

### Common Issues

#### 1. Build Fails: TypeScript Errors

**Symptoms**: Build fails during `astro check` step

**Solution**:
```bash
# Run locally to see errors
npm run build

# Common fixes:
# - Add missing frontmatter to .md files
# - Quote titles with colons: title: "AI: Guide"
# - Check for invalid TypeScript in components
```

#### 2. Build Fails: Missing Dependencies

**Symptoms**: `npm ci` fails or modules not found

**Solution**:
```bash
# Update dependencies locally
npm install

# Commit package-lock.json
git add package-lock.json
git commit -m "Update dependencies"
git push
```

#### 3. Site Shows 404 After Deployment

**Symptoms**: GitHub Pages shows 404 error

**Possible Causes & Solutions**:

a) **Incorrect base path**
   - Check `astro.config.mjs`: `base: '/ai-learning'`
   - Should match repository name

b) **GitHub Pages not enabled**
   - Go to Settings > Pages
   - Ensure source is "GitHub Actions"

c) **Deployment not complete**
   - Check Actions tab for completion
   - Wait 2-3 minutes for CDN to update

#### 4. Search Not Working

**Symptoms**: Search box doesn't return results

**Solution**:
- Search only works in production builds
- Verify Pagefind completed in build logs
- Check for errors in browser console
- Clear browser cache

#### 5. Workflow Permission Denied

**Symptoms**: Deployment fails with permission error

**Solution**:
1. Go to Settings > Actions > General
2. Enable "Read and write permissions"
3. Re-run the workflow

#### 6. Slow Build Times

**Symptoms**: Builds taking longer than 3 minutes

**Optimization**:
- npm cache should be working (check logs)
- Consider using `npm ci --prefer-offline`
- Check for unnecessary dependencies
- Review path-ignore patterns in workflow

### Getting Help

If you encounter issues not covered here:

1. **Check workflow logs**: Actions tab > failed run > view logs
2. **Review documentation**:
   - [MIGRATION.md](./MIGRATION.md) - Migration details
   - [.github/workflows/README.md](./.github/workflows/README.md) - Workflow docs
   - [Astro Documentation](https://docs.astro.build)
3. **Open an issue**: Include error logs and steps to reproduce

---

## Advanced Configuration

### Environment-Specific Builds

To create different builds for staging and production:

1. Create a new workflow: `.github/workflows/deploy-staging.yml`
2. Modify the trigger and environment:
   ```yaml
   on:
     push:
       branches:
         - develop
   ```
3. Use different Astro config for staging

### Build Caching Strategies

The workflow already uses npm caching. To improve further:

```yaml
- name: Cache Astro build
  uses: actions/cache@v3
  with:
    path: |
      .astro
      node_modules/.astro
    key: ${{ runner.os }}-astro-${{ hashFiles('**/package-lock.json') }}
```

### Notifications

Add Slack or Discord notifications on deployment:

```yaml
- name: Notify Slack
  if: always()
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

### Deploy Previews for Pull Requests

To create preview deployments for PRs:

1. Set up a service like Netlify or Vercel
2. Add their GitHub app to the repository
3. Preview URLs will appear in PRs automatically

---

## Security Considerations

### Secrets Management

The workflow uses GitHub's built-in secrets:

- `GITHUB_TOKEN`: Automatically provided by Actions
- `id-token`: Used for OIDC authentication

**Never commit secrets to the repository.**

### Dependency Security

The build shows security vulnerabilities. To fix:

```bash
# Review vulnerabilities
npm audit

# Fix automatically (may break compatibility)
npm audit fix

# Or update specific packages
npm update <package-name>
```

### Content Security

- All content is public (GitHub Pages serves static files)
- Ensure no sensitive information in documentation
- Review all markdown files before publishing

---

## Maintenance

### Regular Tasks

**Monthly:**
- Review and update npm dependencies
- Check for security vulnerabilities: `npm audit`
- Review workflow performance in Actions tab

**Quarterly:**
- Update GitHub Actions versions (checkout, setup-node, etc.)
- Review and optimize build times
- Check for Astro and Starlight updates

**Annually:**
- Review custom domain configuration
- Audit and clean up unused dependencies
- Update documentation and guides

### Dependency Updates

```bash
# Check for outdated packages
npm outdated

# Update to latest within semver range
npm update

# Update to latest (may break compatibility)
npm install <package>@latest

# Always test after updates
npm run build
```

---

## Additional Resources

### Documentation
- [Astro Documentation](https://docs.astro.build)
- [Starlight Documentation](https://starlight.astro.build)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

### Repository Files
- [MIGRATION.md](./MIGRATION.md) - Migration from BookGen to Astro
- [readme.md](./readme.md) - Project overview
- [.github/workflows/README.md](./.github/workflows/README.md) - Workflow details
- [VALIDATION_CHECKLIST.md](./VALIDATION_CHECKLIST.md) - Content validation

### Community
- [Astro Discord](https://astro.build/chat)
- [GitHub Community Forums](https://github.community)

---

## Summary Checklist

Use this checklist to ensure your deployment is properly configured:

- [ ] GitHub Pages enabled (Settings > Pages > Source: GitHub Actions)
- [ ] Workflow permissions configured (Settings > Actions > General)
- [ ] Workflow file exists (`.github/workflows/deploy-pages.yml`)
- [ ] First deployment successful (Actions tab shows ✅)
- [ ] Site accessible at https://curationsla.github.io/ai-learning/
- [ ] Search functionality working
- [ ] Mobile responsive design verified
- [ ] Custom domain configured (if applicable)
- [ ] HTTPS enabled
- [ ] Status badge added to README (optional)
- [ ] Team members notified of deployment URL

**Deployment Status**: ✅ Complete

---

*Last updated: November 15, 2025*
*Maintained by: BUNKER Team*
