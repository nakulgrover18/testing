"""Setup script for controlfile interface client"""

from setuptools import setup
import setuptools

REQUIREMENTS = []

with open('requirements.txt') as requirements:
    for requirement in requirements.readlines():
        REQUIREMENTS.append(requirement)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='controlfile_interface_utility',
    version='1.1',
    packages=['controlfile_interface_utility'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tr/cdo_data_lake/wiki/Controlfile-Interface-Utility',
    license='TR',
    author='Commercial Data Organisation',
    author_email='DEVOPS-CDO-DL-TR@thomsonreuters.com',
    install_requires=REQUIREMENTS,
    description='Developed for the controlfile integration',
    python_requires='>=3.6'
)