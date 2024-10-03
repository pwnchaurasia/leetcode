from lld.ride_sharing.driver_service import DriverService
from lld.ride_sharing.enums import RideStatus
from lld.ride_sharing.notification import Notification
from lld.ride_sharing.settings import RIDE_BASE_PRICE, PER_KM_PRICE
from lld.ride_sharing.users import User





class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.ride_status = RideStatus.Requested
        self.driver = None

    def assign_driver(self, driver):
        self.driver = driver
        Notification(driver, f"Ride assigned. Pickup {self.rider.name}").send()
        Notification(self.rider, f"Driver {self.driver.name} is on the way").send()

    def get_distance(self):
        return abs(self.end_location - self.start_location)

    def ride_price(self):
        distance = self.get_distance()
        km = int(distance)
        price = RIDE_BASE_PRICE + km * PER_KM_PRICE

    def get_cancellation_price(self):
        km = int(self.get_distance())
        price = RIDE_BASE_PRICE + km * PER_KM_PRICE
        return price

    def search(self):
        """
            Broadcast the ride to all drivers using DriverService.
        """
        print("Broadcasting ride to all available drivers...")
        DriverService.broadcast_ride(self)

    def ride_accepted(self, driver):
        self.ride_status = RideStatus.Accepted
        self.driver = driver
        print(f"Ride from {self.start_location} to {self.end_location} has been accepted by {driver.name}")


    def cancel_ride(self):
        if self.ride_status == RideStatus.Accepted:
            print(f"You will be charged {self.get_cancellation_price()}")
