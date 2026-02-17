from datetime import datetime, date
from models import Customer, Owner, Vehicle, Car, Motorcycle, Rental, Rating




class RentalSystem:
    def __init__(self):
    

        self.vehicles: list[Vehicle] = []
        self.rentals: list[Rental] = []
      

        self._next_rental_id = 1
    

        self._seed_demo_data()

    # ---------------------------------------------------
    # DEMO DATA
    # ---------------------------------------------------


        car = Car(
            vehicle_id=1,
            plate="ΙΚΧ1234",
            brand="Toyota",
            model="Yaris",
            owner_id=owner.user_id,
            number_of_doors=5,
            trunk_capacity=350
        )
        self.vehicles.append(car)

        moto = Motorcycle(
            vehicle_id=2,
            plate="ΜΟΤ5678",
            brand="Honda",
            model="CB500",
            owner_id=owner.user_id,
            engine_cc=500,
            moto_type="Street"
        )
        self.vehicles.append(moto)

        rental1 = Rental(
            rental_id=self._next_rental_id,
            customer_id=1,
            vehicle_id=1,
            start_date=parse_date("2025-01-10"),
            end_date=parse_date("2025-01-12"),
            status="completed"
        )
        self.rentals.append(rental1)
        self._next_rental_id += 1

        rental2 = Rental(
            rental_id=self._next_rental_id,
            customer_id=1,
            vehicle_id=2,
            start_date=parse_date("2025-03-01"),
            end_date=parse_date("2025-03-03"),
            status="completed"
        )
        self.rentals.append(rental2)
        self._next_rental_id += 1

        rental3 = Rental(
            rental_id=self._next_rental_id,
            customer_id=2,
            vehicle_id=1,
            start_date=parse_date("2026-03-10"),
            end_date=parse_date("2026-03-15"),
            status="pending"
        )
        self.rentals.append(rental3)
        self._next_rental_id += 1

        rental4 = Rental(
            rental_id=self._next_rental_id,
            customer_id=1,
            vehicle_id=2,
            start_date=parse_date("2026-04-01"),
            end_date=parse_date("2026-04-05"),
            status="pending"
        )
        self.rentals.append(rental4)
        self._next_rental_id += 1

    # ---------------------------------------------------
    # LOGIN SUPPORT
    # ---------------------------------------------------
    def find_customer(self, name: str, email: str):
        for c in self.customers:
            if c.name == name and c.email == email:
                return c
        return None

    # ---------------------------------------------------
    # FIND METHODS
    # ---------------------------------------------------
    def find_vehicle_by_id(self, vehicle_id: int):
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                return v
        return None





    # ---------------------------------------------------
    # AVAILABILITY CHECK
    # ---------------------------------------------------
    def is_vehicle_available(self, vehicle_id: int, start_date: date, end_date: date):
        for rental in self.rentals:
            if rental.vehicle_id != vehicle_id:
                continue

            # Overlap check
            if not (end_date < rental.start_date or start_date > rental.end_date):
                return False

        return True

    def search_available_vehicles(self, start_date: date, end_date: date):
        return [
            v for v in self.vehicles
            if self.is_vehicle_available(v.vehicle_id, start_date, end_date)
        ]

    # ---------------------------------------------------
    # CREATE RENTAL
    # ---------------------------------------------------
    def create_rental(self, customer_id: int, vehicle_id: int, start_str: str, end_str: str):
        rental = Rental(
            rental_id=self._next_rental_id,
            customer_id=customer_id,
            vehicle_id=vehicle_id,
            start_date=parse_date(start_str),
            end_date=parse_date(end_str),
            status="pending"
        )
        self.rentals.append(rental)
        self._next_rental_id += 1
        return rental


 
