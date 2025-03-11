# PysegReduce

A CUDA-accelerated segmented reduction library for Python.

## Description

PysegReduce provides high-performance segmented reduction operations implemented in CUDA, exposed to Python through pybind11 bindings. It currently supports:

- Segmented reduction of 3D vectors (`reduce_vec3f`)
- Segmented reduction of 3x3 matrices (`reduce_mat33f`)

These operations are useful in a variety of contexts where you need to perform segmented reductions on GPU data, without transferring the data back to the CPU.

## Requirements

- Python 3.8 or higher
- CUDA Toolkit 10.0 or higher
- A CUDA-capable GPU

## Installation

### From Source

1. Ensure CUDA Toolkit is installed and `CUDA_HOME` is set correctly
2. Install the package:

```bash
pip install .
```

### From PyPI

```bash
pip install pysegreduce
```

## Usage

```python
import torch
import pysegreduce

# For vec3f reduction
# Prepare your data - must be contiguous in memory
vec3_data = torch.rand(1000, 3, dtype=torch.float32, device='cuda')
# Segment boundaries
starts = torch.tensor([0, 200, 400, 600, 800], dtype=torch.int32, device='cuda')
ends = torch.tensor([200, 400, 600, 800, 1000], dtype=torch.int32, device='cuda')
# Output buffer
output = torch.zeros(5, 3, dtype=torch.float32, device='cuda')

# Perform segmented reduction
pysegreduce.reduce_vec3f(
    vec3_data.data_ptr(),
    starts.data_ptr(),
    ends.data_ptr(),
    len(starts),
    output.data_ptr(),
    torch.cuda.current_stream().cuda_stream
)

# Similarly for mat33f reduction with 3x3 matrices
```

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 