#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :http_request.py
# @Time      :2020/6/7 22:43
# @Author    :江梅
import requests
import json

#封装一个post，get请求的类
class HttpRequest_Mode():
    def http_requests(self,method,url,data=None,heard=None,cookie=None):
        if method.lower() == 'get':
            res = requests.get(url,data,headers=heard,cookies = cookie)
            return res
        elif method.lower() == 'post':
            res = requests.post(url,data,headers=heard,cookies = cookie)
            return res

if __name__ == "__main__":
    #注册
    url = 'http://api.lemonban.com/futureloan/member/register'
    data = {'mobile_phone': '13922221101', 'pwd': '12345678'}
    data = json.dumps(data)
    heard = {'X-Lemonban-Media-Type': 'lemonban.v2','Content-Type':'application/json'}
    res = HttpRequest_Mode().http_requests('post', url, data, heard)
    print(res.json())

    #登录
    url_login = ' http://api.lemonban.com/futureloan/member/login'
    login_data = {'mobile_phone': '13922221101', 'pwd': '12345678'}
    login_data = json.dumps(login_data)
    print(login_data)
    login_heard = {'X-Lemonban-Media-Type': 'lemonban.v2','Content-Type':'application/json'}
    login_res = HttpRequest_Mode().http_requests('post',url_login,login_data,login_heard)
    token = login_res.json()['data']['token_info']['token']
    print(token)

    #充值接口
    # url_recharge = '  http://api.lemonban.com/futureloan/member/recharge'
    # data_recharge = {'member_id': '10989', 'amount': '100'}
    # data_recharge = json.dumps(data_recharge)
    # heard_recharge = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Content-Type': 'application/json',
    #                   'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEwOTg5LCJleHAiOjE1OTE2MjUzNzR9.-S5pH9RHJzPJb2fWH-v0PpiE2aiAV4BVu3JC_R7YyWaDbFkqD1rzqumQIkP5w-03VzK3wKuAbcabZzOYcz5hoA'}
    # res_recharge = HttpRequest_Mode().http_requests('post', url_recharge, data_recharge, heard_recharge)
    # print(res_recharge.json())