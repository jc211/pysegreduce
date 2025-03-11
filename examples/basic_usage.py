"""
Basic usage example for pysegreduce.

This example demonstrates how to use the segmented reduction operations
with PyTorch tensors.
"""

import torch
import pysegreduce

# Check for CUDA availability
if not torch.cuda.is_available():
    print("CUDA is not available. This example requires a CUDA-capable GPU.")
    exit(1)

# Create some test data for vec3f reduction
num_elements = 1000
num_segments = 5
elements_per_segment = num_elements // num_segments

# Create 3D vectors (1000 vectors with 3 elements each)
vec3_data = torch.rand(num_elements, 3, dtype=torch.float32, device='cuda')
# Print first few vectors
print("Input vec3 data (first 5):")
print(vec3_data[:5])

# Create segment boundaries
starts = torch.zeros(num_segments, dtype=torch.int32, device='cuda')
ends = torch.zeros(num_segments, dtype=torch.int32, device='cuda')

for i in range(num_segments):
    starts[i] = i * elements_per_segment
    ends[i] = (i + 1) * elements_per_segment

# Output buffer for results
output = torch.zeros(num_segments, 3, dtype=torch.float32, device='cuda')

# Perform segmented reduction
pysegreduce.reduce_vec3f(
    vec3_data.data_ptr(),
    starts.data_ptr(),
    ends.data_ptr(),
    len(starts),
    output.data_ptr(),
    torch.cuda.current_stream().cuda_stream
)

# Print results
print("\nSegment reduction results:")
for i in range(num_segments):
    print(f"Segment {i}: {output[i].cpu().numpy()}")

# Verify the results
for i in range(num_segments):
    start = int(starts[i])
    end = int(ends[i])
    segment_sum = vec3_data[start:end].sum(dim=0)
    print(f"Verification for segment {i}: {segment_sum.cpu().numpy()}")
    assert torch.allclose(segment_sum, output[i], rtol=1e-5, atol=1e-5)

print("\nAll verifications passed!") 