# BookGen

**A modern, lightweight static site generator for this repository.**

## What is this?

BookGen is a custom-built alternative to GitBook CLI that generates documentation websites from Markdown files. It was created specifically for this repository to solve compatibility and maintenance issues with GitBook CLI.

## Files in this directory

- **`generator.py`** - The main static site generator script
- **`build.sh`** - Convenience wrapper for building the site

## Quick Start

Build the documentation:

```bash
# From the repository root
./.bookgen/build.sh
```

This will generate the static site in the `_book/` directory.

## Documentation

For complete documentation, see [BOOKGEN.md](../BOOKGEN.md) in the repository root.

## Requirements

- Python 3.6 or higher
- `markdown` Python package

## Why BookGen?

GitBook CLI had several issues:
- ❌ Compatibility problems with Node.js 16+
- ❌ 59+ security vulnerabilities
- ❌ Abandoned since 2018
- ❌ Slow builds (2-3 minutes)

BookGen solves these:
- ✅ Works with any Python 3.6+
- ✅ Zero known vulnerabilities
- ✅ Actively maintained
- ✅ Fast builds (1-2 seconds)

## Features

- Sidebar navigation from SUMMARY.md
- Light/dark theme switching
- Search functionality
- Responsive design
- Code syntax highlighting
- Back to top button
- Print optimization
- SEO friendly

## License

Part of the CURATIONS AI Learning Hub repository.
