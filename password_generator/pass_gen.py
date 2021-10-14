#!/usr/bin/env python3
# 
# A random password generator that is customizable in terms of:
#      - password length
#      - character sets
#

class GenPass:
    """ Generate password based on a list of rules """
    
    def __init__(self):
        self._pass_len = 6
        self._char_set = "x"

    @property
    def pass_len(self):
        return self._pass_len

    @pass_len.setter
    def pass_len(self, value):
        self._pass_len = value

    def passwd(self, char_set, pass_len):
        if not isinstance(char_set, str):
            char_set = str(char_set)
        return char_set * pass_len
