from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from uuid import UUID

class BoothListItem(BaseModel):
    id: UUID
    slug: str = Field(..., pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    name: str
    summary: Optional[str] = None
    category: Optional[str] = None
    image_url: Optional[str] = None
    open_from: Optional[datetime] = None
    open_to: Optional[datetime] = None

class BoothDetail(BoothListItem):
    description_md: Optional[str] = None
    location: Optional[str] = None
    
class BoothCreateIn(BaseModel):
    name: str
    slug: Optional[str] = None  # 必須にしたいなら: str
    summary: Optional[str] = None
    category: Optional[str] = None
    description_md: Optional[str] = None
    image_url: Optional[str] = None
    location: Optional[str] = None
    open_from: Optional[datetime] = None  # 送るなら ISO 8601
    open_to: Optional[datetime] = None