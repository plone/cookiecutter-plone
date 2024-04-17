"""Pre generation hook."""

import re
import sys
from cookieplone.utils import console
from pathlib import Path
from textwrap import dedent
from typing import List


output_path = Path().resolve()

context = {
    "addon_name": "{{ cookiecutter.addon_name }}",
    "addon_title": "{{ cookiecutter.addon_title }}",
    "description": "{{ cookiecutter.description }}",
    "author": "{{ cookiecutter.author }}",
    "email": "{{ cookiecutter.email }}",
    "github_organization": "{{ cookiecutter.github_organization }}",
    "npm_package_name": "{{ cookiecutter.npm_package_name }}",
}


def validate_not_empty(value: str) -> str:
    """Value should not be empty."""
    return "" if value.strip() else "should be provided"


def validate_addon_name(value: str) -> str:
    """Validate addon_name is valid."""
    pattern = "^[a-z0-9-~][a-z0-9-._~]*$"
    if not re.match(pattern, value):
        return "Invalid addon_name"


def validate_npm_package_name(value: str) -> str:
    """Validate npm_package_name is valid."""
    pattern = "^(@[a-z0-9-~][a-z0-9-._~]*\/)?[a-z0-9-~][a-z0-9-._~]*$"
    if not re.match(pattern, value):
        return "Invalid npm_package_name"


VALIDATORS = {
    name: func for name, func in locals().items() if name.startswith("validate_")
}


def check_errors(data: dict) -> List[str]:
    """Check for errors in the provided data."""
    errors = []
    for key, value in data.items():
        func = VALIDATORS.get(f"validate_{key}", validate_not_empty)
        error = func(value)
        if error:
            errors.append(f"  - {key}: {error}")
    return errors


def main():
    """Validate context."""
    success = True
    value_errors = check_errors(context)
    if value_errors:
        msg = "Value errors prevent running cookiecutter:"
        for error in value_errors:
            msg = f"{msg}\n{error}"
        success = False
    else:
        msg = dedent(
            f"""
            Summary:
              - Volto version: [bold blue]{{ cookiecutter.__version_plone_volto }}[/bold blue]
              - Output folder: [bold blue]{output_path}[/bold blue]
        """
        )
    console.panel(
        title = '{{ cookiecutter.addon_title }} generation',
        msg=msg
    )
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
