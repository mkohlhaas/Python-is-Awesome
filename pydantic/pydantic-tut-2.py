from pydantic import validate_arguments


@validate_arguments
def add(x: int, y: int) -> int:
    return x + y


if __name__ == "__main__":
    print(add(3, 5))
