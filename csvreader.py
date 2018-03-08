#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from user import User

def read(fname):
    users = []

    with open(fname, 'r') as f:
        for row in f:
            values = row.split(",")
            users.append(User(values[0], values[1].lower()))
    f.close()

    return users