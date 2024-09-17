import uvicorn
from fastapi import FastAPI

from src.api.routes.files_routes import files_router

app = FastAPI(title= 'Загрузка файлов к задаче')
app.include_router(files_router, prefix='/event', tags=['Files'])


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0")

