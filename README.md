# SoCo2
# Little German Language Interpreter `lgl_interpreter.py`

This Python module performs various operations based on a domain-specific language represented in JSON format. The operations range from arithmetic to class and data structure manipulations. Each operation is defined within a function, which collectively can execute more complex instructions defined in a JSON file provided as an input argument.

## Functions Overview
### Arithmetic Operations

- `do_addieren(args, env)`: Performs addition between two numbers.
- `do_absolutwert(args, env)`: Returns the absolute value of a number.
- `do_differenz(args, env)`: Calculates the difference between two numbers.
- `do_multiplizieren(args, env)`: Performs multiplication of two numbers.
- `do_dividieren(args, env)`: Divides one number by another, ensuring that division by zero does not occur.
- `do_power(args, env)`: Raises a number to the power of another.

### Output Operation

- `do_ausgeben(args, env)`: Outputs a value to the console.

### Class and Object Operations

- `do_funktion(args, env)`: Defines a function with parameters and a body to be called.
- `do_instanziieren(args, env)`: Creates an instance of a class with attributes and methods.
- `konstruieren(name, args, instance, env)`: Helper function for `do_instanziieren` that constructs a class instance with given arguments.
- `do_neue_klasse(args, env)`: Defines a new class with optional attributes, methods, a constructor, and inheritance.
- `do_setzen_klasse(args, env)`: Sets an attribute value in a class.
- `do_abrufen_klasse(args, env)`: Retrieves an attribute value from a class.
- `do_aufrufen_klasse(args, env)`: Invokes a class method.
- `find_class_method(name, method_name, env)`: Continuously searches for method name while the parent is still defined in object.

### Loop Operation

- `do_solange(args, env)`: Executes a loop as long as the given condition is true.

### Array Operations

- `do_array(args, env)`: Creates an array with a specified size and initializes it with given values.
- `get_index(args, env)`: Retrieves an element at a specific index in the array.
- `set_index(args, env)`: Sets a value at a specific index in the array.

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

- `do_abfolge(args, env)`: Executes a sequence of operations.

### Function Invocation Operation

- `do_aufrufen(args, env)`: Invokes a function with given arguments.

### The `do` Dispatch Function

- `do(expr, env)`: The core function that dispatches the execution based on the operation type specified in the expression.

### Main Execution Function

- `main()`: The entry point of the program that reads a JSON file as input, parses it as a list of operations, and executes the program.

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

This Python script reads a trace file, calculates durations for each event, and generates a report summarizing the functions' performance statistics.

### Script Components

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

To run the script, use the following command:

`python reporting.py trace_file.log`




