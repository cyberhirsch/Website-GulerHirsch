# Clay Theme (Astro Edition)

[![Netlify Status](https://api.netlify.com/api/v1/badges/098d9ba5-fd1a-4c6b-83c1-0b70fd7e017c/deploy-status)](https://app.netlify.com/projects/clay-astro-theme/deploys)
[![Built with Astro](https://img.shields.io/badge/Built%20with-Astro-orange?style=flat-square&logo=astro&logoColor=white)](https://astro.build)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://opensource.org/licenses/MIT)

A minimalist, image-centric theme for photographers and artists. Originally a Gatsby theme, now fully ported to **Astro** for superior performance and modern development experience.

> **Note**: This theme is a modern Astro port of the beautiful [Clay Theme](https://github.com/lilxyzz/clay-theme) by `lilxyzz`.

<p align="center">
  <img src="public/img/clay_astro_light.png" width="48%" alt="Light Mode" style="border-radius: 10px; border: 1px solid #ddd;">
  <img src="public/img/clay_astro_dark.png" width="48%" alt="Dark Mode" style="border-radius: 10px; border: 1px solid #333;">
</p>

Check out the [Live Demo](https://clay-astro-theme.netlify.app) or view on the [Astro Themes Portal](https://portal.astro.build/themes/clay/).

## Features

-   **Astro-Powered**: Blazing fast static site generation with zero-JS output by default.
-   **Client Router**: Seamless client-side navigation (formerly View Transitions) for an SPA-like feel.
-   **Responsive Design**: Mobile-friendly layout with a collapsible menu.
-   **Dark Mode**: Native dark mode support with a toggle switch and persistence.
-   **CMS Ready**: Pre-configured with **Decap CMS** (formerly Netlify CMS) for easy content management.
-   **Scoped CSS**: Modular, component-scoped styles replacing legacy monolithic CSS.
-   **Typography**:
    -   **Titles/Menu**: Futura (Small Caps)
    -   **Body**: EB Garamond
-   **Content Collections**: Type-safe Markdown content management for Work, News, Sold items, and Pages.

## Project Structure

```text
/
├── public/                 # Static assets (images, admin config)
│   ├── admin/              # Decap CMS configuration
│   └── img/                # Uploaded images
├── src/
│   ├── components/         # Reusable Astro components (PostCard, etc.)
│   ├── content/            # Content Collections (Markdown/MDX)
│   │   ├── news/
│   │   ├── pages/
│   │   ├── sold/
│   │   └── work/
│   ├── layouts/            # Main layouts (Layout.astro)
│   ├── pages/              # Route definitions
│   │   ├── index.astro     # Home page
│   │   ├── [slug].astro    # Dynamic route for generic pages
│   │   └── work/[slug].astro # Dynamic routes for collections
│   ├── styles/             # Global variables and resets
│   │   ├── content.css     # Typography for markdown content
│   │   └── vars.css        # CSS Variables (Colors, Fonts)
│   └── templates/          # Templates for different content types
└── astro.config.mjs        # Astro configuration
```

## Getting Started

1.  **Install Dependencies**:

    ```bash
    npm install
    ```

2.  **Start Development Server**:

    ```bash
    npm run dev
    ```

    Visit `http://localhost:4321` to see your site.

3.  **Build for Production**:

    ```bash
    npm run build
    ```

    The output will be in the `dist/` directory.

## Customization

### Fonts & Colors
Edit `src/styles/vars.css` to update CSS variables for colors, fonts, and breakpoints.

### Content
-   Add markdown files to `src/content/` folders.
-   Or use the Admin panel at `/admin` (requires local backend or Netlify deployment).

### Navigation
Edit the `<nav>` section in `src/layouts/Layout.astro` to update valid menu links.

## License

MIT
