import tkinter as tk
window_main = tk.Tk()
window_main.minsize(200, 200) 

check_1 = tk.IntVar()
check_2 = tk.IntVar()
check_3 = tk.IntVar()

def check1Clicked():
    if check_1.get() :
        print('Checkbox 1 selektovan')
    else :
        print('Checkbox 1 odselektovan')
 
def check2Clicked():
    if check_2.get() :
        print('Checkbox 2 selektovan')
    else :
        print('Checkbox 2 odselektovan')
 
def check3Clicked():
    if check_3.get() :
        print('Checkbox 3 selektovan')
    else :
        print('Checkbox 3 odselektovan')
 
check_but_1 = tk.Checkbutton(window_main, text = 'Listening to Music', variable = check_1, onvalue = 1, offvalue = 0, command=check1Clicked)
check_but_1.pack()

check_but_2 = tk.Checkbutton(window_main, text = 'Reading Books', variable = check_2,
                onvalue = 1, offvalue = 0, command=check2Clicked)
check_but_2.pack()
 
check_but_3 = tk.Checkbutton(window_main, text = 'Watching Movies', variable = check_3,
                onvalue = 1, offvalue = 0, command=check3Clicked)
check_but_3.pack()
 
window_main.mainloop()
