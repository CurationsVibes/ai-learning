# GitHub Actions Workflows

## deploy-pages.yml

This workflow automatically builds and deploys the documentation to GitHub Pages using **BookGen**, our custom GitBook alternative. It also supports **PR preview deployments** for testing changes before merging.

### Why BookGen?

BookGen is a lightweight Python-based static site generator we created to replace GitBook CLI, which had compatibility issues with modern Node.js versions. BookGen provides all the GitBook features without the maintenance burden:

- ✅ Modern, actively maintained
- ✅ No Node.js version conflicts
- ✅ Fast builds (1-2 seconds vs 2-3 minutes)
- ✅ Zero security vulnerabilities
- ✅ Easy to customize

See [BOOKGEN.md](../../BOOKGEN.md) for complete documentation.

### Trigger Events

- **Push to main branch**: Automatically builds and deploys to production GitHub Pages when changes are pushed to the main branch
- **Pull requests**: Builds the site and creates a preview deployment with a unique URL for testing
- **Manual dispatch**: Can be manually triggered from the Actions tab in GitHub

### What it does

1. **Build Job**:
   - Checks out the repository
   - Configures GitHub Pages (sets up base URL and origin for correct preview URLs)
   - Sets up Python 3.11 environment
   - Installs python-markdown library
   - **Validates presence of key files** (book.json, SUMMARY.md, readme.md) - fails fast with clear error if missing
   - Makes build script executable (chmod +x ./.bookgen/build.sh)
   - Runs BookGen build script from repo root
   - Uploads _book/ directory as the Pages artifact

2. **Deploy Job** (runs only for push to main or workflow_dispatch):
   - Takes the built artifact from the build job
   - Deploys it to GitHub Pages
   - For main branch: publishes to production at `https://<username>.github.io/<repository>/`
   - For PRs: GitHub automatically creates a preview deployment with a unique URL

### Setup Requirements

To enable this workflow, you need to:

1. **Enable GitHub Pages** in repository settings:
   - Go to Settings > Pages
   - Under "Source", select **"GitHub Actions"** (not "Deploy from a branch")
   - This is required for both production and PR preview deployments

2. **Permissions**: The workflow has the necessary permissions defined in the YAML file:
   - `contents: read` - to checkout the repository
   - `pages: write` - to deploy to GitHub Pages
   - `id-token: write` - for secure OIDC authentication

3. **Branch Protection** (optional but recommended):
   - Protect the main branch to ensure quality control
   - Require status checks before merging
   - Require pull request reviews

### PR Preview Deployments

When you open or update a pull request:
- The workflow runs automatically on the `pull_request` event
- The build job executes and uploads the Pages artifact
- GitHub automatically creates a preview deployment
- A comment is added to the PR with the preview URL
- The preview URL remains active until the PR is closed or merged
- Each PR gets its own unique preview URL

**Note**: The deploy job is skipped for PRs (it only runs on push to main), but GitHub still creates preview deployments automatically for uploaded artifacts.

### Customization

- To use a custom domain, add a `CNAME` file to the repository root with your domain
- To modify the build process, edit `.bookgen/generator.py`
- To change the build behavior, modify this workflow file

### Troubleshooting

If the deployment fails, check the following:

1. **GitHub Pages not enabled or wrong source**:
   - Go to Settings > Pages
   - Ensure "Source" is set to "GitHub Actions" (not "Deploy from a branch")
   - Without this setting, deployments will not publish

2. **Permissions issues**:
   - Verify that the repository has the correct permissions in the workflow file
   - Check that Actions have write access to Pages in Settings > Actions > General

3. **Required files missing**:
   - Ensure book.json, SUMMARY.md, and readme.md are present in the repository root
   - The workflow validates these files and fails fast with a clear error message

4. **Build script not executable**:
   - The workflow automatically makes the script executable with `chmod +x`
   - If you see permission errors, check that .bookgen/build.sh exists

5. **Python markdown library issues**:
   - The workflow installs python-markdown automatically
   - If you see import errors, check the build logs in the Actions tab

6. **Check workflow logs**:
   - Go to Actions tab
   - Click on the failed workflow run
   - Review the build and deploy job logs for specific error messages

7. **PR preview not working**:
   - Ensure GitHub Pages source is set to "GitHub Actions"
   - Check that the build job completed successfully
   - Preview URLs are added as comments to the PR automatically by GitHub

For more detailed troubleshooting, see [BOOKGEN.md](../../BOOKGEN.md).
