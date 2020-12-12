#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ChatbotInstance():
    def __init__(self):
        self.driver = None
        self.start()

    def is_ready(self):
        """
        Returns true, if the chat instance is ready to chat with. Otherwise false.
        """
        return self.driver is not None

    def start(self):
        """
        Launch a new chatbot instance.
        """
        if self.driver is None:
            self.driver = webdriver.PhantomJS()
            self.driver.set_window_size(1280, 720)
            self.driver.get("https://www.cleverbot.com")
            self.driver.implicitly_wait(10)
            return True
        else:
            return False

    def kill(self):
        """
        Kill the current session.
        """
        if self.is_ready():
            self.driver.quit()
            self.driver = None
            return True
        else:
            return False

    def reset(self):
        """
        Kill and start a new session.
        """
        self.kill()
        self.start()

    def chat(self, msg):
        """
        Forward a message to the chatbot and return its answer as string.
        """
        if self.is_ready():
            we = self.driver.find_element_by_css_selector("input.stimulus")
            we.send_keys(msg)
            we.send_keys(Keys.RETURN)
            time.sleep(3)  # Necessary to let Cleverbot process.
            we = self.driver.find_elements_by_css_selector("span.bot")
            return we[-1].text
