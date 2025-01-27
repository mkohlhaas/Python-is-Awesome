#!/usr/bin/env python

# excpt_group = ExceptionGroup(
#     "this is an exception group",
#     [
#         ValueError("value must be greater than 0"),
#         NotADirectoryError("must be a directory"),
#         NotADirectoryError("still must be a directory"),
#         # TypeError("must be an int"),
#     ],
# )

# can be nested
excpt_group = ExceptionGroup(
    "this is an exception group",
    [
        ValueError("value must be greater than 0"),
        ExceptionGroup(
            "directory errors",
            [
                NotADirectoryError("must be a directory"),
                NotADirectoryError("still must be a directory"),
            ],
        ),
        # TypeError("must be an int"),
    ],
)

if __name__ == "__main__":
    # raise excpt_group

    try:
        raise excpt_group
    except* ValueError as e:
        print(f"Handling ValueError: {e.exceptions}")
    except* NotADirectoryError as e:
        print(f"Handling NotADirectoryError: {e.exceptions}")

    try:
        raise TypeError("must be an int")
    except* ValueError as e:
        print(f"Handling ValueError: {e.exceptions}")
    except* NotADirectoryError as e:
        print(f"Handling NotADirectoryError: {e.exceptions}")
    except* TypeError as e:
        print(f"Handling TypeError: {e.exceptions}")
