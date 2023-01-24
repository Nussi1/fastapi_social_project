from fastapi import FastAPI
from . import models
from .database import engine
from .routers import profile, dweet, user, authentication

app = FastAPI(debug=True)

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(dweet.router)
app.include_router(profile.router)
app.include_router(user.router)


# SQLAlchemy~=1.4.45