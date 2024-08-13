from src import database
from src.auth import models
from typing import Union
from sqlalchemy import select


async def add_token(user_id: int, refresh_token: str) -> int:
    """Adds new refresh token to database for user

    Args:
        user_id (int): id of user from database
        refresh_token (str): new refresh_token for this user

    Returns:
        int: id of new token from database
    """
    async with database.async_session() as session:
        new_token = models.Token(refresh_token=refresh_token, user_id=user_id)
        session.add(new_token)
        await session.commit()
        return new_token.id


async def check_token(user_id: int, refresh_token: str) -> Union[int, None]:
    """Checks if refresh_token is correct and active

    Args:
        user_id (int): id of user
        refresh_token (str): refresh_token taken from user

    Returns:
        Union[int, None]: id of token or None if nothing was found
    """
    async with database.async_session() as session:
        tokens = await session.execute(
            select(models.Token).where(models.Token.user_id == user_id)
        )
        tokens = tokens.scalars().all()
        for real_token in tokens:
            if real_token.refresh_token == refresh_token:
                return real_token.id
        return None


async def delete_token(refresh_token_id: str) -> bool:
    """Deletes token from database

    Args:
        refresh_token_id (str): id of refresh_token in database

    Returns:
        bool: True if token was succesfully deleted, False else
    """
    async with database.async_session() as session:
        token = await session.execute(
            select(models.Token).where(models.Token.id == refresh_token_id)
        )
        token = token.scalars().first()
        if token:
            await session.delete(token)
            await session.commit()
            return True
        else:
            return False
