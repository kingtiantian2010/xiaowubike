from . import api
from app import db
from flask import request


# 客户端请求提交自行车停靠点
@api.route('/bikes/', methods=['GET', 'POST'])
def bikes():
    if post:
        bike = request()
        db.session.add(bike)
    bikes = bike.order_by(find.all)
    return jsonify(bikes)
