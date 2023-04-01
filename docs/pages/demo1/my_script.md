

An Very Important Header
-----

**author:** codima

the allmighty and all explaining doc string in the beginning and above all classes/functions

  - barfoo
  - foobar and so on



-----

  first\_function
-----
**declaration**

```python
def first_function(a: bool = True, b: tuple[str, bool, float, int] = ('test', False, -np.pi - 9.1, ~0)) -> bool: 
```

barfoo 


-----

another few important remarks in-between

  - barfoo
  - foobar and so on



-----

▸ TopLevel
-----
**declaration**

```python
class TopLevel(object): 
```


TopLevel example class doc string

the purpose of this class is to demonstrate documentation via Mkdocs supported by tomarkdown.

**fields**

  - barfoo (int): some random field of the TopLevel



**member classes:**

  - ▸ [TopLevel.MidLevel](my_script.TopLevel.md)
  - ▸ [TopLevel.SecondMidClass](my_script.TopLevel.md)


??? abstract "member functions"

    ▹ TopLevel.\_\_init\_\_

    ▹ TopLevel.boofar

    ▹ TopLevel.boofar

    ▹ TopLevel.another

-----
▹ TopLevel.\_\_init\_\_
-----
**declaration**

```python
def __init__(self): 
```


  takes no argument



-----
▹ TopLevel.boofar
-----
**declaration**

```python
@property 
def boofar(self) -> int: 
```


returns the 'boofar'-property value

**returns**

  - int: an integer value



-----
▹ TopLevel.boofar
-----
**declaration**

```python
@boofar.setter 
def boofar(self, new_val: int) -> None: 
```



**args**

  - new_val (int): requires & accepts a new value just to ignore it!



-----
▹ TopLevel.another
-----
**declaration**

```python
@staticmethod 
def another() -> bool: 
```

inline docstring is no problem either 


-----

this doc string will be ignored and not documented as it is supposed to.

class Test2:  # the appearance of a fully fletched out class within a doc string does not confuse tomarkdown!
  barfoo: int = -18.0

  def __init__(self):
    barfoo = 99.0



-----

  with\_code\_line\_breaks
-----
**declaration**

```python
def with_code_line_breaks(a: int, b: float = 99.0) -> tuple[bool, list[str]]: 
```

''' old docstring ''' (now included in new, but still does not confuse tomarkdown)
even this triplet "" " with space in between does not confuse tomarkdown;
also a triplet ""
" with linebreak does not confuse tomarkdown.

**args**

  - a (int): random example input a
  - b (float): random example input b

**returns**

  - tuple[bool, list[str]]: random return but also with a lot of code line breaks



-----
  first\_decorator\_function
-----
**declaration**

```python
def first_decorator_function(func): 
```



-----
  sub\_decorator\_function
-----
**declaration**

```python
def sub_decorator_function(func): 
```


a decorator to be appended to the first_decorator

**args**

  - func (Callable): a callable

**returns**

  - Callable: func from args



-----
  second\_decorator\_function
-----
**declaration**

```python
def second_decorator_function(*args): pass  # as inline function! 
```



-----
  beauty
-----
**declaration**

```python
@first_decorator_function.sub_decorator 
@second_decorator_function 
def beauty(a: int, b: np.ndarray = 99.0@zz) -> tuple[bool, list[str]]: 
```


the final and decorated top level function beauty

**args**

  - a (int): just some input a
  - b (float): just some input b

**returns**

  - tuple[bool, list[str]]: stuff



-----
  another\_function\_generator
-----
**declaration**

```python
def another_function_generator(param1: float) -> Callable: 
```


generates function

**args**

  - param1: influences computation of generated function generator

**returns**

  - a generated function generator



??? abstract "member functions"

    ▹ another\_function\_generator.a\_2nd\_function\_generator

-----
▹ a\_2nd\_function\_generator
-----

**from within:** another\_function\_generator

**declaration**

```python
def a_2nd_function_generator(param2: float) -> Callable: 
```


the generated function generator specialized by its generator

**args**

  - param2: influences computation of generated function generator

**returns**

  - a generated function



??? abstract "member functions"

    ▹ a\_2nd\_function\_generator.another\_generated\_function

-----
▹ another\_generated\_function
-----

**from within:** a\_2nd\_function\_generator

**declaration**

```python
def another_generated_function(arg1: float) -> float: 
```


the generated function specialized by its generator

**args**

  - arg1: is the one and only argument

**returns**

  - a number



-----
  a\_class\_generator
-----
**declaration**

```python
def a_class_generator(param3: float) -> Callable: 
```


generates a class

**args**

  - param3: influences initialization of generated class

**returns**

  - a generated class



**member classes:**

  - ▸ [a\_class\_generator.a\_generated\_class](my_script.a_class_generator.md)


-----