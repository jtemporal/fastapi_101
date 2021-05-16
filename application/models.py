from pydantic import BaseModel


class Quote(BaseModel):
    id: str
    text: str