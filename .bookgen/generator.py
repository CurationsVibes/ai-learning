#!/usr/bin/env python3
"""
BookGen - A Modern GitBook Alternative
A lightweight static site generator that mirrors GitBook features
"""

import os
import re
import json
import markdown
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional

class BookGen:
    """Custom static site generator mirroring GitBook features"""
    
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.output_dir = self.root_dir / "_book"
        self.config = self.load_config()
        
        # Markdown extensions similar to GitBook
        self.md = markdown.Markdown(extensions=[
            'fenced_code',
            'tables',
            'toc',
            'codehilite',
            'nl2br',
            'sane_lists',
            'meta',
            'attr_list',
            'def_list',
            'footnotes',
            'admonition'
        ])
    
    def load_config(self) -> Dict:
        """Load book.json configuration"""
        config_path = self.root_dir / "book.json"
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def parse_summary(self) -> List[Dict]:
        """Parse SUMMARY.md to extract navigation structure"""
        summary_path = self.root_dir / "SUMMARY.md"
        if not summary_path.exists():
            raise FileNotFoundError("SUMMARY.md not found")
        
        with open(summary_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        navigation = []
        current_section = None
        
        # Parse markdown links [Title](path)
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            
            # Section headers (## or ### or ----)
            if line.startswith('#') or line == '---':
                if line.startswith('##'):
                    section_title = line.lstrip('#').strip()
                    current_section = {
                        'title': section_title,
                        'type': 'section',
                        'items': []
                    }
                    navigation.append(current_section)
                continue
            
            # Parse links [Title](path)
            match = re.match(r'\s*\*\s*\[(.*?)\]\((.*?)\)', line)
            if match:
                title, path = match.groups()
                item = {
                    'title': title,
                    'path': path,
                    'type': 'page'
                }
                
                if current_section:
                    current_section['items'].append(item)
                else:
                    navigation.append(item)
        
        return navigation
    
    def render_markdown(self, file_path: Path) -> Tuple[str, Dict]:
        """Render markdown file to HTML with metadata"""
        if not file_path.exists():
            return f"<p>File not found: {file_path}</p>", {}
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Reset markdown instance for new file
        self.md.reset()
        html_content = self.md.convert(content)
        metadata = self.md.Meta if hasattr(self.md, 'Meta') else {}
        
        return html_content, metadata
    
    def generate_sidebar(self, navigation: List[Dict], current_path: str = "") -> str:
        """Generate sidebar navigation HTML"""
        html = '<nav class="book-sidebar">\n'
        html += '<div class="book-sidebar-content">\n'
        
        for item in navigation:
            if item['type'] == 'section':
                html += f'<div class="sidebar-section">\n'
                html += f'<h3 class="sidebar-section-title">{item["title"]}</h3>\n'
                html += '<ul class="sidebar-list">\n'
                
                for subitem in item['items']:
                    active = 'active' if subitem['path'] == current_path else ''
                    html += f'<li class="sidebar-item {active}">\n'
                    html += f'  <a href="/{subitem["path"].replace(".md", ".html")}">{subitem["title"]}</a>\n'
                    html += '</li>\n'
                
                html += '</ul>\n'
                html += '</div>\n'
            
            elif item['type'] == 'page':
                active = 'active' if item['path'] == current_path else ''
                html += f'<div class="sidebar-item {active}">\n'
                html += f'  <a href="/{item["path"].replace(".md", ".html")}">{item["title"]}</a>\n'
                html += '</div>\n'
        
        html += '</div>\n'
        html += '</nav>\n'
        
        return html
    
    def generate_html_template(self, title: str, content: str, sidebar: str, 
                              config: Dict, toc: str = "") -> str:
        """Generate complete HTML page"""
        site_title = config.get('title', 'Documentation')
        
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{config.get('description', '')}">
    <meta name="author" content="{config.get('author', '')}">
    <title>{title} - {site_title}</title>
    <link rel="stylesheet" href="/assets/style.css">
    <link rel="stylesheet" href="/assets/highlight.css">
</head>
<body>
    <div class="book-container">
        <div class="book-header">
            <div class="book-header-content">
                <h1 class="book-title">{site_title}</h1>
                <div class="book-header-controls">
                    <input type="search" class="search-input" placeholder="Search..." id="search-input">
                    <button class="theme-toggle" id="theme-toggle" title="Toggle theme">
                        <span class="theme-icon">🌓</span>
                    </button>
                </div>
            </div>
        </div>
        
        <div class="book-body">
            {sidebar}
            
            <main class="book-main">
                <div class="book-content">
                    {content}
                </div>
                
                <footer class="book-footer">
                    <div class="book-footer-content">
                        <p>Built with BookGen - A modern GitBook alternative</p>
                        <p>Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
                    </div>
                </footer>
            </main>
            
            {f'<aside class="book-toc">{toc}</aside>' if toc else ''}
        </div>
    </div>
    
    <script src="/assets/script.js"></script>
</body>
</html>'''
        
        return html
    
    def generate_css(self) -> str:
        """Generate modern CSS styling"""
        return '''/* BookGen - Modern GitBook Alternative Styles */

:root {
    --primary-color: #4a5568;
    --secondary-color: #667eea;
    --background: #ffffff;
    --sidebar-bg: #f7fafc;
    --text-color: #2d3748;
    --text-muted: #718096;
    --border-color: #e2e8f0;
    --code-bg: #f7fafc;
    --link-color: #667eea;
    --link-hover: #5a67d8;
    --shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
}

[data-theme="dark"] {
    --primary-color: #cbd5e0;
    --secondary-color: #667eea;
    --background: #1a202c;
    --sidebar-bg: #2d3748;
    --text-color: #e2e8f0;
    --text-muted: #a0aec0;
    --border-color: #4a5568;
    --code-bg: #2d3748;
    --link-color: #7c8fed;
    --link-hover: #9ca3f5;
    --shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.3);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 16px;
    line-height: 1.6;
    color: var(--text-color);
    background: var(--background);
    transition: background 0.3s, color 0.3s;
}

