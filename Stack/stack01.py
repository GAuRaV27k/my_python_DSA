def push(stack, item):
    stack.append(item)
    print(f"{item} pushed to stack")

def pop(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print(f"{stack.pop()} popped from stack")

if __name__ == "__main__":
    stack = []
    push(stack, 10)
    push(stack, 20)
    pop(stack)
