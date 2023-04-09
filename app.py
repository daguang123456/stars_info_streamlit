import streamlit as st
# from img_classification import teachable_machine_classification
# from PIL import Image, ImageOps
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import pandas as pd
# import os.path as osp
# import glob

import numpy as np
import pymongo
# import RRDBNet_arch as arch
# import matplotlib.pyplot as plt

import requests
# import base64
import json
# from tempfile import NamedTemporaryFile


# authentification
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')

    st.title("关于星星的信息")
    st.write("API[link](https://rapidapi.com/AndyNorDevelop/api/stars-api)")
    prompt = st.text_input("提示", value="星id...")
    if st.button("生成"):
            with st.spinner("请稍候..."):

                url_s = "https://stars-api.p.rapidapi.com/star"
                querystring = {"id":prompt}
                headers = {
                    "X-RapidAPI-Key": "bd10c657b4msh6dbd4f9bf219b22p14f68ajsn0d507d4fae87",
                    "X-RapidAPI-Host": "stars-api.p.rapidapi.com"
                }
                response_s = requests.request("GET", url_s, headers=headers, params=querystring)
                ini_string_s = response_s.json()
                df_p = pd.DataFrame.from_dict(ini_string_s["planets"], orient='columns')
                st.text("名称: "+ini_string_s["name"])
                st.text("星座: "+ini_string_s["constellation"])
                st.text("右升: "+ini_string_s["rightAscension"])
                st.text("赤纬: "+ini_string_s["declination"])
                st.text("视星等: "+ini_string_s["apparentMagnitude"])
                st.text("距离: "+ini_string_s["distance"])
                st.text("光谱类型: "+ini_string_s["spectralType"])
                st.text("质量: "+ini_string_s["mass"])
                st.text("温度："+ini_string_s["temperature"])
                st.text("年龄: "+ini_string_s["age"])

                st.text("行星")
                st.table(df_p)
                # print(ini_string_s)
                

    # print(response.text)


    # client = MongoClient("mongodb://mitmathvideos:IBBD4bWNuf3UKKtr@172.97.225.1/32:27017") 

    # db = client["db_name"]
    st.title("星星列表及其ID")

    url = "https://stars-api.p.rapidapi.com/starslist"

    headers = {
        "X-RapidAPI-Key": "bd10c657b4msh6dbd4f9bf219b22p14f68ajsn0d507d4fae87",
        "X-RapidAPI-Host": "stars-api.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    ini_string = response.json()

    # df = pd.DataFrame(
    # np.random.randn(10, 5),
    # columns=('col %d' % i for i in range(5)))
    df = pd.DataFrame.from_dict(ini_string, orient='columns')

    st.table(df)

    # for dictionary in ini_string:
    #     for key in dictionary:
    #         print(dictionary[key])
    # print(ini_string)
    # print(response.json)
    # for 
    # jsdata = json.load(response.text)
    # print(jsdata)

    # print(response.text)

elif authentication_status == False:
    st.error("用户名/密码不正确")
elif authentication_status == None:
    st.warning('请输入您的用户名和密码')







