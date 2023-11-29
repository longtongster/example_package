# Import required functions
from setuptools import setup, find_packages

setup(
    author="<your-name>",
    description="A package for converting imperial lengths and weights.",
    name="impyrial",
    # defines what we should include from the package
    packages=find_packages(include=["impyrial", "impyrial.*"]),
    version="0.1.0",

    # defines the dependencies that should be installed
    # this can of course also be provided in a requirements.txt file 
    # install_requires=["numpy>=1.10", "pandas"],

    # you can also define the python version that is required
    # here we define that the version should be higher than
    # 2.7 but should not be any version 3.0 or 3.1
    # python_requires='2.7, !=3.0.*, !=3.1.*'

)