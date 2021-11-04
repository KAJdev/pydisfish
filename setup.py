import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

version = ''
with open('pydisfish/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setuptools.setup(
     name='pydisfish',
     version=version,
     author='kajdev',
     description="A small module to easily interact with discord's phishing domain list.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/kajdev/pydisfish",
     packages=["pydisfish"],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=requirements
 )
