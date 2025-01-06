from marshmallow import Schema, fields  # Marshmallow를 사용하여 데이터 검증 및 직렬화

# Book 데이터 구조를 정의하는 Schema 클래스
class BookSchema(Schema):
    id = fields.Int(dump_only=True)  
    # `id` 필드: 정수형으로만 출력(dump)되며, 요청 데이터에서는 받지 않음(read-only)
    
    title = fields.String(required=True)  
    # `title` 필드: 문자열 타입이며 요청 데이터에서 필수(required)로 받아야 함
    
    author = fields.String(required=True)  
    # `author` 필드: 문자열 타입이며 요청 데이터에서 필수(required)로 받아야 함
