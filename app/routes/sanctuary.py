from flask import Blueprint, jsonify, abort, make_response, request
from app import db

from app.models.sanctuary import Sanctuary
from app.routes.routes_helper import get_valid_item_by_id

sanctuaries_bp =Blueprint("sanctuaries", __name__, url_prefix="/sanctuaries")

@sanctuaries_bp.route("", method=['GET'])
    def handle_sanctuaries():
        name_query = request.args.get("name")
    # if name_query:
    #     sanctuary = Sanctuary.query.filter_by(name=name_query)
    # else:
        sanctuary = Sanctuary.query.all()
    sanctuaries_response = []
    for sanctuary in sanctuaries:
        sanctuaries_response.append(sanctuary.to_dict())
    return jsonify(sanctuaries_response), 200
