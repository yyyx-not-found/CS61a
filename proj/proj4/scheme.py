"""A Scheme interpreter and its read-eval-print loop."""
from __future__ import print_function
from cgi import test  # Python 2 compatibility

import sys
import os

from scheme_builtins import *
from scheme_reader import *
from ucb import main, trace


##############
# Eval/Apply #
##############

def scheme_eval(expr, env, _=None): # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in environment ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    def helper(expr):
        if isinstance(expr, Pair):
            operator = scheme_eval(expr.first, env)
            validate_procedure(operator)

            return scheme_apply(operator, expr.rest, env)
        elif expr is None:
            return None
        else:
            return env.get_value(expr)

    return helper(expr)


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    environment ENV."""
    return procedure.apply(args, env)



################
# Environments #
################

class Frame(object):
    """An environment frame binds Scheme symbols to Scheme values."""

    def __init__(self, parent):
        """An empty frame with parent frame PARENT (which may be None)."""
        "Your Code Here"
        self.environment = {}
        self.parent = parent

        # add special forms
        self.define('define', Define())
        self.define('quote', Quote())
        self.define('quasiquote', Quasiquote())
        self.define('unquote', Unquote())
        self.define('begin', Begin())
        self.define('lambda', Lambda())
        self.define('if', If())
        self.define('cond', Cond())
        self.define('and', And())
        self.define('or', Or())
        self.define('let', Let())
        self.define('mu', Mu())

    def __repr__(self):
        if self.parent is None:
            return '<Global Frame>'
        s = sorted(['{0}: {1}'.format(k, v) for k, v in self.bindings.items()])
        return '<{{{0}}} -> {1}>'.format(', '.join(s), repr(self.parent))

    def define(self, symbol, value):
        """Define Scheme SYMBOL to have VALUE."""
        self.environment.update({symbol: value})
        return symbol

    # BEGIN PROBLEM 2/3
    "*** YOUR CODE HERE ***"
    def get_value(self, symbol):
        if symbol in self.environment:
            return self.environment[symbol]
        else:
            if isinstance(symbol, numbers.Number) or symbol is nil:
                return symbol
            elif self.parent is not None:
                # find in parent frame
                return self.parent.get_value(symbol)
            else:
                raise SchemeError(f'unknown identifier: {symbol}')
    # END PROBLEM 2/3

##############
# Procedures #
##############

class Procedure(object):
    """The supertype of all Scheme procedures."""

def scheme_procedurep(x):
    return isinstance(x, Procedure)

class BuiltinProcedure(Procedure):
    """A Scheme procedure defined as a Python function."""

    def __init__(self, fn, use_env=False, name='builtin'):
        self.name = name
        self.fn = fn
        self.use_env = use_env

    def __str__(self):
        return '#[{0}]'.format(self.name)

    def apply(self, args, env):
        """Apply SELF to ARGS in ENV, where ARGS is a Scheme list.

        >>> env = create_global_frame()
        >>> plus = env.bindings['+']
        >>> twos = Pair(2, Pair(2, nil))
        >>> plus.apply(twos, env)
        4
        """
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        def eval_args(args):
            if args is nil:
                return []
            else:
                return [scheme_eval(args.first, env)] + eval_args(args.rest)

        try:
            if self.use_env:
                return self.fn(*eval_args(args), env=env)
            else:
                return self.fn(*eval_args(args)) 
        except TypeError:
            raise SchemeError(f'incorrect number of arguments: {str(self)}') 
        # END PROBLEM 2


class LambdaProcedure(Procedure):
    """A procedure defined by a lambda expression or a define form."""

    def __init__(self, formals, body, env):
        """A procedure with formal parameter list FORMALS (a Scheme list),
        whose body is the Scheme list BODY, and whose parent environment
        starts with Frame ENV."""
        self.formals = formals
        self.body = body
        self.env = env

        # count the number of formals
        tmp = self.formals
        count = 0
        while tmp is not nil:
            count += 1
            tmp = tmp.rest
        self.formals_num = count

    def __str__(self):
        return str(Pair('lambda', Pair(self.formals, self.body)))

    def __repr__(self):
        return 'LambdaProcedure({0}, {1}, {2})'.format(
            repr(self.formals), repr(self.body), repr(self.env))

    def apply(self, args, env):
        def binding(formals, args, binded):
            if formals is nil:
                for symbol, value in binded:
                    self.env.define(symbol, value)
                return

            binding(formals.rest, args.rest, binded + [(formals.first, scheme_eval(args.first, env))])

        validate_form(args, self.formals_num, self.formals_num)
        binding(self.formals, args, [])

        # evaluate
        procedure = self.body
        while procedure.rest is not nil:
            scheme_eval(procedure.first, self.env)
            procedure = procedure.rest

        return scheme_eval(procedure.first, self.env)


def add_builtins(frame, funcs_and_names):
    """Enter bindings in FUNCS_AND_NAMES into FRAME, an environment frame,
    as built-in procedures. Each item in FUNCS_AND_NAMES has the form
    (NAME, PYTHON-FUNCTION, INTERNAL-NAME)."""
    for name, fn, proc_name in funcs_and_names:
        frame.define(name, BuiltinProcedure(fn, name=proc_name))

#################
# Special Forms #
#################

"""
How you implement special forms is up to you. We recommend you encapsulate the
logic for each special form separately somehow, which you can do here.
"""
class Define(Procedure):
    def apply(self, args, env):
        if isinstance(args.first, Pair):
            # define procedure
            name = args.first.first
            if not scheme_symbolp(name):
                raise SchemeError('non-symbol: {0}'.format(name))

            formals = args.first.rest
            body = args.rest
            lambda_func = Lambda().apply(Pair(formals, body), env)

            # binding
            env.define(name, lambda_func)
            return name
        else:    
            validate_form(args, 2, 2)
            symbol = args.first
            if not scheme_symbolp(symbol):
                raise SchemeError('non-symbol: {0}'.format(symbol))

            value = scheme_eval(args.rest.first, env)

            return env.define(symbol, value)

class Quote(Procedure):
    def apply(self, args, env):
        return args.first

class Quasiquote(Procedure):
    def apply(self, args, env):
        def eval_args(args):
            if args is nil:
                return nil
            elif isinstance(args, Pair):
                if args.first == 'unquote':
                    return Unquote(True).apply(args.rest, env)
                else:
                    return args.map(eval_args)
            else:
                return args
        
        return eval_args(args.first)

class Unquote(Procedure):
    def __init__(self, enclosed=False):
        self.__enclosed = enclosed

    def apply(self, args, env):
        if self.__enclosed:
            return scheme_eval(args.first, env)
        else:
            raise SchemeError('unquote outside of quasiquote')

class Begin(Procedure):
    def apply(self, args, env):
        validate_form(args, 1)
        while args.rest is not nil:
            scheme_eval(args.first, env)
            args = args.rest
        return scheme_eval(args.first, env)


class Lambda(Procedure):
    def apply(self, args, env):
        # validity check
        validate_form(args, 2)
        formals = args.first
        if not isinstance(formals, Pair) and formals is not nil:
            raise SchemeError('Formals must be a list')
        validate_formals(formals)    
        body = args.rest

        func = LambdaProcedure(formals, body, Frame(env)) # create a child frame
        return func

class If(Procedure):
    def apply(self, args, env):
        validate_form(args, 2, 3)
        predicate = scheme_eval(args.first, env)
        consequent = args.rest.first
        alternative = args.rest.rest.first if args.rest.rest.first is not nil else None
        if predicate is not False:
            return scheme_eval(consequent, env)
        else:
            return scheme_eval(alternative, env)

class Cond(Procedure):
    def apply(self, args, env):
        validate_form(args, 1)

        while args is not nil:
            test = args.first.first
            expr = args.first.rest

            # special handle for 'else'
            if test == 'else':
                if args.rest is not nil:
                    raise SchemeError('else must be last')
                else:
                    test = True
            else:
                test = scheme_eval(test, env)

            if test is not False:
                if expr is not nil:
                    procedure = expr
                    while procedure.rest is not nil:
                        scheme_eval(procedure.first, env)
                        procedure = procedure.rest

                    return scheme_eval(procedure.first, env)
                else:
                    return test

            args = args.rest

class And(Procedure):
    def apply(self, args, env):
        if args is nil:
            return True

        while args.rest is not nil:
            expr = args.first
            if scheme_eval(expr, env) is False:
                return False
            args = args.rest

        return scheme_eval(args.first, env)

class Or(Procedure):
    def apply(self, args, env):
        if args is nil:
            return False

        while args.rest is not nil:
            expr = args.first
            val = scheme_eval(expr, env)
            if val is not False:
                return val
            args = args.rest

        return scheme_eval(args.first, env)

class Let(Procedure):
    def apply(self, args, env):
        validate_form(args, 2)
        # seperate formals and values
        formals = Pair(nil, nil)
        values = Pair(nil, nil)

        tmp = args.first
        p_formals, p_values = formals, values
        while tmp is not nil:
            validate_form(tmp.first, 2, 2)
            formal = tmp.first.first
            value = tmp.first.rest.first

            p_formals.first, p_formals.rest = formal, Pair(nil, nil) if tmp.rest is not nil else nil
            p_values.first, p_values.rest = value, Pair(nil, nil) if tmp.rest is not nil else nil
            p_formals, p_values = p_formals.rest, p_values.rest

            tmp = tmp.rest

        body = args.rest

        func = Lambda().apply(Pair(formals, body), env)
        return func.apply(values, env)

class Mu(Procedure):
    def apply(self, args, env):
        validate_form(args, 2)
        formals = args.first
        body = args.rest
        return MuProcedure(formals, body)
        

# Utility methods for checking the structure of Scheme programs

def validate_form(expr, min, max=float('inf')):
    """Check EXPR is a proper list whose length is at least MIN and no more
    than MAX (default: no maximum). Raises a SchemeError if this is not the
    case.

    >>> validate_form(read_line('(a b)'), 2)
    """
    if not scheme_listp(expr):
        raise SchemeError('badly formed expression: ' + repl_str(expr))
    length = len(expr)
    if length < min:
        raise SchemeError('too few operands in form')
    elif length > max:
        raise SchemeError('too many operands in form')

def validate_formals(formals):
    """Check that FORMALS is a valid parameter list, a Scheme list of symbols
    in which each symbol is distinct. Raise a SchemeError if the list of
    formals is not a list of symbols or if any symbol is repeated.

    >>> validate_formals(read_line('(a b c)'))
    """
    symbols = set()
    def validate_and_add(symbol, is_last):
        if not scheme_symbolp(symbol):
            raise SchemeError('non-symbol: {0}'.format(symbol))
        if symbol in symbols:
            raise SchemeError('duplicate symbol: {0}'.format(symbol))
        symbols.add(symbol)

    while isinstance(formals, Pair):
        validate_and_add(formals.first, formals.rest is nil)
        formals = formals.rest

    # here for compatibility with DOTS_ARE_CONS
    if formals != nil:
        validate_and_add(formals, True)

def validate_procedure(procedure):
    """Check that PROCEDURE is a valid Scheme procedure."""
    if not scheme_procedurep(procedure):
        raise SchemeError('{0} is not callable: {1}'.format(
            type(procedure).__name__.lower(), repl_str(procedure)))

#################
# Dynamic Scope #
#################

class MuProcedure(Procedure):
    """A procedure defined by a mu expression, which has dynamic scope.
     _________________
    < Scheme is cool! >
     -----------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
    """

    def __init__(self, formals, body):
        """A procedure with formal parameter list FORMALS (a Scheme list) and
        Scheme list BODY as its definition."""
        self.formals = formals
        self.body = body


    def __str__(self):
        return str(Pair('mu', Pair(self.formals, self.body)))

    def __repr__(self):
        return 'MuProcedure({0}, {1})'.format(
            repr(self.formals), repr(self.body))

    def apply(self, args, env):
        func = Lambda().apply(Pair(self.formals, self.body), env)
        return func.apply(args, env)

##################
# Tail Recursion #
##################

# Make classes/functions for creating tail recursive programs here?

def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not a Thunk.
    Right now it just calls scheme_apply, but you will need to change this
    if you attempt the extra credit."""
    val = scheme_apply(procedure, args, env)
    # Add stuff here?
    return val



