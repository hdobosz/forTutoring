## Feat 1. What is a class method called?

Select one option from the list

- There is no such term in OOP
- Variables and functions inside a class
- Any (non-static) function declared inside a class
- Any variable declared within a class

## Feat 2. What are called class attributes?

Select one option from the list

- Only class variables
- Only class methods
- Instances (objects) of a class
- Variables and method names (references to methods) of a class

## Feat 3. What role does the self parameter play in class methods?

Select one option from the list

- this is a reference to the current class method
- this is a reference to the class that the method belongs to
- it's just a required (reserved) parameter for class methods through which arbitrary data can be passed
- is a reference to the class object from which the method was called

## Feat 4. Declare a class named MediaPlayer with two methods:

- open(file) - to open a media file named file (creates a local property filename with the value of the file argument in
  the object of the MediaPlayer class)
- play() - to play a media file (displays the string "Playing <media file name>")

Create two instances of this class named media1 and media2. Call the open() method from them with the argument "
filemedia1" for media1 and "filemedia2" for media2.
Then call the play() method through the objects. At the same time, two lines should be displayed on the screen (without
quotes):

- "Playback filemedia1"
- "Playback filemedia2"

## Feat 5. Declare a class named Graph and methods:

- set_data(data) - transferring the data set for subsequent display (data - list of numeric data);
- draw() - display the data (in the same order as in the data list)

and attribute:

- LIMIT_Y = [0, 10]

The set_data() method must form the local data property of the Graph class object.
The data attribute must refer to the list passed to the method.
The draw() method must display the list as a string of space-separated numbers that belong to the specified range of the
LIMIT_Y attribute (bounds included).

Create a graph_1 object of the Graph class, call the set_data() method on it, and pass in the list:

- [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]

Then, call the draw() method through the graph_1 object.
A line should appear on the screen with the corresponding set of numbers written with a space.
For example (output without quotes):

- "10 0 2 5 7"

## Feat 6. There is the following class:

```py
class Exercises:
    def next_task(self):
        return "Next task"
```

And an object of this class is created:

- my_st = stepik()

Select all correct options for calling the next_task() method
Select all correct options from the list:

- Stepik.my_st.next_task()
- next_task(my_st)
- Stepik.next_task(my_st)
- my_st.next_task(Stepik)
- next_task(Stepik)
- my_st.next_task()

## Feat 7. There is the following class for reading information from the input stream:

```py
import sys


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # read a list of strings from the input stream
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res
```

Which, then, can be used as follows:

```
sr = StreamReader()
data, result = sr.readlines()
```

It is necessary to declare another StreamData class with the method before the StreamReader class:

```py
def create(self, fields, lst_values): ...
```

which would receive the FIELDS tuple from the names of local attributes (passed to the fields attribute) and the list of
lst_in strings (passed to the lst_values attribute) as input and would form local properties in the StreamData class
object with field names from fields and corresponding values from lst_values.
If the creation of local properties succeeds, then the create() method returns True, otherwise False. If the number of
fields and the number of rows do not match, then the create() method returns False and no local attributes need be
created.

P.S. In the program, only the StreamData class needs to be additionally declared. Nothing more needs to be done.

Sample Input:

10
Python - the basics of craftsmanship
512

## Feat 8. A class is declared in the program:

```py
class String:
     is_empty = False
``` 

And then two instances of it are created:

```py
s1 = String()
s2 = String()
```

After that, the command is executed:

```py
s2.is_empty = True
```

Select the correct statements related to this program
(there are 4 right):

- The last command will create a local property is_empty with a value of True on the s2 instance
- The variable b = s2.is_empty will refer to the local attribute is_empty of the object s2
- The variable a = s1.is_empty will refer to the is_empty attribute of the String class
- The values s1.is_empty and s2.is_empty will be the same and set to True
- The last command will change the is_empty attribute of the String class to True
- Value s1.is_empty will still be False and s2.is_empty will be new True

## Feat 9. Rows of data are read from the input stream using the command:

```py
lst_in = list(map(str.strip, sys.stdin.readlines())) # read a list of lines from the input stream
```

in the format: id, name, old, salary (written with a space). For example:

- 1 John 35 120000
- 2 Bob 23 12000
- 3 Ivan 13 1200

That is, each line is an element of the lst_in list.

Needed in the DataBase class:

```py
class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
```

add two methods. First method:

insert(self, data) - to add new data to the end of the lst_data list from the passed list of data strings. In this case,
each element in the lst_data list must be represented by a dictionary in the format:

{'id': 'number', 'name': 'name', 'old': 'age', 'salary': 'salary'}

For example, the string "1 Sergey 35 120000" should be converted to a dictionary:

{'id': '1', 'name': 'John', 'old': '35', 'salary': '120000'}

and only after that it is added to the lst_data list. And so for all rows from the data list passed to the insert ()
method.

Second method:

select(self, a, b) - to return a new list from the elements of the existing list lst_data in the index range [a; b] (
inclusive) (not id, but list indexes). Keep in mind that the bound b may exceed the length of the list.

Note: In this problem, the number of elements per line (separated by a space) is always the same as the number of fields
in the FIELDS collection.

P.S. Your task is only to add two methods to the DataBase class.

sample input:

- 1 John 35 120000
- 2 Bob 23 12000
- 3 Ivan 13 1200

```py
import sys

# do not change the program, just add two methods
lst_in = list(map(str.strip, sys.stdin.readlines())) # read a list of lines from the input stream


class DataBase:
     lst_data = []
     FIELDS = ('id', 'name', 'old', 'salary')

     # add methods here


db = DataBase()
db.insert(lst_in)
```

## Feat 10. A Translator class is given (for translating from English into German), in which three methods are declared:

```py
class Translator:
     def add(self, eng, de):
         if 'tr' not in self.__dict__:
             self.tr = {}

         self.tr.setdefault(eng, [])
         # continue the add method here

     def remove(self, eng):
         # continue the remove method here

     def translate(self, eng):
         # continue the translate method here
```

An object of this class should store links between English and German words locally (in the tr attribute) in the form of
the following dictionary:

```py
{'<English word>': [<one or more German words>], ...}
```

Methods should do the following:

- add(self, eng, de) - to add a new pair of English and German words to the dictionary (if the English word already
  exists, then the new German word is added as a synonym for the translation, for example, go - go, walk, go); if the
  link eng-de already exists, then you don't need to add it a second time, for example: add('go', 'go'), add('go', '
  go');
- remove(self, eng) - to remove a link from the dictionary by the specified English word;
- translate(self, eng) - for translating from English into German (the method should return a list of German words
  corresponding to the translation of an English word, even if there is only one word in the list).

All additions and deletions of bindings must be performed within each specific object of the Translator class, i.e.
bindings are stored locally inside instances of the Translator class using a dictionary collection. (There is no need to
store bindings directly in the `__dict__` collection!)

Create an instance `tr` of the `Translator` class and call the `add` method on the following bindings:

```
tree - Baum
car - Auto
car - Wagen
leaf - Blätter
river - Fluss
go - gehen
go - fahren
go - laufen
milk - Milch
```

Then, using the `remove()` method, remove the link for the English word `car`. Use the `translate()` method to translate
the word `go`. Print the result on the screen as a string of all German words associated with the word `go`:

```py
class translator:
     def add(self, eng, de):
         if 'tr' not in self.__dict__:
             self.tr = {}

         self.tr.setdefault(eng, [])
         # continue the add method here

     def remove(self, eng):
         # continue the remove method here

     def translate(self, eng):
         # continue the translate method here


# here create an object of class Translator
```

Output in the format (for example word `go`): gehen fahren laufen