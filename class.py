from loader import db,save_db

class Database:
    def __init__(self,ID,name,proficiency,age,dept,zindi="No",kaggle="No"):
        self.ID = ID
        self.name = name
        self.proficiency = proficiency
        self.age = age
        self.dept = dept
        self.zindi = zindi
        self.kaggle = kaggle

    @staticmethod
    def dsn_lead():
        return 'The DSN Lead is Lawrence Okegbemi'
    
    def add(self):
        profile = {self.ID:{"name":self.name,"proficiency":self.proficiency,"age":self.age,\
            "dept":self.dept,"zindi":self.zindi,"kaggle":self.kaggle}}
        if self.ID in db["Database"].keys():
            print("User details already in the database")
        else:
            db["Database"].update(profile)
            save_db()
            print("User details added successfully")

    def update(self):
        profile = {self.ID:{"name":self.name,"proficiency":self.proficiency,"age":self.age,\
            "dept":self.dept,"zindi":self.zindi,"kaggle":self.kaggle}}
        if self.ID not in db["Database"].keys():
            print("No record for this user!")
        else:
            db["Database"].update(profile)
            save_db()
            print("User Profile Successfully Updated")

    def remove(self,id):
        del db["Database"][id]
        save_db()
        print("Details successfully removed")

    
    def retrieve(self):
        print(db)