####################
# Extra Procedures #
####################

def scheme_map(fn, s, env):
    validate_type(fn, scheme_procedurep, 0, 'map')
    validate_type(s, scheme_listp, 1, 'map')
    return s.map(lambda x: complete_apply(fn, Pair(x, nil), env))

def scheme_filter(fn, s, env):
    validate_type(fn, scheme_procedurep, 0, 'filter')
    validate_type(s, scheme_listp, 1, 'filter')
    head, current = nil, nil
    while s is not nil:
        item, s = s.first, s.rest
        if complete_apply(fn, Pair(item, nil), env):
            if head is nil:
                head = Pair(item, nil)
                current = head
            else:
                current.rest = Pair(item, nil)
                current = current.rest
    return head

def scheme_reduce(fn, s, env):
    validate_type(fn, scheme_procedurep, 0, 'reduce')
    validate_type(s, lambda x: x is not nil, 1, 'reduce')
    validate_type(s, scheme_listp, 1, 'reduce')
    value, s = s.first, s.rest
    while s is not nil:
        value = complete_apply(fn, scheme_list(value, s.first), env)
        s = s.rest
    return value

################
# Input/Output #
################

def read_eval_print_loop(next_line, env, interactive=False, quiet=False,
                         startup=False, load_files=()):
    """Read and evaluate input until an end of file or keyboard interrupt."""
    if startup:
        for filename in load_files:
            scheme_load(filename, True, env)
    while True:
        try:
            src = next_line()
            while src.more_on_line:
                expression = scheme_read(src)
                result = scheme_eval(expression, env)
                if not quiet and result is not None:
                    print(repl_str(result))
        except (SchemeError, SyntaxError, ValueError, RuntimeError) as err:
            if (isinstance(err, RuntimeError) and
                'maximum recursion depth exceeded' not in getattr(err, 'args')[0]):
                raise
            elif isinstance(err, RuntimeError):
                print('Error: maximum recursion depth exceeded')
            else:
                print('Error:', err)
        except KeyboardInterrupt:  # <Control>-C
            if not startup:
                raise
            print()
            print('KeyboardInterrupt')
            if not interactive:
                return
        except EOFError:  # <Control>-D, etc.
            print()
            return

