from typing import NewType

from bottles.backend.logger import Logger  # pyright: reportMissingImports=false
from bottles.backend.wine.wineprogram import WineProgram

logging = Logger()


class RunDLL32(WineProgram):
    program = "32-bit DLLs loader and runner"
    command = "rundll32"
