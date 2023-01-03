#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Caroline", "Muthoni")
say_my_name("Calvert", "Lewin")
say_my_name("Paul")
try:
    say_my_name(12, "George")
except Exception as e:
    print(e)
