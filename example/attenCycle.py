#!/usr/bin/env python
"""Example script to cycle through all attenuation settings on an ARX board
"""

import time
import lwa_utils.lwa_arx as arx
import lwautils.ArxException as arxe

ma = arx.ARX()

arxChanCfg = {}
arxChanCfg["dc_on"] = True
arxChanCfg["sig_on"] = True
arxChanCfg["narrow_lpf"] = True
arxChanCfg["narrow_hpf"] = True

for ia in range(0,63):
    arxChanCfg["first_atten"] = ia * 0.5
    arxChanCfg["second_atten"] = ia * 0.5
    try:
        ma.set_chan_cfg(2, 0, arxChanCfg)
        # Sleep for 10 seconds
        time.sleep(10.0)
    except arxe.ArxException ae::
        print(ae)
    

