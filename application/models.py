from pydantic import BaseModel


class Quote(BaseModel):
    id: int
    text: str