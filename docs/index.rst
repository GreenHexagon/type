Type
####
Module for terminal type effects  

.. image:: https://readthedocs.org/projects/type/badge/?version=latest
    :target: https://type.readthedocs.io/en/latest/


Documentation
----
[argument] - required  

<argument> - optional.  

Functions
^^^^
``type``
 Prints out a string. Can be used like as an alternative to the standard `print` or to create typing effects
  [`word:string`], <`delay:float`>, <`instant:boolean`>, <`newline:boolean`>
``colortype``
 Identical to type, but can be passed RGB (0-255) values.
  [`word:string`], [`r`], [`g`], [`b`] <`delay:float`>, <`instant:boolean`>, <`newline:boolean`>

.. note::
    Using ``instant=true`` will automatically make delay 0, regardless of it's previous value.
