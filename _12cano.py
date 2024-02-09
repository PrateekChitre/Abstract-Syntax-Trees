import ast
import astor

def remove_comments(node):
    """
    Remove comments from the AST recursively.
    """
    for field, value in ast.iter_fields(node):
        if isinstance(value, list):
            # If the value is a list, iterate over its items
            new_list = []
            for item in value:
                if isinstance(item, ast.AST):
                    # Recursively remove comments from AST nodes
                    new_item = remove_comments(item)
                    new_list.append(new_item)
                else:
                    new_list.append(item)
            setattr(node, field, new_list)
        elif isinstance(value, ast.AST):
            # Recursively remove comments from AST nodes
            new_node = remove_comments(value)
            setattr(node, field, new_node)
    return node

def canonicalize_code(code):
    # Parse the code into an AST
    tree = ast.parse(code)
    
    # Remove comments from the AST
    tree = remove_comments(tree)
    
    # Convert the modified AST back to code
    canonical_code = astor.to_source(tree)
    
    return canonical_code

# Example usage
code = """
# This is a comment
def foo(x):
    # Another comment
    if x < 0:
        return -x
    else:
        return x
"""

canonical_code = canonicalize_code(code)
print(canonical_code)
