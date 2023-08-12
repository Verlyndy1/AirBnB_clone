#!/usr/bin/python3
"""creates an instance of the FileStorage class to store object data"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
