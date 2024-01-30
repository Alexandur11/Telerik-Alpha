from models.vehicle import Vehicle


class Truck(Vehicle):
    WHEELS_COUNT = 8

    def __init__(self, make, model, price, weight_capacity):
        super().__init__(make, model, price)
        self.weight_capacity = weight_capacity
        self.comments = ()
        self.wheels = Truck.WHEELS_COUNT

    @property
    def weight_capacity(self):
        return self._category

    @weight_capacity.setter
    def weight_capacity(self, value):
        if Vehicle.WEIGHT_CAP_MIN < value < Vehicle.WEIGHT_CAP_MAX:
            self._category = value
        else:
            raise ValueError(Vehicle.WEIGHT_CAP_ERR)

    def __str__(self):
        expected_if_none = '\n'.join([
            'Truck:',
            f'Make: {self.make}',
            f'Model: {self._model}',
            f'Wheels: 8',
            f'Price: ${self.price:.2f}',
            f'Weight Capacity: {self.weight_capacity}t',
            '--NO COMMENTS--'
        ])

        expected_if_any = '\n'.join([
            'Truck:',
            f'Make: {self._make}',
            f'Model: {self.model}',
            f'Wheels: 8',
            f'Price: ${self.price:.2f}',
            f'Weight Capacity: {self.weight_capacity}t',
            '--COMMENTS--',
            f'fake comment',
            '--COMMENTS--'])

        if len(self.comments) == 0:
            return expected_if_none
        else:
            return expected_if_any
