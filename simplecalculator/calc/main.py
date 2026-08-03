import tkinter as tk
import math

reset_display=False

def click(event):
      global reset_display

      current=entry.get()
      button_text=event.widget["text"]

      if button_text=='c':
            entry.delete(0,tk.END)
            entry.insert(tk.END,'0')
            reset_display=False
            return
      elif button_text=='=':
          try:
                expression=current.replace('%','/100')
                result=eval(expression)
                entry.delete(0,tk.END)
                entry.insert(tk.END,str(result))
                reset_display=True

          except Exception:
                entry.delete(0,tk.END)
                entry.insert(tk.END,"Error")
                reset_display=True
          return
      else:
          if reset_display:
                entry.delete(0,tk.END)
                current=""
                reset_display=False

          if current=='0':
                current=""

      operators="+-*/%"
      if current and current[-1] in operators and button_text in operators:
            current=current[:-1]

      if current=="" and button_text in "*/%)":
            return

      entry.delete(0,tk.END)
      entry.insert(tk.END, current + button_text)


root=tk.Tk()
root.title("simple calculator")
root.geometry("300x400")
root.resizable(False,False)
root.configure(bg="#404040")

entry=tk.Entry(root,bd=5,font=('arial',20),justify='right',width=16,bg='#90EE90')
entry.pack(pady=5)


btnFrame=tk.Frame(root,bg="#404040")
btnFrame.pack(padx=3,pady=3)

buttons=[['c','(',')','/'], ['7','8','9','*'], ['4','5','6','-'], ['1','2','3','+'], ['.','0','%','=']]

for i in range(len(buttons)):
        for j in range(len(buttons[i])):
              btn=tk.Button(btnFrame,text=buttons[i][j],
                            font=("arial",16),width=3,height=1)
              btn.grid(row=i,column=j,padx=10,pady=10)
              btn.bind('<Button-1>',click)
            

root.mainloop()