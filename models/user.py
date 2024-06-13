#!/usr/bin/python3
"""Define a blueprint for a user of our Airbnb clone"""


class User(BaseModel):
    """The user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
