### set number of CPU threads
import torch
torch.set_num_threads(2) # 4 is also good


### Seeding
# This still produces random x
torch.manual_seed(0)
for i in range(10):
    x = torch.rand(5, 3)
    print(x)
  
# This produces same x
for i in range(10):
    torch.manual_seed(0)
    x = torch.rand(5, 3)
    print(x)

# counts the number of parameters in a model
def count_parameters(model: nn.Module) -> int:
    return sum(p.numel() for p in model.parameters() if p.requires_grad)
