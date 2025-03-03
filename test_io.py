import sys
sys.path.append("/home/e78368jw/Documents/MULE/")

from packs.core.io import load_evt_info
from packs.core.io import load_rwf_info

import numpy as np

print(load_evt_info('three_channel.h5'))
print(load_rwf_info('three_channel.h5', samples = 1000))
