#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import json
from pymisp.tools import FileObject
import pathlib


class TestFileObject(unittest.TestCase):
    def test_mimeType(self):
        file_object = FileObject(filepath=pathlib.Path(__file__))
        attributes = json.loads(file_object.to_json())['Attribute']
        mime = next(attr for attr in attributes if attr['object_relation'] == 'mimetype')
        # was "Python script, ASCII text executable"
        self.assertEqual(mime['value'], 'text/x-python')
