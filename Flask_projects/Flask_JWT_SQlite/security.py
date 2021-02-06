from users import User
from werkzeug.security import safe_str_cmp

user_list = [
    User(1, "tskaro", "unilab21"),
    User(2, "user2", "unilab22"),
    User(3, "user3", "unilab23"),
]

username_mapping = {user.username: user for user in user_list}
userid_mapping = {user.id: user for user in user_list}


def authentication(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
