# type
Module for terminal type effects

## How to use
Copy the function definition in main.py, take time to understand it, or don't. Make sure sys and time are imported.

The word argument takes a string, any string. 

The delay argument takes an int or a string able to be turned into an int with int(string).

The instant argument is a quick way to set delay to 0. You can use either this or delay = 0. Or both, both will work as well. However, if using both, note that Instant being True will make delay = 0, regardless of whether or not it was non-zero. 

The newline argument shows whether or not to create a new line after each usage of type **or** colortype. 
