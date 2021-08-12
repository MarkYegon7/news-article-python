class Article:
    
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title
        

        
class web:
    def __init__(self,id,name,description,url,language):
        self.id = id
        self.name = name
        self.descripton = description
        self.url = url
        self.language = language
    
