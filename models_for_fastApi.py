from typing import Optional ,List
from pydantic import BaseModel
from enum import Enum
class Gender(str,Enum):
    Male='male'
    female="Female"
class User(BaseModel):
    id:Optional[int]=None
    first_name:str
    last_name:str
    gender:Gender