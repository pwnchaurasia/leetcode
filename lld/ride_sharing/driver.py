from lld.ride_sharing.driver_service import DriverService


class Driver:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.current_ride = None

    def notify_of_ride(self, ride):
        """
        Notifies the driver that a new ride request is available.
        """
        print(f"Driver {self.name} notified of a new ride from {ride.rider.name}.")

    def notify_ride_taken(self, ride, accepted_driver):
        """
        Notify this driver that the ride has been taken by another driver.
        """
        print(f"Driver {self.name}: Ride has been accepted by {accepted_driver.name}. No longer available.")

    def accept_ride(self, ride):
        """
        The driver accepts the ride. DriverService assigns the ride to this driver.
        """
        print(f"Driver {self.name} is accepting the ride...")
        DriverService.assign_driver(self, ride)

    def assign_ride(self, ride):
        """
        Assign the ride to this driver.
        """
        self.current_ride = ride
        print(f"Ride assigned to driver {self.name}. Heading to pick up {ride.rider.name}.")

    def get_location(self):
        return self.location

    def register_driver(self):
        DriverService.register_driver(driver=self)
