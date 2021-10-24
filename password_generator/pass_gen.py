#!/usr/bin/env python3
# 
# A random password generator that is customizable in terms of:
#      - password length
#      - character sets
#

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

    def passwd(self, char_set, pass_len):
        if not isinstance(char_set, str):
            char_set = str(char_set)
        return char_set * pass_len
