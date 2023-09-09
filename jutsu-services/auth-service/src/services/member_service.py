from fastapi import Depends
from fastapi_users.db import BaseUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies.database.database_manager import get_async_session
from src.core.enums import RolesEnum
from src.repositories.member_repository import MemberRepository
from src.repositories.role_repository import RoleRepository


class MemberService:

    def __init__(
            self,
            user_db: BaseUserDatabase,
            session: AsyncSession = Depends(get_async_session)):
        self.user_db = user_db
        self.session = session
        self.member_repo = MemberRepository(self.session)
        self.role_repo = RoleRepository(self.session)

    async def update_member_role(self, member_id: str, role_name: str):
        member = await self.member_repo.get(member_id)
        role = await (
            self.role_repo.get_by_name(role_name)
        )
        member.roles.append(role)
        update_data = {"roles": member.roles}
        await self.user_db.update(member, update_data)
