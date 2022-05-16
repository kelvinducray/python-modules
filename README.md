# Python Modules
If you are not careful when setting up your project, you may end up facing difficulties when you try to import modules. This repository aims to provide practical examples of how importing modules in Python works, so that importing your scripts becomes simple.

## Where you run your script from matters
If you are using an IDE always set your working directory to the base directory of your project. Then place all of your scripts into their own module, and always execute the python command in the base directory of your project. This consistency with ensure predictable behaviour when you are running your project, using relative file paths and importing your own scripts.

## Stop using python <script_name>.py
Use python -m <module_name> in the command line.

## \_\_init\_\_.py
Tells Python explicitly that you want that directory to behave as a module.

## \_\_main\_\_.py
Runs when you call python -m <module_name> where module_name is a directory with an \_\_init\_\_.py file.

## Learn what if __name__ == '__main__' means, and why it's important
A great explanation can be found [here](https://www.youtube.com/watch?v=sugvnHA7ElY).

## Importing your scripts/modules
You can now import any of your modules within your project from any other if you use the full path to the module. E.g. In our test project we have a module called module_a with a script called script_y inside the module so we can write ```import module_a.script_y```. If we are working inside module_a we can use short-hand notation. E.g. ```import .script_y```.

## Implications when using Jupyter Notebooks
Try put them in the base directory of your project if you have a small number of them, you will then easily be able to import all your modules from all the different directories. This is become the working directory where your code is executed will depend on the directory of the notebook.
