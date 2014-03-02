#!/usr/bin/env python
# coding:utf-8

import sys
try:
    import requests
except ImportError:
    print("缺少requests库")

xidian = 'http://10.255.44.33/cgi-bin/srun_portal'

def login():
    action = 'login'
    username = '03111181'
    password = 'peter1994'
    ac_id = 6
    type = 1

    login = {'action': action,
            'username': username,
            'password': password,
            'ac_id': ac_id,
            'type':type}

    try:
        requests.post(xidian, login)
    except requests.ConnectionError:
        print('未连上校园网')

def logout():
    logout = {'action': 'logout'}
    requests.post(xidian, logout)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'login':
            login()
        if sys.argv[1] == 'logout':
            logout()
    else:
        print('''invalid command,use
            ``python xidian.py login`` to login
            ``python xidian.py logout`` to logout''')

