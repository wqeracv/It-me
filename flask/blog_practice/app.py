from flask import Flask
from flask_mysqldb import MySQL
import yaml  # YAML 파일 읽기를 위한 라이브러리
from flask_smorest import Api  # Swagger와 API 문서화를 위한 라이브러리
from posts_routes import create_posts_blueprint  # posts 관련 API를 정의한 모듈 가져오기

# Flask 애플리케이션 생성
app = Flask(__name__)

# 데이터베이스 설정 정보를 `db.yaml` 파일에서 읽어옴
db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

# MySQL 연결 객체 생성
mysql = MySQL(app)

# OpenAPI(Swagger)를 위한 설정
app.config["API_TITLE"] = "My API"  # API 이름
app.config["API_VERSION"] = "v1"  # API 버전
app.config["OPENAPI_VERSION"] = "3.1.3"  # OpenAPI의 버전
app.config["OPENAPI_URL_PREFIX"] = "/"  # API 문서 기본 경로
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"  # Swagger UI 경로
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  # Swagger UI 라이브러리 URL

# Flask-Smorest API 객체 생성
api = Api(app)

# posts 관련 API 엔드포인트를 블루프린트로 등록
posts_blp = create_posts_blueprint(mysql)
api.register_blueprint(posts_blp)

# 블로그 관리 페이지 렌더링을 위한 라우트
from flask import render_template
@app.route('/blogs')
def manage_blogs():
    return render_template("posts.html")  # posts.html 템플릿 파일 렌더링

# Flask 앱 실행
if __name__ == "__main__":
    app.run(debug=True)  # 디버그 모드로 실행
