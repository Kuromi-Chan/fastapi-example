from typing import List

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.domain.models.file import File


class FilesRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def save_files(self, files: List[File]):
        if files:
            self.db_session.add_all(files)
            await self.db_session.flush()
            await self.db_session.commit()

        return None

    async def get_files(self, event_id):
        query = select(File).where(File.event_id == event_id)
        result = await self.db_session.execute(query)
        files = result.scalars().all()

        return files

    async def delete_file(self, alias):
        query = delete(File).where(File.alias == alias)
        await self.db_session.execute(query)
        await self.db_session.commit()

        return None


