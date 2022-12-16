
from command_center import CommandCenter
from help import Help


class CommandOperator():
    def __init__(self, command_center: CommandCenter):
        self.command_center = command_center
        self.list_available_commands()
        self.listen_for_command()

    def list_available_commands(self):

        print("""
Welcome to the the demo student success prediction program.      
This program uses a two layer neural network to demonstrate 
The use of such technology in the process of research in 
fields of humanities and education.
the data in this program is fully fabricated and to a large
extent random used only for demonstration purposes. 
There is a hypothetical premise that we hold to be true in the
hypothetical world in which this program lives. The premise is:
A student with high primary school grades and low parents education
with high access to modern technology and high confidence will be
successful a competency based education environment.
               
              """)
        print('Type "help" or "h" to see instructions for using the program.')
        print('Type "exit" or "q" to end the program.')

    def listen_for_command(self):
        command = str(input('NC> '))
        if(command == 'exit' or command == 'q'):
            self.command_center.exit()

        elif(command == 'help' or command == 'h'):
            self.show_help()
        else:
            print("No such command found.")
            print('Type "help" or "h" to see instructions for using the program.')
            self.listen_for_command()

    def show_help(self):
        Help().show_help()
        self.listen_for_command()
