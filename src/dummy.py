# This code is originally from https://maurcz.github.io/posts/002-customizing-the-python-debugger/
# All source code related to the post is available at https://github.com/maurcz/posts/tree/main/python-customizing-pdb


from random import random


def print_the_things(number: int, text: str, big_list: list):
    import debug; debug.stop()

    print(f"Number: {number}, Text: {text}, big_list: {big_list}")

# import debug; debug.stop()
print_the_things(number=10, 
                 text="Blame and lies, contradictions arise",
                 big_list=[random() for _ in range(5)]
)