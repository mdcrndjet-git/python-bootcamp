class Door:
    def __init__(self):
        self._state = "CLOSED"

    def open(self):
        if self._state == "OPEN":
            raise ValueError("Door is already opened.")
        self._state = "OPEN"
        print("Door is now opened.")

    def close(self):
        if self._state == "CLOSED":
            raise ValueError("Door is already closed.")
        self._state = "CLOSED"
        print("Door is now closed.")

door = Door()
door.open()
#door.open()
door.close()
#door.close()