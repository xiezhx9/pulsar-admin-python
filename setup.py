from setuptools import setup, find_packages

setup(
    name="pulsar_admin",
    version="0.0.2",
    author="hezhangjian",
    author_email="hezhangjian97@gmail.com",
    description="A Python package for interacting with the Pulsar admin API",
    long_description_content_type="text/markdown",
    url="https://github.com/protocol-laboratory/pulsar_admin",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
