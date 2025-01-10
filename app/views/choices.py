from flask_smorest import Blueprint
from flask import request, jsonify
from flask.views import MethodView
from ..models import Choices, db

choices_blp = Blueprint('Choices', 'choices', description="Operations on Choices", url_prefix='/choices')

# Choices 목록 조회
@choices_blp.route('/')
class ChoicesList(MethodView):
    def get(self):
        choices = Choices.query.all()
        return jsonify([{
            'id': choice.id,
            'content': choice.content,
            'is_active': choice.is_active,
            'sqe': choice.sqe
        } for choice in choices])

    def post(self):
        data = request.json
        new_choice = Choices(
            content=data['content'],
            is_active=data['is_active'],
            sqe=data['sqe']
        )
        db.session.add(new_choice)
        db.session.commit()
        
        return jsonify({"msg": "Successfully created choice"}), 201

# 특정 Choice 조회, 수정, 삭제
@choices_blp.route('/<int:choice_id>')
class ChoiceResource(MethodView):
    def get(self, choice_id):
        # 특정 Choice 조회
        choice = Choices.query.get_or_404(choice_id)
        return jsonify({
            'id': choice.id,
            'content': choice.content,
            'is_active': choice.is_active,
            'sqe': choice.sqe
        })
    
    def put(self, choice_id):
        # 특정 Choice 수정
        choice = Choices.query.get_or_404(choice_id)
        data = request.json

        choice.content = data.get('content', choice.content)
        choice.is_active = data.get('is_active', choice.is_active)
        choice.sqe = data.get('sqe', choice.sqe)
        
        db.session.commit()
        return jsonify({'msg': 'Successfully updated choice'}), 200

    def delete(self, choice_id):
        # 특정 Choice 삭제
        choice = Choices.query.get_or_404(choice_id)
        db.session.delete(choice)
        db.session.commit()
        return jsonify({'msg': 'Successfully deleted choice'}), 200
