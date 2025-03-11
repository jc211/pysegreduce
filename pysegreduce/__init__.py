"""
PysegReduce - A CUDA-accelerated segmented reduction library for Python.
"""

try:
    from ._pysegreduce import reduce_vec3f, reduce_mat33f
except ImportError:
    import warnings
    warnings.warn(
        "Failed to import PysegReduce CUDA extension. "
        "CUDA functionality will not be available. "
        "Please ensure CUDA is installed and the package was compiled with CUDA support."
    )
    
    def reduce_vec3f(*args, **kwargs):
        raise RuntimeError("PysegReduce CUDA extension is not available")
    
    def reduce_mat33f(*args, **kwargs):
        raise RuntimeError("PysegReduce CUDA extension is not available")

__version__ = "0.1.0" 