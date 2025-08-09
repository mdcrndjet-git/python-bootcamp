class Door:
    def __init__(self):
        self._state = "CLOSED"

    def open(self):
        if self._state == "LOCK":
            raise ValueError("Door is locked.")
        if self._state == "OPEN":
            raise ValueError("Door is already opened.")
        self._state = "OPEN"
        print("Door is now opened.")

    def close(self):
        if self._state == "CLOSED":
            raise ValueError("Door is already closed.")
        self._state = "CLOSED"
        print("Door is now closed.")

    def lock(self):
        if self._state == "CLOSED":
            self._state = "LOCK"
            print("Door is now locked.")


door = Door()

door.open()
#door.open()
door.close()
#door.close()
door.lock()
door.open()