from setuptools import find_namespace_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="git-owners",
    version="0.0.4",
    scripts=["src/git-owners"],
    author="Alessandro Crugnola",
    author_email="alessandro.crugnola@gmail.com",
    description="A simple utility to generate a report about the owners of files inside a git repo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sephiroth74/git-owners",
    license="MIT",
    py_modules=[],
    package_dir={"": "src"},
    python_requires=">=3.8",
    packages=find_namespace_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
