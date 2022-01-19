from enum import Enum


class Sector(str, Enum):
    IT = "IT"
    TECH = "TECH"
    FINANCE = "FINANCE"
    CRYPTO = "CRYPTO"


class Segment(str, Enum):
    LARGE = "LARGE"
    MID = "MID"
    SMALL = "SMALL"
    MICRO = "MICRO"
