[![Releases](https://img.shields.io/github/v/release/danilopeixoto/gitlab-changelog?color=blue)](https://github.com/danilopeixoto/gitlab-changelog/releases)
[![Issues](https://img.shields.io/github/issues/danilopeixoto/gitlab-changelog?color=blue)](https://github.com/danilopeixoto/gitlab-changelog/issues)
[![Pull requests](https://img.shields.io/github/issues-pr/danilopeixoto/gitlab-changelog?color=blue)](https://github.com/danilopeixoto/gitlab-changelog/pulls)
[![License](https://img.shields.io/pypi/l/gitlab-changelog?color=blue)](LICENSE.md)

# GitLab Changelog

Automatically generate changelogs from merge requests on GitLab.

GitLab Changelog automatically creates changelogs by analyzing merge requests that have been merged since the latest tag for a specific branch. It utilizes a customizable template to generate the changelogs.

Template variables:

- `tag_name`
- `tag_url`
- `tag_date`
- `features`
- `improvements`
- `bug_fixes`

```
# Changelog

## [{{ tag_name }}]({{ tag_url }}) ({{ tag_date.strftime('%Y-%m-%d') }})
{% if features %}

### New features

{% for feature in features %}
- {{ feature }}
{% endfor %}
{% endif %}
{% if improvements %}

### Improvements

{% for improvement in improvements %}
- {{ improvement }}
{% endfor %}
{% endif %}
{% if bug_fixes %}

### Bug fixes

{% for bug_fix in bug_fixes %}
- {{ bug_fix }}
{% endfor %}
{% endif %}
```

The tool determines the release version and notes by inspecting the titles and labels of the merge requests:

Scoped labels:

- `type::feature`
- `type::improvement`
- `type::bugfix`

Basic labels:

- `breakingchange`

If no merge requests are available, a feature release is generated based on the project description.

The versioning scheme follows the [Semantic Versioning (SemVer)](https://semver.org) specification.

## Prerequisites

* [Python (>=3.8.0)](https://www.python.org)

## Installation

### Production

Install package:

```console
pip install gitlab-changelog
```

### Development

Install package:

```console
pip install -e .[development]
```

> **Note** Use the `-e, --editable` flag to install the package in development mode.

> **Note** Set up a virtual environment for development.

Sort imports:

```console
isort .
```

Format source code:

```console
autopep8 --recursive --in-place .
```

Check static typing:

```console
mypy .
```

Lint source code:

```console
pylint setup.py gitlab_changelog tests/
```

Test package:

```console
pytest
```

Report test coverage:

```console
pytest --cov
```

> **Hint** See also the [`Makefile`](Makefile) for development.

## Usage

Generate changelog content:

```console
gitlab-changelog --project-id <project-id> generate
```

The command-line application will also retrieve configuration from specific environment variables:

- `CI_SERVER_URL`
- `GITLAB_ACCESS_TOKEN`
- `CI_PROJECT_ID`

## Copyright and license

Copyright (c) 2023, Danilo Peixoto Ferreira. All rights reserved.

Project developed under [BSD-3-Clause License](LICENSE.md).
