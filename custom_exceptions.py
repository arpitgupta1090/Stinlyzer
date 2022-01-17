from fastapi import Request
from fastapi.responses import JSONResponse
# from main import app


class DuplicateUserException(Exception):
    def __init__(self, username: str):
        self.username = username


@app.exception_handlers(DuplicateUserException)
def duplicate_user_exception(request: Request, exc: DuplicateUserException):
    return JSONResponse(status_code=418, content={"msg": f"User name {exc.username} already exists. "})
