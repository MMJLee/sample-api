import uvicorn
from fastapi import FastAPI
from config import get_settings
from api import issue
from event import (create_db_connection_pool,close_db_connection_pool)

def get_application():
    config_settings = get_settings()
    base_url = f"/v{config_settings.API_MAJOR_VERSION}"

    app = FastAPI(
        title=config_settings.API_TITLE,
        version=config_settings.API_VERSION,
        description="Sample API",
    )
    app.state.config = config_settings

    # register api event handlers
    app.add_event_handler("startup", create_db_connection_pool(app))
    app.add_event_handler("shutdown", close_db_connection_pool(app))

    # register api endpoints
    app.include_router(issue.router, prefix=base_url+'/issue', tags=["issue"])

app = get_application()
if __name__ == "__main__":  # pragma: no cover
    uvicorn.run(app, host="0.0.0.0", port=8000)