from setuptools import setup, find_packages
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

version = ""
with open("ez_db/__init__.py") as file:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', file.read(), re.MULTILINE).group(1)

description = "Async sqlite database handler for the faint of heart."
long_description = "A package that simplifies async database configuration with simple to understand functions!"
    
setup(
    name="ez-db",
    version=version,
    author="Timothy Pidashev",
    url="https://github.com/timothypidashev/ez-db",
    author_email="<pidashev.tim@gmail.com>",
    description=description,
    long_description_content_type="text/markdown",
    long_description=long_description,
    license="MIT",
    packages=find_packages(),
    keywords=["python", "async sqlite", "easy database" "ezdb"],
    python_requires=">=3.5.3",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)