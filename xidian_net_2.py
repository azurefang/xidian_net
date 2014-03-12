#!/usr/bin/python2
# coding:utf-8

import pickle
import requests
import os.path

home = os.path.expanduser('~')
config = os.path.join(home, '.xidian')
try:
    f = open(config, 'r')
except IOError:
    f = open(config, 'w')
    f.close()
xidian = 'http://10.255.44.33/cgi-bin/srun_portal'
info_site = 'http://10.255.44.33/cgi-bin/rad_user_info'
def login():
    action = 'login'
    with open(config, 'rb+') as f:
        try:
            account = pickle.load(f)
            username = account["username"]
            password = account["password"]
        except EOFError:
            username = raw_input('username:')
            password = raw_input('password:')
            account = {"username": username, "password": password}
            pickle.dump(account, f, 2)

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
        print('未连上校园网\n')


    def get_ds():
        online = requests.get(info_site)
        if online == 'not_online':
            print('未登录')
        user_info = online.text.split(',')
        data_stream = int(user_info[6]) / 1000000
        print("已用流量{}M\n".format(data_stream))
    mode = '1'
    while mode == '1':
        mode = raw_input("注销0,实时查流量1其他键关闭窗口\n")
        if mode == '0':
            logout()
        if mode == '1':
            get_ds()

def logout():
    logout = {'action': 'logout'}
    requests.post(xidian, logout)
    print("已注销\n")

if __name__ == '__main__':
    mode = raw_input('login[1],logout[2]')
    if mode == '1':
        login()
    if mode == '2':
        logout()

