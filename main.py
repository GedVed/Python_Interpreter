
from interpreter import Toy_Interpreter

byte_code_inter = Toy_Interpreter()


sample_instructions = {
    "instructions": [
        ("add_to_stack", 0),
        ("save_env_variable",0),
        ("add_to_stack", 1),
        ("save_env_variable",1),
        ("load_env_variable", 0),
        ("load_env_variable", 1),
        ("addition", None),
        ("result", None)],
    "variable_values": [5, 2],
    "variable_names": ["first_value", "second_value"]
}

"""
Instructions above translate to:

first_value = 5
second_value = 2
print(first_value+second+value)

"""



byte_code_inter.run(sample_instructions)