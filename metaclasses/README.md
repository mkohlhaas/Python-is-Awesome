### Links

- [Metaprogramming in Python](https://developer.ibm.com/tutorials/ba-metaprogramming-python/)
- [Metaprogramming with Metaclasses in Python](https://www.geeksforgeeks.org/metaprogramming-metaclasses-python/)
- [Python Metaprogramming by David Beazley](http://www.dabeaz.com/py3meta/Py3Meta.pdf)

### Concepts

- Everything is an Object/Instance:
  - 5
  - "str"
  - Function
  - Class
  - ...
- Object = Instance of a Class
  -> Every Object belongs to a Class.
  - 5          -> int          -> type                   -> type ...
  - "str"      -> str          -> type                   -> type ...
  - [1,2,3]    -> list         -> type                   -> type ...
  - Function   -> function     -> type                   -> type ...
  - Class      -> MetaClass    -> type                   -> type ...
  - ...        -> class of ... -> class of class of ...  -> ...    -> type ...
- Metaclass -> Class == Class -> Object
  -> Object -> Class -> MetaClass
- Class defines how to create an Object.
- MetaClass defines how to create a Class.
