from models.vehicle import Vehicle


class Motorcycle(Vehicle):
    WHEELS_COUNT = 2

    def __init__(self, make, model, price, category):
        super().__init__(make, model, price)
        self.category = category
        self.wheels = Motorcycle.WHEELS_COUNT
        self.comments = ()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if Vehicle.CATEGORY_LEN_MIN < len(value) < Vehicle.CATEGORY_LEN_MAX:
            self._category = value
        else:
            raise ValueError(Vehicle.CATEGORY_LEN_ERR)

    def __str__(self):
        expected_if_none = '\n'.join([
            'Motorcycle:',
            f'Make: {self.make}',
            f'Model: {self._model}',
            f'Wheels: 2',
            f'Price: ${self.price:.2f}',
            f'Category: {self.category}',
            '--NO COMMENTS--'
        ])

        expected_if_any = '\n'.join([
            'Motorcycle:',
            f'Make: {self._make}',
            f'Model: {self.model}',
            f'Wheels: 2',
            f'Price: ${self.price:.2f}',
            f'Category: {self.category}',
            '--COMMENTS--',
            f'fake comment',
            '--COMMENTS--'])
        if len(self.comments) == 0:
            return expected_if_none
        else:
            return expected_if_any
