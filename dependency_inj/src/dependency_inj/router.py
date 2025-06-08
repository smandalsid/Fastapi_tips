from fastapi import APIRouter, Depends
from typing import Any

from .service import valid_post_id

# we can also use dependencies to already make validations and not just for fetching prerequisites

router = APIRouter(
    tags=['/test']
)

@router.get("/test_id")
async def get_test(post: dict[str, Any] = Depends(valid_post_id)):
    return post
    

# in fastapi the dependency calls are cached for a particular router