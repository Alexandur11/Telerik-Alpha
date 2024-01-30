class Vehicle:
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    CATEGORY_LEN_MIN = 3
    CATEGORY_LEN_MAX = 10
    CATEGORY_LEN_ERR = f'Category must be between {CATEGORY_LEN_MIN} and {CATEGORY_LEN_MAX} characters long!'

    WEIGHT_CAP_MIN = 1
    WEIGHT_CAP_MAX = 100
    WEIGHT_CAP_ERR = f'Weight capacity must be between {WEIGHT_CAP_MIN} and {WEIGHT_CAP_MAX}!'

    CAR_SEATS_MIN = 1
    CAR_SEATS_MAX = 10
    CAR_SEATS_ERR = f'Seats must be between {CAR_SEATS_MIN} and {CAR_SEATS_MAX}!'

    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price


    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        if Vehicle.MAKE_LEN_MIN < len(value) < Vehicle.MAKE_LEN_MAX:
            self._make = value
        else:
            raise ValueError(Vehicle.MAKE_LEN_ERR)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if Vehicle.MODEL_LEN_MIN < len(value) < Vehicle.MODEL_LEN_MAX:
            self._model = value
        else:
            raise ValueError(Vehicle.MODEL_LEN_ERR)


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if Vehicle.PRICE_MIN < value < Vehicle.PRICE_MAX:
            self._price = value
        else:
            raise ValueError(Vehicle.PRICE_ERR)

    def add_comment(self, value):
        self.comments = list(self.comments)
        self.comments.append(value)
        self.comments = tuple(self.comments)

    def remove_comment(self, value):
        self.comments = list(self.comments)

        if value in self.comments:
            self.comments.remove(value)
            self.comments = tuple(self.comments)
        else:
            self.comments = tuple(self.comments)

    def get_comment(self, value):
        if value < 0 or value > len(self.comments):
            raise ValueError("There is no comment on this index.")
        return self.comments[0]
