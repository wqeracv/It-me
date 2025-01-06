from flask import Flask  # Flask 웹 애플리케이션 생성 및 실행
from flask_smorest import Api  # Flask-Smorest API 생성 및 관리
from flask_2.api import book_blp  # book_blp(Blueprint) 정의가 포함된 파일 임포트

app = Flask(__name__)  # Flask 애플리케이션 인스턴스 생성

# 애플리케이션 설정 (OpenAPI 사양 및 API 문서 관련 설정)
app.config['API_TITLE'] = 'Book API'  # API 제목 설정
app.config['API_VERSION'] = 'v1'  # API 버전 설정
app.config['OPENAPI_VERSION'] = '3.0.2'  # OpenAPI(Swagger) 버전 지정
app.config["OPENAPI_URL_PREFIX"] = "/"  # OpenAPI 문서의 URL 경로 프리픽스
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"  # Swagger UI 경로
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  
# Swagger UI 정적 파일의 외부 CDN 경로

# Flask-Smorest API 인스턴스 생성 및 Flask 앱에 연결
api = Api(app)

# book_blp(Blueprint) 등록: /books 경로와 관련된 API 엔드포인트를 연결
api.register_blueprint(book_blp)

# Flask 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)  # 디버그 모드로 서버 실행 (개발 단계에서 유용)
