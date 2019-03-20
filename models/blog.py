import uuid
from database import Database
from models.posts import Posts
import datetime

class Blog:
    def __init__(self, author, title, description, id =None):
        self.author=author
        self.title = title
        self.description= description
        self.id = uuid.uuid4().hex if id is None else id
    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter new content: ")
        date = input("Enter post date or leave black for today(In format DDMMYYYY):")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date=datetime.datetime.strptime(date,'%d%m%y')
        post= Posts(blog_id= self.id,
                    title=title,
                    content=content,
                    date= date,
                    author= self.author
        )
        post.save_to_mongo()
    def get_post(self):
        return Posts.from_blog(self.id)
    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())
    def json(self):
        return{
            'author': self.author,
            'title': self.title,
            'description':self.description,
            'id': self.id
            }
    @classmethod
    def from_mongo(cls,id):
        blog = Database.find_one(collection='blogs', query=({'id':id}))
        return cls(author=blog['author'],
                   title=blog['title'],
                   description=blog['description'],
                   id=blog['id'])