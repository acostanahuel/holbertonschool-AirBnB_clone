# -*- coding: utf-8 -*-
"""Initalizes the main models package."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
