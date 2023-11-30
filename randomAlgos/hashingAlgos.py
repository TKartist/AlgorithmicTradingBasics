def basic_custom_hash(input_string):
    hash_value = 0

    multiplier = 34

    for char in input_string:
        hash_value = (hash_value * multiplier + ord(char)) % (2**32)
    return hash_value


input_data = "Hello, World!"
input_data2 = "!dlorW ,olleH"
hashed_value = basic_custom_hash(input_data)
hashed_value2 = basic_custom_hash(input_data2)
print(f"Input: {input_data}\nHashed Value: {hashed_value}")
print(f"Input: {input_data2}\nHashed Value: {hashed_value2}")

# Easy to do collision attack (I believe)
