# GitHub Actions Workflows

## deploy-pages.yml

This workflow automatically builds and deploys the GitBook documentation to GitHub Pages.

### Trigger Events
- **Push to main branch**: Automatically builds and deploys when changes are pushed to the main branch
- **Manual dispatch**: Can be manually triggered from the Actions tab in GitHub

### What it does
1. **Build Job**:
   - Checks out the repository
   - Sets up Node.js environment
   - Installs GitBook CLI (version 3.2.3)
   - Installs any GitBook plugins defined in book.json
   - Builds the GitBook into static HTML files
   - Uploads the built files as a Pages artifact

2. **Deploy Job**:
   - Takes the built artifact from the build job
   - Deploys it to GitHub Pages
   - Publishes the site at: `https://<username>.github.io/<repository>/`

### Setup Requirements

To enable this workflow, you need to:

1. **Enable GitHub Pages** in repository settings:
   - Go to Settings > Pages
   - Under "Source", select "GitHub Actions"

2. **Permissions**: The workflow has the necessary permissions defined in the YAML file

3. **Branch Protection** (optional but recommended):
   - Protect the main branch to ensure quality control
   - Require status checks before merging

### Customization

- To use a custom domain, add a `CNAME` file to the repository root with your domain
- To modify the GitBook version, update the `gitbook fetch` command
- To add more plugins, update the `book.json` file

### Troubleshooting

If the deployment fails:
1. Check the Actions tab for error logs
2. Ensure GitHub Pages is enabled with "GitHub Actions" as the source
3. Verify that the repository has the correct permissions
4. Check that all required files (readme.md, SUMMARY.md) are present
