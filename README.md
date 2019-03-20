Please excuse my readme as this is my first one I have ever made.
# simpleTerminalBlog
This is a python based blog that uses mongoDB as the database. The technologies I used include: uuid, pymongo, datetime. This is the first OOP python program I have created so let me know how I could make it better. I would love to to know if you guys find any edge cases.

#Database.py (takes in no arguments)is where I used pymongo to connect my local mongodb database to the app.
-initialize(): This method is what initializes which database you would like to use
-insert(collection, data): this method lets you enter the collection you want to enter the data into 
-find(collection, query): lets you query through the collection you specify and find all the values that match the value you enter into the query(no matter number of documents matched, a cursor is returned, never null.)
-find_one(collection, query):very similar to find except this returns a only one (if query matches, first document is returned, otherwise null)

#post.py(blog_id,title, content, author,date,id) this post class is basically a way to create a set of data and then send it to your  database without you actually having to to use the mongodb shell incorporates OOP to make the process a lot more standardized.
- __init__: gives you a unique id if you dont provide the id in the instantiation of the class
-save_to_mongo: This 

