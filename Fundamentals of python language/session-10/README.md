# Session 10: Python Tuples — Immutability, Indexing & Operations

This folder contains completed assignments for Session 10, demonstrating tuple definition, indexing, slicing, error inspection under item assignment (immutability), and concatenation.

## Tasks Overview

| Task # | File Name | Description | Key Concepts |
| :--- | :--- | :--- | :--- |
| **Task 1** | [`create_fav_apps_tuple.py`](./create_fav_apps_tuple.py) | Defines `fav_apps` tuple with 5 popular mobile apps and prints it. | Tuple creation `(...)`, `len()`, `type()` |
| **Task 2** | [`access_tuple_elements.py`](./access_tuple_elements.py) | Accesses 2nd app (index 1) and 4th app (index 3) via indexing. | 0-based indexing `tuple[i]` |
| **Task 3** | [`tuple_immutability_test.py`](./tuple_immutability_test.py) | Attempts item assignment `fav_apps[0] = 'YouTube'`, catches `TypeError`, and explains immutability. | Tuple immutability, `TypeError`, fixed memory allocation |
| **Task 4** | [`slice_middle_apps.py`](./slice_middle_apps.py) | Extracts middle 3 apps from 5-item tuple using `fav_apps[1:4]`. | Tuple slicing `tuple[start:end]` |
| **Task 5** | [`concatenate_apps_tuples.py`](./concatenate_apps_tuples.py) | Joins `fav_apps` and `new_apps` using `+` operator into `all_apps`. | Tuple concatenation, immutable object reproduction |
