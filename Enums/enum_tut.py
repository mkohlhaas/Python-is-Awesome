#!/usr/bin/env python


import logging
import time
from enum import Enum, Flag, IntEnum, StrEnum, auto


class State(Enum):
    PLAYING = auto()
    PAUSED = auto()
    GAME_OVER = auto()


class MessageType(Enum):
    CHAT_ENDED_EVENT = "chat_ended_event"
    MESSAGE_DELETED_EVENT = "message_deleted_event"
    NEW_SPONSOR_EVENT = "new_sponsor_event"
    SPONSOR_ONLY_MODE_STARTED_EVENT = "sponsor_only_mode_started_event"
    SPONSOR_ONLY_MODE_ENDED_EVENT = "sponsor_only_mode_ended_event"
    MEMBER_MILESTONE_CHAT_EVENT = "member_milestone_chat_event"
    SUPER_CHAT_EVENT = "super_chat_event"
    SUPER_STICKER_EVENT = "super_sticker_event"
    TEXT_MESSAGE_EVENT = "text_message_event"
    TOMBSTONE = "tombstone"
    USER_BANNED_EVENT = "user_banned_event"


class Category(IntEnum):
    GENERAL_KNOWLEDGE = 9
    ENTERTAINMENT_BOOKS = 10
    ENTERTAINMENT_FILM = 11
    ENTERTAINMENT_MUSIC = 12
    ENTERTAINMENT_MUSICALS_AND_THEATRES = 13
    ENTERTAINMENT_TELEVISION = 14
    ENTERTAINMENT_VIDEO_GAMES = 15
    ENTERTAINMENT_BOARD_GAMES = 16
    SCIENCE_AND_NATURE = 17
    SCIENCE_COMPUTERS = 18
    SCIENCE_MATHEMATICS = 19
    MYTHOLOGY = 20
    SPORTS = 21
    GEOGRAPHY = 22
    HISTORY = 23
    POLITICS = 24
    ART = 25
    CELEBRITIES = 26
    ANIMALS = 27
    VEHICLES = 28
    ENTERTAINMENT_COMICS = 29
    SCIENCE_GADGETS = 30
    ENTERTAINMENT_JAPANESE_ANIME_AND_MANGA = 31
    ENTERTAINMENT_CARTOON_AND_ANIMATIONS = 32


class Colour(StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class RunFlags(Flag):
    NONE = 1 << 0
    VERBOSE = 1 << 1
    BUILD = 1 << 2
    DRY_RUN = 1 << 3
    DEBUG = VERBOSE | DRY_RUN


def run(*, flags: RunFlags = RunFlags.NONE):
    log = logging.getLogger("run")

    if flags & RunFlags.VERBOSE:
        log.setLevel(logging.DEBUG)

    if flags & RunFlags.BUILD:
        log.info("Building...")
        log.debug("This may take a while!")
        time.sleep(2)

    log.info("Running...")
    if flags & RunFlags.DRY_RUN:
        log.debug("Running as a dry-run, nothing will change")
    else:
        log.debug("Not running as a dry-run")

    time.sleep(1)
    log.info("Complete!")


if __name__ == "__main__":
    # State ####################################################################

    print(State.PLAYING)  # State.PLAYING

    state = State.PLAYING
    if state == State.PLAYING:
        print("I am playing!")

    print(state.value)  # 1

    print(State.PLAYING.name)  # PLAYING
    print(State.PAUSED.name)  # PAUSED
    print(State.GAME_OVER.name)  # GAME_OVER

    print(State(1))  # State.PLAYING
    print(State.PLAYING.value)  # 1
    print(State.PAUSED.value)  # 2
    print(State.GAME_OVER.value)  # 3

    print(State["PLAYING"])  # State.PLAYING
    print(State.PLAYING.value + State.GAME_OVER.value)  # 4

    # MessageType ##############################################################

    # getting a value from the chat API
    value = "chat_ended_event"
    msgType = MessageType(value)  # initialize MessageType with this 'value'
    print(msgType)

    # IntEnum ##################################################################

    print(Category.GENERAL_KNOWLEDGE + Category.GEOGRAPHY)  # 31 (9 + 22)

    # StrEnum ##################################################################

    print(Colour.RED + Colour.GREEN)  # redgreen

    # Flag #####################################################################

    logging.basicConfig(level=logging.INFO)
    run(flags=RunFlags.DEBUG)
