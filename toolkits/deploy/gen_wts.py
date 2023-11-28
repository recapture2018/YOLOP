import os, sys
import torch
import struct
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from lib.models import get_net
from lib.config import cfg


# Initialize
device = torch.device('cpu')
# Load model
model = get_net(cfg)
checkpoint = torch.load('weights/End-to-end.pth', map_location=device)
model.load_state_dict(checkpoint['state_dict'])
# load to FP32
model.float()
model.to(device).eval()

with open('yolop.wts', 'w') as f:
    f.write(f'{len(model.state_dict().keys())}\n')
    for k, v in model.state_dict().items():
        vr = v.reshape(-1).cpu().numpy()
        f.write(f'{k} {len(vr)} ')
        for vv in vr:
            f.write(' ')
            f.write(struct.pack('>f',float(vv)).hex())
        f.write('\n')
