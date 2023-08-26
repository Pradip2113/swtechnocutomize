from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cutomize/__init__.py
from cutomize import __version__ as version

setup(
	name="cutomize",
	version=version,
	description="Customize",
	author="Quantbit Team",
	author_email="abhishek.shinde@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
