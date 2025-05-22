import math
import re

class CalculatorTool:
    def calculate(self, expression):
        try:
            # Allow common math functions, limited for safety
            allowed_names = {
                "sqrt": math.sqrt,
                "log": math.log,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "pi": math.pi,
                "e": math.e,
                "pow": math.pow,
            }
            # Remove anything not number/operator/parentheses/math func
            clean_expr = re.sub(r'[^0-9\.\+\-\*\/\(\)\,\s\w]', '', expression)
            result = eval(clean_expr, {"__builtins__": None}, allowed_names)
            return f"Calculator result: {result}"
        except Exception as e:
            return "Invalid calculation."
