# GitHub Actions Workflows

## deploy-pages.yml

This workflow automatically builds and deploys the documentation to GitHub Pages using **Astro + Starlight**.

### Why Astro + Starlight?

Astro is a modern static site generator with excellent performance, and Starlight is a documentation theme built specifically for Astro. Together they provide:

- ⚡ **Lightning-fast builds**: ~15 seconds for 40+ pages
- 🔍 **Built-in search**: Pagefind integration with 6,763 words indexed
- 🎨 **Modern UI**: Light/Dark/Auto theme support
- 📱 **Mobile-first**: Fully responsive design
- 🚀 **Active ecosystem**: Regular updates and community support
- ♿ **Accessible**: ARIA labels and keyboard navigation

See [MIGRATION.md](../../MIGRATION.md) for migration details.

### Trigger Events
- **Push to main branch**: Automatically builds and deploys when changes are pushed to the main branch (excluding markdown-only changes in certain directories)
- **Manual dispatch**: Can be manually triggered from the Actions tab in GitHub

### What it does
1. **Build Job**:
   - Checks out the repository with full history
   - Sets up Node.js 20.x environment with npm caching
   - Validates configuration files (astro.config.mjs, package.json, content directory)
   - Installs npm dependencies
   - Builds the site with Astro
   - Verifies build output and reports statistics
   - Uploads the built files as a Pages artifact

2. **Deploy Job**:
   - Takes the built artifact from the build job
   - Deploys it to GitHub Pages
   - Reports deployment status and URL
   - Publishes the site at: `https://curationsla.github.io/ai-learning/`

### Setup Requirements

To enable this workflow, you need to:

1. **Enable GitHub Pages** in repository settings:
   - Go to Settings > Pages
   - Under "Build and deployment" > "Source", select "GitHub Actions"

2. **Verify Workflow Permissions** in Settings > Actions > General:
   - Ensure "Read and write permissions" is selected
   - The workflow has the necessary permissions defined in the YAML file

3. **Branch Protection** (optional but recommended):
   - Protect the main branch to ensure quality control
   - Require status checks before merging

### Build Optimizations

The workflow includes several optimizations:

- **Path-based triggers**: Skips builds for documentation-only changes to certain legacy files
- **npm caching**: Speeds up dependency installation
- **Validation steps**: Catches configuration errors before building
- **Build verification**: Ensures output is complete before deployment
- **Concurrency control**: Prevents conflicting deployments

### Customization

- To use a custom domain, add a `CNAME` file to the `public/` directory with your domain
- To modify the build process, edit `astro.config.mjs` or `package.json` scripts
- To change styling, edit `src/styles/custom.css`
- To change the sidebar navigation, edit the sidebar property in `astro.config.mjs`

### Troubleshooting

If the deployment fails:
1. Check the Actions tab for error logs
2. Ensure GitHub Pages is enabled with "GitHub Actions" as the source
3. Verify that the repository has the correct permissions
4. Check that all required files are present:
   - `astro.config.mjs` - Astro configuration
   - `package.json` - Dependencies and scripts
   - `src/content/docs/` - Content directory
5. Review validation step output for specific errors
6. Ensure Node.js version matches the workflow (20.x)

### Common Issues

**Build fails with TypeScript errors:**
- Run `npm run build` locally to see the errors
- Check frontmatter in markdown files
- Ensure all content files have required `title` field

**Deployment succeeds but site shows 404:**
- Verify the `base` path in `astro.config.mjs` matches your repository name
- Check that the `site` URL is correct
- Clear browser cache and try again

**Search not working:**
- Search is only generated in production builds
- Ensure Pagefind step completed in the build logs

For more detailed troubleshooting, see [MIGRATION.md](../../MIGRATION.md).
