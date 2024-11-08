
class Frame(object):
    def __init__(self, code_object, local_variables, global_variables, previous_frame):
        self.code_object = code_object
        self.local_var = local_variables
        self.global_var = global_variables
        self.prev_frame = previous_frame
    

class Function(object):
    def __init__(self) -> None:
        pass


class Data_stack(object):
    def __init__(self):
        self.data = []
    
    
class Block_stack:
    def __init__(self) -> None:
        pass