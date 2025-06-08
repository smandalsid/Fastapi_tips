from typing import Any

m = {"123": "123"}

async def valid_post_id(post_id: str) -> dict[str, Any]:
    post = await get_test(post_id)
    return post

async def get_test(id: str):
    if id in m:
        return m[id]
    else:
        return "LOL"