'''
Run Javascript inside Python Environment
Author: Ayushi Rawat

Equivalent Python code:

1. example1: a JS command:-

            print('Hello World!')
            
2. example2: a JS function:-

            def add(a, b):
                return a + b
                
'''

import js2py

#example 1
#a JS command
js1 = 'console.log( "Hello World!" )'

res1 = js2py.eval_js(js1)
#print the result
res1

#exapmle 2
#a JS function

#take user input
a = int(input('Enter a num: '))
js2 = '''function add(a, b){
    return a + b;
    }'''
    
res2 = js2py.eval_js(js2)

#print the result
print(res2(a,3))