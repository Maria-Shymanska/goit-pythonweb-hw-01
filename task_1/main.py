from abc import ABC, abstractmethod
import logging


# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()  # Вивід у консоль
    ]
)

# Створення логера
logger = logging.getLogger(__name__)



# Абстрактний клас транспортного засобу
class Vehicle(ABC):
    def __init__(self, make: str, model: str, region):
        self.make = make
        self.model = model
        self.region = region

    @abstractmethod
    def start_engine(self) -> None:
        pass


# Клас автомобіля
class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.region} Spec): Двигун запущено")


# Клас мотоцикла
class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.region} Spec): Мотор заведено")


# Абстрактна фабрика
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model:str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


# Фабрика для США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str)-> Car:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str)-> Motorcycle:
        return Motorcycle(make, model, "US")


# Фабрика для ЄС
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU")


# Використання фабрик
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Chevrolet", "Camaro")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("Ducati", "Panigale V4")
vehicle2.start_engine()
