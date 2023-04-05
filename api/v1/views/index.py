#!/usr/bin/python3
"""
comment
"""
from api.v1.views import app_views
from models import storage
from flask import jsonify


@app_views.route('/status')
def status():
    """
    comment
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def get_count():
    """
    comment
    """
    from models.state import State
    from models.city import City
    from models.user import User
    from models.place import Place
    from models.review import Review
    from models.amenity import Amenity
    classes = {Amenity: "amenities",
               City: "cities",
               Place: "places",
               Review: "reviews",
               State: "states",
               User: "users"}
    return jsonify({name: storage.count(cls) for cls, name in classes.items()})
