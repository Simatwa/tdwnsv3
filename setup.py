from setuptools import setup, find_packages

__info__ = "Simple local-files server with security on top!"
__version__ = "1.9.2"
__author__ = "Smartwa Caleb"
__email__ = "smartwacaleb@gmail.com"
__repo__ = "https://github.com/Simatwa/tdwnsv3"


def get_file(nm: str) -> list:
    with open(nm, encoding="utf-8") as fp:
        return fp.readlines()


setup(
    name="tdwnsv3",
    packages=find_packages(),
    version=__version__,
    url=__repo__,
    project_urls={"Bug Report": f"{__repo__}/issues/new"},
    license="MIT",
    author=__author__,
    install_requires=[
        "Flask>=2.2.2",
        "cryptography>=39.0.0",
        "appdirs>=1.4.4",
    ],
    author_email=__email__,
    maintainer=__author__,
    maintainer_email=__email__,
    description=__info__,
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
    entry_points={
        "console_scripts": [
            "tdwnsv3 = tdwnsv3.tdwnsv3:main",
        ]
    },
)
