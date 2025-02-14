# UMBiBio Website

This is a MkDocs-based website using the Material theme.

## Setup

1. Install the requirements:
```bash
pip install -r requirements.txt
```

2. Run the development server:
```bash
mkdocs serve
```

3. Visit http://127.0.0.1:8000 to see your site

## Adding Content

- Add your markdown files in the `docs` directory
- Update the navigation in `mkdocs.yml`
- Place your logo in `docs/assets/images/logo.png`

## Deployment

### Option 1: GitHub Pages (Recommended)
1. Push your repository to GitHub
2. Enable GitHub Pages in your repository settings
3. Deploy using:
```bash
mkdocs gh-deploy
```

### Option 2: Netlify/Vercel
1. Connect your repository
2. Set build command: `mkdocs build`
3. Set publish directory: `site`

### Option 3: Traditional Web Server
1. Build the site:
```bash
mkdocs build
```
2. Copy the contents of the `site` directory to your web server
3. Configure your web server (Nginx/Apache) to serve the static files
