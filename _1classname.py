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
    print(' ' * indent + node.__class__.__name__)
    for child_node in ast.iter_child_nodes(node):
        print_ast(child_node, indent + 4)

# Example usage
if __name__ == "__main__":
    python_code = """
x = 10
y = 20
z = x + y
print(z)
"""
    ast_tree = generate_ast(python_code)
    print_ast(ast_tree)
