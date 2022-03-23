#!/usr/bin/env python3
""" Mongo with python"""
import pymongo


def list_all(mongo_collection):
    """ List all documents in a collection
    """

    if mongo_collection:
        return list(mongo_collection.find())
    return []