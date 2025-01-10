from flask_smorest import Blueprint
from flask import request, jsonify
from flask.views import MethodView
from ..models import Question , db

question_blp = Blueprint('Questions','quetsions',description="Operations on Questions", url_prefix = 'questions')

@question_blp.route('/')
class QuestionList(MethodView):
    def get_question(self):
        questions = Question.query.all()
        return jsonify([{'title' : question.title,
                        'is_active' : question.is_active,
                        'sqe' : question.sqe ,
                        'image_id' : question.image_id,
                        'image'  :question.image
                        } for question in questions])

    def post_question(self):
        data = request.json
        new_question = Question(
            title = data['title'], 
            is_active = data['is_active'],
            sqe = data['sqe'],
            image_id = data['iamge_id']
            )
        db.session.add(new_question)
        db.session.commit()
        
        return jsonify({"msg" : "Successfully create question"}), 201
    

@question_blp.route('/<int:question_id>')
class QuestionResource(MethodView):
    def get(self, question_id):
        # 특정 질문 조회
        question = Question.query.get_or_404(question_id)
        return jsonify({
            'title': question.title,
            'is_active': question.is_active,
            'sqe': question.sqe,
            'image_id': question.image_id,
            'image': question.image.to_dict() if question.image else None,
        })
    
    def put(self, question_id):
        # 특정 질문 수정
        question = Question.query.get_or_404(question_id)
        data = request.json

        question.title = data.get('title', question.title)
        question.is_active = data.get('is_active', question.is_active)
        question.sqe = data.get('sqe', question.sqe)
        question.image_id = data.get('image_id', question.image_id)
        
        db.session.commit()
        return jsonify({'msg': 'Successfully updated question'}), 200

    def delete(self, question_id):
        # 특정 질문 삭제
        question = Question.query.get_or_404(question_id)
        db.session.delete(question)
        db.session.commit()
        return jsonify({'msg': 'Successfully deleted question'}), 200


