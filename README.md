# Mathematics and Biology Lab (MathBioLab) at the University of Massachusetts Boston

This repository contains the source code of the MathBioLab at UMass Boston website.

## Setup

1. Install the requirements:
```bash
pip install -r requirements.txt
```

2. Run the development server:
```bash
mkdocs serve
```

3. Visit http://127.0.0.1:8000 to preview the website

## Adding Content

- Add markdown files in the `docs` directory
- Update the navigation in `mkdocs.yml`
- Place logo in `docs/assets/images/logo.png`

## Deployment

### Option 1: GitHub Pages (Recommended)
1. Push the repository to GitHub
2. Enable GitHub Pages in the corresponding repository settings
3. Deploy using:
```bash
mkdocs gh-deploy
```

### Option 2: Traditional Web Server
1. Build the site:
```bash
mkdocs build
```
2. Copy the contents of the `site` directory to the web server
3. Configure your web the (Nginx/Apache) to serve the static files
