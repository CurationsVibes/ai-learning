# GitHub Actions Workflows

## deploy-pages.yml

This workflow automatically builds and deploys the documentation to GitHub Pages using **BookGen**, our custom GitBook alternative.

### Why BookGen?

BookGen is a lightweight Python-based static site generator we created to replace GitBook CLI, which had compatibility issues with modern Node.js versions. BookGen provides all the GitBook features without the maintenance burden:

- ✅ Modern, actively maintained
- ✅ No Node.js version conflicts
- ✅ Fast builds (1-2 seconds vs 2-3 minutes)
- ✅ Zero security vulnerabilities
- ✅ Easy to customize

See [BOOKGEN.md](../BOOKGEN.md) for complete documentation.

### Trigger Events
- **Push to main branch**: Automatically builds and deploys when changes are pushed to the main branch
- **Manual dispatch**: Can be manually triggered from the Actions tab in GitHub

### What it does
1. **Build Job**:
   - Checks out the repository
   - Sets up Python environment
   - Validates configuration files (book.json, SUMMARY.md)
   - Installs markdown library
   - Builds the site with BookGen
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
- To modify the build process, edit `.bookgen/generator.py`
- To change the build behavior, modify this workflow file

### Troubleshooting

If the deployment fails:
1. Check the Actions tab for error logs
2. Ensure GitHub Pages is enabled with "GitHub Actions" as the source
3. Verify that the repository has the correct permissions
4. Check that all required files (readme.md, SUMMARY.md, book.json) are present
5. See [BOOKGEN.md](../BOOKGEN.md) for detailed troubleshooting
