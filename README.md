# Nested Dictionary Solver

A Python solution for accessing values in deeply nested dictionaries using path-like strings.

## 🎯 Problem Statement

Given a nested dictionary and a key path (e.g., "a/b/c"), extract the corresponding value from the nested structure.

### Challenge Examples:
- **Input:** `{"a":{"b":{"c":"d"}}}` with key `"a/b/c"`
- **Output:** `"d"`

- **Input:** `{"x":{"y":{"z":"a"}}}` with key `"x/y/z"`
- **Output:** `"a"`

## 🚀 Quick Start

```python
from nested_dict_solver import get_nested_value

# Basic usage
obj = {"a": {"b": {"c": "d"}}}
result = get_nested_value(obj, "a/b/c")
print(result)  # Output: "d"
```

## 📋 Features

- ✅ Navigate nested dictionaries using path strings
- ✅ Comprehensive error handling
- ✅ Safe version that returns `None` instead of raising errors
- ✅ Extensive test suite
- ✅ No external dependencies
- ✅ Clean, readable code with documentation

## 🔧 API Reference

### `get_nested_value(obj, key_path)`

**Parameters:**
- `obj` (dict): The nested dictionary to search in
- `key_path` (str): The path to the value, separated by '/' (e.g., "a/b/c")

**Returns:**
- The value at the specified path

**Raises:**
- `KeyError`: If the path doesn't exist in the dictionary

**Example:**
```python
obj = {"user": {"profile": {"name": "Alice"}}}
name = get_nested_value(obj, "user/profile/name")
print(name)  # Output: "Alice"
```

### `get_nested_value_safe(obj, key_path)`

**Parameters:**
- `obj` (dict): The nested dictionary to search in
- `key_path` (str): The path to the value, separated by '/' (e.g., "a/b/c")

**Returns:**
- The value at the specified path, or `None` if the path doesn't exist

**Example:**
```python
obj = {"user": {"profile": {"name": "Alice"}}}
email = get_nested_value_safe(obj, "user/profile/email")
print(email)  # Output: None (no error raised)
```

## 🧠 How It Works

### Step-by-Step Algorithm:

1. **Input Validation:** Check if dictionary and key path are valid
2. **Path Splitting:** Split the key path by '/' into individual keys
3. **Navigation:** Iterate through each key, moving deeper into the dictionary
4. **Type Checking:** Ensure each level is a dictionary before accessing
5. **Error Handling:** Raise `KeyError` if path doesn't exist
6. **Return Value:** Return the final value found

### Visual Example:

```python
# Input
obj = {"a": {"b": {"c": "d"}}}
key_path = "a/b/c"

# Step 1: Split path
keys = ["a", "b", "c"]

# Step 2: Navigate
current = {"a": {"b": {"c": "d"}}}  # Start at root
current = current["a"]              # current = {"b": {"c": "d"}}
current = current["b"]              # current = {"c": "d"}
current = current["c"]              # current = "d"

# Step 3: Return
return "d"
```

## 🧪 Testing

The solution includes comprehensive tests covering:

- ✅ Challenge examples from the problem statement
- ✅ Single-level dictionary access
- ✅ Deep nesting (4+ levels)
- ✅ Error handling for invalid paths
- ✅ Safe version functionality
- ✅ Edge cases (empty objects, empty paths)

### Running Tests:

```bash
python nested_dict_solver.py
```

This will run both the demonstration and all test cases.

## 📝 Usage Examples

### Example 1: Configuration Access
```python
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "credentials": {
            "username": "admin",
            "password": "secret"
        }
    }
}

# Access nested configuration
host = get_nested_value(config, "database/host")
username = get_nested_value(config, "database/credentials/username")
print(f"Host: {host}")        # Output: Host: localhost
print(f"User: {username}")    # Output: User: admin
```

### Example 2: User Profile Data
```python
user_data = {
    "user": {
        "profile": {
            "personal": {
                "name": "Alice",
                "age": 25,
                "location": "New York"
            },
            "contact": {
                "email": "alice@example.com",
                "phone": "123-456-7890"
            }
        }
    }
}

# Extract user information
name = get_nested_value(user_data, "user/profile/personal/name")
email = get_nested_value(user_data, "user/profile/contact/email")
print(f"Name: {name}")    # Output: Name: Alice
print(f"Email: {email}")  # Output: Email: alice@example.com
```

### Example 3: Error Handling
```python
obj = {"a": {"b": {"c": "d"}}}

# This will raise KeyError
try:
    result = get_nested_value(obj, "a/b/nonexistent")
except KeyError as e:
    print(f"Error: {e}")
    # Output: Error: Key path 'a/b/nonexistent' not found. Failed at key 'nonexistent'

# Safe version returns None
result = get_nested_value_safe(obj, "a/b/nonexistent")
print(result)  # Output: None
```

## 🔍 Code Structure

```
nested_dict_solver.py
├── get_nested_value()           # Main function with error handling
├── get_nested_value_safe()      # Safe version that returns None
├── test_nested_dict_solver()    # Comprehensive test suite
├── demonstrate_solution()       # Example demonstrations
└── __main__                     # Program entry point
```

## 🎯 Real-World Applications

This solution is useful for:

- **Configuration Management:** Accessing nested settings in config files
- **API Response Processing:** Extracting data from complex JSON responses
- **Data Analysis:** Navigating hierarchical data structures
- **Web Development:** Processing nested form data or user profiles
- **Database Operations:** Working with nested document structures

## 🚀 Performance Considerations

- **Time Complexity:** O(n) where n is the depth of nesting
- **Space Complexity:** O(1) - no additional data structures needed
- **Memory Efficient:** Processes keys one at a time without storing intermediate results

## 🛠️ Requirements

- Python 3.6+
- No external dependencies

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve this solution.

---

**Note:** This solution was created as part of a coding challenge and demonstrates clean, well-tested Python code with comprehensive error handling.
