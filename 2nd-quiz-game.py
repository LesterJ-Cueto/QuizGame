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
        ("1.Who is the God of the sky and lightning?", ans1.get(), "c) Zeus"),
        ("2.Who is the God of the sea?", ans2.get(), "a) Poseidon"),
        ("3.Who is the God of the underworld?", ans3.get(), "a) Hades"),
        ("4.Which Greek God is the Personification of the Earth?", ans4.get(), "a) Gaia"),
        ("5.Who is the Goddess of wisdom?", ans5.get(), "a) Athena"),
        ("6.Who is the God of war?", ans6.get(), "a) Ares"),
        ("7.Who is the God of music and medicine?", ans7.get(), "a) Apollo"),
        ("8.Who was the child of Poseidon and Medusa?", ans8.get(), "b) Pegasus"),
        ("9.Poseidon is the god of the sea and?", ans9.get(), "a) Earthquake"),
        ("10.How many children does Zeus have?", ans10.get(), "a) Around 100")
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

    ans1.set(0)

    ans2.set(0)

    ans3.set(0)

    ans4.set(0)

    ans5.set(0)

    ans6.set(0)

    ans7.set(0)

    ans8.set(0)

    ans9.set(0)

    ans10.set(0)

    global score

    if score > 0:
        score -= score
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
    frame.pack(padx=0, pady=0)
    frame.place(x=65, y=50)


    header = tk.Label(master=quiz, text="Quiz about Mythology", font=("Quiz about Mythology", 20), bg="#90EE90")
    header.pack()
    header.place(x=120, y=5)

    canvas = tk.Canvas(frame,  background="#FFC0CB")
    canvas.pack(side=tk.LEFT, fill='both', expand=True)

    vbar = tk.Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    vbar.pack(side=RIGHT, fill=Y)
    canvas.config(yscrollcommand=vbar.set)

    interior = tk.Frame(canvas, background="#FFC0CB")
    interior.pack(padx=30, pady=50)

    # Add labels and radio buttons
    text1 = tk.Label(master=interior, text="1.Who is the God of the sky and lightning?",bg="#FFC0CB")
    text1.pack()
    tk.Radiobutton(interior, text="a) Apollo", variable=ans1, value="a) Apollo",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) Cronus", variable=ans1, value="b) Cronus",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) Zeus", variable=ans1, value="c) Zeus",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) Tartarus", variable=ans1, value="d) Tartarus",bg="#FFC0CB").pack()

    text2 = tk.Label(master=interior, text="2.Who is the God of the sea?",bg="#FFC0CB")
    text2.pack()
    tk.Radiobutton(interior, text="a) Poseidon", variable=ans2,
                   value="a) Poseidon",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) Artemis", variable=ans2,
                   value="b) Artemis",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) Erebus", variable=ans2,
                   value="c) Erebus",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) Cronus", variable=ans2,
                   value="d) Cronus",bg="#FFC0CB").pack()

    text3 = tk.Label(master=interior, text="3.Who is the God of the underworld?",bg="#FFC0CB")
    text3.pack()
    tk.Radiobutton(interior, text="a) Hades", variable=ans3, value="a) Hades",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) Cronus", variable=ans3, value="b) Cronus",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) Zeus", variable=ans3, value="c) Zeus",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) Titan", variable=ans3, value="d) Titan",bg="#FFC0CB").pack()

    text4 = tk.Label(master=interior, text="4.Which Greek God is the Personification of the Erath",bg="#FFC0CB")
    text4.pack()
    tk.Radiobutton(interior, text="a) Gaia", variable=ans4, value="a) Gaia",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) Apollo", variable=ans4, value="b) Apollo",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) Cronus", variable=ans4, value="c) Cronus",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) Ourea", variable=ans4, value="d) Ourea",bg="#FFC0CB").pack()

    text5 = tk.Label(master=interior, text="5.Who is the Goddess of wisdom?",bg="#FFC0CB")
    text5.pack()
    tk.Radiobutton(interior, text="a) Athena", variable=ans5, value="a) Athena",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b)Aphrodite", variable=ans5, value="b)Aphrodite",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) Metis", variable=ans5, value="c) Metis",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) Dione", variable=ans5, value="d) Dione",bg="#FFC0CB").pack()

    text6 = tk.Label(master=interior, text="6.Who is the God of war?",bg="#FFC0CB")
    text6.pack()
    tk.Radiobutton(interior, text="a) Ares", variable=ans6, value="a) Ares",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) Hades", variable=ans6, value="b) Hades",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) Apollo", variable=ans6, value="c) Apollo",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) Cronus", variable=ans6, value="d) Cronus",bg="#FFC0CB").pack()

    text7 = tk.Label(master=interior, text="7.Who is the God of music and medicine?",bg="#FFC0CB")
    text7.pack()
    tk.Radiobutton(interior, text="a) Apollo", variable=ans7, value="a) Apollo",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) Artemis", variable=ans7, value="b) Artemis",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) Ares", variable=ans7, value="c) Ares",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) Metis", variable=ans7, value="d) Metis",bg="#FFC0CB").pack()

    text8 = tk.Label(master=interior, text="8.Who was the child of Poseidon and Medusa?",bg="#FFC0CB")
    text8.pack()
    tk.Radiobutton(interior, text="a) Perseus", variable=ans8, value="a) Perseus",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) Pegasus", variable=ans8, value="b) Pegasus",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) Andromeda", variable=ans8, value="c) Andromeda",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) Hercules", variable=ans8, value="d) Hercules",bg="#FFC0CB").pack()

    text9 = tk.Label(master=interior, text="9.Poseidon is the god of the sea and?",bg="#FFC0CB")
    text9.pack()
    tk.Radiobutton(interior, text="a) Earthquake", variable=ans9, value="a) Earthquake",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) Rain", variable=ans9, value="b) Rain",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) Sand", variable=ans9, value="c) Sand",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) Fish", variable=ans9, value="d) Fish",bg="#FFC0CB").pack()

    text10 = tk.Label(master=interior, text="10.How many children does Zeus have?",bg="#FFC0CB")
    text10.pack()
    tk.Radiobutton(interior, text="a) Around 100", variable=ans10, value="a) Around 100",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="b) Around 50", variable=ans10, value="b) Around 50",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="c) 10 sons & 8 daughters", variable=ans10, value="c) 10 sons & 8 daughters",bg="#FFC0CB").pack()
    tk.Radiobutton(interior, text="d) Nothing, he just have siblings", variable=ans10, value="d) Nothing, he just have siblings",bg="#FFC0CB").pack()

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
    if selection1 == "c) Zeus":
        score += 1
    if selection2 == "a) Poseidon":
        score += 1
    if selection3 == "a) Hades":
        score += 1
    if selection4 == "a) Gaia":
        score += 1
    if selection5 == "a) Athena":
        score += 1
    if selection6 == "a) Ares":
        score += 1
    if selection7 == "a) Apollo":
        score += 1
    if selection8 == "b) Pegasus":
        score += 1
    if selection9 == "a) Earthquake":
        score += 1
    if selection10 == "a) Around 100":
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

    result = tk.Label(master=interior, text="1.Who is the God of the sky and lightning?", bg="#FFC0CB")
    answer1 = tk.Label(master=interior, text="c) Apollo", fg="#00008b", bg="#FFC0CB")
    result.pack()
    answer1.pack()

    result2 = tk.Label(master=interior, text="2.Who is the God of the sea?", bg="#FFC0CB")
    result2.pack()
    answer2 = tk.Label(master=interior, text="a) Poseidon", fg="#00008b", bg="#FFC0CB")
    answer2.pack()

    result3 = tk.Label(master=interior, text="3.Who is the God of the underworld?",
                       bg="#FFC0CB")
    result3.pack()
    answer3 = tk.Label(master=interior, text="c) Hades", fg="#00008b", bg="#FFC0CB")
    answer3.pack()

    result4 = tk.Label(master=interior, text="4.Which Greek God is the Personification of the Erath", bg="#FFC0CB")
    result4.pack()
    answer4 = tk.Label(master=interior, text="b) Gaia", fg="#00008b", bg="#FFC0CB")
    answer4.pack()

    result5 = tk.Label(master=interior, text="5.Who is the Goddess of wisdom", bg="#FFC0CB")
    result5.pack()
    answer5 = tk.Label(master=interior, text="a) Athena", fg="#00008b", bg="#FFC0CB")
    answer5.pack()

    text6 = tk.Label(master=interior, text="6.Who is the God of war?", bg="#FFC0CB")
    text6.pack()
    answer6 = tk.Label(master=interior, text="b) Ares", fg="#00008b", bg="#FFC0CB")
    answer6.pack()

    text7 = tk.Label(master=interior, text="7.Who is the God of music and medicine?", bg="#FFC0CB")
    text7.pack()
    answer7 = tk.Label(master=interior, text="d) Apollo", fg="#00008b", bg="#FFC0CB")
    answer7.pack()

    text8 = tk.Label(master=interior, text="8.Who was the child of poseidon and Medusa?", bg="#FFC0CB")
    text8.pack()
    answer8 = tk.Label(master=interior, text="b) Pegasus", fg="#00008b", bg="#FFC0CB")
    answer8.pack()

    text9 = tk.Label(master=interior, text="9.Poseidon is the god of the sea and?", bg="#FFC0CB")
    text9.pack()
    answer9 = tk.Label(master=interior, text="c) Earthquake", fg="#00008b", bg="#FFC0CB")
    answer9.pack()

    text10 = tk.Label(master=interior, text="10.How many children does Zeus have?",
                      bg="#FFC0CB")
    text10.pack()
    answer10 = tk.Label(master=interior, text="d) Around 100", fg="#00008b", bg="#FFC0CB")
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