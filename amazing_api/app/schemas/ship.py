from abc import ABC, abstractmethod
from pydantic import BaseModel


class IShip(BaseModel, ABC):
    total_weight_capacity: int
    max_number_of_all_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km: float

    port_id: int
    id: int

    def sail_to(self, port) -> bool:
        pass

    def refuel(self, amount_of_fuel: float) -> None:
        pass

    def load(self, container) -> bool:
        pass

    def unload(self, container) -> bool:
        pass

    class Config:
        orm_mode = True


class LightWeightShip(IShip):
    pass


class MediumWeightShip(IShip):
    pass


class HeavyWeightShip(IShip):
    pass
