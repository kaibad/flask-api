# __all__ = ["user_controller"]

import glob
import os

__all__ = [
    os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")
]
