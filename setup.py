import pathlib
from setuptools import setup
from scabi import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

# test dependencies
test_deps = [
    'pytest',
    'pytest-cov',
]
extras = {
    'test': test_deps,
}

setup(
    name="scabi",
    version=__version__,
    description="Implement vulnerabilities scanning on top of package management system like apt, pip, composer...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/remiflavien1/scabi",
    author="shadawck",
    author_email="hug211mire@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        'Topic :: Security',
    ],
    packages=["scabi"],
    install_requires=["requests", "mitrecve", "getdep", "docopt"],
    tests_require=test_deps,
    extras_require=extras,
    keywords='security, dependencies, package management',
    entry_points={
        "console_scripts": [
            "scabi=scabi.__main__:main",
        ]
    },
)