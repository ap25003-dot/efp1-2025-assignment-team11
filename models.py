class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"{self.user_id}: {self.name} ({self.email})"


class Customer(User):
    def __init__(self, user_id: int, name: str, email: str, driving_license: str):
        super().__init__(user_id, name, email)
        self.driving_license = driving_license

    def __str__(self) -> str:
        return f"{super().__str__()} | DL: {self.driving_license}"


class Owner(User):
    def __init__(self, user_id: int, name: str, email: str, tax_assessment_notice: str):
        super().__init__(user_id, name, email)
        self.tax_assessment_notice = tax_assessment_notice

    def __str__(self) -> str:
        return f"{super().__str__()} | Tax Notice: {self.tax_assessment_notice}"


class Vehicle:
    def __init__(self, vehicle_id: int, plate: str, brand: str, model: str, owner_id: int):
        self.vehicle_id = vehicle_id
        self.plate = plate
        self.brand = brand
        self.model = model
        self.owner_id = owner_id

    def __str__(self) -> str:
        return f"{self.vehicle_id}: {self.brand} {self.model} [{self.plate}]"


class Car(Vehicle):
    def __init__(self, vehicle_id: int, plate: str, brand: str, model: str,
                 owner_id: int, number_of_doors: int, trunk_capacity: int):
        super().__init__(vehicle_id, plate, brand, model, owner_id)
        self.number_of_doors = number_of_doors
        self.trunk_capacity = trunk_capacity

    def __str__(self) -> str:
        return (f"{super().__str__()} | Doors: {self.number_of_doors}, "
                f"Trunk: {self.trunk_capacity}L")


class Motorcycle(Vehicle):
    def __init__(self, vehicle_id: int, plate: str, brand: str, model: str,
                 owner_id: int, engine_cc: int, moto_type: str):
        super().__init__(vehicle_id, plate, brand, model, owner_id)
        self.engine_cc = engine_cc
        self.moto_type = moto_type

    def __str__(self) -> str:
        return (f"{super().__str__()} | {self.engine_cc}cc, Type: {self.moto_type}")
    
    
class Rental:
    def __init__(self, rental_id: int, customer_id: int, vehicle_id: int,
                 start_date: str, end_date: str, status: str):
        self.rental_id = rental_id
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.rating = None

    def __str__(self) -> str:
        return (f"Rental {self.rental_id} - Customer {self.customer_id} -> "
                f"Vehicle {self.vehicle_id} ({self.start_date} to {self.end_date})")


class Rating:
    def __init__(self, rating_id: int, rental_id: int,
                 score_vehicle: int, score_owner: int, comment: str):
        self.rating_id = rating_id
        self.rental_id = rental_id
        self.score_vehicle = score_vehicle
        self.score_owner = score_owner
        self.comment = comment

    def __str__(self) -> str:
        return (f"Rating {self.rating_id}: Vehicle={self.score_vehicle}, "
                f"Owner={self.score_owner} - '{self.comment}'")
