from passlib.hash import argon2
from fastapi.concurrency import run_in_threadpool

async def generate_hash(value: str) -> str:
    """
        Generate a hash of provided value.
    """
    return await run_in_threadpool(argon2.hash,value)

async def verify_hash(plain: str,hashed: str) -> bool:
    """
        Compare plain value with hashed value.
    """
    return await run_in_threadpool(argon2.verify,plain,hashed)