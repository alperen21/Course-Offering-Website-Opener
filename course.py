from selenium import webdriver
import random
import time

term = input("enter the term: ")

if term.lower() == "fall":
    term = "01"
elif term.lower() == "spring":
    term = "02"
elif term.lower() == "summer":
    term = "03"

year = input("enter the year: ")
subject = input("enter the subject: ")
subject = subject.upper()
code = input("enter the code: ")

browser = webdriver.Firefox(executable_path=r'/Users/alperen/Desktop/geckodriver')

url = f"https://www.sabanciuniv.edu/syllabus/courses.cfm?term={term}&year={year}&subject={subject}&code={code}"
browser.get(url)
time.sleep(30)

browser.close()
