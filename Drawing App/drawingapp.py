'''
Provides a simple drawing app
Hold down the left button to draw
Provides some single key commands:
R-red O-Orange Y-yellow G-green B-blue I-indigo V-violet P-pink
C-clear
'''

from tkinter import *

class Drawing(object):

    def display(self):
        root = Tk()

        canvas = Canvas(root, width=1430, height=860)
        canvas.grid(row=0, column=0)

        draw_color = 'red'

        def mouse_move(event):
            '''
            Draws a 10 pixel rectangle centered about the mouse
            position
            '''
            canvas.create_rectangle(event.x-5, event.y-5,
            event.x+5, event.y+5, fill=draw_color, outline=draw_color)

        canvas.bind('<B1-Motion>', mouse_move)

        def key_press(event):
            nonlocal draw_color
            ch = event.char.upper()
            if ch == 'C':
                canvas.delete("all")
            elif ch == 'R':
                draw_color = 'red'
            elif ch == 'O':
                draw_color = 'orange'
            elif ch == 'Y':
                draw_color = 'yellow'
            elif ch == 'G':
                draw_color = 'green'
            elif ch == 'B':
                draw_color = 'blue'
            elif ch == 'I':
                draw_color = 'indigo'    
            elif ch == "V":
                draw_color = 'violet'
            elif ch == 'P':
                draw_color = 'pink'
            elif ch == 'W':
                draw_color = 'white'
            elif ch == 'T':
                draw_color = 'teal'
            elif ch == 'A':
                draw_color = 'aquamarine'
            elif ch == 'H':
                draw_color = 'hazel'
            elif ch == 'W':
                draw_color = 'white'
            elif ch == 'L':
                draw_color = 'lime green'
            elif ch == 'M':
                draw_color = 'magenta'
            elif ch == 'D':
                draw_color = "#6F4E37"
            
            


        
            

        canvas.bind('<KeyPress>', key_press)
        canvas.focus_set()

        root.mainloop()





if __name__ == '__main__':
    app = Drawing()
    app.display()     
