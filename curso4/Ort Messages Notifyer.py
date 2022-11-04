# PENDIENTE DEFINIR EL FLUJO SI SE DEJA TODO EL TIEMPO CON UN WHILE TRUE PARA REFRESCAR LA PAGINA Y VERIFICAR SI HAY NUEVOS MENSAJES

import time
import datetime
import csv
import pandas as pd
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import sys

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# GUIDE
# This program generates an email when it detects there are new messages on the ORT Campus whiteboards
# Created 2020-06-13

# PARAMETERS
web_site = 'https://campus.almagro.ort.edu.ar'
ort_username = ""
ort_pwd = ""
sent_from = ''
email_pwd = ''
sent_to = ''
whiteboards_file_name = "whiteboards.csv"

#FUNCTIONS
def open_database():
    print("Opening Database")
    whiteboards = pd.read_csv(whiteboards_file_name,index_col='subject_name')
    print("Dataframe:\n",whiteboards)
    whiteboards_dict = whiteboards.to_dict()
    print("Dictionary Read:\n",whiteboards_dict)

    return (whiteboards_dict)

###################################################################################################################

def initialize_browser():
    print('Initializing Browser')
    preferences = {'download.prompt_for_download': 'false'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', preferences)
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=options)
    browser.get(web_site)
    time.sleep(1)
    return browser

###################################################################################################################

def login_campus(browser):
    web_access = False
    print("Selecting Login")
    try:
        browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/nav/div/ul[1]/li[1]/a').click()
        time.sleep(1)
        
    except:
        print ("Login not Found")

    print("Entering User and Pwd")
    try:
        browser.find_element_by_id('TxtNombreUsuario').send_keys(ort_username)
        browser.find_element_by_id('TxtPassword').send_keys(ort_pwd)
        browser.find_element_by_id('BtnLogin').click()
        time.sleep(2)
        print("Navigating to notifications")
        browser.find_element_by_id('btnNotificacionesNavbar').click()
        time.sleep(2)
        web_access = True
    except:
        print ("User/pwd not found or error navigating to notifications")

    return web_access

###################################################################################################################

def get_whiteboards(browser):

    print ("Searching for whiteboards")
    try:
        whiteboards = browser.find_elements_by_class_name('itemGrupoTexto')
        print ("whiteboards found")
    except:
        print("whiteboards not found")

    subjects_dict = {}

    for element in whiteboards:
        subject_name = element.text.split('\n')[0]
        num_not_read = element.text.split('\n')[1]

        subject_name = subject_name.partition(" (marcar como leído)")[0].lower()
        num_not_read = num_not_read.partition(" mensaje")[0]
        print("Subject :", subject_name," | Messages: ", num_not_read)
        subjects_dict[subject_name] = num_not_read

        print("Dictionary created:\n",subjects_dict)

    return(subjects_dict)

###################################################################################################################

def compare_dicts (old_subjects_d, current_subjects_d):
    mail_needed = False
    print("Comparing Whiteboards Information")
    for subject in current_subjects_d:
        old_subject_num_not_read = old_subjects_d['num_not_read'].get(subject,-1)
        current_subject_num_not_read = current_subjects_d.get(subject)
        if old_subject_num_not_read == -1:
            mail_needed = True
        elif int(old_subject_num_not_read) < int(current_subject_num_not_read):
            mail_needed = True
    print("mail needed: ", mail_needed)

    return(mail_needed)

###################################################################################################################

def save_database(dict_to_save):
    print("Saving to config file:\n",dict_to_save)

    with open(whiteboards_file_name,'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["subject_name", "num_not_read"])
        for subject in dict_to_save:
            writer.writerow([subject,dict_to_save[subject]])
    return

###################################################################################################################

def send_mail(dict_to_send):
    print("Sending email with dict:\n",dict_to_send)
    subject = '[New unread message(s) in ORT Whiteboard(s)]'
    body = str(dict_to_send)
    msg = MIMEMultipart()
    msg['To'] = sent_to
    msg['From'] = sent_from
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))
    message = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    print("Connecting to Gmail servers")
    server.starttls()
    server.login(sent_from,email_pwd)
    print("Sending Email")
    server.sendmail(sent_from,sent_to,message)
    server.quit()
    return

###################################################################################################################

def logout_campus(browser):
    try:
        browser.find_element_by_xpath('//*[@id="btnMenu"]').click()
        time.sleep(1)
    except:
        print ("MM Error")
    try:
        browser.find_element_by_xpath('//*[@id="menuMiCampusVirtual"]/li[8]/a').click()
        time.sleep(1)
    except:
        print ("Logout Error")
    print("Logout Succesfull")
    return

###################################################################################################################
################################################# MAIN THREAD #####################################################
###################################################################################################################


# Start browser with url
browser = initialize_browser()

while True:
    # Reading Database
    old_subjects_dict = open_database()
    # Login and go to notifications screen
    if login_campus(browser) == True:
        # Obtain a list of whiteboards
        current_subjects_dict = get_whiteboards(browser)
        # Decide if mail is needed
        mail_needed = compare_dicts(old_subjects_dict, current_subjects_dict)
        #Save Database
        save_database(current_subjects_dict)
        #Send Mail
        if mail_needed == True:
            send_mail(current_subjects_dict)
        #Logout
        logout_campus(browser)
    now = datetime.datetime.now()
    print("Finished Execution at: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(300)
