"""Post generation hook."""

from collections import OrderedDict  # noQA
from pathlib import Path

from cookieplone import generator
from cookieplone.utils import console, files

context = {{cookiecutter}}


GHA_FILES = [".github"]


DEVOPS_TO_REMOVE = {
    "ansible": [
        "devops/.env_dist",
        "devops/.gitignore",
        "devops/ansible.cfg",
        "devops/etc",
        "devops/inventory",
        "devops/Makefile",
        "devops/playbooks",
        "devops/requirements",
        "devops/tasks",
        "devops/README.md",
    ],
    "gha": [
        ".github/workflows/manual_deploy.yml",
        "devops/.env_gha",
        "devops/README-GHA.md",
    ],
}


def prepare_devops(context: OrderedDict, output_dir: Path):
    """Clean up devops."""
    keep_ansible = int(context.get("devops_ansible"))
    keep_gha_manual_deploy = int("{{ cookiecutter.devops_gha_deploy }}")

    to_remove = []
    if not keep_ansible:
        to_remove.extend(DEVOPS_TO_REMOVE["ansible"])
    if not keep_gha_manual_deploy:
        to_remove.extend(DEVOPS_TO_REMOVE["gha"])
    base_path = Path().cwd()
    files.remove_files(base_path, to_remove)


def prepare_backend(context, output_dir):
    """Run Plone Addon generator."""
    # Go to backend/src/
    output_dir = output_dir / "backend" / "src"
    folder_name = context.get("python_package_name")
    generator.generate_subtemplate(
        "plone_addon", output_dir, folder_name, context, GHA_FILES
    )


def prepare_frontend(context, output_dir):
    """Run volto generator."""
    generator.generate_subtemplate(
        "volto_addon", output_dir, "frontend", context, GHA_FILES
    )


def prepare_cache(context: OrderedDict, output_dir: Path):
    """Add cache structure."""
    # Use the same base folder
    folder_name = output_dir.name
    output_dir = output_dir.parent
    generator.generate_subtemplate("sub_cache", output_dir, folder_name, context)


def prepare_settings(context: OrderedDict, output_dir: Path):
    """Configure language and other settings."""
    # Use the same base folder
    folder_name = output_dir.name
    output_dir = output_dir.parent
    generator.generate_subtemplate(
        "sub_policy_package", output_dir, folder_name, context
    )


def main():
    """Final fixes."""
    output_dir = Path().cwd()
    # Setup Devops
    prepare_devops(context, output_dir)
    # Setup frontend
    prepare_frontend(context, output_dir)
    # Setup backend
    prepare_backend(context, output_dir)
    # Configure language and other settings
    prepare_settings(context, output_dir)
    # Setup Cache
    if int("{{ cookiecutter.devops_cache }}"):
        prepare_cache(context, output_dir)
    msg = """
        [bold blue]{{ cookiecutter.title }}[/bold blue]

        Now, code it, create a git repository, push to your organization.

        Sorry for the convenience,
        The Plone Community.
    """
    console.panel(
        title="New project was generated",
        subtitle="",
        msg=msg,
        url="https://plone.org/",
    )


if __name__ == "__main__":
    main()
