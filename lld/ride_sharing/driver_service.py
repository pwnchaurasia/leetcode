class DriverService:
    available_drivers = []

    @classmethod
    def register_driver(cls, driver):
        cls.available_drivers.append(driver)


    @classmethod
    def broadcast_ride(cls, ride):
        """
            This method broadcasts the ride to all available drivers.
        """
        nearest_driver = cls.find_nearest_drivers(ride)
        if not nearest_driver:
            print("No drivers available to broadcast")
            return

        for driver in nearest_driver:
            driver.notify_of_ride(ride)

        print(f"Notified {len(nearest_driver)} drivers about the ride.")


    @classmethod
    def assign_driver(cls, driver, ride):
        ride.ride_accepted(driver)
        cls.available_drivers.remove(driver)
        cls.notify_other_drivers(driver, ride)


    @classmethod
    def notify_other_drivers(cls, accepted_driver, ride):
        for driver in cls.available_drivers:
            driver.notify_ride_taken(ride, accepted_driver)

    @classmethod
    def find_nearest_drivers(cls, ride, max_distance=5):
        if not cls.available_drivers:
            return None
        rider_location = ride.start_location
        # Basic algorithm: find the driver with the shortest distance to the rider
        # Find all drivers within the max_distance range
        nearby_drivers = [
            driver for driver in cls.available_drivers
            if abs(driver.get_location() - rider_location) <= max_distance
        ]
        return nearby_drivers



