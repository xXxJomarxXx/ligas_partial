from sqlmodel import Field , SQLModel
class Survey(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    types: str
    number: int 
    email: str
    nickname: str 
    age: int 
    religion: str
    country: str
    yearlevel: int
    course: str


