from typing import List, Optional, Sequence
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.v1.users import Member, Role


class RoleRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, member_role: Role) -> Role:
        self.session.add(member_role)
        await self.session.commit()
        return member_role

    async def get_all(self) -> Sequence[Role]:
        result = await self.session.execute(select(Role))
        return result.scalars().all()

    async def filter_by_member(self, member_id: str) -> Optional[List[Role]]:
        member = await (
            self.session.execute(select(Member).filter_by(id=member_id))
        )
        member = member.scalars().first()

        await self.session.refresh(member, ['roles'])

        return member.roles if member else None

    async def get_by_id(self, role_id: str) -> Role | None:
        query = await (
            self.session.execute(select(Role).where(Role.id == role_id))
        )
        role = query.scalars().first()

        return role

    async def get_by_name(self, role_name: str) -> Role | None:
        query = await (
            self.session.execute(select(Role).filter_by(name=role_name))
        )
        return query.scalars().first()

    async def update(self, role_id: str, role_data: dict) -> Role:
        query = (
            update(Role).
            where(Role.id == role_id).
            values(**role_data).
            returning(Role)
        )
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalar_one()

    async def delete(self, role_id: str) -> None:
        query = delete(Role).where(Role.id == role_id)
        await self.session.execute(query)
        await self.session.commit()
