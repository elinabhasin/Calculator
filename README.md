# Calculator
This is a replica of a simple calculator with six operations: a) ADDITION (+)
b) SUBTRACTION (-)
c) MULTIPLICATION (x)
d) DIVISION (/)
e) EXPONENT (^)
f) MODULUS (%)

The project is made using tkinker.Tkinter is a standard Python GUI (Graphic User Interface) library that provides a set of tools and widgets to create desktop applications with graphical interfaces. The name Tkinter comes from the Tk Interface.

I started off by creating a basic display for the calculator and arranging all the buttons referencing actual calculators and tried to make it really symmetric. Using the row and the column configure helped in proportional magnification of icons once increase the dimensions of the calculator.

The code has 3 major functions: a) show
b) inToPost
c) Display


a) show():
This is the first function call to happen once you click any button on the calculator. It takes the text of the button pressed as the parameters. The first thing this function does is set the text shown in the display to 0...making it the default text visible on the calculator display as soon as you open it.

As soon as a digit or a decimal is entered...it gets appended to a list called "data" and if any operator (excluding '=') is entered.. it is appended to data with two spaces...one succeeding and the other preceeding it for better readability. The data is then joined together as a single string and is displayed on the screen in realtime by using display.config().

Now, the assignment operator "=". A very crucial operator. Whenever entered, the user expects the outcome of the expression to be displayed on the screen which brings us to the second function:

b) Display():
This function is used to retrieve the final answer and return it to show() after all the calculations are done.The function that actually performs the entire calculative part is the inToPost()

c) inToPost(): This now has the actual conversion of our infix expression into a postfix expression. The Data list is an infix expression and a parameter for it. This appends the operands into the ex stack and as soon as an operator pops up...it puts it in the op stack or the ex stack after checking for its associativty and precedence.
It returns the final output.

This was definitely a very fun project to work on. I really enjoyed figuring out the infix to postfix part of different operators. I did struggle though..at the % part. As it turns out, it doesn't always divide the number by 100...it depends on the operator preceeding that number.
