import numpy as np

from typing import Union, Callable


'''
An Very Important Header
-----

**author:** codima

the allmighty and all explaining doc string in the beginning and above all classes/functions

    - barfoo
    - foobar and so on
'''


def first_function(a: bool = True, b: tuple[str, bool, float, int] = ('test', False, -np.pi-9.1, ~0)) -> bool:
    ''' barfoo '''
    return a


'''
another few important remarks in-between

    - barfoo
    - foobar and so on
'''


class TopLevel(object):
    '''
    TopLevel example class doc string

    the purpose of this class is to demonstrate documentation via Mkdocs supported by tomarkdown.

    **fields**

        - barfoo (int): some random field of the TopLevel
    '''
    barfoo: int = -18.0

    def __init__(self):
        '''
            takes no argument
        '''
        self.barfoo = 99

    ''' in-between doc string -> ignored during the documentation process'''

    @property
    def boofar(self) -> int:
        '''
        returns the 'boofar'-property value

        **returns**

            - int: an integer value
        '''
        return 999

    @boofar.setter
    def boofar(self, new_val: int) -> None:
        '''

        **args**

            - new_val (int): requires & accepts a new value just to ignore it!
        '''
        print(f'registered and stored: {new_val}')

    class MidLevel(object):
        '''
        MidLevel example class doc string

        the purpose of this class is to demonstrate documentation via Mkdocs supported by tomarkdown.

        **fields**

            - foobar (int): some random field of the MidLevel
        '''
        foobar: int = -18.0

        def good_spam(self, egg: str, l: np.ndarray) -> None:
            '''
            the good_spam function of MidLevel

            **args**

                - egg (str): ...
                - l (np.ndarray): ...

            **returns**

                - None
            '''
            pass

        def _bad_spam(self, egg: str, l: np.ndarray) -> None:  # <tomarkdown:IGNORE>
            '''
            the hidden _bad_spam function of MidLevel

            **args**

                - egg (str): ...
                - l (np.ndarray): ...

            **returns**

                - None
            '''
            pass

        class SubLevel(object):
            '''
            SubLevel example class doc string

            the purpose of this class is to demonstrate documentation via Mkdocs supported by tomarkdown.

            **fields**

                - egg_shell (bool): some random field of the SubLevel
            '''
            egg_shell: bool = False

            def __init__(self):
                '''
                    initializer
                '''
                foo_bar_foo_baz: float = 999.0

            def a_function_generator(self, param1: float) -> Callable:
                '''
                generates function

                **args**

                    - param1: influences computation of generated function

                **returns**

                    - the generated function
                '''

                def a_generated_function(arg1: float) -> float:
                    '''
                    the generated function specialized by its generator

                    **args**

                        - arg1: is the one and only argument

                    **returns**

                        - a number
                    '''
                    return arg1*param1

                return a_generated_function

    class MidLevelHidden(object):  # <tomarkdown:IGNORE>
        '''
        MidLevel example class doc string

        the purpose of this class is to demonstrate documentation via Mkdocs supported by tomarkdown.

        **fields**

            - foobar (int): some random field of the MidLevel
        '''
        foobar: int = -18.0

        def good_spam_hidden(self, egg: str, l: np.ndarray) -> None:
            '''
            the good_spam function of MidLevel

            **args**

                - egg (str): ...
                - l (np.ndarray): ...

            **returns**

                - None
            '''
            pass

        def bad_spam_hidden(self, egg: str, l: np.ndarray) -> None:
            '''
            the hidden _bad_spam function of MidLevel

            **args**

                - egg (str): ...
                - l (np.ndarray): ...

            **returns**

                - None
            '''
            pass

        class SubLevel_hidden(object):
            '''
            SubLevel example class doc string

            the purpose of this class is to demonstrate documentation via Mkdocs supported by tomarkdown.

            **fields**

                - egg_shell (bool): some random field of the SubLevel
            '''
            egg_shell: bool = False

            def __init__(self):
                '''
                    initializer
                '''
                foo_bar_foo_baz: float = 999.0

    class SecondMidClass(object):
        ''' don't bother with me, but I'm not hidden! '''

        def __init__(self):
            ''' the init of SecondMidClass '''
            ...

    @staticmethod
    def another() -> bool:
        ''' inline docstring is no problem either '''
        return True

"""
this doc string will be ignored and not documented as it is supposed to.

class Test2:  # the appearance of a fully fletched out class within a doc string does not confuse tomarkdown! 
    barfoo: int = -18.0

    def __init__(self):
        barfoo = 99.0
"""


def with_code_line_breaks(a: int, b: float \
        = 99.0) -> tuple[bool,\
                         list[str]]:
    """ ''' old docstring ''' (now included in new, but still does not confuse tomarkdown)
    even this triplet "" " with space in between does not confuse tomarkdown;
    also a triplet ""
    " with linebreak does not confuse tomarkdown.

    **args**

        - a (int): random example input a
        - b (float): random example input b

    **returns**

        - tuple[bool, list[str]]: random return but also with a lot of code line breaks
    """
    c = a - b

    return c < 0.0,\
            \
            \
           ['O.O']


def first_decorator_function(func):
    return func


def sub_decorator_function(func):
    '''
    a decorator to be appended to the first_decorator

    **args**

        - func (Callable): a callable

    **returns**

        - Callable: func from args
    '''
    return func


first_decorator_function.sub_decorator = sub_decorator_function


def second_decorator_function(*args): pass  # as inline function!


zz = np.ones(shape = (3,))


@first_decorator_function.sub_decorator
@second_decorator_function
def beauty(a: int, b: np.ndarray = 99.0@zz) -> tuple[bool, list[str]]:
    """
    the final and decorated top level function beauty

    **args**

        - a (int): just some input a
        - b (float): just some input b

    **returns**

        - tuple[bool, list[str]]: stuff
    """
    c = a - b

    return c < 0.0, ['O.O']


def another_function_generator(param1: float) -> Callable:
    '''
    generates function

    **args**

        - param1: influences computation of generated function generator

    **returns**

        - a generated function generator
    '''
    def a_2nd_function_generator(param2: float) -> Callable:
        '''
        the generated function generator specialized by its generator

        **args**

            - param2: influences computation of generated function generator

        **returns**

            - a generated function
        '''
        def another_generated_function(arg1: float) -> float:
            '''
            the generated function specialized by its generator

            **args**

                - arg1: is the one and only argument

            **returns**

                - a number
            '''
            return arg1*param1 - param2

        return another_generated_function

    return a_2nd_function_generator


def a_class_generator(param3: float) -> Callable:
    '''
    generates a class

    **args**

        - param3: influences initialization of generated class

    **returns**

        - a generated class
    '''
    class a_generated_class(object):
        '''
        the generated class
        '''

        def __init__(self, a: float):
            self.a = a/param3

    return a_generated_class
