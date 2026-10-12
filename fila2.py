stack = []

pos = 0
size = 0

def push(item, stack, size):
    global pos
    if pos < size:
        stack.append(item)
        pos+=1
    else:
        return "Stack is full"
    
def show(stack):
        return stack

size = int(input("Enter the size of the stack: "))

while True:
    item = input("Dime un valor: ")
    push(item, stack, size)
    answer = input("Desea agregar otro valor? (s/n): ")
    if answer.lower() == 'n':
        break
 
    print("Stack contents:", stack)