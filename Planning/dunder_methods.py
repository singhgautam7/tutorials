class MyCash:

    def __init__(self, *, hundreds: int = 0, five_hundreds: int = 0, two_thousands: int = 0):
        """
        The Python equivalent of the C++ constructor in an object-oriented approach.
        The __init__ function is called every time an object is created from a class.
        The __init__ method lets the class initialize the object's attributes and serves no other purpose
        :param hundreds: number of notes of hundreds
        :param five_hundreds: number of notes of five_hundreds
        :param two_thousands: number of notes of two_thousands
        """
        self.hundreds = hundreds
        self.five_hundreds = five_hundreds
        self.two_thousands = two_thousands

    def __repr__(self):
        """
        Defines the printable representation of any given object.
        Mainly used for debugging and development.
        The goal is to be unambiguous.
        """
        return f"Cash({self.hundreds}*100 + {self.five_hundreds}*500 + {self.two_thousands}*2000)"

    def __str__(self):
        """
        It is used for creating output for end user.
        The goal is to be human-readable.
        """
        return f"Rs. {self.total_amount}"

    def __add__(self, other):
        """
        Method returns a new object that represents the sum of two objects
        """
        new_wallet = MyCash(
            hundreds=self.hundreds+other.hundreds,
            five_hundreds=self.five_hundreds + other.five_hundreds,
            two_thousands=self.two_thousands + other.two_thousands
        )
        return new_wallet

    def __len__(self):
        """
        Returns a positive integer that represents the length of the object on which it is called
        """
        return self.hundreds + self.five_hundreds + self.two_thousands

    def __call__(self, *args, **kwargs):
        pass

    def __del__(self):
        self.hundreds, self.five_hundreds, self.two_thousands = [0] * 3     # [0] * 3 is equivalent to [0,0,0]
        print("I am broke :|")

    @property
    def total_amount(self) -> int:
        return (self.hundreds * 100) + (self.five_hundreds * 500) + (self.two_thousands * 2000)


if __name__ == '__main__':
    ramesh_wallet = MyCash(hundreds=5, five_hundreds=2)
    suresh_wallet = MyCash(two_thousands=1)

    print(f"Ramesh has {ramesh_wallet}")
    print(f"Suresh has {suresh_wallet}")

    combined_wallet = ramesh_wallet + suresh_wallet
    print(f"Combined Wallet Amount {combined_wallet}")

    print(f"Total notes in Ramesh pocket {len(ramesh_wallet)}")
    print(f"Total notes in Suresh pocket {len(suresh_wallet)}")

    # For iterators - __iter__, __next__
    # For context managers - __enter__, __exit__

    del ramesh_wallet
