from modules.date_time import *


class Notes():

    def __init__(self):
        self.__id = "1"
        self.__title = "None"
        self.__body = "None"

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_body(self):
        return self.__body

    def set_body(self, body):
        self.__body = body

    def display_info(self):
        return f'{date_time()} \nid: {self.__id} \nTitle: {self.__title} \n - {self.__body} \n'
    
    
