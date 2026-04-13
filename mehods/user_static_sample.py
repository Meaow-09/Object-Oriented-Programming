class User:
    

    def __init__(self, name):
        if self.is_valid_name(name):
            self.name = name
        else:
            raise Exception("invalid User name")
    
    def is_valid_name(name):
        return name.isalpha()
    

##usage
u1=User("John Cena")
u2=User("Joan Doe")

print(u1.get_user_count())
print(u2.get_user_count())


