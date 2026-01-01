#!/usr/bin/env python3
"""
This is a test Python file created to demonstrate basic Python functionality.
"""

def hello_world():
    """A simple function that prints a greeting."""
    print("Hello, World!")
    return "Hello, World!"


def add_numbers(a, b):
    """A function to add two numbers."""
    return a + b


def main():
    """Main function to demonstrate the test file functionality."""
    print("Running tests from the test Python file...")
    
    # Test the hello_world function
    result = hello_world()
    print(f"Function returned: {result}")
    
    # Test the add_numbers function
    sum_result = add_numbers(5, 3)
    print(f"5 + 3 = {sum_result}")
    
    print("Test file execution completed successfully!")


if __name__ == "__main__":
    main()