.book-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.book-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: var(--background);
    border-bottom: 1px solid var(--border-color);
    z-index: 100;
    box-shadow: var(--shadow);
}

.book-header-content {
    max-width: 1400px;
    margin: 0 auto;
    height: 100%;
    padding: 0 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.book-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--primary-color);
}

.book-header-controls {
    display: flex;
    gap: 15px;
    align-items: center;
}

.search-input {
    padding: 8px 15px;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    background: var(--background);
    color: var(--text-color);
    font-size: 14px;
    width: 250px;
    transition: border-color 0.3s;
}

.search-input:focus {
    outline: none;
    border-color: var(--secondary-color);
}

.theme-toggle {
    background: none;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    padding: 8px 12px;
    cursor: pointer;
    font-size: 20px;
    transition: all 0.3s;
}

.theme-toggle:hover {
    background: var(--sidebar-bg);
}

.book-body {
    display: flex;
    margin-top: 60px;
    flex: 1;
}

.book-sidebar {
    width: 280px;
    position: fixed;
    left: 0;
    top: 60px;
    bottom: 0;
    background: var(--sidebar-bg);
    border-right: 1px solid var(--border-color);
    overflow-y: auto;
    padding: 20px;
}

.sidebar-section {
    margin-bottom: 25px;
}

.sidebar-section-title {
    font-size: 0.875rem;
    font-weight: 600;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 10px;
    letter-spacing: 0.05em;
}

.sidebar-list {
    list-style: none;
}

.sidebar-item {
    margin-bottom: 5px;
}

.sidebar-item a {
    display: block;
    padding: 8px 12px;
    color: var(--text-color);
    text-decoration: none;
    border-radius: 4px;
    transition: all 0.2s;
}

.sidebar-item a:hover {
    background: var(--background);
    color: var(--link-color);
}

.sidebar-item.active a {
    background: var(--secondary-color);
    color: white;
    font-weight: 500;
}

.book-main {
    flex: 1;
    margin-left: 280px;
    padding: 40px 60px;
    max-width: 900px;
}

.book-content {
    margin-bottom: 60px;
}

.book-content h1 {
    font-size: 2.5rem;
    margin-bottom: 20px;
    color: var(--primary-color);
}

.book-content h2 {
    font-size: 2rem;
    margin-top: 40px;
    margin-bottom: 15px;
    color: var(--primary-color);
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 10px;
}

.book-content h3 {
    font-size: 1.5rem;
    margin-top: 30px;
    margin-bottom: 10px;
    color: var(--primary-color);
}

.book-content p {
    margin-bottom: 15px;
    line-height: 1.7;
}

