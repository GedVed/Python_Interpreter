

class Toy_Interpreter:
    def __init__(self):
        self.stack = []
        self.environment = {} #holds env variables

    def add_to_stack(self, value):
        self.stack.append(value) 

    def remove_from_stack(self):
        #somewhat redudant since pop already returns value, but since add_to_stack is there it stands to reason that remove should be there too
        return self.stack.pop() 

    def save_env_variable(self, variable_name):
        variable_value = self.stack.pop()
        self.environment[variable_name] = variable_value

    def load_env_variable(self, variable_name):
        variable_value = self.environment[variable_name]
        self.add_to_stack(variable_value)

    def parser(self, instruction, argument, execute):
        #translation of arguments to instructions
        variable_values = ["add_to_stack"]
        variable_names = ["save_env_variable", "load_env_variable"]

        if instruction in variable_values:
            argument = execute["variable_values"][argument]
        elif instruction in variable_names:
            argument = execute["variable_names"][argument]
    

        return argument

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
        for execution_step in instructions:
            instruction, argument = execution_step
            argument = self.parser(instruction, argument, execute)
            """
            if instruction == "add_to_stack":
                self.add_to_stack(argument)
            elif instruction == "addition":
                self.addition()
            elif instruction == "result":
                self.result()
            elif instruction == "save_env_variable":
                self.save_env_variable(argument)
            elif instruction == "load_env_variable":
                self.load_env_variable(argument)
            """
            execution_method = getattr(self, instruction) #dynamic method lookup to avoid elif bloat
            
            if (execution_method is None):
                execution_method()
            else:
                execution_method(argument)
            


    
