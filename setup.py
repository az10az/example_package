import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_package",
    version="0.0.1",
    author="Arlens",
    author_email="email@gmail.com",
    description="Neural Correspondence Mapping Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/az10az/example_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=[
	'numpy',
	'pandas',
    ]
)
