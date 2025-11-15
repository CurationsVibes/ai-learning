# GitHub Pages Setup Instructions

This guide walks you through enabling GitHub Pages for this repository.

## Prerequisites

- Repository admin access
- GitHub Actions enabled (usually enabled by default)

## Step-by-Step Setup

### 1. Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/CurationsLA/ai-learning`
2. Click on **Settings** (gear icon in the top menu)
3. In the left sidebar, scroll down and click **Pages** (under "Code and automation")
4. Under **"Build and deployment"** section:
   - **Source**: Select **"GitHub Actions"** from the dropdown
   - This allows the workflow in `.github/workflows/deploy-pages.yml` to deploy automatically

### 2. Verify Workflow Permissions

1. While in Settings, click on **Actions** > **General** in the left sidebar
2. Scroll down to **"Workflow permissions"**
3. Ensure **"Read and write permissions"** is selected
4. Check **"Allow GitHub Actions to create and approve pull requests"**
5. Click **Save** if you made changes

### 3. Trigger the First Build

You have two options:

**Option A: Push to Main Branch**
```bash
# Make any change and push to main
git checkout main
git pull
# Make a change, then:
git add .
git commit -m "Trigger GitHub Pages build"
git push
```

**Option B: Manual Trigger**
1. Go to the **Actions** tab in your repository
2. Click on **"Deploy to GitHub Pages"** workflow
3. Click **"Run workflow"** button
4. Select `main` branch
5. Click **"Run workflow"**

### 4. Monitor the Deployment

1. Go to the **Actions** tab
2. You should see a workflow run in progress
3. Click on it to view the logs
4. The deployment has two jobs:
   - **Build**: Installs GitBook and builds the site (~2-3 minutes)
   - **Deploy**: Deploys the built site to GitHub Pages (~30 seconds)

### 5. Access Your Site

Once the deployment is complete (green checkmark):

1. The site URL will be displayed in the workflow logs
2. By default, it's: `https://curationsla.github.io/ai-learning/`
3. You can also find it in **Settings** > **Pages** at the top

### 6. Custom Domain (Optional)

If you want to use a custom domain (e.g., `docs.curations.org`):

#### A. Add CNAME File

1. Rename `CNAME.example` to `CNAME`:
   ```bash
   mv CNAME.example CNAME
   ```

2. Edit the `CNAME` file and add your domain:
   ```
   docs.curations.org
   ```

3. Commit and push:
   ```bash
   git add CNAME
   git commit -m "Add custom domain"
   git push
   ```

#### B. Configure DNS

**For Subdomain (e.g., docs.curations.org):**

Add a CNAME record with your DNS provider:
```
Type: CNAME
Name: docs
Value: curationsla.github.io
TTL: 3600 (or default)
```

**For Apex Domain (e.g., curations.org):**

Add A records with your DNS provider pointing to GitHub Pages IPs:
```
Type: A
Name: @
Value: 185.199.108.153
Value: 185.199.109.153
Value: 185.199.110.153
Value: 185.199.111.153
TTL: 3600 (or default)
```

#### C. Enable HTTPS

1. Go to **Settings** > **Pages**
2. Under **"Custom domain"**, enter your domain
3. Click **Save**
4. Wait a few minutes for DNS to propagate
5. Check **"Enforce HTTPS"** once available (recommended)

## Troubleshooting

### Build Fails

**Error: GitBook installation failed**
- Check the Actions logs for specific errors
- The workflow uses GitBook CLI 3.2.3 which requires Node.js 12-16
- Verify `book.json` syntax is valid (it should be after setup)

**Error: Permission denied**
- Verify workflow permissions in Settings > Actions > General
- Ensure "Read and write permissions" is enabled

### Site Not Updating

**Changes don't appear on the live site**
- Check that changes were pushed to the `main` branch
- Go to Actions tab and verify the workflow ran successfully
- Clear your browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Wait a few minutes for GitHub Pages CDN to update

### 404 Errors

**Home page shows 404**
- Verify `readme.md` exists in the repository root
- Check `.gitbook.yaml` has correct `readme: readme.md` setting

**Other pages show 404**
- Verify file paths in `SUMMARY.md` are correct
- Check that all referenced files exist
- Use the file verification script:
  ```bash
  grep -oP '\]\(\K[^)]+' SUMMARY.md | while read file; do [ -f "$file" ] && echo "✓ $file" || echo "✗ $file"; done
  ```

### Custom Domain Issues

**"Domain is not properly configured"**
- Verify DNS records are correct and propagated
- Use `dig` or `nslookup` to check DNS:
  ```bash
  dig docs.curations.org
  ```
- DNS propagation can take 24-48 hours

**HTTPS not available**
- Wait for DNS to fully propagate first
- GitHub Pages needs to provision SSL certificate
- Can take several hours after DNS is configured

## Updating Content

After the initial setup, updating is automatic:

1. Edit markdown files locally or on GitHub
2. Commit and push to `main` branch
3. GitHub Actions automatically rebuilds and deploys
4. Changes appear on the site in 2-4 minutes

## Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitBook Documentation](https://docs.gitbook.com/)
- [Custom Domain Setup](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## Need Help?

- Check the Actions tab for build logs
- Review `GITBOOK_INTEGRATION.md` for detailed documentation
- Check `.github/workflows/README.md` for workflow documentation
- Consult GitHub Pages documentation for hosting-related issues
