from student import Student, DBCo
from write import Xlwriter

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
        val = toto.push_in_db()
        if (val == 1):
            print("New student register : " +  email)
            return "You are succefully registered !"
        if (val == -2):
            return "Your mail is not an epitech mail !"
        if (val == -3):
            toto.get_db_by_id()
            return "You are already registered with this email (" + str(toto.email) + ").\nIf it's not you, contact a pedago !"

    def check_presence(self, list_s):
        toto = Student(self.id)
        if toto.get_db_by_id() is False:
            return "You aren't registered ... Try this command: /register [email]"
        if len(list_s.tab[0][0]) == 0:
            return "There are no activities in progress !"
        if list_s.is_email_in(toto.email) is False:
            return "Your aren't registered to this activity, contact a pedago if there is a problem !"
        list_s.update_presence(toto.email, "present")
        print("This student is present : " + toto.get_email())
        return "All is good ! Because you are here !"

    def close_all(self, list_s, list_p):
        toto = Student(self.id)
        toto.get_db_by_id()
        if list_p.is_pedago(toto.email) is False:
            return "You don't have the rights to execute this command"
        DBCo().conn.close()
        list_s.create_xls()
        return "stop"

    def list_register(self, list_s, list_p):
        toto = Student(self.id)
        toto.get_db_by_id()
        if list_p.is_pedago(toto.email) is False:
            return "You don't have the rights to execute this command"
        lists = ""
        for i, j in list_s.tab:
            lists = lists + i + ": " + j + "\n"
        print(lists)
        if lists == "absent\n":
            return "None"
        return lists

    def do(self, list_s, list_p):
        if (self.command is None):
            return None
        if (self.command == "register"):
            return self.register_student()
        if (self.command == "present"):
            return self.check_presence(list_s)
        if (self.command == "list_register"):
            return self.list_register(list_s, list_p)
        if (self.command == "stop"):
            return self.close_all(list_s, list_p)
        return None
        