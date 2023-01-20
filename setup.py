from setuptools import find_packages
from setuptools import setup

dependencies = [
    "tk",
]

setup(
    name="Forum Lingua",
    version="0.1",
    description="A multi-language translator written in Python and Go",
    author="Nicolas Janis",
    packages=find_packages(),
    install_requires=dependencies,
    entry_points={"console_scripts": ["ForumLingua=python.main:main"]}
)