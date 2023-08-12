#!/usr/bin/python3
"""User class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """creates the User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
