#!/usr/bin/env python3
""" Mongo with python"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document based on the name
    """
    name_update = {"name": name}
    topics_update = {"$set" : {"topics": topics} }
    return mongo_collection.update_many(name_update, topics_update)