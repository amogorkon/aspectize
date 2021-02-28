
from setuptools import find_packages, setup

with open("README.md") as f:
    LONG_DESCRIPTION = f.read()
  
setup(
    name="aspectize",
    description="Decorate (almost) EVERYTHING! - a simple, yet powerful Python 3 functional decorator lib inspired by the AOP paradigm",
    long_description=LONG_DESCRIPTION,
    license="MIT",
    url="https://github.com/amogorkon/aspectize",
    version="0.0.0",
    author="Anselm Kiefner",
    python_requires="=>3.9",
    keywords=["aop", "decorator", "debugging", "logging"],
    author_email="aspectize-pypi@anselm.kiefner.de",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        ],
    packages=find_packages(where="src/aspectize"),
    package_dir={"": "src/aspectize/"},
    long_description_content_type="text/markdown",
)
