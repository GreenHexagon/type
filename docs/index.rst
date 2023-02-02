Type
####
Module for terminal type effects  

.. image:: https://readthedocs.org/projects/type/badge/?version=latest
    :target: https://type.readthedocs.io/en/latest/


Documentation
----


Functions
^^^^  

*type(word:string, delay=0.25, instant=True, newline=True)*
~~~~
Prints out a string. Can be used like as an alternative to the standard ``print`` or to create typing effects
 

*colortype(word, r=0, g=0, b=0, delay=0, instant=True, newline=True)*
~~~~
Identical to ``type``, but can be passed RGB (0-255) values.
 

.. note::
    Using ``instant=true`` will automatically make delay 0, regardless of it's previous value.
