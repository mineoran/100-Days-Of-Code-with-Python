In this project; We will learn what local and global scop means


Local (or function) Scope:

Local scope is the code block or body of any Python function or lambda expression. This Python scope contains the names that you define inside the function. These names will only be visible from the code of the function. It’s created at function call, not at function definition, so you’ll have as many different local scopes as function calls. In short, variables defined in a function are called local variables. What we mean by local variables is that the variables are specific to the function.

Global Scope:
They are variables declared outside of a function or in a global scope in Python, so we can access global variables inside and outside the function.

**EXAMPLE(local scope)

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

**EXAMPLE(glocal scope)
-Global scope, ıt's available anywhere within our file because it was defined at the top level of the file-

x = 300

def myfunc():
  print(x)

myfunc()

print(x)
