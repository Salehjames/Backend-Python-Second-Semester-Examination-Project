from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication


app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
