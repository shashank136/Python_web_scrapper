from selenium import webdriver
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re


def school_fun(new_url):
    filename = "schools_details.csv"
    f = open(filename, "a")

    try:
        my_url = new_url

        # opening up the connection, grabbing the page
        newClient = uReq(my_url)
        new_page_html = newClient.read()
        newClient.close()

        # html parsing
        new_page_soup = soup(new_page_html, "html.parser")

        # clicking the link
        driver = webdriver.Firefox()
        driver.get(new_url)

        # doc = driver.page_source
        new_container = new_page_soup.findAll('font', {"face": "times new roman, serif"})

        # getting school_name and school_email_id
        school_name = new_container[1].text.strip()
        email_id = new_container[9].text.strip()

        school_email_id = re.findall(r'[\w\.-]+@[\w\.-]+', email_id)

        # you can comment off the following four print commands if not needed
        print "--------------------------------------------------------------------------------------------------------"
        print "School_Name:     " + school_name
        print "School-Email_id: " + school_email_id[0].strip()
        print "--------------------------------------------------------------------------------------------------------"

        f.write(school_name + "," + school_email_id[0].strip() + "\n")
        # f.close()

    except:
        pass
        print "--------------------------------------------------------------------------------------------------------"
        print "DATA CANNOT BE RETRIVE"
        print "--------------------------------------------------------------------------------------------------------"

    f.close()
    driver.quit();
