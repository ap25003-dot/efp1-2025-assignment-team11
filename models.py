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
