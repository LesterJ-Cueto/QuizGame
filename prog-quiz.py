import tkinter as tk
from tkinter import VERTICAL, RIGHT, Y
import datetime

quiz = tk.Tk()
quiz.title("Quiz System")
quiz.geometry("500x350")
#Getting/ Setting the value of the answers
ans1 = tk.StringVar()
ans1.set(0)

ans2 = tk.StringVar()
ans2.set(0)

ans3 = tk.StringVar()
ans3.set(0)

ans4 = tk.StringVar()
ans4.set(0)

ans5 = tk.StringVar()
ans5.set(0)

ans6 = tk.StringVar()
ans6.set(0)

ans7 = tk.StringVar()
ans7.set(0)

ans8 = tk.StringVar()
ans8.set(0)

ans9 = tk.StringVar()
ans9.set(0)

ans10 = tk.StringVar()
ans10.set(0)

score = 0

#Saving the history
def save_score_history():
    global score
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    score_text = f'Score: {score}/10, Date: {timestamp}\n'


    question_answers = [
        ("1.Which of the following is a programming language?", ans1.get(), "c) Python"),
        ("2.What does HTTP stand for in web development?", ans2.get(), "a) HyperText Transfer Protocol"),
        ("3.In programming, what do you use to store data temporarily?", ans3.get(), "a) Variables"),
        ("4.Which tool is used for tracking changes in source code during software development?", ans4.get(), "a) Git"),
        ("5.What symbol is often used to start a single-line comment in many programming languages?", ans5.get(), "a) //"),
        ("6.What does HTML stand for in web development?", ans6.get(), "a) HyperText Markup Language"),
        ("7.Which type of programming allows you to reuse code and avoid redundancy?", ans7.get(), "a) Object-Oriented Programming"),
        ("8.In programming, what is the result of 10 modulo 3?", ans8.get(), "b) 1"),
        ("9.What does CSS stand for in web development?", ans9.get(), "a) Cascading Style Sheets"),
        ("10.Which type of loop runs a block of code a specific number of times?", ans10.get(), "a) For loop")
    ]

    for question, user_answer, correct_answer in question_answers:
        score_text += f'\nQuestion: {question}\nUser Answer: {user_answer}\nCorrect Answer: {correct_answer}\n'

    with open('score_history.txt', 'a') as file:
        file.write(score_text)
    print("Score history saved.")

#page1
def show_page1():
    for widget in quiz.winfo_children():
        widget.destroy()
    header = tk.Label(master=quiz, text="Quiz about programming", font=("Quiz about programming", 20), bg="#90EE90")
    header.pack()
    header.place(x=100, y=30)

    #Button to proceed to page2
    button1 = tk.Button(quiz, text="Proceed", fg="black", bg="#90EE90",
                        command=show_page2)
    button1.pack(pady=15, padx=10)
    button1.place(x=222, y=200)


