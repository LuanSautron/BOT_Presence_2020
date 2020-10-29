from student import Student

class Event:

    def __init__(self, message):
        self.command = None
        self.id = message.author.id
        self.content = message.content
        if (message.content[0] == '/'):
            try:
                self.command = message.content.split('/')[1].split(' ')[0]
            except Exception as e:
                print(e)

    def register_student(self):
        email = ""
        try:
            email = self.content.split(' ')[1]
        except IndexError:
            return "There is a problem with your email !"
        toto = Student(self.id, email)
        if (toto.push_in_db() is False):
            return "There is a problem with your email !"
        return "You succefully register !"
    
    def check_presence(self):
        toto = Student(self.id)
        if toto.get_db_by_id() is False:
            return "You aren't register... Try this command: /register [email]"
        return "All is good ! Because you are here !"
    
    def do(self):
        if (self.command is None):
            return None
        if (self.command == "register"):
            return self.register_student()
        if (self.command == "present"):
            return self.check_presence()
        return None
        