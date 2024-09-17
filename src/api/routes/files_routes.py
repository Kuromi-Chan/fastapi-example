from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.domain.session import get_db
from src.core.schemas.file_schemas import FilesRequestSchema, FileResponseSchema, FileDeleteSchema
from src.core.schemas.response_message import ResponseMessage
from src.core.service.files_service import _add_files, _get_files, _delete_file

files_router = APIRouter()

@files_router.post('/files', response_model=ResponseMessage, summary='Добавление файлов к задаче')
async def add_files(
        data: FilesRequestSchema,
        db: AsyncSession = Depends(get_db),
):
    response = await _add_files(data, db)

    return response

@files_router.get('/files', response_model=FileResponseSchema, summary='Получить файлы задачи')
async def get_files(
        event_id: str,
        db: AsyncSession = Depends(get_db),
):
    response = await _get_files(event_id, db)
    return response

@files_router.delete('/files', response_model=str, summary='Удалить файл задачи')
async def delete_file(
        data: FileDeleteSchema,
        db: AsyncSession = Depends(get_db),
):
    await _delete_file(data.alias, db)
    return 'Файлы удалены'