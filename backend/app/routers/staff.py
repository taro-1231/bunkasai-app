from fastapi import APIRouter, status, Response
from uuid import uuid4
from ..schemas import BoothDetail, BoothCreateIn
from .public import DB

router = APIRouter(prefix="/api/v1/staff", tags=["staff"])

# class BoothCreateIn(BaseModel):
#     name: str
#     slug: str
#     summary: str | None = None
#     category: str | None = None
#     description_md: str | None = None
#     image_url: str | None = None
#     location: str | None = None
#     open_from: str | None = None
#     open_to: str | None = None

@router.post("/booths", status_code=status.HTTP_201_CREATED)
def create_booth(payload: BoothCreateIn, response: Response):
    if any(b.slug == payload.slug for b in DB["booths"]):
        return JSONResponse(
            status_code=409,
            content={"error":{"code":"slug_conflict","message":"slug already exists","details":{"slug":payload.slug}}}
        )
    detail = BoothDetail(id=uuid4(), **payload.model_dump())
    DB["booths"].append(detail)
    # return JSONResponse(
    #     status_code=201,
    #     headers={"Location": f"/api/v1/public/booths/{detail.slug}"},
    #     content=detail.model_dump()
    # )
    response.headers["Location"] = f"/api/v1/public/booths/{detail.slug}"
    return detail
