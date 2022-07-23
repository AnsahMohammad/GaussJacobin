import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gaussJacobin",                     # This is the name of the package
    version="4.5.1",                        # The initial release version
    author="AnsahMohammad",                     # Full name of the author
    description="GaussJacobin solver Package in python ",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["gaussJacobin"],             # Name of the python package
    package_dir={'':'gaussJacobin.py'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)