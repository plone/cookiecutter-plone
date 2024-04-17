"""Post generation hook."""
from cookieplone.utils import console


def main():
    """Final fixes."""
    msg = """
        [bold blue]{{ cookiecutter.addon_name }}[/bold blue]

        Now, enter the generated directory and finish the install:

        cd {{ cookiecutter.addon_name }}
        make install

        start coding, and push to your organization.

        Sorry for the convenience,
        The Plone Community.
    """
    console.panel(
        title="New addon was generated",
        subtitle="",
        msg=msg,
        url="https://plone.org/"
    )



if __name__ == "__main__":
    main()
