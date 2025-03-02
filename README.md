# Mathematics and Biology Lab (MathBioLab) Website

This repository contains the source code for the MathBioLab website at the University of Massachusetts Boston. The site is built using [MkDocs Material](https://squidfunk.github.io/mkdocs-material/), a modern static site generator optimized for technical documentation.

## Setup and Installation

### Using uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver. It's recommended for creating and managing virtual environments.

1. Install uv if you don't have it already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create a virtual environment and install dependencies:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

3. Run the development server:
```bash
mkdocs serve
```

4. Visit http://127.0.0.1:8000 to preview the website

### Using pip (Alternative)

1. Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the development server:
```bash
mkdocs serve
```

## Website Structure

- **docs/** - All content is stored as Markdown files in this directory
- **docs/assets/** - Images, CSS, and other static assets
- **docs/news/** - Blog posts and news announcements
- **docs/people/** - Team member profiles and information
- **docs/publications/** - Research papers and publications
- **docs/research/** - Research projects and areas
- **mkdocs.yml** - Main configuration file for the website
- **overrides/** - Custom templates for the site

## Adding Content

### Content Types

1. **News Posts**: Add Markdown files to `docs/news/posts/` with proper frontmatter
2. **Team Members**: Add profiles to `docs/people/profiles/` and update author entries in `.authors.yml`
3. **Publications**: Add papers to `docs/publications/papers/` with appropriate categories and author references
4. **Research Projects**: Add project descriptions to `docs/research/projects/`

### Frontmatter Format

Every content file should include the appropriate YAML frontmatter. For example:

```yaml
---
title: Sample Publication
date: 2024-03-01
categories:
  - Genomics
  - Machine Learning
authors:
  - jsmith
  - mchen
---
```

## Deployment

### GitHub Pages (Recommended)
1. Push the repository to GitHub
2. Enable GitHub Pages in the repository settings
3. Deploy using:
```bash
mkdocs gh-deploy
```

### Traditional Web Server
1. Build the static site:
```bash
mkdocs build
```
2. Copy the contents of the `site` directory to the web server
3. Configure your web server (Nginx/Apache) to serve the static files

## Updating Dependencies

To update all dependencies to their latest compatible versions:

```bash
uv pip sync --upgrade requirements.txt
```

## License

[MIT License](LICENSE)
