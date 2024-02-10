def compare_ast(node1, node2):
    if type(node1) != type(node2):
        return False
    if isinstance(node1, ast.AST):
        for field, value1 in ast.iter_fields(node1):
            value2 = getattr(node2, field, None)
            if not compare_ast(value1, value2):
                return False
        return True
    elif isinstance(node1, list):
        if len(node1) != len(node2):
            return False
        return all(compare_ast(x, y) for x, y in zip(node1, node2))
    else:
        return node1 == node2

# Example usage:
if __name__ == "__main__":
    import ast
    
    # Example ASTs
    code1 = "x = 10"
    code2 = "x = 10"
    
    ast1 = ast.parse(code1)
    ast2 = ast.parse(code2)
    
    # Compare ASTs
    if compare_ast(ast1, ast2):
        print("ASTs are equivalent")
    else:
        print("ASTs are different")