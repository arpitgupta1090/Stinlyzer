from fastapi import Request
from fastapi.responses import JSONResponse


class DuplicateUserException(Exception):
    def __init__(self, username: str):
        self.username = username


def duplicate_user_exception(request: Request, exc: DuplicateUserException):
    return JSONResponse(status_code=461, content={"msg": f"User name {exc.username} already exists. "})
