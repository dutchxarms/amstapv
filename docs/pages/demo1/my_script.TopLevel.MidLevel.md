
▸ [...].SubLevel
-----

**member of:** [[...].MidLevel](my_script.TopLevel.md)

**declaration**

```python
class SubLevel(object): 
```


SubLevel example class doc string

the purpose of this class is to demonstrate documentation via Mkdocs supported by tomarkdown.

**fields**

  - egg_shell (bool): some random field of the SubLevel



??? abstract "member functions"

    ▹ [...].SubLevel.\_\_init\_\_

    ▹ [...].SubLevel.a\_function\_generator

-----
▹ SubLevel.\_\_init\_\_
-----
**declaration**

```python
def __init__(self): 
```


  initializer



-----
▹ SubLevel.a\_function\_generator
-----
**declaration**

```python
def a_function_generator(self, param1: float) -> Callable: 
```


generates function

**args**

  - param1: influences computation of generated function

**returns**

  - the generated function



??? abstract "member functions"

    ▹ SubLevel.a\_function\_generator.a\_generated\_function

-----
▹ a\_generated\_function
-----

**from within:** SubLevel.a\_function\_generator

**declaration**

```python
def a_generated_function(arg1: float) -> float: 
```


the generated function specialized by its generator

**args**

  - arg1: is the one and only argument

**returns**

  - a number



-----