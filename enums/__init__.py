from enum import Enum


class Sector(str, Enum):
    IT = "IT"
    TECH = "TECH"
    FINANCE = "FINANCE"
    RETAIL = "RETAIL"
    CRYPTO = "CRYPTO"


class Segment(str, Enum):
    LARGE = "LARGE"
    MID = "MID"
    SMALL = "SMALL"
    MICRO = "MICRO"