def scheme_load(*args):
    """Load a Scheme source file. ARGS should be of the form (SYM, ENV) or
    (SYM, QUIET, ENV). The file named SYM is loaded into environment ENV,
    with verbosity determined by QUIET (default true)."""
    if not (2 <= len(args) <= 3):
        expressions = args[:-1]
        raise SchemeError('"load" given incorrect number of arguments: '
                          '{0}'.format(len(expressions)))
    sym = args[0]
    quiet = args[1] if len(args) > 2 else True
    env = args[-1]
    if (scheme_stringp(sym)):
        sym = eval(sym)
    validate_type(sym, scheme_symbolp, 0, 'load')
    with scheme_open(sym) as infile:
        lines = infile.readlines()
    args = (lines, None) if quiet else (lines,)
    def next_line():
        return buffer_lines(*args)

    read_eval_print_loop(next_line, env, quiet=quiet)

def scheme_open(filename):
    """If either FILENAME or FILENAME.scm is the name of a valid file,
    return a Python file opened to it. Otherwise, raise an error."""
    try:
        return open(filename)
    except IOError as exc:
        if filename.endswith('.scm'):
            raise SchemeError(str(exc))
    try:
        return open(filename + '.scm')
    except IOError as exc:
        raise SchemeError(str(exc))

