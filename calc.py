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
    ["^", "0", ".", "="]
]

# Place buttons using grid
for r, row in enumerate(buttons): #buttons is also a list of 
    for c, text in enumerate(row): #row here is a list= ["CLR", "BACK", "%", "/"]
        button = Button(root, text=text, bg="powder blue", relief='solid', borderwidth=2, width=6, height=2,command=lambda text=text:show(text))
        button.grid(row=r+1, column=c, padx=3, pady=3, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

data=[]
displayStr=''
def inToPost(data):
    ex=[]
    op=[]
    for i in data:
        if i!='+' and i!='-' and i!='/' and i!='x' and i!='^':
            ex.append(i)
        elif i==' ':
            pass
        else:
            while(True):
                if(len(op)!=0):
               
                    if(op[-1]=='/' or op[-1]=='x') and (i=='+' or i=='-'):
                        a=op.pop()
                        ex.append(a)
                    elif (op[-1]=='/' or op[-1]=='x') and (i=='/' or i=='x'):
                        a=op.pop()
                        ex.append(a)
                    elif (op[-1]=='+' or op[-1]=='-') and (i=='+' or i=='-'):
                        a=op.pop()
                        ex.append(a)
                    elif (op[-1]=='^') and (i=='/' or i=='-' or i=='+' or i=='x'):
                        a=op.pop()
                        ex.append(a)
                    else:
                        op.append(i)
                        break
                else:
                    op.append(i)
                    break
    while(len(op)>0):
        a=op.pop()
        ex.append(a)
    print(ex)
    op=[]
    for i in ex:
        if i!='+' and i!='-' and i!='x' and i!='/' and i!='^':
            op.append(i)
        else:

            if(i=='+'):
                op[-2]=float(op[-2])+float(op[-1])
                op.pop()
            elif i=='x':
                op[-2]=float(op[-2])*float(op[-1])
                op.pop()
            elif i=='/':
                if float(op[-1])==0:
                    return "Error! Can't Divide By 0."
                op[-2]=float(op[-2])/float(op[-1])
                op.pop()
            elif i=='-':
                op[-2]=float(op[-2])-float(op[-1])
                op.pop()
            elif i=='^':
                op[-2]=(float(op[-2]))**(float(op[-1]))
                op.pop()
            else:
                op.append(i)
    ans=op.pop()
    return ans

def Display(data):
    ans=inToPost(data)
    return ans
def show(text):
    if text=='%':
        if len(data)==0:
            display.config(text=0)
        if len(data)==1:
            data[0]=str(float(data[0])/100)
            displayStr=''.join(data)
            display.config(text=displayStr)
        else:
            if(data[-1]==' '):
                pass
            elif data[-1]=='.':
                data.append('0')
            temp=''
            t=''
            index=0
            for i in range(len(data)-1,-1,-1):
                if data[i]==' ':
                    index=i
                    break
                temp=temp+data[i]
                temp=temp[::-1]
            if data[index-1]=='x' or data[index-1]=='/':
                data[index+1]=str(float(temp)/100)
                del data[index+2:]
                displayStr=''.join(data)
                display.config(text=displayStr)
            elif data[index-1]=='+' or data[index-1]=='-':
                Data=[]
                num=''
                for i in data[:index-2]:
                    if i=='x' or i=='/' or i=='-' or i=='+':
                        Data.append(num)
                        Data.append(i)
                        num=''
                    else:
                        num=num+i
                Data.append(num)
                t=inToPost(Data)
                t=str(((float(t))*float(temp))/100)
                data[index+1]=t
                del data[index+2:]
                displayStr=''.join(data)
                display.config(text=displayStr)
            temp=''
            if ' ' not in data:
                for i in data:
                    temp=temp+i
                temp=str(float(temp)/100)
                data[0]=temp
                del data[1:]
                displayStr=''.join(data)
                display.config(text=displayStr)
        if(len(data)==0):
            data.append('0')
            data.append('.')
            displayStr=''.join(data)
            display.config(text=displayStr)
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
    if (text>='0' and text<='9') or text=='.':
        data.append(text)
        displayStr=''.join(data)
        display.config(text=displayStr)
    if len(data)>=2 and (text=='+' or text=='-' or text=='x' or text=='/' or text=='^'):
        if(data[-2]=='+' or data[-2]=='/' or data[-2]=='x' or data[-2]=='-' or data[-2]=='^'):
            data.pop()
            data.pop()
            data.append(text)
            data.append(' ')
            displayStr=''.join(data)
            display.config(text=displayStr)
        else:
            data.append(' ')
            data.append(text)
            data.append(' ')
            displayStr=''.join(data)
            display.config(text=displayStr)
            # data[-2]=text
    if len(data)<2 and (text=='+' or text=='-' or text=='x' or text=='/' or text=='^'):
        data.append(" ")
        data.append(text)
        data.append(" ")
        displayStr=''.join(data)
        display.config(text=displayStr)
    elif len(data)==0 and (text=='+' or text=='-' or text=='x' or text=='/' or text=='^'):
        data.append("0")
        data.append(" ")
        data.append(text)
        data.append(" ")
        displayStr=''.join(data)
        display.config(text=displayStr)
    if(text=='='):
        print(data)
        Data=[]
        num=''
        for i in data:
            if i=='x' or i=='/' or i=='-' or i=='+' or i=='^':
                Data.append(num)
                Data.append(i)
                num=''
            else:
                num=num+i
        Data.append(num)
        print(Data)
        ans=Display(Data)
        display.config(text=ans)
        return Data

root.mainloop()
