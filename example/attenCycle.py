#!/usr/bin/env python
"""Example script to cycle through all attenuation settings on an ARX board
"""

import time
import lwautils.lwa_arx as arx
import lwautils.ArxException as arxe

M_ARX = arx.ARX()

ARX_CHAN_CFG = {}
ARX_CHAN_CFG["dc_on"] = True
ARX_CHAN_CFG["sig_on"] = True
ARX_CHAN_CFG["narrow_lpf"] = True
ARX_CHAN_CFG["narrow_hpf"] = True

for ia in range(58, 63):
    ARX_CHAN_CFG["first_atten"] = ia * 0.5
    ARX_CHAN_CFG["second_atten"] = ia * 0.5
    try:
        M_ARX.set_chan_cfg(2, 0, ARX_CHAN_CFG)
        # Sleep for 10 seconds
        time.sleep(10.0)
    except arxe.ArxException as arx_ex:
        print(arx_ex)
