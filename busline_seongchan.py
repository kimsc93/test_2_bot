import re
import urllib.request
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from slackclient import SlackClient
from flask import Flask, request, make_response, render_template
import time


def busline(bus_num):
    driver = webdriver.Chrome(r'./chromedriver.exe')
    url = "http://www.jeonjuits.go.kr/index.jeonju?menuCd=DOM_000000101000000000"
    driver.get(url)
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    for e in driver.find_elements_by_class_name("tab01_content"):
        print(e.text)

    print("버스번호 입력 : ", end="")
    bus_num = input()

    driver.find_element_by_id("search-busroute-keyword").send_keys(bus_num)
    bt = driver.find_element_by_tag_name("button")
    bt.click()
    time.sleep(1)
    bt2 = driver.find_element_by_class_name("tab01_box03")
    bt2.click()
    time.sleep(1)
    load_list = driver.find_element_by_tag_name("ul").text
    print(load_list)
    for i in driver.find_elements_by_class_name("tab01_box02_guide"):
        print(i.text)


    return load_list


if __name__ == "__main__":

    busline(1)
    pass
