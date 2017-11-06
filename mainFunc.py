import time
import xlrd
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import fileinput
import random




aUsr = 'https://www.instagram.com/'




browser = webdriver.Chrome()
Followed = []
unFollowed = []



print("going to insta")

browser.get('https://www.instagram.com/accounts/login/')


def login():
    username = 'TheRealTonaldDrump'#raw_input("username for Insta Account: ")
    password = 'username'#raw_input("Password for Insta Account: ")
    correct = 'y'#raw_input("Is info correct? y/n: ")

    print(" ")

    print("Loging In")

    if correct == 'y':
        print(username, password)
        usrnm = browser.find_element_by_name('username')  # Find the search box
        usrnm.send_keys(username)

        passwrd = browser.find_element_by_name('password')
        passwrd.send_keys(password + Keys.RETURN)

        time.sleep(5)
    else:
        login()

def followWithLink(path):
    users = open(path, 'r')

    list = users.readlines()

    for i in list:

        print("Attempting to get reach " + str(i))
        print(" ")
        browser.get(i)
        print("Reached!, attempting to follow")
        print(" ")
        print("waiting.....")
        time.sleep(random.randint(1, 5))
        print("Wait Complete, Following")

        try:
            browser.find_element_by_xpath("//*[contains(text(), 'Follow')]").click()
            time.sleep(random.randint(2,5))
        except:
            'Error'
        print("succsess " + str(i) + " followed")


def unfollowWithLink(path):
    users = open(path, 'r')
    list = users.readlines()

    for i in list:
        Followed.append(i)
        print("Attempting to get reach " + str(i))
        print(" ")
        browser.get(i)
        print("Reached!, attempting to unfollow")
        print(" ")
        print("waiting.....")
        time.sleep(random.randint(60, 70))
        print("Wait Complete, unfollowing")

        try:
            browser.find_element_by_xpath("//*[contains(text(), 'Following')]").click()
            time.sleep(random.randint(2,5))

            print(unFollowed)
        except:
            'Error'
        print("succsess " + str(i) + " followed")


def followUsers(listOfNames):
    users = open(listOfNames, 'r')
    list = users.readlines()

    for i in list:
        follow = (aUsr + i)
        Followed.append(i)
        print("Attempting to get " + str(i)+ " profile")
        browser.get(follow)
        print("complete, attempting to follow")

        time.sleep(random.randint(2, 5))
        try:
            browser.find_element_by_xpath("//*[contains(text(), 'Follow')]").click()
        except:
            'Error'
        print("succsess " + str(i) + " followed")


def checkUsers(path):
    users = open(path, 'r')
    list = users.readlines()

    for i in list:
        print("Attempting to get reach " + str(i))
        print(" ")
        browser.get(i)
        print("Reached!, attempting to follow")
        print(" ")
        print("waiting.....")
        time.sleep(2)

def main():
    login()
    type = raw_input("would you like t follow, unfollow, or check Users f/uf/cu: ")

    path = raw_input("what is the file path/name: ")
    path = str(path)
    if type == 'f':
        followWithLink(path)
    elif type == 'uf':
        unfollowWithLink(path)
    else:
        main()






login()

followWithLink('Afile.csv')#this runs the program