from flask.views import MethodView  # Flask에서 제공하는 클래스를 기반으로 한 뷰를 생성하기 위한 모듈
from flask_smorest import Blueprint, abort  # Flask-Smorest에서 API Blueprint 생성과 에러 처리를 위한 모듈
from flask_2.schemas import BookSchema  # Book 데이터를 검증하고 직렬화/역직렬화하기 위한 스키마

# Blueprint 생성: 'books'라는 이름으로 API 라우트 그룹을 설정
book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# 책 데이터를 저장할 리스트. 메모리 내 데이터베이스 역할을 함.
books = []

# /books 경로에 대한 엔드포인트 정의
@book_blp.route('/')
class BookList(MethodView):  # MethodView는 클래스 기반 뷰를 만들기 위한 Flask의 기본 클래스
    # HTTP GET 메서드에 대한 핸들러 정의
    @book_blp.response(200, BookSchema(many=True))  # 응답 데이터를 BookSchema를 사용해 검증 및 직렬화 (여러 개 처리)
    def get(self):
        # 모든 책 데이터를 반환
        return books

    # HTTP POST 메서드에 대한 핸들러 정의
    @book_blp.arguments(BookSchema)  # 요청 데이터를 BookSchema로 검증 및 역직렬화
    @book_blp.response(201, BookSchema)  # 응답 데이터를 BookSchema로 검증 및 직렬화
    def post(self, new_data):
        # 새로운 책 데이터에 고유 ID를 추가
        new_data['id'] = len(books) + 1
        # 리스트에 새 책 데이터 추가
        books.append(new_data)
        # 추가된 책 데이터를 반환
        return new_data

# /books/<int:book_id> 경로에 대한 엔드포인트 정의
@book_blp.route('/<int:book_id>')
class Book(MethodView):  # 특정 책 ID와 관련된 작업을 처리
    # HTTP GET 메서드에 대한 핸들러 정의
    @book_blp.response(200, BookSchema)  # 응답 데이터를 BookSchema로 검증 및 직렬화
    def get(self, book_id):
        # books 리스트에서 요청된 ID와 일치하는 책을 찾음
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            # 책을 찾을 수 없으면 404 오류 반환
            abort(404, message="Book not found.")
        # 찾은 책 데이터를 반환
        return book

    # HTTP PUT 메서드에 대한 핸들러 정의
    @book_blp.arguments(BookSchema)  # 요청 데이터를 BookSchema로 검증 및 역직렬화
    @book_blp.response(200, BookSchema)  # 응답 데이터를 BookSchema로 검증 및 직렬화
    def put(self, new_data, book_id):
        # books 리스트에서 요청된 ID와 일치하는 책을 찾음
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            # 책을 찾을 수 없으면 404 오류 반환
            abort(404, message="Book not found.")
        # 기존 책 데이터를 요청 데이터로 업데이트
        book.update(new_data)
        # 업데이트된 책 데이터를 반환
        return book

    # HTTP DELETE 메서드에 대한 핸들러 정의
    @book_blp.response(204)  # 성공 시 HTTP 204 상태 코드 반환 (내용 없음)
    def delete(self, book_id):
        global books  # 전역 변수 books를 수정하기 위해 global 선언
        # books 리스트에서 요청된 ID와 일치하는 책을 찾음
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            # 책을 찾을 수 없으면 404 오류 반환
            abort(404, message="Book not found.")
        # 해당 ID를 가진 책을 리스트에서 제거
        books = [book for book in books if book['id'] != book_id]
        # 내용 없이 반환
        return ''
