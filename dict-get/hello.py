#!/usr/bin/env python

player_1 = {"xp": 234, "level": 3}
player_2 = {"xp": 181, "level": 1}
player_3 = {"xp": 0}  # brand-new player
player_db = [
    player_1,
    player_2,
    player_3,
]

if __name__ == "__main__":
    for player in player_db:
        lvl = player.get("level", None)
        print(f"Level: {lvl}")
