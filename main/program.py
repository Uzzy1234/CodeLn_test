import mongoengine
import data.mongo_setup as mongo_setup
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password, make_password

from data.users import User
from .Authbackend import NewCustomAuthBackend


authenticate = NewCustomAuthBackend.authenticate


def authenticate_user():
    email = input("Please enter an email ")
    password = input("Please enter your password")
    tries = 3


    if email and password != "":
        if User.objects.filter(email=email).exists():

            user = User.objects.filter(email=email).first()

            print(user)

        is_password = check_password(password, user.password)

        while tries <=3:
            if not is_password:
                print("You have {} more tries!".format(tries))
                tries = tries - 1
        save_ip()

        SUBJECT = "WARNING!!!"
        SENDER = "uzochukwu.onuegbu25@gmail.com"
        MESSAGE = "Suspicious activiting on your account, please verify if you tried to login"
        send_mail(SUBJECT, MESSAGE, SENDER, [email], fail_silently=False)

        

        if is_password:
        # authenticate the user email and password
            authenticate(request, email=user.email, password=user.password)
            print('User Authenticated!')
            SUBJECT = "WELCOME"
            SENDER = "uzochukwu.onuegbu25@gmail.com"
            MESSAGE = "You have been authenticated!"
            send_mail(SUBJECT, MESSAGE, SENDER, [email], fail_silently=False)
        else:
            print("'password' : ['Incorrect password']")




def create_user():
    name = input('Please add your name ')
    email = input('Input your email here: ')
    password = input('Password: ')
    hashed_password = make_password(password)

    user = User()
    user.name = name
    user.email = email
    user.password = hashed_password

    user.save()
    print('User has been saved')


def ip_address_process(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def save_ip(ip):
    mongo_setup.global_init(db_name='test_db')
    user = User()
    ip_address = ip_address_process()
    if ip_address:
        try:
            user.ip_address = ip_address
            user.save()
        except Exception as e:
            print(e.message)



