import uuid
import logging
from typing import List

from src.core.domain.models.file import File
from src.core.domain.repositories.files_repository import FilesRepository
from src.core.schemas.file_schemas import FilesRequestSchema, FileResponseSchema, FileSchema
from src.core.schemas.response_message import ResponseMessage



async def _add_files(data: FilesRequestSchema, session):
    new_files = []
    for file in data.files:
        new_file = File(
            alias=uuid.uuid4(),
            name = file.name,
            extension = file.extension,
            event_id = str(data.event_id)
        )
        new_files.append(new_file)

    file_repository = FilesRepository(session)
    try:
        await file_repository.save_files(new_files)
        return ResponseMessage(message = "Данные успешно сохранены")
    except Exception as e:
        logging.error(f"Ошибка при сохранении файлов: {e}")
        return ResponseMessage(message = "Произошла ошибка при сохранении файлов")



async def _get_files(event_id, session):
    file_repository = FilesRepository(session)
    try:
        files = await file_repository.get_files(event_id)
        response =  mapping_to_response(files)
        return response
    except Exception as e:
        logging.error(f"Ошибка при получении файлов: {e}")


""" хз тут вообще надо функцию асинхронной делать? """
def mapping_to_response(files: List[File]) -> FileResponseSchema:
    file_schemas = [FileSchema(name=file.name, extension=file.extension, alias=file.alias)
                    for file in files]

    return FileResponseSchema(files=file_schemas)


async def _delete_file(alias, session):
    file_repository = FilesRepository(session)
    try:
        await file_repository.delete_file(alias)
        return None
    except Exception as e:
        logging.error(f"Ошибка при удалении файлов: {e}")