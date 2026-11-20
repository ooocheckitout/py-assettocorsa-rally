from ctypes import (
    LittleEndianStructure,
    sizeof,
    c_float,
    c_int32,
    c_uint8,
    c_wchar,
)
from typing import Sequence


class GraphicsPage(LittleEndianStructure):
    packet_id: int
    current_time: str
    distance_traveled_m: float
    car_coordinates: Sequence[Sequence[float]]

    _layout_ = "ms"
    _pack_ = 4

    _fields_ = [
        ("packet_id", c_int32),
        ("_unused_4", (c_uint8 * 8)),
        ("current_time", (c_wchar * 15)),
        ("_unused_42", (c_uint8 * 114)),
        ("distance_traveled_m", c_float),
        ("_unused_160", (c_uint8 * 96)),
        ("car_coordinates", ((c_float * 3) * 60)),
        ("_unused_976", (c_uint8 * 612)),
    ]


assert sizeof(GraphicsPage) == 1588, "GraphicsPage differs from the ACR ABI"
