import unittest
from model.abstract_entity import Entity
import shutil

class TestAbstractEntity(unittest.TestCase):
    def setUp(self):
        return

    def TearDown(self):
        #TODO: delete the copy the results in dwh
        return

    def test_configuration(self):
        """
        When implemented
        """
        return

    def test_populate_without_dependency(self):
        return

    def test_populate_with_dependency_and_no_dependency_of_dependency(self):
        return

    def test_populate_with_dependency_and_already_existing_dependency_of_dependency(self):
        return

    def test_populate_with_dependency_and_circular_dependency(self):
        """
        When implemented
        """
        return

    def test_header_export(self):
        return