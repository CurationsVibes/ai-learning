# GitBook Integration Guide

This document explains the GitBook integration in this repository and how it's configured for GitHub Pages hosting.

## Overview

This repository uses GitBook to generate static documentation from Markdown files. The documentation is automatically built and deployed to GitHub Pages using GitHub Actions.

## Repository Structure

```
ai-learning/
├── .github/
│   └── workflows/
│       ├── deploy-pages.yml    # GitHub Actions workflow for deployment
│       └── README.md            # Workflow documentation
├── docs/                        # Main documentation folder
│   ├── cookbooks/              # AI × Human Cookbook content
│   ├── about-curations.md      # About CURATIONS
│   ├── about-curationsla.md    # About CurationsLA
│   └── ...                     # Other documentation files
├── .gitbook.yaml               # GitBook configuration
├── .nojekyll                   # Tells GitHub Pages not to use Jekyll
├── book.json                   # GitBook CLI configuration and plugins
├── SUMMARY.md                  # Table of contents
└── readme.md                   # Landing page
```

## GitBook Configuration Files

### 1. `.gitbook.yaml`
The main GitBook configuration file that defines:
- Root directory for documentation
- Structure (readme, summary, glossary, etc.)
- URL redirects for moved pages

This file is used by the GitBook platform (gitbook.com) and newer GitBook versions.

### 2. `book.json`
Configuration for GitBook CLI (legacy but still widely used):
- Book metadata (title, author, description)
- GitBook version
- Plugins and their configurations
- Custom links in the sidebar
- Theme settings

### 3. `SUMMARY.md`
The table of contents that defines the navigation structure. This file uses Markdown with links to create a hierarchical menu.

### 4. `readme.md`
The landing page/home page of the documentation.

## GitBook Plugins

The following plugins are configured in `book.json`:

- **search-plus**: Enhanced search functionality
- **fontsettings**: Allows users to customize font size and family
- **sharing**: Social sharing buttons (configured for Twitter)
- **page-toc**: Automatic table of contents for each page
- **back-to-top-button**: Adds a "back to top" button for long pages
- **expandable-chapters**: Collapsible chapters in the sidebar

## GitHub Pages Deployment

### How it Works

1. When changes are pushed to the `main` branch, the GitHub Actions workflow is triggered
2. The workflow installs GitBook CLI and builds the documentation
3. GitBook generates static HTML files in the `_book/` directory
4. These files are uploaded and deployed to GitHub Pages
5. The site becomes available at `https://<username>.github.io/<repository>/`

### Setup Instructions

To enable GitHub Pages for this repository:

1. **Go to Repository Settings**
   - Navigate to Settings > Pages

2. **Configure Source**
   - Under "Source", select "GitHub Actions"
   - This allows the workflow to deploy automatically

3. **Custom Domain (Optional)**
   - If you want to use a custom domain, add a `CNAME` file to the repository root
   - Add your domain name in the file (e.g., `docs.curations.org`)
   - Configure DNS settings with your domain provider

4. **Wait for Deployment**
   - The first deployment happens automatically after setup
   - Check the "Actions" tab to monitor the deployment progress

## Local Development

To build and preview the GitBook locally:

### Prerequisites
```bash
# Install Node.js (version 12 or higher recommended)
# Then install GitBook CLI globally
npm install -g gitbook-cli
```

### Build and Serve
```bash
# Install plugins (first time only)
gitbook install

# Build the book
gitbook build

# Serve locally (opens browser automatically)
gitbook serve
```

The local server will be available at `http://localhost:4000`

## Adding New Content

### Adding a New Page

1. **Create the Markdown file** in the appropriate directory
   ```bash
   # Example: adding a new cookbook
   touch docs/cookbooks/new-cookbook.md
   ```

2. **Add content** to the file using Markdown syntax

3. **Update SUMMARY.md** to include the new page in the navigation
   ```markdown
   * [New Cookbook Title](docs/cookbooks/new-cookbook.md)
   ```

4. **Commit and push** the changes
   ```bash
   git add .
   git commit -m "Add new cookbook"
   git push
   ```

5. The GitHub Actions workflow will automatically rebuild and deploy

### Organizing Content

- Use folders to group related content (e.g., `docs/cookbooks/`)
- Keep the folder structure shallow (2-3 levels deep maximum)
- Use descriptive file names with hyphens (e.g., `quantum-prompting.md`)
- Update `SUMMARY.md` to reflect the hierarchy

## Customization

### Changing the Theme

GitBook CLI supports custom themes. To change the theme:

1. Find a GitBook theme (e.g., from npm or GitHub)
2. Add it to `book.json` plugins:
   ```json
   "plugins": ["theme-custom"]
   ```
3. Configure theme settings in `pluginsConfig`

### Adding Custom CSS

Create a `styles/website.css` file in the repository root:
```css
/* Custom styles */
.book-summary {
  background-color: #f5f5f5;
}
```

### Adding Custom JavaScript

Create a `book.js` file in the repository root for custom scripts.

## Troubleshooting

### Build Fails

**Problem**: GitBook CLI fails to install or build

**Solutions**:
- Ensure Node.js version is compatible (12.x - 16.x recommended)
- Try clearing npm cache: `npm cache clean --force`
- Check for errors in `book.json` syntax (must be valid JSON)

### Plugins Not Working

**Problem**: Plugins don't appear after installation

**Solutions**:
- Run `gitbook install` to ensure plugins are installed
- Check plugin compatibility with GitBook version 3.2.3
- Remove problematic plugins from `book.json`

### Pages Not Updating

**Problem**: Changes don't appear on the deployed site

**Solutions**:
- Check the Actions tab for build/deploy errors
- Ensure changes were pushed to the `main` branch
- Clear browser cache or try incognito mode
- Wait a few minutes for GitHub Pages cache to clear

### Broken Links

**Problem**: Internal links showing 404 errors

**Solutions**:
- Verify file paths in SUMMARY.md are correct
- Use relative paths (e.g., `docs/file.md` not `/docs/file.md`)
- Check that all referenced files exist in the repository
- Update the `redirects` section in `.gitbook.yaml` for moved pages

## GitBook vs GitHub Pages

### GitBook Platform (gitbook.com)
- Hosted service with automatic builds
- Modern interface with built-in features
- Free tier available for public documentation
- Uses `.gitbook.yaml` for configuration

### GitHub Pages (this setup)
- Free hosting from GitHub
- Full control over build process
- Uses GitBook CLI (legacy but stable)
- Requires GitHub Actions for automation

### Why Both?

This repository is configured to work with both:
- `.gitbook.yaml` for GitBook platform integration
- `book.json` for GitBook CLI (GitHub Pages)
- `SUMMARY.md` and markdown files work with both

## Best Practices

1. **Keep Content Modular**: One topic per file, reusable sections
2. **Use Consistent Formatting**: Follow Markdown best practices
3. **Update SUMMARY.md**: Always reflect the current structure
4. **Write Clear Titles**: Descriptive headings for navigation
5. **Test Locally**: Preview changes before pushing
6. **Version Control**: Use meaningful commit messages
7. **Documentation First**: Document as you build

## Additional Resources

- [GitBook Documentation](https://docs.gitbook.com/)
- [GitBook CLI (Legacy)](https://github.com/GitbookIO/gitbook)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Markdown Guide](https://www.markdownguide.org/)

## Support

For issues specific to this repository:
- Check existing documentation
- Review the Actions tab for build logs
- Refer to the troubleshooting section above

For GitBook or GitHub Pages issues:
- Consult official documentation
- Check community forums and Stack Overflow
- Review relevant GitHub repositories for examples
