from abc import ABC, abstractmethod
from datetime import datetime

class Vehicle(ABC):
    def __init__(self, make:str, model:str, year:int, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def __repr__(self):
        return f"{self.__class__.__name__}({self.make}, {self.model}, {self.year})"

    @abstractmethod
    def drive_to(self):
        pass

    @abstractmethod
    def refill(self):
        pass

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model 

    @property
    def year(self):
        return self._year

    @property
    def engine(self):
        return self._engine

    @make.setter
    def make(self, make_value:str) -> str:
        if not isinstance(make_value, str):
            raise TypeError(f"{__class__.__name__} -> {make_value.__class__.__name__} Error: Expected 'str'")
        if not make_value.strip():
            raise ValueError(f"{__class__.__name__} -> {make_value.__class__.__name__} Error: Make cannot be 'empty'")
        self._make = make_value

    @model.setter
    def model(self, model_value:str) -> str:
        if not isinstance(model_value, str):
            raise TypeError(f"{__class__.__name__} -> {model_value.__class__.__name__} Error: Expected 'str'")
        if not model_value.strip():
            raise ValueError(f"{__class__.__name__} -> {model_value.__class__.__name__} Error: Model cannot be empth")
        self._model = model_value

    @year.setter
    def year(self, year_value:int) -> int:
        current_date = datetime.today()
        current_year = current_date.year
        if not isinstance(year_value, int):
            raise TypeError(f"{__class__.__name__} -> {year_value.__class__.__name__} Error: Expected 'int'")
        if year_value < 1886 or year_value > current_year + 1:
            raise ValueError(f"{__class__.__name__} -> {year_value.__class__.__name__} Error: Year outside range(1886, current + 1)")
        self._year = year_value
        
    @engine.setter
    def engine(self, engine_object):
        if not isinstance(engine_object, Engine):
            raise TypeError(f"{__class__.__name__} -> {engine_object.__class__.__name__} Error: {engine_object} in not part of <Engine Class>.")
        self._engine = engine_object
       
class Car(Vehicle):

    highway_mpg = 33
    city_mpg = 25
    gas_tank_gallons = 18
    current_gas = 18

    def drive_to(self, destination, distance, highway_or_city):
        if highway_or_city.strip().lower() == "highway":
            speed = 80
        if highway_or_city.strip().lower() == "city":
            speed = 45
        time = distance / speed
        hours, minutes = time.split('.')
        minutes = round(minutes, 2) * 60
        gas_used = distance / Car.highway_mpg
        gas_used = round(gas_used, 2)
        Car.current_gas = Car.gas_tank_gallons - gas_used
        if Car.current_gas <= Car.gas_tank_gallons * .25:
            self.refill()
        return f"Driving to {destination}, ETA is {hours} hours and {minutes} minutes."

    def refill(self):
        print("Stop and get gas and the nearest gas station")

class Truck(Vehicle):

    highway_mpg = 36
    city_mpg = 18
    gas_tank_gallons = 36
    current_gas = 36

    def drive_to(self, destination, distance, highway_or_city):
        if highway_or_city.strip().lower() == "highway":
            speed = 80
        if highway_or_city.strip().lower() == "city":
            speed = 45
        time = distance / speed
        hours, minutes = time.split('.')
        minutes = round(minutes, 2) * 60
        gas_used = distance / Truck.highway_mpg
        gas_used = round(gas_used, 2)
        Truck.current_gas = Truck.gas_tank_gallons - gas_used
        if Truck.current_gas <= Truck.gas_tank_gallons * .25:
            self.refill()
        return f"Driving to {destination}, ETA is {hours} hours and {minutes} minutes."

    def refill(self):
        print("Stop and get gas and the nearest gas station")

class Motorcycle(Vehicle):

    highway_mpg = 70
    city_mpg = 35
    gas_tank_gallons = 3
    current_gas = 3

    def drive_to(self, destination, distance, highway_or_city):
        if highway_or_city.strip().lower() == "highway":
            speed = 80
        if highway_or_city.strip().lower() == "city":
            speed = 45
        time = distance / speed
        hours, minutes = time.split('.')
        minutes = round(minutes, 2) * 60
        gas_used = distance / Motorcycle.highway_mpg
        gas_used = round(gas_used, 2)
        Motorcycle.current_gas = Motorcycle.gas_tank_gallons - gas_used
        if Motorcycle.current_gas <= Motorcycle.gas_tank_gallons * .25:
            self.refill()
        return f"Driving to {destination}, ETA is {hours} hours and {minutes} minutes."

    def refill(self):
        print("Stop and get gas and the nearest gas station")

class Engine(ABC):
    counter = 0
    engines_made = []
    def __init__(self, miles, year_made, last_maintenance):
        self.miles = miles
        self.year_made = year_made
        self.last_maintenance = last_maintenance
        Engine.counter += 1

    def __repr__(self):
        return f"{self.__class__.__name__}({self.miles}, {self.year_made}, {self.last_maintenance})"

    @abstractmethod
    def start_engine(self):
        return f"{__class__.__name__} start engine"

    @abstractmethod
    def stop_engine(self):
        return f"{__class__.__name__} stop engine"

class Electric(Engine):
    horsepower = 500

    def start_engine(self):
        return f"{__class__.__name__} start engine"

    def stop_engine(self):
        return f"{__class__.__name__} stop engine"

class Gas(Engine):
    horsepower = 350

    def start_engine(self):
        return f"{__class__.__name__} start engine"
    
    def stop_engine(self):
        return f"{__class__.__name__} stop engine"

class Diesel(Engine):
    horsepower = 280

    def start_engine(self):
        return f"{__class__.__name__} start engine"
    
    def stop_engine(self):
        return f"{__class__.__name__} stop engine"

class VehicleFactory:
    engines_created = []
    engine_counts = {
        "gas": 0,
        "electric": 0,
        "diesel": 0
    }

    def __repr__(self):
        return f"{self.__class__.__name__}({self.engine_counts.items()} {self.engines_created})"

    def _validate_vehicle(self, vehicle_object:str, specs:list) -> object:
        make, model, year, engine= specs
        object_type = ["car", "truck", "motorcycle"]
        if vehicle_object not in object_type:
            raise ValueError(f"{__class__.__name__} -> {self._validate_vehicle.__name__} Error: {vehicle_object} is not a valid entry. [car | truck | motorcycle]")
        vehicle_object = vehicle_object.capitalize()
        validated_vehicle = globals().get(vehicle_object)
        return validated_vehicle(make, model, year, engine)

    def create_vehicle(self, vehicle:str, specs:list):
        if not isinstance(vehicle, str):
            raise TypeError(f"{__class__.__name__} -> {self.create_vehicle.__name__} Error: {vehicle} is not a 'str'")
        if not vehicle.strip():
            raise ValueError(f"{__class__.__name__} -> {self.create_vehicle.__name__} Error: {vehicle} is an empty 'str' '', must no be empty")
        created_vehicle = self._validate_vehicle(vehicle, specs)
        return created_vehicle

    def _validate_engine(self, engine:str, specs:list):
        miles, year_made, last_maintenance = specs
        engine_types = ["gas", "electric", "diesel"]
        if engine not in engine_types:
            raise ValueError(f"{__class__.__name__} -> {self._validate_engine.__name__} Error: {engine} is not a valid entry. [gas | electric | diesel]")
        engine = engine.capitalize()
        validated_engine = globals().get(engine)
        return validated_engine(miles, year_made, last_maintenance)

    def create_engine(self, engine:str, specs:list[int,int,int]):
        if not isinstance(engine, str):
            raise TypeError(f"{__class__.__name__} -> {self.create_engine.__name__} Error: {engine} must be a 'str'")
        if not engine.strip():
            raise ValueError(f"{__class__.__name__} -> {self.create_engine.__name__} Error: {engine} must be a non-empty 'str'")
        created_engine = self._validate_engine(engine, specs)
        VehicleFactory.engines_created.append(created_engine)
        VehicleFactory.engine_counts[engine] +=1
        return created_engine

class Fleet:
    def __init__(self) -> list[object]:
        self.vehicles = []
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.vehicles):
            raise StopIteration
        current_value = self.vehicles[self.index]
        self.index += 1
        return current_value

    def __repr__(self):
        return f"{__class__.__name__}({self.vehicles})"

    def add_vehicles(self, vehicle):
        self.vehicles.append(vehicle)

factory = VehicleFactory()
james_truck_engine = factory.create_engine("gas", [37, 2026, 2026])
james_truck = factory.create_vehicle("truck", ["Toyota", "4Runner", 2026, james_truck_engine])

james_car_engine = factory.create_engine("electric", [5, 2026, 2026])
james_car = factory.create_vehicle("car", ["Tesla", "Model_33", 2026, james_car_engine])

james_motorcycle_engine = factory.create_engine("diesel", [10000, 2025, 2024])
james_motorcycle = factory.create_vehicle("motorcycle", ["Yamaha", "YZT-7", 2026, james_motorcycle_engine])

fleet = Fleet()
add_vehicles = [james_truck, james_car, james_motorcycle]
for item in add_vehicles:
    fleet.add_vehicles(item)

engines_made = [james_truck_engine, james_car_engine, james_motorcycle_engine]
print(fleet)
print(factory)