def show_page2():
    for widget in quiz.winfo_children():
        widget.destroy()


    #back button to page1
    button2 = tk.Button(quiz, text="Back to Page 1",
                        command=show_page1,fg="black", bg="#90EE90")
    button2.pack(pady=15, padx=10)
    button2.place(x=0, y=0)

    button3 = tk.Button(quiz, text="Submit", command=show_rating,fg="black", bg="#90EE90")
    button3.pack()
    button3.place(x=238, y=320)
    #Pink frame/ Frame for question and radio button choices
    frame = tk.Frame(quiz, bg="#90EE90")
    frame.pack(padx=30, pady=50)
    frame.place(x=65, y=50)

    header = tk.Label(master=quiz, text="Quiz about programming", font=("Quiz about programming", 20), bg="#90EE90")
    header.pack()
    header.place(x=120, y=5)

    canvas = tk.Canvas(frame)
    canvas.pack(side=tk.LEFT, fill='both', expand=True)

    vbar = tk.Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    vbar.pack(side=RIGHT, fill=Y)
    canvas.config(yscrollcommand=vbar.set)

    interior = tk.Frame(canvas, background="#FFC0CB")
    interior.pack(padx=30, pady=50)

    # Add labels and radio buttons
    text1 = tk.Label(master=interior, text="1.Which of the following is a programming language?",bg="#FFC0CB")
    text1.pack()
    tk.Radiobutton(interior, text="a) HTML", variable=ans1, value="a) HTML",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) CSS", variable=ans1, value="b) CSS",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) Python", variable=ans1, value="c) Python",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) JPEG", variable=ans1, value="d) JPEG",bg="#FFC0CB").pack()

    text2 = tk.Label(master=interior, text="2.What does HTTP stand for in web development?",bg="#FFC0CB")
    text2.pack()
    tk.Radiobutton(interior, text="a) HyperText Transfer Protocol", variable=ans2,
                   value="a) HyperText Transfer Protocol",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) HyperText Transfer Process", variable=ans2,
                   value="b) HyperText Transfer Process",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) HyperText Transfer Protocol", variable=ans2,
                   value="c) HyperText Transfer Protocol",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) HyperText Transfer Process", variable=ans2,
                   value="d) HyperText Transfer Process",bg="#FFC0CB").pack()

    text3 = tk.Label(master=interior, text="3.In programming, what do you use to store data temporarily?",bg="#FFC0CB")
    text3.pack()
    tk.Radiobutton(interior, text="a) Variables", variable=ans3, value="a) Variables",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) Functions", variable=ans3, value="b) Functions",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) Arrays", variable=ans3, value="c) Arrays",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) Loops", variable=ans3, value="d) Loops",bg="#FFC0CB").pack()

    text4 = tk.Label(master=interior, text="4.Which tool is used for tracking",bg="#FFC0CB")
    text41 = tk.Label(master=interior,text="changes in source code during software development?",bg="#FFC0CB")
    text4.pack()
    text41.pack()
    tk.Radiobutton(interior, text="a) Git", variable=ans4, value="a) Git",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) Java", variable=ans4, value="b) Java",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) PHP", variable=ans4, value="c) PHP",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) SQL", variable=ans4, value="d) SQL",bg="#FFC0CB").pack()

    text5 = tk.Label(master=interior, text="5.What symbol is often used to start a single-line",bg="#FFC0CB")
    text51 = tk.Label(master=interior,text="comment in many programming languages?",bg="#FFC0CB")
    text5.pack()
    text51.pack()
    tk.Radiobutton(interior, text="a) //", variable=ans5, value="a) //",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) **", variable=ans5, value="b) **",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) --", variable=ans5, value="c) --",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) #", variable=ans5, value="d) #",bg="#FFC0CB").pack()

    text6 = tk.Label(master=interior, text="6.What does HTML stand for in web development?",bg="#FFC0CB")
    text6.pack()
    tk.Radiobutton(interior, text="a) HyperText Markup Language", variable=ans6, value="a) HyperText Markup Language",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) HyperText Makeup Language", variable=ans6, value="b) HyperText Makeup Language",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) HyperText Model Language", variable=ans6, value="c) HyperText Model Language",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) HyperText Manage Language", variable=ans6, value="d) HyperText Manage Language",bg="#FFC0CB").pack()

    text7 = tk.Label(master=interior, text="7.Which type of programming",bg="#FFC0CB")
    text71 = tk.Label(master=interior, text="allows you to reuse code and avoid redundancy?",bg="#FFC0CB")
    text7.pack()
    text71.pack()
    tk.Radiobutton(interior, text="a) Object-Oriented Programming", variable=ans7, value="a) Object-Oriented Programming",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) Procedural Programming", variable=ans7, value="b) Procedural Programming",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) Functional Programming", variable=ans7, value="c) Functional Programming",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) Logical Programming", variable=ans7, value="d) Logical Programming",bg="#FFC0CB").pack()

    text8 = tk.Label(master=interior, text="8.In programming, what is the result of 10 modulo 3?",bg="#FFC0CB")
    text8.pack()
    tk.Radiobutton(interior, text="a) 0", variable=ans8, value="a) 0",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) 1", variable=ans8, value="b) 1",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) 2", variable=ans8, value="c) 2",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) 3", variable=ans8, value="d) 3",bg="#FFC0CB").pack()

    text9 = tk.Label(master=interior, text="9.What does CSS stand for in web development?",bg="#FFC0CB")
    text9.pack()
    tk.Radiobutton(interior, text="a) Cascading Style Sheets", variable=ans9, value="a) Cascading Style Sheets",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) Creative Style Sheets", variable=ans9, value="b) Creative Style Sheets",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) Computer Style Sheets", variable=ans9, value="c) Computer Style Sheets",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) Colorful Style Sheets", variable=ans9, value="d) Colorful Style Sheets",bg="#FFC0CB").pack()

    text10 = tk.Label(master=interior, text="10.Which type of loop runs a block of code a specific number of times?",bg="#FFC0CB")
    text10.pack()
    tk.Radiobutton(interior, text="a) For loop", variable=ans10, value="a) For loop",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) While loop", variable=ans10, value="b) While loop",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) Do-while loop", variable=ans10, value="c) Do-while loop",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) If loop", variable=ans10, value="d) If loop",bg="#FFC0CB").pack()

    # Update the window to show interior frame
    canvas.create_window((0, 0), window=interior, anchor=tk.NW)

    # Update the scrollable region
    interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


