###Imports
import json
import argparse
import csv
from datetime import datetime
from functools import wraps


konst_count = 0

###Define decorator for tracing
trace_setting = False
id_counter = 1

def trace_decorator(function):
    global trace_setting
    global id_counter
    if trace_setting:
        with open('trace_file.log', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'function_name', 'event', 'timestamp'])
            
    @wraps(function)
    def wrapper(*args, **kwargs):
        global trace_setting
        global id_counter
        if trace_setting:
            id = id_counter
            id_counter += 1
            with open('trace_file.log', mode='a', newline='') as file:
                writer = csv.writer(file)
                new_function_name = function.__name__[3:] if function.__name__.startswith("do_") else function.__name__
                writer.writerow([id,new_function_name, 'start', datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")])
                result = function(*args, **kwargs)
                writer.writerow([id,new_function_name, 'stop', datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")])
                return result
        else:
            return function(*args, **kwargs)
    return wrapper


###actual lgl_interpreter script
@trace_decorator
def do_addieren(args, env):
    assert len(args) == 2
    return do(args[0], env) + do(args[1], env)

@trace_decorator
def do_absolutwert(args, env):
    assert len(args) == 1
    return abs(do(args[0], env))

@trace_decorator
def do_differenz(args, env):
    assert len(args) == 2
    return do(args[0], env) - do(args[1], env)

@trace_decorator
def do_multiplizieren(args, env):
    assert len(args) == 2
    return do(args[0], env) * do(args[1], env)

@trace_decorator
def do_funktion(args, env):
    assert len(args) == 2
    return {
        "name": "funktion",
        "parameter": args[0],
        "aufruf": args[1],
    }

@trace_decorator
def do_dividieren(args, env):
    assert len(args) == 2
    right = do(args[1], env)
    assert right != 0
    return do(args[0], env) / right

@trace_decorator
def do_power(args, env):
    assert len(args) == 2
    value = do(args[0], env) 
    return value ** do(args[1], env) 

@trace_decorator
def do_ausgeben(args, env):
    assert len(args) == 1
    print(do(args[0], env))

@trace_decorator
def do_instanziieren(args, env):
    env["const_count"] = 0
    assert len(args) >= 1
    assert isinstance(args[0], str)
    class_name = args[0]
    class_definition = env[class_name]
    assert isinstance(class_definition, dict) and class_definition["name"].startswith(
        "klasse_"
    )

    instance = {"parent": None}

    for attribute in class_definition["attribute"]:
        instance[attribute] = None
    for name, func in class_definition["funktionen"]:
        instance[name] = func
    parent_class_name = class_definition["parent"]
    if parent_class_name is not None:
        parent_instance = do_instanziieren([parent_class_name, args[1]], env)
        instance["parent"] = parent_instance

    constructor = class_name in env[class_name + "_new"]
    
    if constructor:
        value = konstruieren(class_name, args[1:], instance, env)
        env["const_count"] += value

    return instance

@trace_decorator
def konstruieren(name, args, instance, env):
    count = 0
    args = args[0]

    for i in instance:
        if instance[i] is None and i != "parent":
            assert len(args) > 0, f"too few arguments for creation of {name}"
            value = do(args[count + env["const_count"]], env)
            instance[i] = value
            count += 1
    return count

@trace_decorator
def do_neue_klasse(args, env):
    assert len(args) > 0
    assert isinstance(args[0], str)
    cname = args[0] + "_new"
    temp = {
        "name": "klasse_" + args[0],
        "parent": None,
        "konstruktor": None,
        "attribute": [],
        "funktionen": [],
    }
    if len(args) > 1:
        for i in range(1, len(args)):
            curr = args[i]
            if isinstance(curr, list):
                assert isinstance(curr[0], str)
                if curr[0] == "parent":
                    assert curr[1] in env
                    temp["parent"] = curr[1]
                elif curr[0] == "konstruktor":
                    env[cname] = []
                    temp["konstruktor"] = do(curr[1], env)
                    for i in curr[1]:
                        if isinstance(i, list) and i[0] == "setzen_klasse":
                            env[cname].append(i[1].replace("klasse_", ""))
                else:
                    temp["funktionen"].append((curr[0], do(curr[1], env)))
            else:
                assert isinstance(curr, str)
                temp["attribute"].append(curr)
    env[cname].append(args[0])
    env[args[0]] = temp

@trace_decorator
def do_solange(args, env):
    assert len(args) == 2
    while eval(" ".join([str(do(val, env)) for val in args[0]])):
        do(args[1], env)

@trace_decorator
def get_index(args, env):
    assert len(args) == 2
    index = do(args[1], env)
    assert isinstance(index, int) and index < env[args[0]]["size"] and index >= 0
    return env[args[0]]["array"][index]

@trace_decorator
def set_index(args, env):
    assert len(args) == 2
    assert isinstance(args[1], list)
    l = [do(arg, env) for arg in args[1]]
    assert args[0] in env
    env[args[0]]["array"][l[0]] = l[1]

@trace_decorator
def do_array(args, env):
    assert len(args) >= 1
    assert len(args) - 1 <= args[0]
    return {
        "name": "array",
        "size": do(args[0], env),
        "array": [do(arg, env) for arg in args[1:]] if len(args) > 1 else [],
        "get": get_index,
        "set": set_index,
    }

@trace_decorator
def do_dictionary(args, env):
    assert len(args) >= 0
    return {
        "name": "dictionary",
        "dictionary": {
            do(args[i], env): do(args[i + 1], env) for i in range(0, len(args), 2)
        }
        if len(args) > 1
        else {},
        "get": get_keyval,
        "set": set_keyval,
        "merge": merge_dict,
    }

@trace_decorator
def do_setzen(args, env):
    assert len(args) == 2
    assert isinstance(args[0], str)
    env[args[0]] = do(args[1], env)

@trace_decorator
def do_setzen_klasse(args, env):
    assert (len(args)) == 3
    assert isinstance(args[0], str)
    assert isinstance(args[1], str)
    env[args[0]][args[1]] = do(args[2], env)

@trace_decorator
def do_abrufen_klasse(args, env):
    assert len(args) == 2
    name = do(args[0],env)
    para = do(args[1], env)
    assert isinstance(name, str)
    assert isinstance(para, str)
    assert name in env
    assert para in env[name]
    
    return env[name][para]

@trace_decorator
def do_aufrufen_klasse(args, env):
    assert len(args) >= 2
    classname = args[0]
    methodname = find_class_method(classname, args[1], env)
    assert methodname is not None
    if isinstance(methodname, dict):
        arguments = args[2:]
        values = [do(arg, env) for arg in arguments]
        
        assert isinstance(methodname, dict)
        assert methodname["name"] == "funktion"
        func_params = methodname["parameter"]
        assert len(func_params) == len(values)

        local_frame = dict(zip(func_params, values))
        curr = "local_frame_of_class"
        env[curr] = local_frame
        body = methodname["aufruf"]
        result = do(body, env)
        env[curr] = ""

    else:
        assert len(args) == 3
        result = methodname([classname, args[2]], env)
    return result



# ToDo: pruefen ob in liste of local frames
@trace_decorator
def do_abrufen(args, env):
    assert len(args) == 1
    assert isinstance(args[0], str)
    assert args[0] in env or args[0] in env["local_frame_of"] or args[0] in env["local_frame_of_class"]
    
    return (
        do(env[args[0]], env)
        if args[0] in env 
        else do(env["local_frame_of"][args[0]], env) if args[0] in env["local_frame_of"]
        else do(env["local_frame_of_class"][args[0]], env)
    )

@trace_decorator
def get_keyval(args, env):
    assert len(args) == 2
    assert args[0] in env
    key = do(args[1], env)
    return env[args[0]]["dictionary"][key]

@trace_decorator
def set_keyval(args, env):
    assert len(args) == 2
    assert isinstance(args[1], list)
    l = [do(arg, env) for arg in args[1]]
    assert args[0] in env
    env[args[0]]["dictionary"][l[0]] = l[1]

@trace_decorator
def merge_dict(args, env):
    assert len(args) == 2
    d = do(args[1][0], env)
    od = do(args[1][1], env)

    assert isinstance(d, dict) and isinstance(od, dict)

    return d | od


# ToDo: aufrufen nested functions, ideas for putting functionscope in env , myb list of dictionaries
@trace_decorator
def do_aufrufen(args, env):
    assert len(args) >= 1
    name = do(args[0], env) if isinstance(args[0], list) else args[0]
    arguments = args[1:]
    values = [do(arg, env) for arg in arguments]
    func = env[name] if isinstance(name, str) else name
    

    assert isinstance(func, dict)
    assert func["name"] == "funktion"

    func_params = func["parameter"]

    assert len(func_params) == len(values)

    local_frame = dict(zip(func_params, values))
    curr = "local_frame_of"
    env[curr] = local_frame
    body = func["aufruf"]
    result = do(body, env)
    env[curr] = ""
    return result

@trace_decorator
def find_class_method(name, method_name, env):
    if method_name in env[name]:
        return env[name][method_name]
    if "parent" not in env[name]:
        return None
    curr = env[name]["parent"]
    while curr is not None and method_name not in curr:
        curr = curr["parent"]
    return curr[method_name] if curr is not None else None

@trace_decorator
def do_abfolge(args, env):
    assert len(args) > 0
    for operation in args:
        result = do(operation, env)
    return result


operations = {
    name.replace("do_", ""): func
    for (name, func) in globals().items()
    if name.startswith("do_")
}


def do(expr, env):
    if (
        isinstance(expr, int)
        or isinstance(expr, float)
        or isinstance(expr, tuple)
        or isinstance(expr, str)
    ):
        return expr

    assert expr[0] in operations or expr[0].endswith("_new")
    start = datetime.now()
    result = operations[expr[0]](expr[1:], env) if expr[0] in operations else do_instanziieren([expr[0].replace("_new", ""), expr[1:]], env)
    return result


###Entry point to script
def main():
    parser = argparse.ArgumentParser(description="Interpret .gsc files with optional tracing.")
    parser.add_argument("filename", type=str, help="The .gsc file to interpret")
    parser.add_argument("--trace", type=str, help="Enable tracing and specify the trace file.")
    args = parser.parse_args()

    global trace_setting
    if args.trace:
        trace_setting = True
        # If tracing is enabled, write the header to the log file.
        with open('trace_file.log', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'function_name', 'event', 'timestamp'])
        
    with open(args.filename, "r") as source_file:
        program = json.load(source_file)
    assert isinstance(program, list)
    env = {}
    env["local_frame_of"] = ""
    env["local_frame_of_class"] = ""
    result = do(program, env)
    print(f"=> {result}")

if __name__ == "__main__":
    main()
