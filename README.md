# RoboArt

### Avatars lovingly delivered by Robohash.org

RoboArt is a basic random avatar generator which generates avatar in 4 different sets when hash is provided.

## Installation

You can install RoboArt via pip:

```bash
pip install roboart
```

## Usage

Import RoboArt in your Python script and create an instance of the roboart class:

```python
from roboart import roboart
ra = roboart()
```

Then, generate an avatar by passing a hash value to the robo() method:

```python
ra.robo("thisishash")
```

This will generate an avatar based on the provided hash value.

## Quick Example

```python
from roboart import roboart

ra = roboart()

ra.robo("Robot") # It generates a robot avatar
ra.monster("Monster") # It generates a monster avatar
ra.robohead("Head") # It generates a robot head avatar
ra.kitten('cats') # It generates a cat avatar
```

## License:

This project is licensed under the terms of the MIT license. You can find the full license text in the LICENSE file.
