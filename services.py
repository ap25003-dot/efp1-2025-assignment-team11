from datetime import datetime, date
from models import Customer, Owner, Vehicle, Car, Motorcycle, Rental, Rating


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, "%Y-%m-%d").date()


class RentalSystem:
    def __init__(self):
        self.customers: list[Customer] = []
        self.owners: list[Owner] = []
        self.vehicles: list[Vehicle] = []
        self.rentals: list[Rental] = []
        self.ratings: list[Rating] = []

        self._next_rental_id = 1
        self._next_rating_id = 1

        self._seed_demo_data()

    # ---------------------------------------------------
    # DEMO DATA
    # ---------------------------------------------------
    def _seed_demo_data(self):
        owner = Owner(
            user_id=1,
            name="Γιάννης Παπαδόπουλος",
            email="owner@mail.com",
            tax_assessment_notice="TAX123"
        )
        self.owners.append(owner)

        customer1 = Customer(
            user_id=1,
            name="Νίκος Κωνσταντίνου",
            email="customer@mail.com",
            driving_license="DL987"
        )
        self.customers.append(customer1)

        customer2 = Customer(
            user_id=2,
            name="Μαρία Δημητρίου",
            email="maria@mail.com",
            driving_license="DL555"
        )
        self.customers.append(customer2)

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

    def find_rental_by_id(self, rental_id: int):
        for r in self.rentals:
            if r.rental_id == rental_id:
                return r
        return None

    def find_owner_by_id(self, owner_id: int):
        for o in self.owners:
            if o.user_id == owner_id:
                return o
        return None

    # ---------------------------------------------------
    # RENTAL FILTERING
    # ---------------------------------------------------
    def completed_rentals_for_customer(self, customer_id: int):
        return [r for r in self.rentals if r.customer_id == customer_id and r.status == "completed"]

    def pending_rentals_for_customer(self, customer_id: int):
        return [r for r in self.rentals if r.customer_id == customer_id and r.status != "completed"]

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

    # ---------------------------------------------------
    # RATING (ΧΩΡΙΣ PRINT)
    # ---------------------------------------------------
    def submit_or_change_rating(self, customer_id: int, rental_id: int,
                                score_vehicle: int, score_owner: int, comment: str):

        rental = self.find_rental_by_id(rental_id)

        if rental is None:
            return None

        rating = Rating(
            rating_id=self._next_rating_id,
            rental_id=rental_id,
            score_vehicle=score_vehicle,
            score_owner=score_owner,
            comment=comment
        )

        rental.rating = rating
        self.ratings.append(rating)
        self._next_rating_id += 1

        owner = self.find_owner_by_id(
            self.find_vehicle_by_id(rental.vehicle_id).owner_id
        )
        self._notify_owner(owner, rating)

        return rating

    # ---------------------------------------------------
    # EMAIL SIMULATION
    # ---------------------------------------------------
    def _notify_owner(self, owner, rating):
        print(f"\n[EMAIL προς {owner.email}]")
        print("Το όχημά σας έλαβε νέα αξιολόγηση.")
        print(f"Βαθμολογία οχήματος: {rating.score_vehicle}")
        print(f"Βαθμολογία ιδιοκτήτη: {rating.score_owner}")
        print(f"Σχόλιο: {rating.comment}")
