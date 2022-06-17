from pickletools import read_uint1
from flask_bcrypt import Bcrypt


class Hashing():
    def __init__(self):
        # creating an instance of the Bcrypt
        self.bcrypt = Bcrypt()

    def gen_hash(self,password):
        '''
        this fucntion will generate hash for the input pass and save the hash to the db
        '''
        hashed_pass = self.bcrypt.generate_password_hash(password=password)
        return hashed_pass.decode('utf-8')

    def check_hash(self,hashed_pass,login_pass):
        '''
        this fucntn will check whether the input password and the generated hash for the pass
        are same or not
        It will return true if the password entered for the entered email is matched with the 
        user data present in the db  
        '''
        check_pass = self.bcrypt.check_password_hash(hashed_pass,login_pass)
        print('hashed_pass ',hashed_pass)
        print('login_pass ',login_pass)
        print('return ',check_pass)
        return check_pass

# h = Hashing()
# x = h.gen_hash('password')
# y = h.check_hash(x,'password')
# print(x,y)


# h2 = Hashing()
# x2 = h.gen_hash('password')
# y2 = h.check_hash(x2,'password')
# print(x2,y2)


# print(x is x2 )