#!/usr/bin/python3
"""Review class defination"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing  Review."""
    place_id = ""
    user_id = ""
    text = ""

# Hassan Munene
