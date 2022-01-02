from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in card/__init__.py
from card import __version__ as version

setup(
	name="card",
	version=version,
	description="Print multi document in page.",
	author="amadhaji@open-alt.com",
	author_email="amadhaji@open-alt.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
