cmake_minimum_required(VERSION 3.20...3.27)
project(
    ${SKBUILD_PROJECT_NAME},
    VERSION ${SKBUILD_PROJECT_VERSION}
    LANGUAGES CXX CUDA
)


find_package(Python 3.8 COMPONENTS Interpreter Development.Module REQUIRED)

find_package(pybind11 CONFIG REQUIRED)


pybind11_add_module(_pysegreduce
    src/segmented_reduce.cu
)


install(TARGETS _pysegreduce
    DESTINATION ${Python_SITELIB}
)