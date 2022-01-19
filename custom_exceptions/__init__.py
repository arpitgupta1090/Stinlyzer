from fastapi import Request
from fastapi.responses import JSONResponse


class DuplicateUserException(Exception):
    def __init__(self, username: str):
        self.username = username


def duplicate_user_exception(request: Request, exc: DuplicateUserException):
    return JSONResponse(status_code=461, content={"msg": f"User name {exc.username} already exists. "})


class SymbolNotFoundException(Exception):
    def __init__(self, symbol: str):
        self.symbol = symbol


def symbol_not_found(request: Request, exc: SymbolNotFoundException):
    return JSONResponse(status_code=462, content={"msg": f"No data received for {exc.symbol} from Yahoo API. "})


class DuplicateSectorException(Exception):
    def __init__(self, sector: str):
        self.sector = sector


def duplicate_sector_exception(request: Request, exc: DuplicateSectorException):
    return JSONResponse(status_code=463, content={"msg": f"User name {exc.sector} already exists. "})


class DuplicateSegmentException(Exception):
    def __init__(self, segment: str):
        self.segment = segment


def duplicate_segment_exception(request: Request, exc: DuplicateSegmentException):
    return JSONResponse(status_code=464, content={"msg": f"User name {exc.segment} already exists. "})


class TargetLimitExceeded(Exception):
    pass


def target_limit_exceeded(request: Request, exc: TargetLimitExceeded):
    return JSONResponse(status_code=465, content={"msg": "Total target cannot be more than 100%"})

