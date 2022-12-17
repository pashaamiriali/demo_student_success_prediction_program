
class Help:
    @staticmethod
    def show_welcome():
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

    def show_help(self):
        print(self.help_text)
    help_text = """
        How to use the program:
        When the program first starts, if the database is empty it will 
        show a message saying "Program is not trained." 
        To be able to use the program you first need to give it data to 
        train on and then give data to predict. 
        To train the program you can use the "train" command (explained below).
        To predict the success of failure of a student, you can use the "think"
        command (explained below).
        To why the program thinks that a student will succeed or fail you can 
        use the "why" command after predicting a students' future, and see 
        what variables were involved in the decision.
        
        Command: exit -> closes the program
       
        Command: reset database -> clears all saved data and resets the 
        program. It will ask for reassurance.
       
        Command: create new student -> takes in the students' data and stores
        it in memory to perform operations on. 
        If there is an existing student, it will be replaced with a prompt.
       
        Command: show current student -> shows the data for current student. 
       
        Command: remove current student -> removes the current student.
       
        Command: save current student -> saves the current student to database
        and will return its' id.
        
        Command: find student -> tries to find a student with the given id and
        store it memory as the current student.
       
        Command: predict -> predicts the students' 
        success or failure and gives you a number between 0 and 1 that 
        shows the chance for the given students' success or failure.
      
        Command: train -> Takes in the number of student data that you
        will be entering and then will ask you for entering each students' data
        and then entering its' success or failure status. After getting done with
        entering all of the students, you can enter the number of training
        sessions that the program should spend. then the training starts and after 
        it's done you can view the synaptic weights of each data to success and failure.
        after the training process is done the program will ask you to either save the 
        training results. 
        
        
        Command: train auto -> this command will take in two numerical inputs for
        how many instances of data should be generated and how many will the training
        epochs be. Then it will generate random students and will add train itself
        based on that data.
        
        Command: think-> it will ask to whether take the current students' data or
        a new student and predict if it will succeed or not. it will both give a 
        message of succeed or failure and a number (between 0 and 1) that shows 
        the chance of success.
        
        
    """
