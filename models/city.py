#!/usr/bin/python3
"""model for city class which inherits from Base class"""


from models.base_model import BaseModel


class City(BaseModel):
    """creates the city class"""
    state_id = ""
    name = ""
