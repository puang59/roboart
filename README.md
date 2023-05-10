# RoboArt

### Avatars lovingly delivered by Robohash.org

RoboArt is a basic random avatar generator which generates avatar in 4 different sets when hash is provided.

## Installation

You can install RoboArt via pip:

```bash
pip3 install -U RoboArt
```

This will install the latest version of RoboArt

To update your existing RoboArt package, use:

```bash
pip3 install RoboArt - U
```

## Usage

Import RoboArt in your Python script and create an instance of the roboart class:

```python
from RoboArt import roboart
ra = roboart()
```

Then, generate an avatar by passing a hash value to the robo() method:

```python
ra.robo("thisishash")
```

This will generate an avatar based on the provided hash value.

## Quick Example

```python
from RoboArt import roboart

ra = roboart()

# You can use any random string hash, it doesnt matter
Robot = ra.robo("Robot") # It generates a robot avatar
Monster = ra.monster("Monster") # It generates a monster avatar
RoboHead = ra.robohead("Head") # It generates a robot head avatar
Kittens = ra.kitten('cats') # It generates a cat avatar

print(Robot) # prints robo
```

## License:

This project is licensed under the terms of the MIT license. You can find the full license text in the LICENSE file.
