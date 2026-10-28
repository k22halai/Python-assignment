# Session 8: Strings — Indexing, Slicing & Built-in Methods

This folder contains completed assignments for Session 8, covering Python string operations: positive/negative indexing, substring slicing, delimiter searching (`index()`), manual reversal with loop constraints, tokenization (`split()`), and string masking.

## Tasks Overview

| Task # | File Name | Description | Key Concepts & Methods |
| :--- | :--- | :--- | :--- |
| **Task 1** | [`insta_caption.py`](./insta_caption.py) | Takes an Instagram caption and prints the first 10 characters with individual index breakdown. | Positive indexing `[0:10]`, index enumeration |
| **Task 2** | [`extract_spotify_artist.py`](./extract_spotify_artist.py) | Defines `extract_artist(song_title)` to slice and return the artist from `'Song - Artist'` format. | `index('-')`, string slicing `[dash+1:]`, `.strip()` |
| **Task 3** | [`reverse_message.py`](./reverse_message.py) | Defines `reverse_message(message)` to invert strings without using `reversed()` or `[::-1]`. | Manual character accumulation loop, loop constraints |
| **Task 4** | [`flipkart_product_words.py`](./flipkart_product_words.py) | Analyzes a Flipkart description to extract the first word, last word, and total word count. | `.split()`, index `[0]`, negative index `[-1]`, `len()` |
| **Task 5** | [`mask_phone_number.py`](./mask_phone_number.py) | Defines `mask_phone_number(phone)` to return masked format `'******1234'`. | Negative slicing `[-4:]`, string concatenation (`+`) |
