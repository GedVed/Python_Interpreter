
class Interpreter(object):
    def __init__(self):
        self.frames = [] #stack of frames
        self.current_frame = None
        self.return_value = None
        self.exception = None


class InterpreterErr(Exception):
    pass

