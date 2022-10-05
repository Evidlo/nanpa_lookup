from setuptools import find_packages, setup

with open("README.md") as f:
    README = f.read()

version = {}

setup(
    # some basic project information
    name="nanpa_lookup",
    version='1.0.1',
    license="GPL3",
    description="Lookup numbers in NANPA database",
    long_description=README,
    long_description_content_type='text/markdown',
    author="Evan Widloski",
    author_email="evan_ex@widloski.com",
    url="https://github.com/evidlo/nanpa_lookup",
    # your project's pip dependencies
    install_requires=[
    ],
    package_data={
    'nanpa_lookup': ['database.sqlite']
    },
    include_package_data=True,
    # automatically look for subfolders with __init__.py
    packages=find_packages(),
    # if you want your code to be able to run directly from command line
    entry_points={
        'console_scripts': [
            'nanpa_lookup = nanpa_lookup.lookup:main',
        ]
    },
)
