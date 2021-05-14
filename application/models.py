from pydantic import BaseModel


class Quote(BaseModel):
    name: str
    message: str