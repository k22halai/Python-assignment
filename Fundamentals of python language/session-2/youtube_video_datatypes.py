# task - 4: YouTube Video Variables - Primitive vs Non-Primitive Data Types

# Variable Declarations
title = "Python Full Course for Beginners [2026]"
views = 1542000
likes = 98500
is_premium = False

print("=" * 65)
print("             YOUTUBE VIDEO DATA TYPE ANALYSIS                    ")
print("=" * 65)

print(f"Variable: title\n  Value: '{title}'\n  Python Type: {type(title).__name__}\n  Category: Non-Primitive (Sequence / Composite)\n")
print(f"Variable: views\n  Value: {views}\n  Python Type: {type(views).__name__}\n  Category: Primitive (Scalar / Atomic Numeric)\n")
print(f"Variable: likes\n  Value: {likes}\n  Python Type: {type(likes).__name__}\n  Category: Primitive (Scalar / Atomic Numeric)\n")
print(f"Variable: is_premium\n  Value: {is_premium}\n  Python Type: {type(is_premium).__name__}\n  Category: Primitive (Scalar / Boolean)")

print("=" * 65)

'''
================================================================================
EXPLANATION: PRIMITIVE VS NON-PRIMITIVE DATA TYPES
================================================================================

1. PRIMITIVE DATA TYPES (Scalar / Atomic):
   - Definition: Primitive data types are the most basic, atomic building blocks 
     in programming. They hold a single direct value at a time and cannot be broken 
     down into simpler data structures.
   
   - Identified in this task:
     * `views` (int)      -> Primitive: Holds a single integer count (1542000).
     * `likes` (int)      -> Primitive: Holds a single integer count (98500).
     * `is_premium` (bool)-> Primitive: Holds a single truth value (True or False).

2. NON-PRIMITIVE DATA TYPES (Composite / Collection / Reference):
   - Definition: Non-primitive types are complex data structures that can store 
     multiple values, collections, or sequences of items.
   
   - Identified in this task:
     * `title` (str)      -> Non-Primitive: A string in Python is an immutable 
                             sequence (collection) of individual characters. Because 
                             it represents a sequence of elements rather than an atomic 
                             scalar, computer science classifies it as non-primitive/composite.

--------------------------------------------------------------------------------
Note on Python's Object Model:
In Python, "everything is an object" (even ints and bools are instances of classes). 
However, conceptually in software development and data structure design:
- Atomic, single-value types (int, float, bool) act as Primitive types.
- Collections and sequential types (str, list, tuple, dict, set) act as Non-Primitive types.
================================================================================
'''
