from fastapi import APIRouter


router = APIRouter(prefix="/paste", tags=["pastes"])

@router.post("/")
async def create_paste() -> str:
    pass


@router.get("/{hash}")
async def get_paste(hash: str):
    pass


@router.put("/{hash}")
async def update_paste(hash: str):
    pass


@router.delete("/{hash}")
async def delete_paste(hash: str):
    pass