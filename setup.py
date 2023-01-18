import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="magneticfielddb",
    version="0.1.1",
    author="Matthias Wiesenberger",
    author_email="mattwi@fysik.dtu.dk",
    description="Store and access magnetic field coefficients for Feltor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/feltor-dev/magneticfielddb",
    #packages=setuptools.find_packages(),
    pymodules=["magneticfielddb"],
    include_package_data=True,
    #    Accept all data files and directories matched by MANIFEST.in.
    package_data={
        "": ["data/*"]
    },
    #    Specify additional patterns to match files that may or may not be matched by MANIFEST.in or found in source control.
    exclude_package_data={"": ["polynomial_field.py"]},
    #    Specify patterns for data files and directories that should not be included when a package is installed, even if they would otherwise have been included due to the use of the preceding options.

    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific simulations :: Libraries",
        "Topic :: Utilities",
    ],
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