.book-content a {
    color: var(--link-color);
    text-decoration: none;
}

.book-content a:hover {
    color: var(--link-hover);
    text-decoration: underline;
}

.book-content ul, .book-content ol {
    margin-bottom: 15px;
    padding-left: 30px;
}

.book-content li {
    margin-bottom: 8px;
}

.book-content code {
    background: var(--code-bg);
    padding: 2px 6px;
    border-radius: 3px;
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
    font-size: 0.9em;
}

.book-content pre {
    background: var(--code-bg);
    padding: 15px;
    border-radius: 6px;
    overflow-x: auto;
    margin-bottom: 20px;
    border: 1px solid var(--border-color);
}

.book-content pre code {
    background: none;
    padding: 0;
}

.book-content blockquote {
    border-left: 4px solid var(--secondary-color);
    padding-left: 20px;
    margin: 20px 0;
    color: var(--text-muted);
    font-style: italic;
}

.book-content table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
}

.book-content th, .book-content td {
    padding: 12px;
    text-align: left;
    border: 1px solid var(--border-color);
}

.book-content th {
    background: var(--sidebar-bg);
    font-weight: 600;
}

.book-footer {
    margin-top: 60px;
    padding-top: 30px;
    border-top: 1px solid var(--border-color);
}

.book-footer-content {
    text-align: center;
    color: var(--text-muted);
    font-size: 0.875rem;
}

.book-footer-content p {
    margin-bottom: 5px;
}

/* Responsive Design */
@media (max-width: 768px) {
    .book-sidebar {
        transform: translateX(-100%);
        transition: transform 0.3s;
        z-index: 50;
    }
    
    .book-sidebar.open {
        transform: translateX(0);
    }
    
    .book-main {
        margin-left: 0;
        padding: 20px;
    }
    
    .search-input {
        width: 150px;
    }
}

/* Print Styles */
@media print {
    .book-header,
    .book-sidebar,
    .book-footer {
        display: none;
    }
    
    .book-main {
        margin-left: 0;
    }
}
'''
    
    def generate_js(self) -> str:
        """Generate JavaScript for interactivity"""
        return '''// BookGen - Interactive Features

// Theme Toggle
const themeToggle = document.getElementById('theme-toggle');
const root = document.documentElement;

// Load saved theme or detect preference
const savedTheme = localStorage.getItem('theme') || 
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
root.setAttribute('data-theme', savedTheme);

themeToggle.addEventListener('click', () => {
    const currentTheme = root.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
});

// Simple Search Functionality
const searchInput = document.getElementById('search-input');
let searchIndex = [];

// Build search index from page content
function buildSearchIndex() {
    const content = document.querySelector('.book-content');
    if (!content) return;
    
    const headings = content.querySelectorAll('h1, h2, h3');
    headings.forEach(heading => {
        searchIndex.push({
            text: heading.textContent,
            element: heading,
            level: heading.tagName
        });
    });
}

// Search functionality
searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase();
    
    if (query.length < 2) {
        clearHighlights();
        return;
    }
    
    clearHighlights();
    
    searchIndex.forEach(item => {
        if (item.text.toLowerCase().includes(query)) {
            item.element.style.backgroundColor = 'rgba(102, 126, 234, 0.2)';
            item.element.style.transition = 'background-color 0.3s';
        }
    });
    
    // Scroll to first match
    const firstMatch = searchIndex.find(item => 
        item.text.toLowerCase().includes(query)
    );
    if (firstMatch) {
        firstMatch.element.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
});

