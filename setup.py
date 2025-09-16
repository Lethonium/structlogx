from setuptools import setup, find_packages

setup(
    name="structlogx",  # Replace with your package's preferred name
    version="0.1.1",  # Start with an initial version (e.g., 0.1.0)
    description="A simple Python logging package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",  # To display README.md on PyPI
    author="lethonium",
    author_email="info@lethonium.com",
    url="https://github.com/Lethonium/structlogx",  # Use your GitHub URL
    license="MIT",  # Choose your license, e.g., MIT, Apache
    packages=find_packages(),  # Automatically find the `my_logger` package
    install_requires=["python-json-logger"],  # List any dependencies, e.g., ['requests']
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",  # Specify supported Python versions
)