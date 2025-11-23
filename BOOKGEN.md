# BookGen - Modern GitBook Alternative (DEPRECATED)

> **⚠️ DEPRECATED**: This repository has been migrated to Astro with Starlight. BookGen is no longer used for building this documentation site.
> 
> See the main [README.md](readme.md) for information about the current Astro-based documentation system.

---

**Original BookGen Documentation Below**

---

# BookGen - Modern GitBook Alternative

**A lightweight, modern static site generator designed to mirror GitBook features while being compatible with current technology stacks.**

## 📖 Overview

BookGen is a custom-built static site generator created specifically for this repository as a modern alternative to GitBook CLI. It provides all the essential features of GitBook while eliminating compatibility issues with modern Node.js versions.

## 🎯 Why BookGen?

GitBook CLI (v3.2.3) has several limitations:

- **Legacy Software**: Last updated in 2018, not maintained for modern environments
- **Node.js Compatibility**: Has dependency issues with Node.js 16+ (graceful-fs errors)
- **Security Vulnerabilities**: Contains 59+ known vulnerabilities in dependencies
- **No Modern Features**: Lacks contemporary web features and optimizations

BookGen solves these problems by providing:

- ✅ **Modern Technology**: Built with Python 3, stable and widely supported
- ✅ **Zero Compatibility Issues**: No Node.js version conflicts
- ✅ **Lightweight**: ~500 lines of code, easy to maintain and customize
- ✅ **Fast Builds**: Generates complete site in seconds
- ✅ **GitBook-Like Features**: Sidebar navigation, search, theming, responsive design
- ✅ **Easy Deployment**: Works seamlessly with GitHub Actions and Pages

## 🏗️ Architecture

BookGen consists of three main components:

1. **Generator (`generator.py`)**: Core Python script that:
   - Parses `SUMMARY.md` for navigation structure
   - Converts Markdown to HTML using Python-Markdown
   - Generates sidebar navigation
   - Creates responsive HTML pages
   - Copies and generates assets

2. **Build Script (`build.sh`)**: Simple wrapper that:
   - Checks Python availability
   - Installs dependencies
   - Runs the generator
   - Provides user feedback

3. **GitHub Actions Workflow**: Automates:
   - Build on push to main
   - Validation of configuration
   - Deployment to GitHub Pages

## 📂 Directory Structure

```
ai-learning/
├── .bookgen/
│   ├── generator.py      # Core static site generator
│   └── build.sh          # Build wrapper script
├── _book/                # Generated output (git-ignored)
│   ├── assets/           # CSS, JS, and other assets
│   ├── docs/             # Generated HTML pages
│   ├── index.html        # Home page
│   └── .nojekyll         # GitHub Pages configuration
├── docs/                 # Source markdown files
├── book.json             # Configuration (metadata, title, etc.)
├── SUMMARY.md            # Navigation structure
└── readme.md             # Home page content
```

## 🚀 Usage

### Building Locally

**Prerequisites:**
- Python 3.6 or higher
- `markdown` Python package

**Build the site:**

```bash
# Option 1: Use the build script
./.bookgen/build.sh

# Option 2: Run the generator directly
python3 .bookgen/generator.py .
```

**Preview the site:**

```bash
# Serve the _book directory with any HTTP server
python3 -m http.server --directory _book 8000

# Open http://localhost:8000 in your browser
```

### Automatic Deployment

Every push to the `main` branch automatically:

1. Validates configuration files
2. Builds the site with BookGen
3. Deploys to GitHub Pages
4. Makes the site available at: `https://hub.curations.org/`

## 🎨 Features

### Navigation
- **Hierarchical Sidebar**: Automatically generated from `SUMMARY.md`
- **Active Page Highlighting**: Current page highlighted in sidebar
- **Responsive Design**: Mobile-friendly with collapsible sidebar
- **Smooth Scrolling**: Enhanced navigation experience

### Content
- **Markdown Support**: Full markdown syntax including:
  - Headings, paragraphs, lists
  - Code blocks with syntax highlighting
  - Tables, blockquotes, links
  - Footnotes, abbreviations
  - Attributes and metadata
- **Table of Contents**: Auto-generated for each page
- **Clean Typography**: Optimized for readability

### Theming
- **Light/Dark Mode**: Automatic theme switching
- **Theme Persistence**: Remembers user preference
- **System Preference Detection**: Follows OS theme by default
- **Custom Colors**: Easy to customize via CSS variables

### Search
- **Live Search**: Instant search as you type
- **Content Highlighting**: Matched content highlighted on page
- **Auto-scroll**: Automatically scrolls to first match
- **Keyboard Accessible**: Full keyboard navigation support

### Additional Features
- **Back to Top Button**: Appears when scrolling down
- **Print Optimization**: Clean print styles
- **Fast Loading**: Minimal JavaScript, optimized CSS
- **SEO Friendly**: Proper meta tags and semantic HTML
- **Accessible**: ARIA labels and keyboard navigation

## ⚙️ Configuration

### book.json

BookGen reads `book.json` for site metadata:

```json
{
  "title": "Your Site Title",
  "description": "Site description",
  "author": "Author Name",
  "language": "en"
}
```

All fields are optional. BookGen provides sensible defaults.

### SUMMARY.md

Defines the site structure using markdown:

