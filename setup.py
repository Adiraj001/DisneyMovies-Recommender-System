from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

Author_NAME = "Aditya Raj Pandey"
SRC = 'src'
LIST_OF_REQUIREMENTS = ["streamlit"]

setup(
    name="SRC_repo",
    version="0.0.1",
    author=Author_NAME,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=LIST_OF_REQUIREMENTS,
    packages=[SRC],
)