class Stack:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def list_items(self):
        if self.is_empty():
            return "Stack is empty"
        return "\n".join(self.items)

stack = Stack()

while True:
    print("\nPlease select an option below:")
    print("1: Add an item")
    print("2: Remove the top item")
    print("3: Show the top item")
    print("4: List all items")
    print("5: Exit")
    
    option = input("Enter your option: ")

    if option == '1':
        item = input("Enter the item you want to stack: ")
        stack.add_item(item)
        print(f"The added item in the stack is: {item}")

    elif option == '2':
        removed_item = stack.pop()
        if removed_item is not None:
            print(f"The removed item from the stack is: {removed_item}")
        else:
            print("Stack is empty, nothing to remove.")

    elif option == '3':
        top_item = stack.peek()
        if top_item is not None:
            print(f"The top item in the stack is: {top_item}")
        else:
            print("Stack is empty.")

    elif option == '4':
        print("Items in the stack:")
        print(stack.list_items())

    elif option == '5':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
