#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 20:45:34 2023

@author: chinmayakumarpalo
"""

import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation


    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


length = int(input("Enter the desired length of the password: "))


password = generate_password(length)
print("Generated password:", password)
