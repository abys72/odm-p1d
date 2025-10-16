from setuptools import setup, find_packages

setup(
    name="odm_p1d",
    version="0.0.3",
    packages=find_packages(),
    install_requires=[
        "odmantic",
        "pydantic",
        "pymongo"
    ],
    python_requires=">=3.10",
)