def create_global_frame():
    """Initialize and return a single-frame environment with built-in names."""
    env = Frame(None)
    env.define('eval',
               BuiltinProcedure(scheme_eval, True, 'eval'))
    env.define('apply',
               BuiltinProcedure(complete_apply, True, 'apply'))
    env.define('load',
               BuiltinProcedure(scheme_load, True, 'load'))
    env.define('procedure?',
               BuiltinProcedure(scheme_procedurep, False, 'procedure?'))
    env.define('map',
               BuiltinProcedure(scheme_map, True, 'map'))
    env.define('filter',
               BuiltinProcedure(scheme_filter, True, 'filter'))
    env.define('reduce',
               BuiltinProcedure(scheme_reduce, True, 'reduce'))
    env.define('undefined', None)
    add_builtins(env, BUILTINS)
    return env

@main
def run(*argv):
    import argparse
    parser = argparse.ArgumentParser(description='CS 61A Scheme Interpreter')
    parser.add_argument('--pillow-turtle', action='store_true',
                        help='run with pillow-based turtle. This is much faster for rendering but there is no GUI')
    parser.add_argument('--turtle-save-path', default=None,
                        help='save the image to this location when done')
    parser.add_argument('-load', '-i', action='store_true',
                       help='run file interactively')
    parser.add_argument('file', nargs='?',
                        type=argparse.FileType('r'), default=None,
                        help='Scheme file to run')
    args = parser.parse_args()

    import scheme
    scheme.TK_TURTLE = not args.pillow_turtle
    scheme.TURTLE_SAVE_PATH = args.turtle_save_path
    sys.path.insert(0, '')
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(scheme.__file__))))

    next_line = buffer_input
    interactive = True
    load_files = []

    if args.file is not None:
        if args.load:
            load_files.append(getattr(args.file, 'name'))
        else:
            lines = args.file.readlines()
            def next_line():
                return buffer_lines(lines)
            interactive = False

    read_eval_print_loop(next_line, create_global_frame(), startup=True,
                         interactive=interactive, load_files=load_files)
    tscheme_exitonclick()