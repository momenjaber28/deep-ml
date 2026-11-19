import torch

def reshape_matrix(a, new_shape) -> torch.Tensor:
    """
    Reshape a 2D matrix `a` to shape `new_shape` using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a tensor of shape `new_shape`, or an empty tensor (`torch.tensor([])`)
    if the number of elements does not match.
    """
    # Your implementation here
    if(a.numel()!=(new_shape[0]* new_shape[1])):
        return torch.tensor([])
    
    a=torch.tensor(a).reshape(new_shape)
    return a
    
    pass

