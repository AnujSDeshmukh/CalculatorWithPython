import customtkinter as ctk
import math

#window 
window = ctk.CTk()
window.title("Calculator")
window.geometry("400x600")
window.resizable(False,False)
window.iconbitmap("calculator.ico")

error = False
equals = 0
plus = True

#methods
def show(text):
    global error
    if error:
       error = False
       textbox_operation.delete(0, ctk.END)
    i = ctk.END
    textbox_operation.insert(i, text)

def valuate():
   global error
   try:
    textbox_formula.insert(ctk.END, textbox_operation.get()+" = ")
    ans = eval(textbox_operation.get())
    textbox_operation.delete(0, ctk.END)
    textbox_operation.insert(ctk.END, ans)
   except:
      error = True
      textbox_operation.delete(0, ctk.END)
      textbox_operation.insert(ctk.END, "Error")
      textbox_formula.delete(0, ctk.END)

def clear():
   textbox_operation.delete(0, ctk.END)
   textbox_formula.delete(0, ctk.END)

def enter(event):
   if event.keysym == "Return" or event.keysym == "Enter":
      valuate()


#grid layout
window.rowconfigure((0,1,2,3,4,5), weight = 1, uniform = "a")
window.columnconfigure((0,1,2,3), weight = 1, uniform = "a")

#text frame
text_frame = ctk.CTkFrame(window)
text_frame.grid(row = 0, column = 0, sticky = "we", columnspan = 4)

formula = ctk.StringVar()

textbox_formula = ctk.CTkEntry(text_frame, corner_radius = 0, border_width = 0,
                               font = ("Helvetica", 20, "bold"),
                               justify = "right",
                               fg_color = "gray14")
textbox_formula.place(relx = 0, rely = 0, anchor = "nw", relwidth = 1, relheight = 0.5)

textbox_formula.bind("<Motion>", lambda event: textbox_formula.configure(state = "disabled"))
textbox_formula.bind("<Leave>", lambda event: textbox_formula.configure(state = "normal"))


textbox_operation = ctk.CTkEntry(text_frame, corner_radius = 0, border_width = 0,
                                 font = ("Helvetica", 25, "bold"),
                                 justify = "right",
                                 textvariable = formula,
                                 fg_color = "gray14")
textbox_operation.place(relx = 0, rely = 0.45, anchor = "nw", relwidth = 1, relheight = 0.6)

#check if enter is pressed
window.bind("<KeyPress>", lambda event: enter(event))



#button layout
num9 = ctk.CTkButton(window, text = "9", font = ("Helvetica", 20, "bold"),
corner_radius = 0, command = lambda:show("9"))
num9.grid(row = 2, column = 0, sticky = "news", padx = 2, pady = 3)

num8 = ctk.CTkButton(window, text = "8", font = ("Helvetica", 20, "bold"),
corner_radius = 0, command = lambda:show("8"))
num8.grid(row = 2, column = 1, sticky = "news", padx = 2, pady = 3)

num7 = ctk.CTkButton(window, text = "7", font = ("Helvetica", 20, "bold"),
corner_radius = 0, command = lambda:show("7"))
num7.grid(row = 2, column = 2, sticky = "news", padx = 2, pady = 3)

num6 = ctk.CTkButton(window, text = "6", font = ("Helvetica", 20, "bold"),
corner_radius = 0, command = lambda:show("6"))
num6.grid(row = 3, column = 0, sticky = "news", padx = 2, pady = 3)

num5 = ctk.CTkButton(window, text = "5", font = ("Helvetica", 20, "bold"),
corner_radius = 0, command = lambda:show("5"))
num5.grid(row = 3, column = 1, sticky = "news", padx = 2, pady = 3)

num4 = ctk.CTkButton(window, text = "4", font = ("Helvetica", 20, "bold"),
corner_radius = 0, command = lambda:show("4"))
num4.grid(row = 3, column = 2, sticky = "news", padx = 2, pady = 3)

num3 = ctk.CTkButton(window, text = "3", font = ("Helvetica", 20, "bold"),
corner_radius = 0, command = lambda:show("3"))
num3.grid(row = 4, column = 0, sticky = "news", padx = 2, pady = 3)

num2 = ctk.CTkButton(window, text = "2", font = ("Helvetica", 20, "bold"),
corner_radius = 0, command = lambda:show("2"))
num2.grid(row = 4, column = 1, sticky = "news", padx = 2, pady = 3)

num1 = ctk.CTkButton(window, text = "1", font = ("Helvetica", 20, "bold"),
corner_radius = 0, command = lambda:show("1"))
num1.grid(row = 4, column = 2, sticky = "news", padx = 2, pady = 3)

num0 = ctk.CTkButton(window, text = "0", font = ("Helvetica", 20, "bold"),
corner_radius = 0, command = lambda:show("0"))
num0.grid(row = 5, column = 0, columnspan = 2, sticky = "news", padx = 2, pady = 3)

#arthemetic buttons
plus = ctk.CTkButton(window, text = "+", font = ("Helvetica", 20, "bold"),
                     corner_radius = 0, command = lambda: show(" + "),
                     fg_color = "#F5761A", hover_color = "#FFA52C")
plus.grid(row = 1, column = 3,rowspan = 2, sticky = "news", padx = 2, pady = 3)

minus = ctk.CTkButton(window, text = "-", font = ("Helvetica", 20, "bold"),
                     corner_radius = 0, command = lambda: show(" - "),
                     fg_color = "#F5761A", hover_color = "#FFA52C")
minus.grid(row = 3, column = 3, sticky = "news", padx = 2, pady = 3)

multiply = ctk.CTkButton(window, text = "X", font = ("Helvetica", 20, "bold"),
                     corner_radius = 0, command = lambda: show(" * "),
                     fg_color = "#F5761A", hover_color = "#FFA52C")
multiply.grid(row = 4, column = 3, sticky = "news", padx = 2, pady = 3)

divide = ctk.CTkButton(window, text = "÷", font = ("Helvetica", 20, "bold"),
                     corner_radius = 0, command = lambda: show(" / "),
                     fg_color = "#F5761A", hover_color = "#FFA52C")
divide.grid(row = 5, column = 3, sticky = "news", padx = 2, pady = 3)

equal = ctk.CTkButton(window, text = "=", font = ("Helvetica", 20, "bold"),
                     corner_radius = 0, command = valuate,
                      fg_color = "#F5761A", hover_color = "#FFA52C")
equal.grid(row = 5, column = 2, sticky = "news", padx = 2, pady = 3)

#additional buttons
ac = ctk.CTkButton(window, text = "AC", font = ("Helvetica", 20, "bold"),
                     corner_radius = 0, command = clear,
                     fg_color = "#F5761A", hover_color = "#FFA52C")
ac.grid(row = 1, column = 0, sticky = "news", padx = 2, pady = 3)

point = ctk.CTkButton(window, text = ".", font = ("Helvetica", 20, "bold"),
                     corner_radius = 0, command = lambda: show("."),
                     fg_color = "#F5761A", hover_color = "#FFA52C")
point.grid(row = 1, column = 1, sticky = "news", padx = 2, pady = 3)

percentage = ctk.CTkButton(window, text = "%", font = ("Helvetica", 20, "bold"),
                     corner_radius = 0, command = lambda: show("/100 "),
                     fg_color = "#F5761A", hover_color = "#FFA52C")
percentage.grid(row = 1, column = 2, sticky = "news", padx = 2, pady = 3)

#mainloop
window.mainloop()