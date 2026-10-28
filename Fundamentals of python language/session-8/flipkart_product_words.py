# task - 4: Flipkart Product Word Extraction (split(), indexing, len())

# Given Flipkart product description string
product_description = "Apple iPhone 15 features dynamic island aerospace-grade aluminum and all-day battery life"

print("=" * 60)
print("         FLIPKART PRODUCT DESCRIPTION WORD ANALYSIS        ")
print("=" * 60)

# 1. Using split() to break the description into a list of individual words
words_list = product_description.split()

# 2. Using positive indexing [0] to extract the first word
first_word = words_list[0]

# 3. Using negative indexing [-1] to extract the last word
last_word = words_list[-1]

# 4. Using len() to determine the total number of words
total_words = len(words_list)

print(f"Product Description : \"{product_description}\"\n")
print(f"Words Extracted     : {words_list}\n")
print(f"First Word          : \"{first_word}\"")
print(f"Last Word           : \"{last_word}\"")
print(f"Total Number of Words: {total_words}")

print("=" * 60)
