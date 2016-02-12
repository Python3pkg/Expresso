


import expresso.pycas as pc
import rule_symbols as s
from .logic_evaluator import is_numeric,is_atomic

from .canonical_form import format_evaluator
from .logic_evaluator import evaluator as logic_evaluator

compile_evaluator = pc.RewriteEvaluator(recursive=False,split_binary=True)

fold_accuracy = 20

def fold(m):
    try:
        m[s.y] = pc.expresso.create_object(m[s.x].N(fold_accuracy))
    except Exception as e:
        return False

compile_evaluator.add_rule(s.x,s.y,fold)
compile_evaluator.add_rule(s.x**2,s.x*s.x,condition=is_atomic(s.x))

compiler_opt_evaluator = pc.MultiEvaluator(recursive = False, split_binary=True)
compiler_opt_evaluator.add_evaluator(compile_evaluator)
compiler_opt_evaluator.add_evaluator(logic_evaluator)

def optimize_for_compilation(expr,cache = None):
    return format_evaluator(compiler_opt_evaluator(expr, cache = cache))