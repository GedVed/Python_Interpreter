

class Interpreter:
    def __init__(self):
        self.stack = []

    def add_to_stack(self, value):
        self.stack.append(value)

    def remove_from_stack(self):
        self.stack.pop()

    def addition(self):
        first_value = self.stack.pop()
        second_value = self.stack.pop()
        result = first_value + second_value
        self.stack.append(result)

    def result(self):
        result = self.stack.pop()
        print(result)
    
    def run(self, execute):
        instructions = execute["instructions"]
        values = execute["values"]
        for step in instructions:
            instruction, value = step
            if instruction == "add_to_stack":
                value = values[value]
                self.add_to_stack(value)
            elif instruction == "remove_from_stack":
                self.remove_from_stack()
            elif instruction == "addition":
                self.addition()
            elif instruction == "result":
                self.result()


    
