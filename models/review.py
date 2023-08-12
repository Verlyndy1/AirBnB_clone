#!/usr/bin/python3
"""model for Review class which inherits from Base class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """creates the Review class"""
    place_id = ""
    user_id = ""
    text = ""
