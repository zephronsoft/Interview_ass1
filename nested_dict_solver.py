def get_nested_value(obj, key_path):
    """
    Get a value from a nested dictionary using a key path.
    
    Args:
        obj (dict): The nested dictionary to search in
        key_path (str): The path to the value, separated by '/' (e.g., "a/b/c")
    
    Returns:
        The value at the specified path, or None if the path doesn't exist
    
    Raises:
        KeyError: If the path doesn't exist in the dictionary
    """
    if not obj or not key_path:
        return None
    
    # Split the key path by '/'
    keys = key_path.split('/')
    current = obj
    
    # Navigate through the nested structure
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            raise KeyError(f"Key path '{key_path}' not found. Failed at key '{key}'")
    
    return current


def get_nested_value_safe(obj, key_path):
    """
    Safe version that returns None instead of raising KeyError.
    
    Args:
        obj (dict): The nested dictionary to search in
        key_path (str): The path to the value, separated by '/' (e.g., "a/b/c")
    
    Returns:
        The value at the specified path, or None if the path doesn't exist
    """
    try:
        return get_nested_value(obj, key_path)
    except KeyError:
        return None


# Test cases
def test_nested_dict_solver():
    """Test the nested dictionary solver with various cases."""
    
    print("Running tests for nested dictionary solver...")
    
    # Test case 1: From the challenge example
    obj1 = {"a": {"b": {"c": "d"}}}
    key1 = "a/b/c"
    expected1 = "d"
    result1 = get_nested_value(obj1, key1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"✓ Test 1 passed: {key1} -> {result1}")
    
    # Test case 2: From the challenge example
    obj2 = {"x": {"y": {"z": "a"}}}
    key2 = "x/y/z"
    expected2 = "a"
    result2 = get_nested_value(obj2, key2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"✓ Test 2 passed: {key2} -> {result2}")
    
    # Test case 3: Single level
    obj3 = {"name": "John", "age": 30}
    key3 = "name"
    expected3 = "John"
    result3 = get_nested_value(obj3, key3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"✓ Test 3 passed: {key3} -> {result3}")
    
    # Test case 4: Multiple levels with different data types
    obj4 = {
        "user": {
            "profile": {
                "personal": {
                    "name": "Alice",
                    "age": 25
                },
                "contact": {
                    "email": "alice@example.com",
                    "phone": "123-456-7890"
                }
            }
        }
    }
    key4 = "user/profile/personal/name"
    expected4 = "Alice"
    result4 = get_nested_value(obj4, key4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"✓ Test 4 passed: {key4} -> {result4}")
    
    # Test case 5: Test error handling
    try:
        get_nested_value(obj1, "a/b/nonexistent")
        assert False, "Test 5 failed: Should have raised KeyError"
    except KeyError as e:
        print(f"✓ Test 5 passed: Correctly raised KeyError - {e}")
    
    # Test case 6: Test safe version
    result6 = get_nested_value_safe(obj1, "a/b/nonexistent")
    assert result6 is None, f"Test 6 failed: expected None, got {result6}"
    print("✓ Test 6 passed: Safe version returns None for nonexistent key")
    
    # Test case 7: Empty key path
    result7 = get_nested_value_safe(obj1, "")
    assert result7 is None, f"Test 7 failed: expected None, got {result7}"
    print("✓ Test 7 passed: Empty key path returns None")
    
    # Test case 8: Empty object
    result8 = get_nested_value_safe({}, "a/b/c")
    assert result8 is None, f"Test 8 failed: expected None, got {result8}"
    print("✓ Test 8 passed: Empty object returns None")
    
    print("\n🎉 All tests passed!")


def demonstrate_solution():
    """Demonstrate the solution with the challenge examples."""
    print("=" * 50)
    print("NESTED DICTIONARY SOLVER DEMONSTRATION")
    print("=" * 50)
    
    # Example 1 from the challenge
    print("\nExample 1:")
    obj1 = {"a": {"b": {"c": "d"}}}
    key1 = "a/b/c"
    print(f"Object: {obj1}")
    print(f"Key path: {key1}")
    try:
        result1 = get_nested_value(obj1, key1)
        print(f"Result: {result1}")
    except KeyError as e:
        print(f"Error: {e}")
    
    # Example 2 from the challenge
    print("\nExample 2:")
    obj2 = {"x": {"y": {"z": "a"}}}
    key2 = "x/y/z"
    print(f"Object: {obj2}")
    print(f"Key path: {key2}")
    try:
        result2 = get_nested_value(obj2, key2)
        print(f"Result: {result2}")
    except KeyError as e:
        print(f"Error: {e}")
    
    # Additional example
    print("\nAdditional Example:")
    obj3 = {
        "config": {
            "database": {
                "host": "localhost",
                "port": 5432,
                "credentials": {
                    "username": "admin",
                    "password": "secret"
                }
            }
        }
    }
    key3 = "config/database/credentials/username"
    print(f"Object: {obj3}")
    print(f"Key path: {key3}")
    try:
        result3 = get_nested_value(obj3, key3)
        print(f"Result: {result3}")
    except KeyError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Run the demonstration
    demonstrate_solution()
    
    # Run all tests
    print("\n" + "=" * 50)
    test_nested_dict_solver()
