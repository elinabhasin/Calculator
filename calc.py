from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('328x400')

# Display
display = Label(root, text=0, bg="white", width=360, height=8, relief='solid', borderwidth=2, anchor="nw", padx=6, pady=6)
display.grid(row=0, column=0, columnspan=4, padx=3, pady=3)

# Buttons
buttons = [
    ["CLR", "BACK", "%", "/"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["TRIG", "0", ".", "="]
]

for r, row in enumerate(buttons): #buttons is also a list of lists.
    for c, text in enumerate(row): #row here is a list= ["CLR", "BACK", "%", "/"]
        button = Button(root, text=text, bg="orchid3", relief='solid', borderwidth=2, width=6, height=2,command=lambda text=text:show(text))
        button.grid(row=r+1, column=c, padx=3, pady=3, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

data=[]

def inToPost(data):
    
    ex=[]
    op=[]

    for i in data:
        if(i!='+' and i!='-' and i!='/' and i!='x' and i!='%'):
            ex.append(i)

        else:
            if(len(op)!=0):
                if(op[-1]=='/' or op[-1]=='%' or op[-1]=='/') and (i=='+' or i=='-'):
                    a=op.pop()
                    ex.append(a)
                    op.append(i)
                elif (op[-1]=='/' or op[-1]=='%' or op[-1]=='x') and (i=='/' or i=='x' or i=='%'):
                    a=op.pop()
                    ex.append(a)
                    op.append(i)
                elif (op[-1]=='+' or op[-1]=='-') and (i=='+' or i=='-'):
                    a=op.pop()
                    ex.append(a)
                    op.append(i)
                else:
                    op.append(i)
            else:
                op.append(i)
    while(len(op)>0):
        a=op.pop()
        ex.append(a)
    print("Ex:")
    print(ex)

    op=[]

    for i in ex:
        if i!='+' and i!='-' and i!='/' and i!='%' and i!='x':
                # ex.remove(i)
            op.append(i)
        else:

            if(i=='+'):
                op[-2]=float(op[-2])+float(op[-1])
                op.pop()
            elif i=='x':
                op[-2]=float(op[-2])*float(op[-1])
                op.pop()
            elif i=='/':
                op[-2]=float(op[-2])/float(op[-1])
                op.pop()
            elif i=='-':
                op[-2]=float(op[-2])-float(op[-1])
                op.pop()
            elif i=='%':
                op[-2]=float(op[-2])%float(op[-1])
                op.pop()
            else:
                op.append(i)
    ans=op.pop()
    return ans

def show(text):

    if text=="CLR":
        display.config(text=0)
        data.clear()

    elif text=="BACK":

        if(len(data)==1 and data[0]==0):
            display.config(text=0)

        else:
            data.pop()
            displayStr=''.join(data)
            display.config(text=displayStr)

    if text>='0' and text<='9':
        if(len(data)==1):
            if data[0][-1]=='.':
                data[0]=data[0]+text
                displayStr=''.join(data)
                display.config(text=displayStr)

            else:
                data.append(text)
                displayStr=''.join(data)
                display.config(text=displayStr)

        elif(len(data)>1):
            if(data[-1][-1])=='.':
                data[-1]=data[-1]+text
                displayStr=''.join(data)
                display.config(text=displayStr)
            else:
                data.append(text)
                displayStr=''.join(data)
                display.config(text=displayStr)
        else:
            data.append(text)
            displayStr=''.join(data)
            display.config(text=displayStr)

    if len(data)==1 and (text=='+' or text=='-' or text=='x' or text=='/' or text=='%'):
        if((data[0]))[-1]=='.':
            data[0]=data[0]+'0'
            data.append(" ")
            data.append(text)
            data.append(" ")
            displayStr=''.join(data)
            display.config(text=displayStr)

        else:
            data.append(" ")
            data.append(text)
            data.append(" ")
            displayStr=''.join(data)
            display.config(text=displayStr)

    if len(data)>1 and (text=='+' or text=='-' or text=='x' or text=='/' or text=='%'):
        if(data[-1])[-1]=='.':
            data[-1]=data[-1]+'0'
            data.append(" ")
            data.append(text)
            data.append(" ")
            displayStr=''.join(data)
            display.config(text=displayStr)

        elif(data[-2]=='+' or data[-2]=='/' or data[-2]=='x' or data[-2]=='-'):
            data[-2]=text
            displayStr=''.join(data)
            display.config(text=displayStr)

        else:
            data.append(" ")
            data.append(text)
            data.append(" ")
            displayStr=''.join(data)
            display.config(text=displayStr)

    elif len(data)==0 and (text=='+' or text=='-' or text=='x' or text=='/' or text=='%'):
        data.append("0")
        data.append(" ")
        data.append(text)
        data.append(" ")
        displayStr=''.join(data)
        display.config(text=displayStr)

    elif len(data)==0 and text=='.':
        data.append("0.")
        displayStr=''.join(data)
        display.config(text=displayStr)
    
    elif len(data)==1 and text=='.':
         if '.' in data[0]:
             pass
         
         elif '.' not in data[0]:
             a=data[0]
             data[0]=a+'.'
             displayStr=''.join(data)
             display.config(text=displayStr)

    elif len(data)>1 and text=='.':
        if(data[-1]==' '):
            data.append('0.')
            displayStr=''.join(data)
            display.config(text=displayStr)

        else:
            data[-1]=data[-1]+'.'
            displayStr=''.join(data)
            display.config(text=displayStr)
    
    if(text=='='):
        temp=''
        data1=[]
        for i in data:
            if i!=' ' and (i!='+' or i!='-' or i!='/' or i!='x' or i!='%'):
                temp=temp+i
            elif i==' ' and data[data.index(i)+1]=='+' or data[data.index(i)+1]=='-' or data[data.index(i)+1]=='/' or data[data.index(i)+1]=='%' or data[data.index(i)+1]=='x':
                data1.append(temp)
                temp=''
            elif i==' ' and data[data.index(i)+1]!='+' or data[data.index(i)+1]!='-' or data[data.index(i)+1]!='/' or data[data.index(i)+1]!='%' or data[data.index(i)+1]!='x':
                pass
            elif i=='+' or i=='-' or i=='/' or i=='%' or i=='x':
                data1.append(i)
        data1.append(temp)
        print(data1)
        ans=inToPost(data1)
        display.config(text=ans)
        return

root.mainloop()
