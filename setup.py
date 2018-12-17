import os

import sys
from shutil import rmtree

from setuptools import setup, Command


here = os.path.abspath(os.path.dirname(__file__))


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system(
            "{0} setup.py sdist bdist_wheel --universal".format(sys.executable)
        )

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        # self.status("Pushing git tags…")
        # os.system("git tag v{0}".format(about["__version__"]))
        # os.system("git push --tags")

        sys.exit()


setup(
    name="mkdocs-abs-rel-plugin",
    version="0.1",
    packages=["mkdocs_abs_rel_plugin"],
    url="",
    license="MIT",
    author="sander",
    author_email="",
    description="Mkdocs plugin to convert absolute paths to relative ones.",
    entry_points={
        "mkdocs.plugins": [
            "abs-to-rel = mkdocs_abs_rel_plugin.plugin:AbsToRelPlugin"
        ]
    },
    cmdclass={"upload": UploadCommand},
)
