import hashlib
import uuid


def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

if __name__ == '__main__':
    password = input('Please enter a password:')
    hashed_password = hash_password(password)
    print('The string to store in the db is:{}'.format(hashed_password))
    password_again = input('Now please enter the password again to check: ')
    if check_password(hashed_password, password_again):
        print('You entered the right password')

    else:
        print('The password does not match')

