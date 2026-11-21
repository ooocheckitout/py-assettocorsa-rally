# py-assettocorsa-rally

The Python library to read shared memory of Assetto Corsa Rally.

## Install

```bash
pip install py-assettocorsa-rally
```

## Example

```python
from acrally import ACRallySharedMemory

try:
    with ACRallySharedMemory() as memory:
        static, physics, graphics = memory.read_snapshot()
        print(static.car_model, static.track, static.track_spline_length)
        print(physics.speed_kmh, physics.rpms, physics.gear, physics.gas, physics.brake)
        print(graphics.current_time, graphics.distance_traveled)
except FileNotFoundError:
    print("The Assetto Corsa Rally shared memory is unavailable. Start the game.")
```

## Available Models

| Model | Page | Description |
| --- | --- | --- |
| [Static](https://github.com/ooocheckitout/py-assettocorsa-rally/blob/main/acrally/models/static.py) | `acpmf_static` | Car, stage, player name, and stage length. |
| [Physics](https://github.com/ooocheckitout/py-assettocorsa-rally/blob/main/acrally/models/physics.py) | `acpmf_physics` | Inputs, engine, motion, wheel, tyre, and brake telemetry. Updates at ~333 Hz. |
| [Graphics](https://github.com/ooocheckitout/py-assettocorsa-rally/blob/main/acrally/models/graphics.py) | `acpmf_graphics` | Stage timer, stage distance, and car position. Updates every rendered frame. |
