a = 16
a = a // 2
print(a * 2)
a = a + 11
print(a + 1)
a = a - 3


# a = 16
#  = a // 2  # 16 // 2 = 8
# print(a * 2)  # 8 * 2 = 16
# a = a + 11  # 8 + 11 = 19
# print(a + 1)  # 19 + 1 = 20
# a = a - 3  # 19 - 3 = 16

print(2 + 3 * 6 / 2)

# 3 * 6 = 18
# 18 / 2 = 9.0
# 2 + 9.0 = 11.0

import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


def find_c_Jeb_words(filename):
    """
    Reads a file and finds words that start with 'c' and end with 'Jeb'.
    Returns the count of such words.
    """
    try:
        with open(filename, "r") as file:
            text = file.read()

        # Split the text into words
        words = text.split()

        # Count words that match the condition
        count = sum(1 for word in words if word.startswith("c") and word.endswith("Jeb"))

        return count

    except FileNotFoundError:
        print("File not found.")
        return 0

# Lists are mutable
my_list = [1, 2, 3]
print("Original List:", my_list)
my_list[0] = 100  # Changing the first element
print("Modified List:", my_list)

# Strings are immutable
my_string = "hello"
print("Original String:", my_string)

# Trying to change the first character will cause an error
try:
    my_string[0] = "H"  # This will cause an error
except TypeError as e:
    print("Error:", e)

# The correct way to modify a string is by creating a new one
new_string = "H" + my_string[1:]
print("Modified String:", new_string)

import random

# Generate a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Process the list according to the given conditions
for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        # Replace numbers greater than 80 with their negative counterpart
        random_numbers[i] = -random_numbers[i]
    elif random_numbers[i] < 40:
        # Replace numbers less than 40 with the sum of their digits
        num_str = str(random_numbers[i])
        digit_sum = sum(int(digit) for digit in num_str)  # Sum the digits
        random_numbers[i] = digit_sum
# Print the modified list
print("Modified List:", random_numbers)
def is_valid_url(url):
    """
    Function to check if a given string is a valid URL.
    A valid URL starts with 'http://' or 'https://' and contains at least one '.'
    """
    if (url.startswith("http://") or url.startswith("https://")) and "." in url:
        return True
    return False
# Test cases
print(is_valid_url("https://example.com"))  # True
print(is_valid_url("http://google.com"))    # True
print(is_valid_url("ftp://files.com"))      # False
print(is_valid_url("example.com"))          # False

def days_since_birth(birth_date):
  """

  Function to calculate whole years in days since birth.

  Takes birth date in "DD-MM-YYYY" format.

  """
  # Extract the birth year
  birth_year = int(birth_date.split("-")[2])
  # Current year (it's 2025 as we cannot import datetime)
  current_year = 2025
  # Calculate whole years passed
  years_passed = current_year - birth_year - 1
  # Convert years to days
  return years_passed * 365
# Test cases
print(days_since_birth("19-01-2005")) # Expected: (2025-2005-1) * 365 = 6935