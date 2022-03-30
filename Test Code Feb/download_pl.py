import os, warnings
from pynq import PL
from pynq import Overlay

if not os.path.exists("base.bit"):
    warnings.warn('There is no overlay loaded after boot.', UserWarning)
    
ol = Overlay('base.bit')
