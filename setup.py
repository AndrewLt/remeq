from setuptools import find_packages, setup

with open("remeq/README.md", "r") as f:
    long_description = f.read()

setup(
    name="remeq",
    version="1.0.0",
    description="A simple library for creating message queue based on Redis and its channels",
    package_dir={"": "remeq"},
    packages=find_packages(where="remeq"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="AndrewLt",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=["redis >= 5.0.1", "hiredis >= 2.3.2"],
    python_requires=">=3.11",
)
