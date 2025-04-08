from pydantic import BaseModel, ConfigDict


class TableCreate(BaseModel):
    name: str
    seats: int
    location: str


class TableDB(TableCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
