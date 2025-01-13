from flask_smorest import Blueprint
from flask import request, jsonify
from flask.views import MethodView
from ..models import Image, db

image_blp = Blueprint("image", "image", description="Operations On Image", url_prefix="/image")


@image_blp.route('/')
class ImageList(MethodView):
    def get(self):
        imgs = Image.query.all()
        return jsonify([{
            "url": img.url,
            "type": img.type,
        } for img in imgs]), 200

    def post(self):
        data = request.json
        if not data or 'url' not in data or 'type' not in data:
            return jsonify({"msg": "Invalid data"}), 400

        new_img = Image(
            url=data['url'],
            type=data['type']
        )
        db.session.add(new_img)
        db.session.commit()

        return jsonify({"msg": "Successfully created Img"}), 201


@image_blp.route('/<int:image_id>')
class ImageResource(MethodView):
    def put(self, image_id):
        # 특정 이미지 수정
        img = Image.query.get_or_404(image_id)
        data = request.json

        img.url = data.get('url', img.url)  # URL 수정, 없으면 기존 값 유지
        img.type = data.get('type', img.type)  # Type 수정, 없으면 기존 값 유지

        db.session.commit()
        return jsonify({"msg": "Successfully updated Img"}), 200

    def delete(self, image_id):
        # 특정 이미지 삭제
        img = Image.query.get_or_404(image_id)

        db.session.delete(img)
        db.session.commit()
        return jsonify({"msg": "Successfully deleted Img"}), 200
