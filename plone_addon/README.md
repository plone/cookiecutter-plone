[![Cookiecutter Plone Addon CI](https://github.com/plone/cookiecutter-plone/actions/workflows/ci.yml/badge.svg)](https://github.com/plone/cookiecutter-plone/actions/workflows/plone_addon.yml)
[![Built with Cookiecutter](https://img.shields.io/badge/built%20with-Cookiecutter-ff69b4.svg?logo=cookiecutter)](https://github.com/plone/cookiecutter-plone/)
![GitHub](https://img.shields.io/github/license/plone/cookiecutter-plone)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Cookiecutter Plone Addon

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), [Cookiecutter Plone Addon](https://github.com/plone/cookiecutter-plone/plone_addon) is intended to be used by Plone developers to create new addon paclages.

## Getting Started 🏁

### Prerequisites

- **pipx**: A handy tool for installing and running Python applications.

### Installation Guide 🛠️

1. **pipx**

```shell
pip install pipx
```
### Generate Your Plone Addon 🎉

```shell
pipx run cookiecutter gh:plone/cookiecutter-plone
```
Then select the `Plone Add-on` template.


## Project Generation Options

These are all the template options that will be prompted by the [Cookiecutter CLI](https://github.com/cookiecutter/cookiecutter) before generating your project.

| Option                | Description                                                                                                                                          | Example                       |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `addon_title`  | Your addon's human-readable name, capitals and spaces allowed.                                                                                     | **Plone Blog**                |
| `description`         | Describes your addon and gets used in places like ``README.md`` and such.                                                                          | **Create awesome blogs with Plone.** |
| `author`              | This is you! The value goes into places like ``LICENSE``, ``setup.py`` and such.                                                                     | **Our Company**               |
| `email`               | The email address you want to identify yourself in the project.                                                                                      | **email@example.com**         |
| `github_organization` | Used for GitHub and Docker repositories.                                                                                                             | **collective**                |
| `python_package_name` | Name of the Python package used to configure your project. It needs to be Python-importable, so no dashes, spaces or special characters are allowed. | **collective.blog**    |


## Code Quality Assurance 🧐

Your package comes equipped with linters to ensure code quality. Run the following to automatically format your code:

```shell
make format
```

## Internationalization 🌐

Generate translation files with ease:

```shell
make i18n
```
## License 📜

This project is licensed under the [MIT License](/LICENSE).

## Let's Get Building! 🚀

Happy coding!
