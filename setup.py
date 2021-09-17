import setuptools
import os

package_name = "nans_are_numbers"
__local__ = os.path.abspath(os.path.dirname(__file__))

f_version = os.path.join(__local__, package_name, "_version.py")
exec(open(f_version).read())

# Get the long description from the relevant file
description = "A data type built entirely of NaNs"

with open("README.md") as FIN:
    long_description = FIN.read()

setuptools.setup(
    name=package_name,
    packages=setuptools.find_packages(),
    # Include package data...
    include_package_data=True,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=__version__,  # noqa: F821
    # The project's main homepage.
    url=f"https://github.com/thoppe/NansAreNumbers",
    # Author details
    author="Travis Hoppe",
    author_email="travis.hoppe+{package_name}@gmail.com",
    # Choose your license
    license="CC-SA",
    install_requires=[],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5  -Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        "Topic :: Artistic Software",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
    ],
    # What does your project relate to?
    keywords=["art", "math"],
    test_suite="pytest",
    tests_require=["pytest"],
)
