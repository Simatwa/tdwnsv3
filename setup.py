from setuptools import setup, find_packages
from tdwnsv3 import info, __version__, __author__


def get_file(nm: str) -> list:
    with open(nm, encoding="utf-8") as fp:
        return fp.readlines()


setup(
    name="tdwnsv3",
    packages=find_packages(),
    version=__version__,
    install_requires=get_file("requirements.txt"),
    url="https://github.com/Simatwa/tdwnsv3",
    license="MIT",
    author=__author__,
    author_email="simatwaclb@gmail.com",
    description=info,
    long_description="\n".join(get_file("README.md")),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
