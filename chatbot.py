#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Chatbot():
    def __init__(self):
        self.driver = None
        self.startChatbot()

    # Gibt zurück, ob der Bot bereit zum interagieren ist.
    def isOn(self):
        return self.driver is not None

    # Starte die Anbindung zum ChatBot.
    def startChatbot(self):
        if self.driver is None:
            self.driver = webdriver.PhantomJS()
            self.driver.set_window_size(1280, 720)
            self.driver.get("http://cleverbot.com")
            self.driver.implicitly_wait(10)
            return True
        else:
            return False

    # Stoppt die Anbindung zum ChatBot.
    def killChatbot(self):
        if self.isOn():
            self.driver.quit()
            self.driver = None
            return True
        else:
            return False

    # Startet den Bot neu.
    def resetChatbot(self):
        self.killChatbot()
        self.startChatbot()

    # Spreche mit Bot. Returnt die Antwort als String.
    def talk(self, msg):
        if self.isOn():
            we = self.driver.find_element_by_css_selector("input.stimulus")
            we.send_keys(msg)
            we.send_keys(Keys.RETURN)
            time.sleep(3)
            we = self.driver.find_elements_by_css_selector("span.bot")
            return we[-1].text


