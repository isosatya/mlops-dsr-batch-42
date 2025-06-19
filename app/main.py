import torch
import io
from pydantic import BaseModel

# this is a "data model" for the output of the fruit classifier
class Result(BaseModel):
    category: str
    confidence: float
