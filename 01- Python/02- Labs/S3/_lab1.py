from tkinter import *

def Func():
    print("Mohamed Khaled")
window_1 = Tk()
window_1.title("Hello from tkinter ")
#Adding Label 
Label_1 = Label(window_1,text="Mohamed Khaled Elfawakhry")
# Controlling geometry
window_1.geometry('500x500')
# Adding photo to use in button
photo_1 = PhotoImage(file = 'pushbutton.png')
photo_1 = photo_1.subsample(2,2)

# Adding Button
b1 = Button(window_1 , text =" Click Here ",bd = '5',command= Func,background="black",fg='red',font = ('Verdana', 20))
b2 = Button(window_1 , text = "Button 2",bd='5',image=photo_1)
b3 = Button(window_1 , text = "Button 3",bd='6')
b4 = Button(window_1 , text = "Close the window",bd='5', command=window_1.destroy)
Label_1.pack(side = TOP)
#b1.pack(side = TOP )
b1.place(x=50 , y = 360 )
#b2.pack(side = LEFT)
b2.place(relx = 0.5,rely = 1, anchor = CENTER )
b3.pack(side = RIGHT)
b4.pack(side = BOTTOM)
# Call the main loop 
window_1.mainloop()