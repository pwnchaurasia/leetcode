from abc import ABC, abstractmethod


class ParkingSpot:
    def __init__(self, id, reserve) -> None:
        self.id = id
        self.reserve = reserve