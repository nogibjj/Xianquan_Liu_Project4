from pydantic import BaseModel
from enum import Enum
from typing import List

class StringTransformation( str, Enum ):
    replace_number_like = "replace_number_like"
    replace_money = "replace_money"
    replace_email = "replace_email"

class PreprocessingRequest(BaseModel):
    text: str
    steps: List[StringTransformation]
