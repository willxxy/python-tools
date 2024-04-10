import numpy as np
import torch
import random

### ALL SEEDING
fix_seed = 2021
random.seed(fix_seed)
torch.manual_seed(fix_seed)
np.random.seed(fix_seed)
