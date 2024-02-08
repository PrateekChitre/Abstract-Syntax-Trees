import ast

def generate_ast(code):
    """
    Generate abstract syntax tree (AST) for the given Python code.
    """
    return ast.parse(code)

def print_ast(node, indent=0):
    """
    Print AST nodes recursively with proper indentation.
    """
    if isinstance(node, ast.AST):
        print(' ' * indent + node.__class__.__name__)
        for field, value in ast.iter_fields(node):
            if isinstance(value, ast.AST):
                print(' ' * (indent + 4) + field + ":")
                print_ast(value, indent + 8)
            elif isinstance(value, list):
                print(' ' * (indent + 4) + field + ":")
                for item in value:
                    if isinstance(item, ast.AST):
                        print_ast(item, indent + 8)
                    else:
                        print(' ' * (indent + 8) + repr(item))
            else:
                print(' ' * (indent + 4) + field + ": " + repr(value))
    else:
        print(' ' * indent + repr(node))

# Example usage
if __name__ == "__main__":
    python_code = """
i = 0
while i < 3:
    print("Outer loop:", i)
    j = 0
    while j < 2:
        print("Inner loop:", j)
        j += 1
    i += 1
"""
    ast_tree = generate_ast(python_code)
    print_ast(ast_tree)
