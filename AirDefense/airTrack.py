import uuid


class AirTrack:
    
    # Constructor Method
    def __init__(self, name, type, position_x, position_y, heading, speed):
        self._name = name
        self._type = type
        self._id = uuid.uuid1()

        self._position_x = position_x
        self._position_y = position_y
        self._heading = heading
        self._speed = speed

    def updatePosition(self, previousPosition, time):
        pass

    def divert(self):
        self._heading = -self._heading    