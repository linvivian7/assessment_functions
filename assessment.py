"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

def is_hometown(town_name):
    """Determine if town is home town, Yorba Linda

    >>> is_hometown("Berkeley")
    False

    >>> is_hometown("Yorba Linda")
    True

    """

    return town_name == "Yorba Linda"


#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

def full_name(first_name, last_name):
    """Return full name as concatenation of first and last name

    >>> full_name("Meowy", "Smith")
    'Meowy Smith'

    """

    full_name = " ".join([first_name, last_name])
    return full_name

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.


def greet_stranger(other_town_name, first_name, last_name):
    """Greeting with full name and home town_name

    >>> greet_stranger("Sunnyvale", "Scottish", "Fold")
    Hi, Scottish Fold, where are you from?

    >>> greet_stranger("Yorba Linda", "Albert", "Einstein")
    Hi, Albert Einstein, we're from the same place!

    """
    if is_hometown(other_town_name) is True:
        print "Hi, {}, we're from the same place!".format(full_name(first_name, last_name))

    else:
        print "Hi, {}, where are you from?".format(full_name(first_name, last_name))

###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determine if fruit is a berry"""

    return fruit in ["strawberry", "cherry", "blackberry"]


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.


def shipping_cost(fruit):
    """Calculate shipping cost of fruit"""

    if is_berry(fruit) is True:
        return 0
    else:
        return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Create a new list consisting of the old list with the given number
       added to the end."""

    lst.append(num)

    return lst

# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.


def calculate_price(base_price, abbr_state, tax=.05):
    """Create total price after tax and fees, depending on state stipulations"""

    all_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI",
        "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
        "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA",
        "WA", "WV", "WI", "WY"]

    try:
        float(base_price)
        float(tax)
    except ValueError:
        return "Please enter parameters in correct format"

    if abbr_state not in all_states:
        return "Please enter a valid state abbreviation"

    post_tax = base_price * (1 + tax)

    if abbr_state == "CA":
        fee = post_tax * .03

    elif abbr_state == "PA":
        fee = 2

    elif abbr_state == "MA":
            if base_price < 100:
                fee = 1
            else:
                fee = 3

    else:
        if tax == 0:
            return post_tax
        else:
            return float("{:.1f}".format(post_tax))

    total_cost = post_tax + fee
    return float("{:.1f}".format(total_cost))

###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.

def append_any_to_list(user_list, *args):
    """Append or extend list depending on number of arguments

    >>> append_any_to_list([2,4,6,7], 324, 6345345, 12323)
    [2, 4, 6, 7, 324, 6345345, 12323]

    >>> append_any_to_list(["dog","cat",1000], "duck")
    ['dog', 'cat', 1000, 'duck']

    >>> append_any_to_list(["dog","cat",1000], 20)
    ['dog', 'cat', 1000, 20]


    """

    additional = [arg for arg in args]

    user_list.extend(additional)

    return user_list


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def outer_repeat_three(word):
    """Return word and repeat the word three times without spaces

    >>> outer_repeat_three("Balloonicorn")
    ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

    """

    def repeat_three(word):
        return "".join([word, word, word])

    return word, repeat_three(word)


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
