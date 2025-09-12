# django-w-blog

[![CI](https://github.com/youzarsiph/django-w-blog/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/django-w-blog/actions/workflows/ci.yml)
[![CD](https://github.com/youzarsiph/django-w-blog/actions/workflows/cd.yml/badge.svg)](https://github.com/youzarsiph/django-w-blog/actions/workflows/cd.yml)
[![Code Style: Black](https://github.com/youzarsiph/django-w-blog/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/django-w-blog/actions/workflows/black.yml)
[![Code Linting: Ruff](https://github.com/youzarsiph/django-w-blog/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/django-w-blog/actions/workflows/ruff.yml)
[![Docker Image](https://github.com/youzarsiph/django-w-blog/actions/workflows/docker-image.yml/badge.svg)](https://github.com/youzarsiph/django-w-blog/actions/workflows/docker-image.yml)
[![Docker Publish](https://github.com/youzarsiph/django-w-blog/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/youzarsiph/django-w-blog/actions/workflows/docker-publish.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/django-w-blog?logo=pypi&logoColor=white)](https://pypi.org/project/django-w-blog/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-w-blog?logo=python&logoColor=white)](https://pypi.org/project/django-w-blog/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/django-w-blog?logo=pypi&logoColor=white)](https://pypi.org/project/django-w-blog/)
[![PyPI - License](https://img.shields.io/pypi/l/django-w-blog?logo=pypi&logoColor=white)](https://pypi.org/project/django-w-blog/)

## Overview

A reusable, production-ready blog application built with Python, Django, Django REST Framework, and Wagtail CMS, styled with Tailwind CSS and daisyUI. It ships with sane defaults, modern theming, and clean APIs to help you launch quickly and scale confidently.

---

## Key features

- **Full CMS:** Wagtail-powered editorial experience with pages, media, search, and governance.
- **Modern UI:** Tailwind CSS for utility-first styling and responsive layouts.
- **Theming:** All daisyUI themes supported, plus the ability to define custom themes.
- **API ready:** Optional REST API endpoints for content delivery and integrations.
- **CI/CD:** GitHub Actions pipelines for consistent, automated testing and deployment.
- **Dependencies:** Managed with Poetry for reproducibility and clarity.
- **Formatting:** Black for automatic, consistent code formatting.
- **Linting:** Ruff for fast, comprehensive linting.
- **Testing:** Django test runner for unit and integration tests.
- **Configs included:** `.gitignore`, `pyproject.toml`, and other boilerplate to streamline setup.

---

## Installation

```console
pip install django-w-blog
```

---

## Configuration

### Add installed apps

```python
# project/settings.py

INSTALLED_APPS = [
    "blog",
    "blog.api",  # Optional if you don't need the API
    "blog.apps.articles",
    "blog.apps.categories",
    "blog.apps.home",      # Optional if your project includes a Home model ('home.Home')
    "blog.apps.indexes",
    "blog.apps.tags",
    "blog.cms",
    "blog.ui",

    # Dependencies
    "rest_wind",           # Optional if you don't need the API
    "rest_framework",      # Optional if you don't need the API
    "wagtail.contrib.search_promotions",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    # ...
]
```

### Run migrations

```console
# In your project root
python manage.py migrate
```

### Update URL configuration

```python
# project/urls.py

from django.urls import include, path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path("", include("blog.ui.urls")),
    path("api/", include("blog.api.urls")),           # Optional if you don't need the API
    path("api/", include("rest_framework.urls")),     # Optional if you don't need the API
    # ...
    path("documents/", include(wagtaildocs_urls)),
    path("dashboard/", include(wagtailadmin_urls)),
    path("", include(wagtail_urls)),                  # Keep this as the last pattern
]
```

---

## Theming and templates

Each template in django-w-blog extends `blog/base.html`. Start by creating this base template in your project and customize it to match your brand.

### Create the blog template directory

```console
mkdir -p your_app/templates/blog
```

### Create the base template

```console
touch your_app/templates/blog/base.html
```

You can extend `blog/base.html` in your own templates or override any provided template for full control.

### Available blocks and context

- **`blog/base.html`**
  - **Blocks:**
    - **theme:** Default daisyUI theme
    - **toggle_theme:** Secondary daisyUI theme
    - **head:** HTML head content
    - **title:** Page title
    - **styles:** CSS styles links
    - **navbar:** Navigation bar
    - **branding:** Branding in navbar
    - **navbar_center:** Centered navbar links
    - **navbar_end:** Right-aligned navbar links
    - **content:** Main content
    - **footer:** Page footer
    - **drawer_branding:** Sidebar branding
    - **drawer_content:** Sidebar content
  - **Context:**
    - **home:** Site root page

- **`blog/index.html`**
  - **Blocks:** All blocks from `blog/base.html`
  - **Context:**
    - **index:** Blog index page
    - **articles:** Latest blog articles

- **`blog/category.html`**
  - **Blocks:** All blocks from `blog/base.html`
  - **Context:**
    - **category:** Category instance

- **`blog/article.html`**
  - **Blocks:** All blocks from `blog/base.html`
  - **Context:**
    - **article:** Article instance

- **`blog/search.html`**
  - **Blocks:** All blocks from `blog/base.html`
  - **Context:**
    - **search_results:** Results as a `PageQuerySet`

---

## Contributing

We welcome contributions. Please review the [CONTRIBUTING](CONTRIBUTING.md) guide for setup, coding standards, and workflow. Opening an issue before major changes helps align on scope and direction.

---

## Support

For questions, bug reports, or feature requests, open an issue or start a thread in [GitHub Discussions](https://github.com/youzarsiph/django-w-blog/discussions).

---

## License

This project is available under the MIT License. See the [LICENSE](LICENSE) file for details.
