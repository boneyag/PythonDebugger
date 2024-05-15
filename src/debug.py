# This code is originally from https://maurcz.github.io/posts/002-customizing-the-python-debugger/
# All source code related to the post is available at https://github.com/maurcz/posts/tree/main/python-customizing-pdb


import inspect
import pdb
import sys

class Debug(pdb.Pdb):
    def __init__(self, *args, **kwargs):
        super(Debug, self).__init__(*args, **kwargs)
        self.prompt = "[extended-pdb]"

    def do_args_type(self, arg: str):
        """arg_type | at
        Print the argument type list passed to the current frame.
        """
        co = self.curframe.f_code
        dict = self.curframe_locals
        n = co.co_argcount + co.co_kwonlyargcount
        if co.co_flags & inspect.CO_VARARGS:
            n = n + 1
        if co.co_flags & inspect.CO_VARKEYWORDS:
            n = n + 1

        for i in range(n):
            name = co.co_varnames[i]
            if name in dict:
                self.message('%s = %s' % (name, type(dict[name])))
            else:
                self.message('%s == *** undefined ***' % (name,))  

    do_at = do_args_type 

    def do_eval(self, arg: str):
        """eval <expression>
        Evaluate the expression in the current debugging context.
        """
        try:
            result = eval(arg, self.curframe.f_globals, self.curframe.f_locals)
            self.message(f"{arg} = {result}")
        except Exception as e:
            self.message(f"Error evaluating expression: {e}")

    def do_exec(self, arg: str):
        """exec <statement>
        Execute the statement in the current debugging context.
        """
        try:
            exec(arg, self.curframe.f_globals, self.curframe.f_locals)
            self.message(f"Executed: {arg}")
        except Exception as e:
            self.message(f"Error executing statement: {e}")
            
def stop():
    debugger = Debug()
    debugger.set_trace(sys._getframe().f_back)

sys.breakpointhook = stop