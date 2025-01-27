#!/usr/bin/env python

from pathlib import Path
# import pathlib

if __name__ == "__main__":
    path = Path()
    print(path)
    print(path.is_absolute())

    path = Path().cwd()
    print("==========================================================================")
    print(path)

    path = Path("/etc/passwd")
    print("==========================================================================")
    print(path)
    print(path.is_absolute())

    path = Path("./pathlib-tut.py")
    print("==========================================================================")
    print(path)
    print(path.name)
    print(path.stem)
    print(path.suffix)
    # Make the path absolute, resolving all symlinks on the way and also
    # normalizing it.
    print(path.absolute())
    path = path.resolve()
    print(path)
    print(path.as_uri())

    path = Path("/home/schmidh/Gitrepos/Python-Example-Code/pathlib/pathlib-tut.py")
    print("==========================================================================")
    print(path)
    print(path.name)
    print(path.stem)
    print(path.suffix)
    print(path.parts)
    print(path.parts[-1])
    print(path.exists())
    print(path.is_file())
    print(path.is_dir())

    path = Path("lyrics.txt")
    text = path.read_text()
    print("==========================================================================")
    print(text)

    data = path.read_bytes()
    print(data)

    path = Path("/home/schmidh/Gitrepos/")
    print("==========================================================================")
    for dir in path.iterdir():
        print(dir)

    path = Path("/tmp/fu.txt")
    path.touch()

    path = Path("/tmp/fu-dir")
    path.mkdir(exist_ok=True)
    path = Path("/tmp/fu-dir/1/2/3/4/5")
    path.mkdir(parents=True, exist_ok=True)

    path = Path("/tmp/fu-dir/lyrics.txt")
    lyrics = """Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you"""
    path.write_text(lyrics)

    lyrics = b"""Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you"""
    path.write_bytes(lyrics)

    print("==========================================================================")
    with path.open("r") as f:
        print(f.read())

    print("==========================================================================")
    path = Path("/home/schmidh/Gitrepos/")
    for file in path.glob("**/numpy*.py"):
        print(file)

    print("==========================================================================")
    path = Path("/home/schmidh/Gitrepos/")
    for file in path.rglob("numpy*.py"):
        print(file)