function clearHighlights() {
    searchIndex.forEach(item => {
        item.element.style.backgroundColor = '';
    });
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// Mobile sidebar toggle
const sidebarToggle = document.createElement('button');
sidebarToggle.className = 'sidebar-toggle';
sidebarToggle.innerHTML = '☰';
sidebarToggle.style.cssText = `
    display: none;
    position: fixed;
    top: 70px;
    left: 10px;
    z-index: 101;
    background: var(--secondary-color);
    color: white;
    border: none;
    border-radius: 4px;
    padding: 10px 15px;
    font-size: 20px;
    cursor: pointer;
`;

if (window.innerWidth <= 768) {
    document.body.appendChild(sidebarToggle);
    sidebarToggle.style.display = 'block';
}

sidebarToggle.addEventListener('click', () => {
    const sidebar = document.querySelector('.book-sidebar');
    sidebar.classList.toggle('open');
});

// Initialize
buildSearchIndex();

// Back to top functionality
window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        if (!document.querySelector('.back-to-top')) {
            const backToTop = document.createElement('button');
            backToTop.className = 'back-to-top';
            backToTop.innerHTML = '↑';
            backToTop.style.cssText = `
                position: fixed;
                bottom: 30px;
                right: 30px;
                background: var(--secondary-color);
                color: white;
                border: none;
                border-radius: 50%;
                width: 50px;
                height: 50px;
                font-size: 24px;
                cursor: pointer;
                box-shadow: var(--shadow);
                z-index: 99;
                transition: all 0.3s;
            `;
            backToTop.addEventListener('click', () => {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
            document.body.appendChild(backToTop);
        }
    } else {
        const backToTop = document.querySelector('.back-to-top');
        if (backToTop) {
            backToTop.remove();
        }
    }
});
'''
    
    def copy_assets(self):
        """Copy or generate necessary assets"""
        assets_dir = self.output_dir / "assets"
        assets_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate CSS
        with open(assets_dir / "style.css", 'w', encoding='utf-8') as f:
            f.write(self.generate_css())
        
        # Generate JavaScript
        with open(assets_dir / "script.js", 'w', encoding='utf-8') as f:
            f.write(self.generate_js())
        
        # Simple syntax highlighting CSS
        highlight_css = '''/* Code Highlighting */
.codehilite { background: var(--code-bg); padding: 15px; border-radius: 6px; }
.codehilite .c { color: #999; } /* Comment */
.codehilite .k { color: #e06c75; font-weight: bold; } /* Keyword */
.codehilite .s { color: #98c379; } /* String */
.codehilite .n { color: #61afef; } /* Name */
.codehilite .o { color: #c678dd; } /* Operator */
'''
        with open(assets_dir / "highlight.css", 'w', encoding='utf-8') as f:
            f.write(highlight_css)
    
    def build(self):
        """Build the complete static site"""
        print("🚀 BookGen - Building your documentation...")
        
        # Clean and create output directory
        if self.output_dir.exists():
            import shutil
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Parse navigation
        print("📖 Parsing SUMMARY.md...")
        navigation = self.parse_summary()
        
        # Copy assets
        print("🎨 Generating styles and scripts...")
        self.copy_assets()
        
        # Collect all pages to build
        pages_to_build = []
        
        def collect_pages(items):
            for item in items:
                if item['type'] == 'page':
                    pages_to_build.append(item)
                elif item['type'] == 'section' and 'items' in item:
                    collect_pages(item['items'])
        
        collect_pages(navigation)
        
        # Build index page (readme.md)
        readme_path = self.root_dir / "readme.md"
        if readme_path.exists():
            print("🏠 Building home page...")
            sidebar_html = self.generate_sidebar(navigation, "readme.md")
            content_html, metadata = self.render_markdown(readme_path)
            
            full_html = self.generate_html_template(
                title="Home",
                content=content_html,
                sidebar=sidebar_html,
                config=self.config
            )
            
            index_output = self.output_dir / "index.html"
            with open(index_output, 'w', encoding='utf-8') as f:
                f.write(full_html)
        
        # Build all pages
        print(f"📝 Building {len(pages_to_build)} pages...")
        for page in pages_to_build:
            page_path = self.root_dir / page['path']
            if not page_path.exists():
                print(f"⚠️  Warning: {page['path']} not found, skipping...")
                continue
            
            sidebar_html = self.generate_sidebar(navigation, page['path'])
            content_html, metadata = self.render_markdown(page_path)
            
            full_html = self.generate_html_template(
                title=page['title'],
                content=content_html,
                sidebar=sidebar_html,
                config=self.config
            )
            
            # Create output path
            output_path = self.output_dir / page['path'].replace('.md', '.html')
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_html)
        
        # Copy .nojekyll if exists
        nojekyll = self.root_dir / ".nojekyll"
        if nojekyll.exists():
            import shutil
            shutil.copy(nojekyll, self.output_dir / ".nojekyll")
        
        print(f"✅ Build complete! Output in {self.output_dir}")
        print(f"📊 Generated {len(pages_to_build) + 1} pages")

def main():
    """Main entry point"""
    import sys
    
    root_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    try:
        generator = BookGen(root_dir)
        generator.build()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
