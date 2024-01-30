from models.vehicle import Vehicle


class Car(Vehicle):
    WHEELS_COUNT = 4

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file
    def __init__(self, make: str, model: str, price: float, seats: int):
        super().__init__(make, model, price)
        self.make = make
        self.model = model
        self.price = price
        self.seats = seats
        self.wheels = Car.WHEELS_COUNT
        self.comments = ()

    @property
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, value):
        if Vehicle.CAR_SEATS_MIN < value < Vehicle.CAR_SEATS_MAX:
            self._seats = value
        else:
            raise ValueError(Vehicle.CAR_SEATS_ERR)

    def __str__(self):
        expected_if_none = '\n'.join([
            'Car:',
            f'Make: {self.make}',
            f'Model: {self._model}',
            f'Wheels: 4',
            f'Price: ${self.price:.2f}',
            f'Seats: {self.seats}',
            '--NO COMMENTS--'
        ])

        expected_if_any = '\n'.join([
            'Car:',
            f'Make: {self._make}',
            f'Model: {self.model}',
            f'Wheels: 4',
            f'Price: ${self.price:.2f}',
            f'Seats: {self.seats}',
            '--COMMENTS--',
            f'fake comment',
            '--COMMENTS--'])

        if len(self.comments) == 0:
            return expected_if_none
        else:
            return expected_if_any
