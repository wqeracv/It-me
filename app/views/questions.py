from flask_smorest import Blueprint
from flask import request, jsonify
from flask.views import MethodView
from ..models import Question, db

question_blp = Blueprint(
    'Questions', 'questions', description="Operations on Questions", url_prefix='/questions'
)


@question_blp.route('/')
class QuestionList(MethodView):
    def get(self):
        # 모든 질문 조회
        questions = Question.query.all()
        return jsonify([
            {
                'title': question.title,
                'is_active': question.is_active,
                'sqe': question.sqe,
                'image_id': question.image_id,
                'image': question.image.to_dict() if question.image else None,
            }
            for question in questions
        ]), 200

    def post(self):
        # 질문 생성
        data = request.json
        # 입력 데이터 검증
        if not data or 'title' not in data or 'is_active' not in data or 'sqe' not in data:
            return jsonify({'msg': 'Invalid input data'}), 400

        new_question = Question(
            title=data['title'],
            is_active=data['is_active'],
            sqe=data['sqe'],
            image_id=data.get('image_id') 
        )
        db.session.add(new_question)
        db.session.commit()

        return jsonify({'msg': 'Successfully created question'}), 201


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
        }), 200

    def put(self, question_id):
        # 특정 질문 수정
        question = Question.query.get_or_404(question_id)
        data = request.json

        # 입력 데이터 유효성 검증
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
