
from interpreter import Interpreter

byte_code_inter = Interpreter()


sample_instructions = {
    "instructions": [
        ("add_to_stack", 0),
        ("add_to_stack", 1),
        ("addition", None),
        ("result", None)
        ],
    "values": [5, 2]
}


byte_code_inter.run(sample_instructions)