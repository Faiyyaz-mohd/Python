def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))  # Recursively flatten nested lists
        else:
            flat_list.append(item)
    return flat_list

# Example usage
nested_list = [1, [2, 3], [4, [5, 6]]]
flattened = flatten_list(nested_list)
print(f"Flattened list: {flattened}")