show_page1()
#Page3 that includes the user's score
def show_rating():
    #Setting the value of selection using the value get from radio button
    global selection1
    selection1 = ans1.get()

    global selection2
    selection2 = ans2.get()

    global selection3
    selection3 = ans3.get()

    global selection4
    selection4 = ans4.get()

    global selection5
    selection5 = ans5.get()

    global selection6
    selection6 = ans6.get()

    global selection7
    selection7 = ans7.get()

    global selection8
    selection8 = ans8.get()

    global selection9
    selection9 = ans9.get()

    global selection10
    selection10 = ans10.get()

    global score
    #Condition that set the value to score to get the total correct answer
    if selection1 == "c) Python":
        score += 1
    if selection2 == "a) HyperText Transfer Protocol":
        score += 1
    if selection3 == "a) Variables":
        score += 1
    if selection4 == "a) Git":
        score += 1
    if selection5 == "a) //":
        score += 1
    if selection6 == "a) HyperText Markup Language":
        score += 1
    if selection7 == "a) Object-Oriented Programming":
        score += 1
    if selection8 == "b) 1":
        score += 1
    if selection9 == "a) Cascading Style Sheets":
        score += 1
    if selection10 == "a) For loop":
        score += 1

    for widget in quiz.winfo_children():
        widget.destroy()


    header = tk.Label(master=quiz, text="Quiz Results", font=("Quiz Results", 15))
    header.pack()
    header.place(x=66, y=5)

    result = tk.Label(master=quiz, text= ["Your score is:" , str(score),"/10"] , font=("Your score is:", 10), fg="#301934")
    result.pack()
    result.place(x=336, y=5)

    frame = tk.Frame(quiz, bg="#90EE90")
    frame.pack(padx=30, pady=50)
    frame.place(x=65, y=50)

    canvas = tk.Canvas(frame, background="#FFC0CB")
    canvas.pack(side=tk.LEFT, fill='both', expand=True)

    vbar = tk.Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    vbar.pack(side=RIGHT, fill=Y)
    canvas.config(yscrollcommand=vbar.set)

    interior = tk.Frame(canvas, background="#FFC0CB")
    interior.pack(padx=30, pady=50)

    space = tk.Label(master=interior, text="", bg="#FFC0CB")
    space.pack()

    rightans = tk.Label(master=interior, text="List of the correct answers",font=("Your score is:", 10), bg="#FFC0CB", fg="#808080")
    rightans.pack()

    space = tk.Label(master=interior, text="", bg="#FFC0CB")
    space.pack()

    result = tk.Label(master=interior, text="1.Which of the following is a programming language?", bg="#FFC0CB")
    answer1 = tk.Label(master=interior, text="c) Python", fg="#00008b", bg="#FFC0CB")
    result.pack()
    answer1.pack()

    result2 = tk.Label(master=interior, text="2.What does HTTP stand for in web development?", bg="#FFC0CB")
    result2.pack()
    answer2 = tk.Label(master=interior, text="a) HyperText Transfer Protocol", fg="#00008b", bg="#FFC0CB")
    answer2.pack()

    result3 = tk.Label(master=interior, text="3.In programming, what do you use to store data temporarily?", bg="#FFC0CB")
    result3.pack()
    answer3 = tk.Label(master=interior, text="c) def", fg="#00008b", bg="#FFC0CB")
    answer3.pack()

    result4 = tk.Label(master=interior, text="4.Which tool is used for tracking", bg="#FFC0CB")
    result41 = tk.Label(master=interior, text="changes in source code during software development?", bg="#FFC0CB")
    result4.pack()
    result41.pack()
    answer4 = tk.Label(master=interior, text="b) Manage software versions", fg="#00008b", bg="#FFC0CB")
    answer4.pack()

    result5 = tk.Label(master=interior, text="5.What symbol is often used to start a single-line", bg="#FFC0CB")
    result51 = tk.Label(master=interior, text="comment in many programming languages?", bg="#FFC0CB")
    result5.pack()
    result51.pack()
    answer5 = tk.Label(master=interior, text="a) Structured Query Language", fg="#00008b", bg="#FFC0CB")
    answer5.pack()

    text6 = tk.Label(master=interior, text="6.What does HTML stand for in web development?", bg="#FFC0CB")
    text6.pack()
    answer6 = tk.Label(master=interior, text="b) Stack", fg="#00008b", bg="#FFC0CB")
    answer6.pack()

    text7 = tk.Label(master=interior, text="7.Which type of programming", bg="#FFC0CB")
    text71 = tk.Label(master=interior, text="allows you to reuse code and avoid redundancy?", bg="#FFC0CB")
    text7.pack()
    text71.pack()
    answer7 = tk.Label(master=interior, text="d) Instantiation", fg="#00008b", bg="#FFC0CB")
    answer7.pack()

    text8 = tk.Label(master=interior, text="8.In programming, what is the result of 10 modulo 3?", bg="#FFC0CB")
    text8.pack()
    answer8 = tk.Label(master=interior, text="b) JavaScript", fg="#00008b", bg="#FFC0CB")
    answer8.pack()

    text9 = tk.Label(master=interior, text="9.What does CSS stand for in web development?", bg="#FFC0CB")
    text9.pack()
    answer9 = tk.Label(master=interior, text="c) Repeating a block of code", fg="#00008b", bg="#FFC0CB")
    answer9.pack()

    text10 = tk.Label(master=interior, text="10.Which type of loop runs a block of code a specific number of times?", bg="#FFC0CB")
    text10.pack()
    answer10 = tk.Label(master=interior, text="d) Application Programming Interface", fg="#00008b", bg="#FFC0CB")
    answer10.pack()

    # Update the window to show interior frame
    canvas.create_window((0, 0), window=interior, anchor=tk.NW)

    # Update the scrollable region
    interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    button3 = tk.Button(quiz, text="Finished", command=show_page1,fg="black", bg="#90EE90")
    button3.pack()
    button3.place(x=238, y=320)
    #Saving the result
    save_button = tk.Button(quiz, text="Save Score History", command=save_score_history,fg="black", bg="#90EE90")
    save_button.pack()
    save_button.place(x=10, y=320)

quiz.mainloop()
