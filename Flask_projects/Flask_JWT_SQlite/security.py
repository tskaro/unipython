from users import User
from werkzeug.security import safe_str_cmp
from users import find_by_username, find_by_id


# username_mapping = {user.username: user for user in user_list}
# userid_mapping = {user.id: user for user in user_list}


def authentication(username, password):
    user = find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return find_by_id(user_id)
