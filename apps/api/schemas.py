from typing import Optional

from pydantic import BaseModel, confloat, constr


# ==== GameSession ====
class GameSessionBase(BaseModel):
    name: constr(max_length=128)
    description: Optional[constr(max_length=2048)]
    selected_time_offset: Optional[confloat(ge=0, le=168)]
    selected_time_duration: Optional[confloat(ge=0, le=168)]
    selected_time_timezone: Optional[constr(max_length=512)]


class GameSessionCreate(GameSessionBase):
    pass


class GameSession(GameSessionBase):
    id: int
    owner_id: Optional[int]

    class Config:
        orm_mode = True
