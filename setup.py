import os
import sys
import platform
from setuptools import find_packages

# Determine if we should use scikit-build or regular setuptools
if "--no-cmake" in sys.argv:
    sys.argv.remove("--no-cmake")
    use_cmake = False
    from setuptools import setup
else:
    use_cmake = True
    from scikit_build_core.setuptools import setup

# Basic package information
package_info = dict(
    name="pysegreduce",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pybind11>=2.10.0",
    ],
)

# Check if we're running on a supported platform
if platform.system() != "Linux":
    print("Warning: This package is primarily designed for Linux systems.")

if use_cmake:
    # Setup with scikit-build-core
    package_info.update({
        "cmake_args": ["-DCMAKE_BUILD_TYPE=Release"],
        "cmake_install_dir": "pysegreduce",
    })

# Use a single setup call that works for both cases
setup(**package_info) 