```markdown
# Table of Contents

## Section Name

* [Page Title](path/to/page.md)
* [Another Page](path/to/another.md)

---

## Another Section

* [More Pages](more/pages.md)
```

**Supported formats:**
- Section headers: `## Section Name`
- Separator: `---`
- Links: `* [Title](path.md)`
- Nested structure supported via indentation

## 🎨 Customization

### Styling

All styles are in `_book/assets/style.css` (generated during build).

**Custom CSS variables:**

```css
:root {
    --primary-color: #4a5568;
    --secondary-color: #667eea;
    --background: #ffffff;
    --sidebar-bg: #f7fafc;
    /* ... more variables ... */
}
```

To customize, modify the `generate_css()` method in `generator.py`.

### JavaScript

Interactivity is in `_book/assets/script.js` (generated during build).

Features implemented:
- Theme toggle
- Search functionality
- Back to top button
- Mobile sidebar toggle
- Smooth scrolling

To add features, modify the `generate_js()` method in `generator.py`.

### Layout

The HTML template is in the `generate_html_template()` method.

Structure:
- Header: Site title, search, theme toggle
- Sidebar: Navigation menu
- Main: Page content
- Footer: Build info

## 🔧 Advanced Usage

### Adding New Pages

1. Create a markdown file in the appropriate directory
2. Add it to `SUMMARY.md`
3. Rebuild the site

```bash
# Create new page
echo "# New Page" > docs/new-page.md

# Add to SUMMARY.md
echo "* [New Page](docs/new-page.md)" >> SUMMARY.md

# Rebuild
./.bookgen/build.sh
```

### Customizing the Generator

The generator is designed to be easily modified:

**Add new markdown extensions:**

```python
self.md = markdown.Markdown(extensions=[
    'fenced_code',
    'tables',
    'toc',
    # Add your extension here
    'new_extension',
])
```

**Modify HTML template:**

Edit the `generate_html_template()` method to change page structure.

**Add new features:**

The generator is ~500 lines of clean Python. Easy to read and modify.

## 📊 Performance

### Build Performance
- **Build time**: ~1-2 seconds for 40 pages
- **Generated size**: ~2 MB total
- **Page load time**: < 1 second on modern browsers

### Comparison with GitBook CLI

| Metric | GitBook CLI | BookGen |
|--------|-------------|---------|
| Build time | 2-3 minutes | 1-2 seconds |
| Dependencies | Node.js + 500+ packages | Python + 1 package |
| Compatibility | Node 12-16 only | Python 3.6+ |
| Security issues | 59+ vulnerabilities | 0 known issues |
| Maintenance | Abandoned (2018) | Active |
| Size | ~50 MB | ~500 KB |

## 🐛 Troubleshooting

### Build Fails

**Error: `ModuleNotFoundError: No module named 'markdown'`**

Solution:
```bash
pip3 install markdown
```

**Error: `FileNotFoundError: SUMMARY.md not found`**

Solution: Ensure `SUMMARY.md` exists in the repository root.

**Error: `Permission denied: ./.bookgen/build.sh`**

Solution:
```bash
chmod +x ./.bookgen/build.sh
```

### Pages Not Showing

**Check that:**
1. Page is listed in `SUMMARY.md`
2. File path in `SUMMARY.md` is correct
3. Markdown file exists at that path
4. You've rebuilt the site after changes

**Verify paths:**
```bash
# List all markdown files
find . -name "*.md" -type f

# Check SUMMARY.md links
grep -oP '\]\(\K[^)]+' SUMMARY.md
```

### Styling Issues

**Theme not persisting:**
- Check browser localStorage is enabled
- Clear browser cache and reload

**Responsive issues:**
- Test in browser dev tools
- Check viewport meta tag is present
- Verify mobile CSS media queries

## 🔐 Security

BookGen has several security advantages:

- **No known vulnerabilities**: Zero dependencies with security issues
- **Simple codebase**: Easy to audit (~500 lines)
- **No external requests**: All assets bundled
- **Safe markdown rendering**: Uses python-markdown (trusted library)
- **No user input processing**: Static generation only

## 🚀 Future Enhancements

Possible improvements (contributions welcome):

- [ ] Plugin system for extensibility
- [ ] Multiple theme support
- [ ] Full-text search with index
- [ ] Multi-language support
- [ ] Automatic image optimization
- [ ] PDF export functionality
- [ ] Analytics integration
- [ ] Custom plugins for advanced markdown features

## 🤝 Contributing

BookGen is designed to be easily customizable. To contribute:

1. Modify `.bookgen/generator.py`
2. Test your changes locally
3. Update documentation if adding features
4. Submit a pull request

## 📝 License

BookGen is part of the CURATIONS AI Learning Hub repository. See repository license for details.

## 🙏 Credits

Built with:
- **Python-Markdown**: Markdown to HTML conversion
- **GitHub Pages**: Hosting platform
- **GitHub Actions**: CI/CD automation

Inspired by:
- **GitBook**: Original concept and design patterns
- **Material Design**: Modern UI principles
- **Read the Docs**: Documentation best practices

## 📚 Resources

- [Python-Markdown Documentation](https://python-markdown.github.io/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Markdown Guide](https://www.markdownguide.org/)

---

**BookGen** - A modern, maintainable alternative to GitBook CLI.

*Built with ❤️ for the CURATIONS community.*
