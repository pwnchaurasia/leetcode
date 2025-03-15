# Display class
class Display:
    def __init__(self, elevator):
        self.elevator = elevator

    def update(self, current_floor, direction):
        print(f"Elevator {self.elevator.id} Display: Floor {current_floor}, Direction {direction.name}")