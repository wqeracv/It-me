from flask import request, jsonify  # 요청과 JSON 응답 처리
from flask_smorest import Blueprint, abort  # Blueprint와 오류 처리 기능

# posts 블루프린트 생성 함수
def create_posts_blueprint(mysql):
    # posts 관련 API를 정의할 Blueprint 객체 생성
    posts_blp = Blueprint(
        "posts",  # 블루프린트 이름
        __name__,  # 현재 모듈의 이름
        description="posts api",  # 블루프린트 설명
        url_prefix="/posts",  # 엔드포인트의 기본 URL 경로
    )

    # 게시글 조회 및 생성
    @posts_blp.route("/", methods=["GET", "POST"])
    def posts():
        cursor = mysql.connection.cursor()  # MySQL 연결 객체에서 커서 생성

        # **GET 요청**: 게시글 목록 조회
        if request.method == "GET":
            sql = "SELECT * FROM posts"  # 모든 게시글 조회 쿼리
            cursor.execute(sql)

            posts = cursor.fetchall()  # 모든 결과 가져오기
            cursor.close()

            post_list = []  # 게시글 목록 저장
            for post in posts:
                post_list.append(
                    {
                        "id": post[0],
                        "title": post[1],
                        "content": post[2],
                    }
                )
            return jsonify(post_list)  # JSON 형태로 응답

        # **POST 요청**: 게시글 생성
        elif request.method == "POST":
            title = request.json.get("title")  # 요청에서 제목 가져오기
            content = request.json.get("content")  # 요청에서 내용 가져오기

            # 제목 또는 내용이 없는 경우 오류 반환
            if not title or not content:
                abort(400, message="title 또는 content가 없습니다.")

            sql = "INSERT INTO posts(title, content) VALUES(%s, %s)"  # 새 게시글 삽입 쿼리
            cursor.execute(sql, (title, content))
            mysql.connection.commit()  # 변경사항 커밋

            return jsonify({"message": "success"}), 201  # 성공 응답

    # 게시글 상세 조회, 수정 및 삭제
    @posts_blp.route("/<int:id>", methods=["GET", "PUT", "DELETE"])
    def post(id):
        cursor = mysql.connection.cursor()  # MySQL 커서 생성

        # **GET 요청**: 특정 게시글 상세 조회
        if request.method == "GET":
            sql = f"SELECT * FROM posts WHERE id={id}"  # 특정 게시글 조회 쿼리
            cursor.execute(sql)
            post = cursor.fetchone()  # 단일 결과 가져오기

            # 게시글이 없는 경우 오류 반환
            if not post:
                abort(404, message="해당 게시글이 없습니다.")
            return {
                "id": post[0],
                "title": post[1],
                "content": post[2],
            }

        # **PUT 요청**: 특정 게시글 수정
        elif request.method == "PUT":
            title = request.json.get("title")  # 요청에서 제목 가져오기
            content = request.json.get("content")  # 요청에서 내용 가져오기

            # 제목 또는 내용이 없는 경우 오류 반환
            if not title or not content:
                abort(400, message="title 또는 content가 없습니다.")

            # 게시글 존재 여부 확인
            sql = "SELECT * FROM posts WHERE id=%s"
            cursor.execute(sql, (id,))
            post = cursor.fetchone()

            if not post:
                abort(404, message="해당 게시글이 없습니다.")

            # 게시글 업데이트 쿼리 실행
            sql = "UPDATE posts SET title=%s, content=%s WHERE id=%s"
            cursor.execute(sql, (title, content, id))
            mysql.connection.commit()

            return jsonify({"message": "Successfully updated title & content"})

        # **DELETE 요청**: 특정 게시글 삭제
        elif request.method == "DELETE":
            # 게시글 존재 여부 확인
            sql = "SELECT * FROM posts WHERE id=%s"
            cursor.execute(sql, (id,))
            post = cursor.fetchone()

            if not post:
                abort(404, message="해당 게시글이 없습니다.")

            # 게시글 삭제 쿼리 실행
            sql = "DELETE FROM posts WHERE id=%s"
            cursor.execute(sql, (id,))
            mysql.connection.commit()

            return jsonify({"message": "Successfully deleted post"})

    return posts_blp  # Blueprint 객체 반환
