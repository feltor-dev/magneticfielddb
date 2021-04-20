import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="magneticfielddb",
    version="0.1.0",
    author="Matthias Wiesenberger",
    author_email="mattwi@fysik.dtu.dk",
    description="Store and access magnetic field coefficients for Feltor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/feltor-dev/magneticfielddb",
    #pymodules=["magneticfielddb"],
    #packages=["magneticfielddb"],
    #package_dir={"":"src"},
    packages=setuptools.find_packages(),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific simulations :: Libraries",
        "Topic :: Utilities",
    ],
    python_requires='>=3.6',
    setup_requires=['pytest-runner', 'importlib_resources'],
    tests_require=['pytest']
)
