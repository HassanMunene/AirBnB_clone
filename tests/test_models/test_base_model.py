#!/usr/bin/python3
"""This is a unittest module"""
import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel
import time


class TestBaseModel(unittest.TestCase):
    """The TestBaseModel class"""
    def test_initialization(self):
        """test instance initialization"""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)

    def test_str(self):
        """test the __str__ method of the class"""
        base = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(base.id, base.__dict__)
        self.assertEqual(str(base), expected_str)

    def test_save(self):
        """test that the update_at time is updated"""
        base = BaseModel()
        old_updated_at = base.updated_at
        time.sleep(1)
        base.save()
        self.assertNotEqual(base.updated_at, old_updated_at)

    def test_to_dict(self):
        """test the instance is converted to dictionary rep"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertEqual(base_dict['id'], base.id)
        self.assertEqual(base_dict['created_at'], base.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'], base.updated_at.isoformat())
