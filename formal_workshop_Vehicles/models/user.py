from models.comment import Comment
from models.constants.user_role import UserRole
from commands.validation_helpers import password_symbols
from models.car import Car
from models.truck import Truck
from models.motorcycle import Motorcycle
from models.comment import Comment


class User():
    USERNAME_LEN_MIN = 2
    USERNAME_LEN_MAX = 20
    USERNAME_LEN_ERR = f'Username must be between {USERNAME_LEN_MIN} and {USERNAME_LEN_MAX} characters long!'
    USERNAME_INVALID_SYMBOLS = 'Username contains invalid symbols!'

    PASSWORD_LEN_MIN = 5
    PASSWORD_LEN_MAX = 30
    PASSWORD_LEN_ERR = f'Password must be between {PASSWORD_LEN_MIN} and {PASSWORD_LEN_MAX} characters long!'
    PASSWORD_INVALID_SYMBOLS = 'Password contains invalid symbols!'

    LASTNAME_LEN_MIN = 2
    LASTNAME_LEN_MAX = 20
    LASTNAME_LEN_ERR = f'Lastname must be between {LASTNAME_LEN_MIN} and {LASTNAME_LEN_MAX} characters long!'

    FIRSTNAME_LEN_MIN = 2
    FIRSTNAME_LEN_MAX = 20
    FIRSTNAME_LEN_ERR = f'Firstname must be between {FIRSTNAME_LEN_MIN} and {FIRSTNAME_LEN_MAX} characters long!'

    NORMAL_ROLE_VEHICLE_LIMIT = 5

    NORMAL_USER_LIMIT_REACHED_ERR = f'You are not VIP and cannot add more than {NORMAL_ROLE_VEHICLE_LIMIT} vehicles!'
    ADMIN_CANNOT_ADD_VEHICLES_ERR = 'You are an admin and therefore cannot add vehicles!'
    YOU_ARE_NOT_THE_AUTHOR = 'You are not the author of the comment you are trying to remove!'
    THE_VEHICLE_DOES_NOT_EXIT = 'The vehicle does not exist!'

    def __init__(self, username, firstname, lastname, password, user_role):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self._user_role = user_role
        self.is_admin = True if self._user_role == "Admin" else False
        self.is_vip = True if self._user_role == "Vip" else False
        self.vehicles = ()

    @property
    def user_role(self):
        return self._user_role

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if User.USERNAME_LEN_MIN < len(value) < User.USERNAME_LEN_MAX and value.isalpha() or value.isnumeric():
            self._username = value
        else:
            raise ValueError(User.USERNAME_LEN_ERR)

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):

        if User.FIRSTNAME_LEN_MIN < len(value) < User.USERNAME_LEN_MAX and value.isalpha():
            self._firstname = value
        else:
            raise ValueError(User.FIRSTNAME_LEN_ERR)

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        if User.LASTNAME_LEN_MIN < len(value) < User.USERNAME_LEN_MAX and value.isalpha():
            self._lastname = value
        else:
            raise ValueError(User.LASTNAME_LEN_ERR)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if User.PASSWORD_LEN_MIN <= len(value) <= User.PASSWORD_LEN_MAX:
            if password_symbols(value):
                self.__password = value
            else:
                raise ValueError(User.PASSWORD_INVALID_SYMBOLS)
        else:
            raise ValueError(User.PASSWORD_LEN_ERR)

    def add_vehicle(self, value):
        self.vehicles = list(self.vehicles)
        if self.is_admin:
            self.vehicles = tuple(self.vehicles)
            raise ValueError(User.ADMIN_CANNOT_ADD_VEHICLES_ERR)
        if self.is_vip  and len(self.vehicles) == 5:
            self.vehicles.append(value)
            self.vehicles = tuple(self.vehicles)
        else:
            if len(self.vehicles) < 5:
                self.vehicles.append(value)
                self.vehicles = tuple(self.vehicles)
            else:
                self.vehicles = tuple(self.vehicles)
                raise ValueError(User.NORMAL_USER_LIMIT_REACHED_ERR)

    def get_vehicle(self, value):
        if value in range(0, len(self.vehicles)):
            return self.vehicles[value]
        else:
            raise ValueError(User.THE_VEHICLE_DOES_NOT_EXIT)

    def remove_vehicle(self, value):
        self.vehicles = list(self.vehicles)
        if value in self.vehicles:
            self.vehicles.remove(value)
            self.vehicles = tuple(self.vehicles)
        else:
            self.vehicles = tuple(self.vehicles)

    def add_comment(self, comment, vehicle):
        new_comment = Comment(content=comment, author=self.username)
        vehicle.add_comment(new_comment)

    def remove_comment(self, comment, vehicle):
        useless_comment = Comment(content=comment, author=self.username)
        for vehicles in self.vehicles:
            for x in vehicles.comments:
                if User.username == x.author:
                    vehicle.remove_comment(useless_comment)
                else:
                    raise ValueError(User.YOU_ARE_NOT_THE_AUTHOR)

    def print_vehicles(self):
        comments = []
        empty = '\n'.join([
            f'--USER {self.username}--',
            '--NO VEHICLES--'
        ])
        for i, v in enumerate(self.vehicles, start=1):
            comments.append(f"{i}. {v}")
        output = '\n'.join(comments)

        if len(self.vehicles) != 0:
            return f"--USER {self.username}--\n{output}"
        else:
            return empty

    def __str__(self):
        expected = f'Username: {self.username}, FullName: {self.firstname} {self.lastname}, Role: {self._user_role}'
        return expected
