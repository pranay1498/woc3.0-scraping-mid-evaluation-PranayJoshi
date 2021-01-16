from selenium import webdriver
import os

PATH = "chromedriver.exe"


# functions scrape the website and return list of organisation data
def scrape(user_list):
    try:
        # add headless options to chrome so chrome opens without showing window
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        driver = webdriver.Chrome(PATH)
        driver.get("https://summerofcode.withgoogle.com/archive/2020/organizations/", options=options)

        driver.implicitly_wait(5)

        # get the main ul tag holding all the organisations tab
        org_list = driver.find_element_by_xpath("//ul[contains(@class,'organization-list-container')]")

        # get all individual <a> tags of each organisation
        org_tabs = org_list.find_elements_by_tag_name("a")
        datalist = []

        # store number of organisations which we will use to run loop and pass index
        list_size = len(org_tabs)

        # variable to keep count of preferable organisations found
        match_count = 0

        # loops for total organizations
        # clicks on tab reads data comes back to main page and goes to next tab using indexes
        for index in range(list_size):

            # clear console and print some data on console
            # works when script is run from terminal and not pycharm run tab
            if os.name == 'nt':
                # for windows platfrom
                _ = os.system('cls')
            else:
                # for mac and linux
                _ = os.system('clear')
            print(f'Preferable Organistaions Found: {match_count}')
            print("Searching More...")

            # main element containing list of organizations
            org_list = driver.find_element_by_xpath("//ul[contains(@class,'organization-list-container')]")

            # list of all tha links of different organisations
            org_tabs = org_list.find_elements_by_tag_name("a")

            # click the current index link
            org_tabs[index].click()

            driver.implicitly_wait(2)

            # read all the data
            title_element = driver.find_element_by_xpath("//h3[contains(@class,'banner__title')]")
            title = title_element.text
            link = driver.current_url
            tech_ul = driver.find_element_by_xpath("//ul[contains(@class,'org__tag-container')]")
            tech_li = tech_ul.find_elements_by_tag_name("li")

            # list of technologies for current organisation
            tech_list = []
            for li in tech_li:
                tech_list.append(li.text)

            # check if organisation has any technology matching the need
            if any(item in tech_list for item in user_list):
                datalist.append({'organisation': title, 'link': link, 'technology': tech_list})

                # increase match count
                match_count += 1

            # go back to main page
            driver.back()
            driver.implicitly_wait(5)

        return datalist
    except Exception as e:
        print("something went wrong while scraping the website")
        print(e)
