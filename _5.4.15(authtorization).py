USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")


def is_auth(func):
    def wrapper():
        func() if auth else print(f'User dont login')
    return wrapper

def has_access(func):
    def wrapper():
        func() if username in USERS else print(f'itd not for you, {username}')
    return wrapper


@is_auth
@has_access
def from_db():
    print("some data from database")

from_db()