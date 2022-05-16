from sys import argv

from .script_x import weird_function

# NOTE: ^ This is the same as from module_b.script_x import weird_function.
# This is just the short hand notation if you're referring the the module
# that the script is located in.

if __name__ == "__main__":
    try:
        x, y = argv[1:3]  # Take the first two arguments from the command line
        result = weird_function(float(x), float(y))
        print("The result is:", result)
    except ValueError:
        print(
            "Error: You need to specify two numeric arguments. E.g. python -m module_b 5 10",
        )
