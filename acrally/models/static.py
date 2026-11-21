from ctypes import (
    LittleEndianStructure,
    sizeof,
    c_float,
    c_uint8,
    c_wchar,
)


class StaticPage(LittleEndianStructure):
    car_model: str
    track: str
    player_name: str
    track_spline_length: float

    _layout_ = "ms"
    _pack_ = 4

    _fields_ = [
        ("_unused_0", (c_uint8 * 68)),
        ("car_model", (c_wchar * 33)),
        ("track", (c_wchar * 33)),
        ("player_name", (c_wchar * 33)),
        ("_unused_266", (c_uint8 * 254)),
        ("track_spline_length", c_float),
        ("_unused_524", (c_uint8 * 296)),
    ]


assert sizeof(StaticPage) == 820, "StaticPage differs from the ACR ABI"
