from typing import List, Optional
from pydantic import BaseModel
import uuid

""" Тут описываются схемы для репспонсов и реквестов?"""

class FileSchema(BaseModel):
    name: str
    extension: str
    # data: str
    alias: str

class FilesRequestSchema(BaseModel):
    event_id: Optional[uuid.UUID] 
    files: List[FileSchema]

class FileResponseSchema(BaseModel):
    files: List[FileSchema]

class FileDeleteSchema(BaseModel):
    alias: str
    extension: str



