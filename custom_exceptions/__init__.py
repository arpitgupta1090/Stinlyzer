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
