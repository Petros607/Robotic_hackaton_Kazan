from src import database
from src.user import models, schemas
from typing import Union
from sqlalchemy import select



async def is_login_exists(login: str) -> bool:
    async with database.async_session() as session:
        user = await session.execute(
            select(models.User).where(models.User.login == login)
        )
        user = user.scalars().first()
        if user:
            return True
        return False


async def is_email_exists(email: str) -> bool:
    async with database.async_session() as session:
        user = await session.execute(
            select(models.User).where(models.User.email == email)
        )
        user = user.scalars().first()
        if user:
            return True
        return False


async def add_user(
    login: str, password_hash: str, email: str, username: str, sex: bool, age: int
) -> int:
    """Adds new user to database without any checks

    Args:
        login (str): checked login
        password_hash (str): hash of password
        email (str): checked email
        username (str): Name, Surname, Patroname
        sex (bool): sex
        age (int): age

    Returns:
        int: id of new user from database
    """
    async with database.async_session() as session:
        user = models.User(
            login=login,
            password_hash=password_hash,
            email=email,
            username=username,
            sex=sex,
            age=age,
        )
        session.add(user)
        await session.commit()
        return user.id


async def check_password_hash(login: str, password_hash: str) -> Union[int, None]:
    async with database.async_session() as session:
        user = await session.execute(
            select(models.User).where(
                models.User.login == login
                and models.User.password_hash == password_hash
            )
        )
        user = user.scalars().first()
        if user:
            return user.id
        else:
            return None


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
        

async def update_user(user_id: int, habitation: str | None,
                      validation: str | None,
                      profession: str | None,
                      address: str | None,
                      marriage_status: bool | None):
    async with database.async_session() as session:
        user = await session.execute(select(models.User).where(models.User.id == user_id))
        user = user.scalars().first()
        user.habitation = habitation
        user.validation = validation
        user.profession = profession
        user.address = address
        user.marriage_status = marriage_status
        await session.commit()
        
async def get_user_data(user_id: int) -> schemas.UserDataResponse:
    async with database.async_session() as session:
        user = await session.execute(select(models.User).where(models.User.id == user_id))
        user = user.scalars().first()
        return schemas.UserDataResponse(username = user.username,
                                        email = user.email,
                                        sex = user.sex,
                                        age = user.age,
                                        habitation= user.habitation,
                                        validation = user.validation,
                                        profession = user.profession,
                                        address = user.address,
                                        marriage_status = user.marriage_status)
