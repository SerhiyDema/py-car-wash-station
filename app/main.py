class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class  # from 1 to 7
        self.clean_mark = clean_mark  # from dirty - 1 to clean - 10
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center  # 1.0 to 10
        self.clean_power = clean_power  # up to clean_mark
        self.average_rating = average_rating  # from 1.0 to 5.0
        self.count_of_ratings = count_of_ratings  # number of voting

    """
    returns income of CarWashStation for serving list of Car's
    """
    def serve_cars(self, list_cars: list[Car]) -> float:
        return round(sum([self.wash_single_car(car) for car in list_cars]), 1)

    """
    calculates cost for a single car wash
    """
    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    """
    washes only cars with clean_mark < clean_power of wash station,
    up clean_mark after wash
    """
    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            car_income = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return car_income
        return 0

    """
    adds a single rate to the wash station
    """
    def rate_service(self, single_rate: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + single_rate)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
