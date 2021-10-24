#!/usr/bin/env python3
# 
# A random password generator that is customizable in terms of:
#      - password length
#      - character sets
#

import random

ALPHA   = "abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM     = "0123456789"
SPECIAL = "@#$%&*"

class GenPass:
    """ Generate password based on a list of rules """

    def __init__(self):
        self._pass_len = 8
        self._char_set = ALPHA + NUM + SPECIAL


    @property
    def pass_len(self):
        return self._pass_len

    @pass_len.setter
    def pass_len(self, value):
        self._pass_len = value

    @property
    def char_set(self):
        return self._char_set

    @char_set.setter
    def char_set(self, value):
        self._char_set = value

    def passwd(self, pass_len=None, char_set=None):
        """
        Generate the password based on given length and character sets
        """
        if pass_len:
            self.pass_len = pass_len

        if char_set:
            self.char_set = char_set if isinstance(char_set, str) else str(char_set)
            # if not isinstance(char_set, str):
            #     self.char_set = str(char_set)
            # else:
            #     self.char_set = char_set
        
        password = []

        # Randomly pick one character from the set each time
        for i in range(self.pass_len):
            password.append(random.choice(self.char_set))
            
        print(f"password list: {password}")
        
        return password
