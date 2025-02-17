import tkinter, tkinter.messagebox, random, json

class ProgramGUI:

    def __init__(self):
        # Try to open file. Show error message if file doesn't exist or contains invalid JSON format.
        try:
            file = open('data.txt', 'r')
            data = json.load(file)
            file.close()
        except FileNotFoundError:
            tkinter.messagebox.showerror('File Error', 'Missing/Invalid File')
            return
        except json.JSONDecodeError:
            tkinter.messagebox.showerror('File Error', 'Missing/Invalid File')
            return
        
        self.data = data

        # If 'self.data' list doesn't have 2 or more elements, show error message.
        if len(self.data) < 2:
            tkinter.messagebox.showerror('File Error', 'Insufficient fruit items')
            return
        
        self.components = ['energy', 'fibre', 'sugar', 'potassium']
        
        self.question_count = 0
        self.correct_answers = 0

        self.create_window()

        tkinter.mainloop()

    # Creates window with new questions.
    def create_window(self):
        self.main = tkinter.Tk()
        self.main.title('Fruit Quiz')

        self.intro_label = tkinter.Label(self.main, text='Which one has more...').pack()

        self.show_question()

        # Increase question count by 1 when new question is displayed.
        self.question_count += 1
        self.question_label = tkinter.Label(self.main, text=self.question.upper(), font=('Callibri', 24)).pack()

        # Creating a Frame to contain buttons.
        self.buttons = tkinter.Frame(self.main)

        # Calls 'check_answer' function when button is pressed.
        self.left_button = tkinter.Button(self.buttons, text=self.choices[0]['name'], command=lambda: self.check_answer('left'))
        self.right_button = tkinter.Button(self.buttons, text=self.choices[1]['name'], command=lambda: self.check_answer('right'))
        self.left_button.pack(side='left', padx=5, pady=5)
        self.right_button.pack(side='right', padx=5, pady=5)

        self.buttons.pack()
        
    # Sets new fruit question and fruit choices.
    def show_question(self):
        # This method randomly selects two fruit and a nutritional component and displays them in the GUI.
        self.choices = random.sample(self.data, 2)
        self.question = random.choice(self.components)
        
    ## Checks answer, shows appropriate message box, and refreshes window.
    def check_answer(self, choice):   
        # This method is responsible for determining whether the user clicked the correct button.
        self.answers = [self.choices[0][self.question], self.choices[1][self.question]]

        if self.answers[0] == self.answers[1]:
            correct_answer = self.answers[0]
            correct_answer = self.answers[1]
        elif self.answers[0] > self.answers[1]:
            correct_answer = self.answers[0]
        elif self.answers[1] > self.answers[0]:
            correct_answer = self.answers[1]
        
        if choice == 'left':
            if correct_answer == self.answers[0]:
                self.correct_answers += 1
                self.correct = tkinter.messagebox.showinfo('Correct!', 'You got it right.\nScore: ' + str(self.correct_answers) + '/' + str(self.question_count))
            else:
                self.wrong = tkinter.messagebox.showerror('Incorrect!', 'You got it wrong.\nScore: ' + str(self.correct_answers) + '/' + str(self.question_count))
                
        elif choice == 'right':
            if correct_answer == self.answers[1]:
                self.correct_answers += 1
                self.correct = tkinter.messagebox.showinfo('Correct!', 'You got it right.\nScore: ' + str(self.correct_answers) + '/' + str(self.question_count))
            else:
                self.wrong = tkinter.messagebox.showerror('Incorrect!', 'You got it wrong.\nScore: ' + str(self.correct_answers) + '/' + str(self.question_count))

        self.main.destroy()
        self.create_window()
        
# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
