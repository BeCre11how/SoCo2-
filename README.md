# SoCo2 - README for `lgl_interpreter.py` and `reporting.py`

# Little German Language Interpreter `lgl_interpreter.py`

A python script that performs various operations based on a specific language represented in JSON format.
The operations range from arithmetic  to class and data structure manipulation. Every operation is defined as a function, which combined can execute complex instructions from a JSON file provided in the command-line argument as input.

## Functions Overview
Here a list of all the functions with their corresponding is description is given. A number can also be a call to a different or recursive function that returns a number.

### Arithmetic Operations
- `do_addieren(args, env)`: Returns the addition of two numbers.
- `do_absolutwert(args, env)`: Returns the absolute value of a number.
- `do_differenz(args, env)`: Returns the difference of two numbers.
- `do_multiplizieren(args, env)`: Returns the multiplication of two numbers.
- `do_dividieren(args, env)`: Returns the division of one number by another and ensures that division by zero does not occur.
- `do_power(args, env)`: Returns a number to the power of another.

### Output Operation
- `do_ausgeben(args, env)`: Outputs a value to the console, commonly known as print-statement.

### Class and Object Operations
- `do_funktion(args, env)`: Defines a function with parameters and a body to be called.
- `do_instanziieren(args, env)`: Creates an instance of a class with its corresponding attributes and methods.
- `konstruieren(name, args, instance, env)`: Helper function for `do_instanziieren` that constructs a class instance with given arguments.
- `do_neue_klasse(args, env)`: Defines a new class with optional attributes, methods, a constructor, and inheritance.
- `do_setzen_klasse(args, env)`: Sets an attribute value in a class.
- `do_abrufen_klasse(args, env)`: Retrieves an attribute value from a class.
- `do_aufrufen_klasse(args, env)`: Invokes a class method.
- `find_class_method(name, method_name, env)`: Continuously searches for the method name while the parent is still defined in an object.

### Loop Operation
- `do_solange(args, env)`: Executes a loop as long as the given condition is true. Commonly known as while-loop.

### Array Operations
- `do_array(args, env)`: Creates an array with a specified size and initializes it with given values.
- `get_index(args, env)`: Retrieves an element at a specific index in an array.
- `set_index(args, env)`: Sets a value at a specific index in an array.

### Dictionary Operations
- `do_dictionary(args, env)`: Creates a dictionary with operations to get, set, and merge entries.
- `get_keyval(args, env)`: Retrieves a value for a given key in the dictionary.
- `set_keyval(args, env)`: Sets a value for a given key in the dictionary.
- `merge_dict(args, env)`: Merges two dictionaries.

### Variable Operation
- `do_setzen(args, env)`: Sets a variable in the environment.

### Retrieval Operation
- `do_abrufen(args, env)`: Retrieves a value from the environment or the current function's local frame.

### Sequence Operation
- `do_abfolge(args, env)`: Executes a sequence of operations and allows for multiple functions to be run after one another.

### Function Invocation Operation
- `do_aufrufen(args, env)`: Invokes a function with given arguments.

### The `operations` variable
- `operations`: Detects all methods in the script starting with `do_` and adds them to a dictionary ready to be called by the `do` function.

### The `do` Dispatch Function
- `do(expr, env)`: The core function of the script that handles the execution of the functions listed in the `operations` variable or allows for the definition of new operations in the language file.

### Main Execution Function
- `main()`: The entry point of the script that reads a JSON file as input, parses it as a list of operations, executes the program and allows for optional tracing for a log-file.

## Usage
To execute a program written in the custom JSON-based language, run the following command (replace filename.gsc with your filename):

`python lgl_interpreter.py filename.gsc` 

To execute the program with tracing enabled use (replace filename.gsc with your filename, trace_file.log with your log file name):
`python lgl_interpreter.py filename.gsc --trace trace_file.log` 

The JSON file should define a list of operations in the form:

[
    ["operation", "argument1", "argument2", ...],
    ...
]

# Reporting for Little German Language Interpreter `reporting.py`

## Overview
This Python script reads a trace file, output by the `lgl_interpreter.py` when run with tracing enabled. It calculates durations for each event, and generates a report summarizing the functions' performance statistics:
- `Function name`
- `Number of calls`
- `Total time per function`
- `Average time per function`

## Functions Overview
### Reading function
- `read_trace_file(trace_file_path)`: Reads the trace file specified by trace_file_path and returns a list of events.

### Calculation function
- `calculate_durations(trace_events)`: Calculates the duration of each event and returns a list of dictionaries containing event id, function name, and duration.

### Sorting function
- `sort_functions_by_name(event_durations)`: Sorts the events by function name and calculates statistics (number of calls, total time, average time) for each function and returns a list of lists containing function name, number of calls, total time, and average time.

### Printing function
- `print_report(stats)`: Prints a formatted report of function statistics.

### Main Execution Function
- `main(trace_file_path)`: Entry point to the script. Calls the above functions in sequence and prints the final report.

## Usage
To run the script, use the following command (replace trace_file.log with your log file name):

`python reporting.py trace_file.log`




