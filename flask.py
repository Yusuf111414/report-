from enum import Enum
from dataclasses import dataclass
class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
@dataclass
class User :
    first_name:str
    last_name:str
    id:int
    gender:Gender