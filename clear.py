import os
import subprocess
from typing import Final

IS_WINDOWS: Final[bool] = os.name == 'nt'
CLEAR_CMD: Final[str] = 'cls' if IS_WINDOWS else 'clear'

def clear() -> None:
    """Clears terminal screen."""
    try:
        if IS_WINDOWS:
            subprocess.run(CLEAR_CMD, shell=True, check=True)
        else:
            subprocess.run([CLEAR_CMD], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\n" * 100)