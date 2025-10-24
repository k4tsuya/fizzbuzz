"""The fizzbuzz program."""


class FizzBuzz:
    """Class to handle the FizzBuzz logic."""

    def __init__(self, n: int) -> None:
        """Initialize the FizzBuzz class."""
        self.n = n

    def check_input(self) -> None:
        """Check the input to see if it is a positive integer."""
        try:
            self.n = int(self.n)
        except ValueError as e:
            msg = "Input must be an integer"
            raise ValueError(msg) from e
        if self.n <= 0:
            msg = "Input must be a positive integer"
            raise ValueError(msg)

    def fizz_buzz(self) -> list:
        """Return a list of the fizzbuzz sequence up to n."""
        result: list = []

        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result


if __name__ == "__main__":
    n = input("Enter a positive integer: ")
    fizz_buzz = FizzBuzz(n)
    fizz_buzz.check_input()
    print(fizz_buzz.fizz_buzz())
