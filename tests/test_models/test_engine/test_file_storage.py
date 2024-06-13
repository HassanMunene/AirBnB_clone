import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """the test class"""
    def setUp(self):
        """set up the test environment"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Remove file.json if it exists"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage.__objects = {}

    def test_all(self):
        """
        test that all() returns the correct dictionary where
        key=className.id and value=object
        """
        self.assertEqual(self.storage.all(), {"BaseModel.{}".format(self.model.id): self.model})

    def test_new(self):
        """test that new() correctly adds an object to __objects"""
        self.assertIn("BaseModel.{}".format(self.model.id), self.storage.all())

    def test_save(self):
        """test save() correctly  serializes objects to file.json"""
        self.storage.save()
        self.assertTrue(os.path.isfile(self.file_path))

        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.assertIn("BaseModel.{}".format(self.model.id), data)
            self.assertEqual(data["BaseModel.{}".format(self.model.id)]["id"], self.model.id)

    def test_reload(self):
        """Test that reload() correctly deserializes objects from file.json"""
        self.storage.save()
        self.storage.reload()
        self.assertIn("BaseModel.{}".format(self.model.id), self.storage.all())
        reloaded_model = self.storage.all()["BaseModel.{}".format(self.model.id)]
        self.assertEqual(reloaded_model.id, self.model.id)
        self.assertEqual(reloaded_model.created_at.isoformat(), self.model.created_at.isoformat())
        self.assertEqual(reloaded_model.updated_at.isoformat(), self.model.updated_at.isoformat())
