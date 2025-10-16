from setuptools import setup, find_packages

setup(
    name="odm-p1d",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        "odmantic",
        "pydantic",
        "pymongo"
    ],
    python_requires=">=3.10",
)
