from typing import List, Optional
from pydantic import BaseModel, field_validator


class Movie(BaseModel):
    id: int
    title: str
    director: str

    model_config = {
        'json_schema_extra':{
            'example': {
                'id': 1,
                "title":'Inception',
                "director":'Christopher Nolan'
            }
        }
    }

    # @field_validator('title')
    # def validate_title(cls, value):
    #     if len(value)<5:
    #         raise ValueError('Title field must have a min length of 5 characters')
    #     if len(value)>20:
    #         raise ValueError('Title must have a max length of 20 characters')
    #     return value
    

movies: List[Movie] = []    
