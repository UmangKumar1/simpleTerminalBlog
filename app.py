from database import Database
from models.blog import Blog
from menu import menu


Database.initialize()

menu = menu()

menu.run_menu()