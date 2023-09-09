from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.models.v1.users import Member


class MemberRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, member_id: str) -> Member:
        member = await (
            self.session.execute(select(Member).options(joinedload(Member.roles)).filter_by(id=member_id)))

        member = member.scalar()

        return member
