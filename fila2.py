stack = []
pos = 0

def push(item, stack, size):
    global pos
    if pos < size:
        stack.append(item)
        pos += 1
        return "Item pushed successfully"
    else:
        return "Pila llena..."

def show(stack):
    my_stack = ""
    my_stack += "┌" + "-"*8 + "┐\n"
    my_stack += "| PILA   |\n"
    for item in reversed(stack):
        my_stack += f"|" + "-"*8 + "|\n"
        my_stack += f"| {item:>6} |\n"
    my_stack += "└" + "-"*8 + "┘"
    return my_stack

def peek(stack):
    if isEmpty(stack):
        return "La pila esta vacía..."
    return stack[-1]

def isEmpty(stack):
    return not stack



print(peek(stack)) 

size = int(input("Dime el tamaño de la pila: "))

while True:
    item = input("Dime un valor: ")
    print(push(item, stack, size))
    
    answer = input("Desea agregar otro valor? (s/n): ")
    if answer.lower() == 'n':
        break

print("\n" + show(stack))
print("Cima actual (peek):", peek(stack))