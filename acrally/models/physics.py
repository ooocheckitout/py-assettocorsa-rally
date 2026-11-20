from ctypes import (
    LittleEndianStructure,
    sizeof,
    c_float,
    c_int32,
    c_uint8,
)
from typing import Sequence


class PhysicsPage(LittleEndianStructure):
    packet_id: int
    gas: float
    brake: float
    fuel: float
    gear: int
    rpm: int
    steer_angle: float
    speed_kmh: float
    velocity: Sequence[float]
    g_force: Sequence[float]
    wheel_slip: Sequence[float]
    wheel_load: Sequence[float]
    wheel_pressure: Sequence[float]
    wheel_angular_speed: Sequence[float]
    tyre_core_temperature_k: Sequence[float]
    suspension_travel: Sequence[float]
    heading: float
    pitch: float
    roll: float
    air_temperature_k: float
    road_temperature_k: float
    local_angular_velocity: Sequence[float]
    final_ff: float
    brake_temperature_k: Sequence[float]
    clutch: float
    tyre_contact_point: Sequence[Sequence[float]]
    tyre_contact_normal: Sequence[Sequence[float]]
    tyre_contact_heading: Sequence[Sequence[float]]
    brake_bias: float
    local_velocity: Sequence[float]
    max_rpm: int
    mz: Sequence[float]
    fx: Sequence[float]
    fy: Sequence[float]
    slip_ratio: Sequence[float]
    slip_angle: Sequence[float]
    water_temperature: float
    ignition_on: int
    starter_engine_on: int
    is_engine_running: int
    slip_vibration: float
    g_vibration: float

    _layout_ = "ms"
    _pack_ = 4

    _fields_ = [
        ("packet_id", c_int32),
        ("gas", c_float),
        ("brake", c_float),
        ("fuel", c_float),
        ("gear", c_int32),
        ("rpm", c_int32),
        ("steer_angle", c_float),
        ("speed_kmh", c_float),
        ("velocity", (c_float * 3)),
        ("g_force", (c_float * 3)),
        ("wheel_slip", (c_float * 4)),
        ("wheel_load", (c_float * 4)),
        ("wheel_pressure", (c_float * 4)),
        ("wheel_angular_speed", (c_float * 4)),
        ("_unused_120", (c_uint8 * 32)),
        ("tyre_core_temperature_k", (c_float * 4)),
        ("_unused_168", (c_uint8 * 16)),
        ("suspension_travel", (c_float * 4)),
        ("_unused_200", (c_uint8 * 8)),
        ("heading", c_float),
        ("pitch", c_float),
        ("roll", c_float),
        ("_unused_220", (c_uint8 * 68)),
        ("air_temperature_k", c_float),
        ("road_temperature_k", c_float),
        ("local_angular_velocity", (c_float * 3)),
        ("final_ff", c_float),
        ("_unused_312", (c_uint8 * 36)),
        ("brake_temperature_k", (c_float * 4)),
        ("clutch", c_float),
        ("_unused_368", (c_uint8 * 52)),
        ("tyre_contact_point", ((c_float * 3) * 4)),
        ("tyre_contact_normal", ((c_float * 3) * 4)),
        ("tyre_contact_heading", ((c_float * 3) * 4)),
        ("brake_bias", c_float),
        ("local_velocity", (c_float * 3)),
        ("_unused_580", (c_uint8 * 8)),
        ("max_rpm", c_int32),
        ("mz", (c_float * 4)),
        ("fx", (c_float * 4)),
        ("fy", (c_float * 4)),
        ("slip_ratio", (c_float * 4)),
        ("slip_angle", (c_float * 4)),
        ("_unused_672", (c_uint8 * 40)),
        ("water_temperature", c_float),
        ("_unused_716", (c_uint8 * 56)),
        ("ignition_on", c_int32),
        ("starter_engine_on", c_int32),
        ("is_engine_running", c_int32),
        ("_unused_784", (c_uint8 * 4)),
        ("slip_vibration", c_float),
        ("g_vibration", c_float),
        ("_unused_796", (c_uint8 * 4)),
    ]


assert sizeof(PhysicsPage) == 800, "PhysicsPage differs from the ACR ABI"
