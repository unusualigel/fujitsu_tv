"""Use serial protocol of fujitsu_tv to obtain state of the tv."""
from __future__ import annotations

from typing import Final

from homeassistant.const import STATE_OFF, STATE_ON

CONF_WRITE_TIMEOUT: Final = "write_timeout"

DEFAULT_NAME: Final = "Fujitsu TV"
DEFAULT_TIMEOUT: Final = 1
DEFAULT_WRITE_TIMEOUT: Final = 1

ICON: Final = "mdi:remote-tv"

POWER_MODE: Final = "Power Mode"
AUTO_DISPLAY: Final = "Automatic Display"
INPUT_SOURCE: Final = "Input Source"
ASPECT_RATIO: Final = "Aspect Ratio"
STATE_OFF: Final = "1"
STATE_ON: Final = "0"

CONN: "@G\r"
TERM: "@Q\r"
RET: "@S"

# Commands known to the projector
CMD_DICT: Final[dict[str, str]] = {
    POWER_MODE: "%A0080\r",
    AUTO_DISPLAY: "%A0180\r",    
    INPUT_SOURCE: "%A1080\r",
    ASPECT_RATIO: "%A1180\r",
}

