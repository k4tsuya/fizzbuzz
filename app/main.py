"""The fizzbuzz program."""


def fizz_buzz(n: int) -> list:
    """Return a list of the fizzbuzz sequence up to n."""
    try:
        n = int(n)
    except ValueError as e:
        msg = "Input must be an integer"
        raise ValueError(msg) from e

    result: list = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


print(fizz_buzz(15))
