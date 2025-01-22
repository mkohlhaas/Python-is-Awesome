#!/usr/bin/env python


def display_bio(name: str, age: int, job: str | None = None) -> None:
    job_text = f"I am a {job}" if job else "I am unemployed"
    print(f"My name is {name}, I am {age} years old, and {job_text}.")


if __name__ == "__main__":
    display_bio("John", 32)
