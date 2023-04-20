from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
from pythonEmail import *

COURSE_SEARCH = [
    ['CAS', 'CS', '111'],
    ['CAS', 'CS', '112'],
    ['CAS', 'CS', '330'],
]

def postpone():
        while True:
            pass

class By:
    ID = "id"
    CLASS_NAME = "class name"
    NAME = "name"
    TAG_NAME = "tag name"

class BUScraper:
    def __init__(self):
            chromedriver = "/chromedriver"
            option = webdriver.ChromeOptions()
            #option.add_argument("--headless")
            option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
            s = Service(chromedriver)
            self.browser = webdriver.Chrome(service=s, options=option)
            #self.browser = webdriver.Safari()

    def login(self, username, password):
        self.browser.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1681937313?ModuleName=final_exam.pl")
        self.browser.find_element(By.ID, 'j_username').send_keys(username)
        self.browser.find_element(By.ID, 'j_password').send_keys(password)
        self.browser.find_element(By.CLASS_NAME, 'input-submit').click()
        while 'studentlink' not in self.browser.current_url:
           pass

    def generate_url(self, college, dept, courseNum, sem="Summer+1+2023", keySem="20241"):
        return f"https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1681941437?ModuleName=reg%2Fadd%2Fbrowse_schedule.pl&SearchOptionDesc=Class+Number&SearchOptionCd=S&ViewSem={sem}&KeySem={keySem}&AddPlannerInd=&College={college}&Dept={dept}&Course={courseNum}&Section="
    
    def get_course(self, college, dept, courseNum):
        self.browser.get(self.generate_url(college, dept, courseNum))
        class_list = []
        try:
            webTable = self.browser.find_element(By.NAME, 'SelectForm')
            rows = webTable.find_elements(By.TAG_NAME, 'tr')
            for row in rows:
                cols = row.find_elements(By.TAG_NAME, 'td')
                counter = 0
                tmpClass = []
                for col in cols:
                    if counter == 2:
                        tmpClass.append(col.text)
                    elif counter == 5:
                        tmpClass.append(col.text)
                    counter += 1
                class_list.append(tmpClass)
            return class_list
        except:
            return []

    def filterClass(self, college="CAS", dept="CS", courseNum="111"):
        class_list = self.get_course(college, dept, courseNum)
        found = False
        for tmpClass in class_list:
            if tmpClass != [] and dept+courseNum in tmpClass[0]:
                print("Course Name: ", tmpClass[0], ", Seats Open: ", tmpClass[1])
                found = True
                if int(tmpClass[1]) > 0:   
                    sendMail("Class Found", f"Class {tmpClass[0]} has {tmpClass[1]} seats open!")
        
        if not found:
            print("No classes found for ", dept, courseNum)

    def driver(self):
        with open('secrets.json') as f:
            data = json.load(f)
        self.login(data['bu_username'], data['bu_password'])
        for course in COURSE_SEARCH:
            self.filterClass(course[0], course[1], course[2])


scraper = BUScraper()
scraper.driver()