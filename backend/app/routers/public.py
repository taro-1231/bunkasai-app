from fastapi import APIRouter, HTTPException, Query
from uuid import uuid4
from ..schemas import BoothListItem, BoothDetail

router = APIRouter(prefix="/api/v1/public", tags=["public"])

DB = {
    "booths": [
        BoothDetail(id=uuid4(), slug="takoyaki-3a", name="たこ焼き 3A", summary="外カリ中トロ", category="food")
    ]
}

@router.get("/booths")
def list_booths(q: str = "", category: str | None = None, page: int = 1, limit: int = Query(20, le=100)):
    items = []
    for b in DB["booths"]:
        if q and q.lower() not in b.name.lower(): continue
        if category and b.category != category: continue
        items.append(BoothListItem(**b.model_dump()))
    total = len(items)
    start = (page-1)*limit
    return {"items":[i.model_dump() for i in items[start:start+limit]], "page":page, "limit":limit, "total":total}

@router.get("/booths/{slug}", response_model=BoothDetail)
def get_booth(slug: str):
    for b in DB["booths"]:
        if b.slug == slug:
            return b
    raise HTTPException(status_code=404, detail="Not Found")
