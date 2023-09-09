import click

from src.core.dependencies.database.database_manager import async_session_maker
from src.core.security.rbac_manager import (
    seed_permissions,
    seed_roles,
    setup_role_permissions
)


async def main():
    async with async_session_maker() as session:
        await seed_roles(session)
        click.echo(click.style('✅ seed_roles done', fg='green'))

        await seed_permissions(session)
        click.echo(click.style('✅ seed_permissions done', fg='green'))

        await setup_role_permissions(session)
        click.echo(click.style('✅ setup_role_permissions done', fg='green'))

        await session.commit()
        click.echo(click.style('✅ Database commit done', fg='green'))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
