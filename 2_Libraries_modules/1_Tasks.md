## Exercise: Absolute Import
Create the following directory structure:
```plaintext
project/
├── main.py
└── mymodule/
    ├── __init__.py
    └── module1.py
```

In module1.py, define a function greet() that prints "Hello from module1".
In main.py, import and use the greet() function from module1.py.

## Exercise: Relative Import
Expand on the previous exercise's directory structure:
```plaintext
project/
├── main.py
└── mymodule/
    ├── __init__.py
    ├── module1.py
    └── subpackage/
        ├── __init__.py
        └── module2.py
```
In module2.py, define a function welcome() that prints "Welcome from module2".
In main.py, import and use the welcome() function using a relative import.


Hint:
Remember to always consider the context and structure of your project when choosing between absolute and relative imports.
Absolute imports start from the top-level package/module and are more stable in larger projects,
while relative imports are useful for importing from sibling or nested modules within the same package.

## Exercise: Nested Relative Imports
Create the following directory structure:
```plaintext
project/
├── main.py
└── mypackage/
    ├── __init__.py
    ├── module1.py
    └── subpackage/
        ├── __init__.py
        └── module2.py
```
In module1.py, define a function calculate() that returns the square of a given number.
In module2.py, import the calculate() function from module1.py using a relative import and use it to calculate the square of a number.
In main.py, import and use the calculate() function from module1.py using an absolute import.

use unix commands to build the directory structure, to practise and recap the unix commands from the fundamentals module.

## Exercise: Understanding Relative Imports

- Objective: Create a directory structure for a project named "Zoo". Within the Zoo project, there will be two main categories: Mammals and Birds. Each category will have two animals. For Mammals, we'll have "Lion" and "Elephant", and for Birds, we'll have "Eagle" and "Penguin". Each animal will have a function to make its respective sound.

Directory Structure:
```plaintext
zoo_project/
├── main.py
└── zoo/
    ├── __init__.py
    ├── mammals/
    │   ├── __init__.py
    │   ├── lion.py
    │   └── elephant.py
    └── birds/
        ├── __init__.py
        ├── eagle.py
        └── penguin.py
```

#### Tasks:

- In lion.py, define a function roar() that prints "Roar!".
- In elephant.py, define a function trumpet() that prints "Pawoo!".
- In eagle.py, define a function screech() that prints "Kreeee!".
- In penguin.py, define a function honk() that prints "Honk honk!".
- In the __init__.py inside the mammals folder, import the roar function from lion using a relative import.
- In main.py, use an absolute import to import and call the roar function.
Expected Outputs:

When you run main.py, it should print:

Roar!

# Homework
## Task 1: Simple Absolute Import with Virtual Environment
Directory Structure:
```plaintext
simple_project/
├── main.py
└── utilities/
    ├── __init__.py
    └── math_tools.py
```
Objective:

- Create a virtual environment using python -m venv myenv.
- Activate the virtual environment (source myenv/bin/activate on Unix/macOS, myenv\Scripts\activate on Windows).
- In math_tools.py, define two functions as previously described.
- In main.py, import both functions and print the results.

## Task 2: Nested Relative Import with Classes, Methods, and External Libraries
Directory Structure:
```plaintext
nested_project/
├── main.py
└── mylibrary/
    ├── __init__.py
    ├── shapes.py
    └── calculations/
        ├── __init__.py
        └── area_calculator.py
```

Objective:

- Create a virtual environment and activate it.
- Install a package (e.g., NumPy) using pip install numpy.
- Modify the shapes.py file to define a class Circle that uses NumPy to calculate the area of a circle.
- Complete the rest of the task as previously described.

## Task 3: Complex Project with Multiple Levels, Virtual Environment, and Multiple External Libraries
```plaintext
complex_project/
├── main.py
└── analytics/
    ├── __init__.py
    ├── data.py
    ├── processing/
    │   ├── __init__.py
    │   └── cleaner.py
    └── analysis/
        ├── __init__.py
        └── statistics.py
```

Objective:

- Create a virtual environment and activate it.
- Install multiple packages (e.g., Pandas, SciPy) using pip install pandas scipy.
- Modify data.py to simulate loading a dataset using Pandas.
- Modify statistics.py to use SciPy for statistical calculations.
- Complete the rest of the task as previously described.


## Bonus: Creating a Namespace Package
Bonus: Creating a Namespace Package
Create the following directory structure:
path1/
└── mynamespace/
    ├── module1.py
    └── module2.py
path2/
└── mynamespace/
    ├── module3.py
    └── module4.py

unify the namespace package and import all modules