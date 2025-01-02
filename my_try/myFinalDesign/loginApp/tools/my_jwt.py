import jwt
import datetime


class MyJWT:
    SECRET_KEY = 'Li123456'

    @staticmethod
    def generate_jwt(user_id):
        payload = {
            'user_id': user_id,
            # 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2),  # 2小时有效期
            # 'iat': datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, MyJWT.SECRET_KEY, algorithm='HS256')
        return token
