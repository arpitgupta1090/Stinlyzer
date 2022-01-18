from fastapi import FastAPI
from DataBase import models
from DataBase.database import engine
from routers import transaction, user, stock
from fastapi.openapi.utils import get_openapi
from custom_exceptions.exception import (DuplicateUserException,
                                         duplicate_user_exception,
                                         SymbolNotFoundException,
                                         symbol_not_found)


app = FastAPI(docs_url="/", redoc_url="/docs")

models.Base.metadata.create_all(engine)

app.include_router(user.router)
app.include_router(stock.router)
app.include_router(transaction.router)

app.add_exception_handler(DuplicateUserException, duplicate_user_exception)
app.add_exception_handler(SymbolNotFoundException, symbol_not_found)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Stinlyzer API",
        version="1.0.0",
        description="Stinlyzer is Stock Investment analyzer",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
