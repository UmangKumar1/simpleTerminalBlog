import uuid
import datetime
from database import Database
#this post class is basically a way to create a set of data and then
# send it to your  database without you actually having to to use the mongodb shell
#incorporates OOP to make the process a lot more standardized
Database.initialize()
class Posts:
    #class Post takes 6 inputs
    def __init__(self, blog_id,title, content, author,date= datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content= content
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id
        self.created_date = date
    #this takes your already created instance of a class and sends the related data to the right collection
    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data= self.json())
    #takes the object values and returns a json with the same information
    def json(self):
        return{
            'id': self.id,
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_date': self.created_date
            }
    @staticmethod
    #this function takes the id as a parameter and then returns the data linked to that data
    def from_mongo(id):
        return Database.find_one(collection='posts', query ={'id':id})
    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id':id})]







