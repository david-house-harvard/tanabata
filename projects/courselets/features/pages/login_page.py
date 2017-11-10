"""
Class to work with login page

"""
from .base_page import BasePage
import time


class LoginPage(BasePage):

    def signup_form(self, email):
        email_button = self.click(attr_name='body > div.container > div.buttons > div.container-fluid > div > a')

        email_input = self.find(attr_name='#email-modal > form:nth-child(1) > div:nth-child(2) >'
            ' div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)')

        email_input.send_keys(email)
        login_button = self.click(attr_name='#email-modal > form:nth-child(1) > '
            'div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)')

        time.sleep(3)

    def email_sent_popup(self):
        email_sent_popup = self.find(attr_name='code')
        return email_sent_popup.text

    def alert_email(self):
        email_alert = self.find(attr_name='#alert-popup > div > div > div.modal-body > li')
        return email_alert.text

    def twitter(self, email, password):
        twitter_button = self.click(attr_name='body > div.container > div.buttons > div.row > a:nth-child(5)')
        time.sleep(3)
        email_field = self.find(attr_name='#username_or_email').send_keys(email)
        password_field = self.find(attr_name='#password').send_keys(password)
        enter_button = self.click(attr_name='#allow')
