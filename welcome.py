#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def welcomeUser(text, name, url):
    t = text.replace("{{name}}", name)
    t = t.replace("{{url}}", url)
    return t
