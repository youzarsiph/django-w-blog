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

A reusable blog app powered by Python, Django, DRF, Wagtail CMS, TailwindCSS and DaisyUI.

## Get started

Install the package:

```console
pip install django-w-blog
```

Configure your `Django` settings:

```python
# project/settings.py

# Application definition
INSTALLED_APPS = [
    "blog",
    "blog.api",  # Optional if you do not want to use the API
    "blog.apps.articles",
    "blog.apps.categories",
    "blog.apps.home",
    "blog.apps.indexes",
    "blog.apps.tags",
    "blog.cms",
    "blog.ui",
    # Deps
    "rest_wind",  # Optional if you do not want to use the API
    "rest_framework",  # Optional if you do not want to use the API
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
    ...
]
```

Run the migrations:

```console
# In your project root
python mange.py migrate
```

Update your `URLConf`:

```python
# project/urls.py

from django.urls import include, path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    path("", include("blog.ui.urls")),
    path("api/", include("blog.api.urls")),  # Optional if you do not want to use the API
    path("api/", include("rest_framework.urls")),  # Optional if you do not want to use the API
    ...
    path("documents/", include(wagtaildocs_urls)),
    path("dashboard/", include(wagtailadmin_urls)),
    path("", include(wagtail_urls)),  # Make sure this line is the last
]
```

## Key Features

- **CI/CD Pipelines**: Automated using GitHub Actions to ensure consistent and reliable deployment processes.
- **Dependency Management**: Powered by Poetry, a sophisticated tool for managing project dependencies with precision and reliability.
- **Code Formatting**: Automatically formatted with Black to maintain a consistent and readable codebase.
- **Code Linting**: Utilizes Ruff to identify and address potential issues early, enhancing code quality and maintainability.
- **Code Testing**: Utilizes Django to run tests.
- **Configuration Files**: Includes `.gitignore`, `pyproject.toml`, and other essential configuration files to streamline setup.

## Contributing

We warmly welcome contributions from the community. Please refer to our [CONTRIBUTING](CONTRIBUTING.md) guide for detailed instructions on how to contribute effectively. Your feedback and participation are essential for the continued improvement of this template.

## Support

For inquiries or support, please open an issue or join the discussion in the [GitHub Discussions](https://github.com/youzarsiph/django-w-blog/discussions) section to engage with the community.

## Licensing

This project is licensed under the MIT License. A detailed copy of the terms can be found in the [LICENSE](LICENSE) file.
