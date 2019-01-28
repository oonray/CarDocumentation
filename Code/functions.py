"""
.. codeauthor:: Alexander Bjørnsrud
.. date:: 2018-01-07
.. modulename:: lists


1. Construct a User class
    *the user should have a username and a password.

    *there should be a method taking a username and a password as input
        #this function should compare the userame and password to the input
        #it should return true if the user and pass is equal and false if not.

"""
from Crypto.Hash import SHA256, SHA512


class User:
    """
        This user class stores usernames and passwords
        and do user related tasks.

        :param username: The username of the user
        :type username: str

        :param password: The password of the user
        :type password: str
    """
    def __init__(self, *args):
        """
            The constructor
        """

        self.usr = args[0]
        self.pas = self.generate_hash(args[1])
        self.access = 0
        self.authenticated = False

    def generate_hash(self,password):
        """
        Generates hash from string, using SHA256

        :param password: The string to encode
        :type password: str

        :return: SHA265 hash
        :rtype: str
        """
        sha = SHA256.new()
        sha.update(password.encode())
        return sha.hexdigest()

    def check_user(self,username,password):
        """
        Checks wether username and password is correct for this user.

        :param username: The username to check
        :type username: str

        :param password: The password to check
        :type password: str

        :return: True if atuhenticated False if not
        :rtype: bool
        """
        if self.usr == username and self.pas == self.generate_hash(password):
            return True
        return False

    def check_access(self,right):
        """
        This function checks the access rights of the user against the rights provided

        :param right: The right to check against
        :type right: int

        :return: True if access False if not
        :rtype: bool
        """
        if int(right) <= self.access:
            print("Acecss Granted!")
            return True
        else:
            print("No Access")
            return False


class UserFactory:
    Users = []
    User_Values = ["Username","Password"]

    def __init__(self):
        pass

    def add_user(self):
        """
        Adds a user Using inputs
        The config is defined in self.UserValues

        The users can be found using self.get_users or in self.Users

        """
        print("Registering a new user:")
        values = []

        for i in self.User_Values:
            values.append(input("Please Enter your {}>".format(i)))

        self.Users.append(User(values[0],values[1]))

    def get_user(self, username):
        """
        Gets a single user useing username

        :param username: the username to return
        :type username: str

        :return: The user if found or false
        :rtype: User | bool
        """
        for i in self.Users:
            if i.usr == username:
                return i
        return False

    def get_users(self):
        """
        Returns all users

        :return: returns the users
        :rtype: list
        """
        return self.Users

    def set_user(self, User):
        idx = self.Users.index(User)
        self.Users.insert(idx,User)

class Admin(User):
    def __init__(self, Username,Password):
        User.__init__(self,Username,Password)
        self.access = 3

class Authenticator:
    def __init__(self):
        self.factory = UserFactory()

    def authenticate(self, User):
        auth = self.factory.get_user(User.usr)
        if auth:
            if auth.check_user(User.usr,User.pas):
                auth.authenticated = True
                self.factory.set_user(auth)
        else: return False

    def get_auth(self, User):
        return self.factory.get_user(User.usr).authenticated






a = UserFactory()

a.add_user()
b = Authenticator()

u_name = input("Username:>")
p_name = input("Username:>")

login = User(u_name,p_name)

b.authenticate(login)
print(b.get_auth(login))
