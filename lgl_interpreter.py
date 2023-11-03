# conten: a python file implementing the interpreter of the LGL 2 language, as described in the 3 exercises below

import sys
import json


# Basil ish schwul
def do_addieren(args, env):
    assert len(args) == 2
    return do(args[0], env) + do(args[1], env)


def do_absolutwert(args, env):
    assert len(args) == 1
    return abs(do(args[0], env))


def do_differenz(args, env):
    assert len(args) == 2
    return do(args[0], env) - do(args[1], env)


def do_multiplizieren(args, env):
    assert len(args) == 2
    return do(args[0], env) * do(args[1], env)


def do_funktion(args, env):
    assert len(args) == 2
    return {
        "name": "funktion",
        "parameter": args[0],
        "aufruf": args[1],
        "local_frame": None,
    }


def do_dividieren(args, env):
    assert len(args) == 2
    right = do(args[1])
    assert right != 0
    return do(args[0], env) / right


def do_power(args, env):
    assert len(args) == 2
    return do(args[0], env) ** do(args[1], env)


def do_ausgeben(args, env):
    assert len(args) == 1
    print(do(args[0], env))


def do_instanziieren(args, env):
    assert len(args) >= 1
    assert isinstance(args[0], str)
    temp = env[args[0]]
    assert isinstance(temp, dict) and temp["name"].startswith("klasse_")
    res = {"parent": None}
    parent = temp["parent"]
    if parent is not None:
        #fix needed
        x = do(["instanziieren", env[parent]["konstruktor"], args], env)
        res["parent"] = x
    else:
        count = 1 + len(res["parent"])
        for x in temp["attributes"]:
            if count < len(args):
                res[x] = args[count]

    for name, func in temp["funktionen"]:
        res[name] = func
    return res

def do_neue_klasse(args, env):
    assert len(args) > 0
    assert isinstance(args[0], str)
    c = True
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
                elif curr[0] == "konstruktor" and c:
                    temp["konstruktor"] = curr
                    c = False
                else:
                    temp["funktionen"].append((curr[0], curr[1:]))
            else:
                assert isinstance(curr, str)
                temp["attribute"].append(curr)
    env[args[0]] = temp


def do_solange(args, env):
    assert len(args) == 2
    while args[0]:
        do(args[1], env)

def do_wenn(args, env):
    assert len(args) == 3
    condition = do(args[0], env)
    if condition:
        return do(args[1], env)
    else:
        return do(args[2], env)
def get_index(args, env):
    assert len(args) == 2
    index = do(args[1], env)
    assert isinstance(index, int) and args[1] < env[args[0]["size"]] and index >= 0
    return env[args[0]["array"][index]]


def set_index(args, env):
    assert len(args) == 3
    index = do(args[1], env)
    assert isinstance(index, int) and args[1] < env[args[0]["size"]] and index >= 0
    env[args[0]["array"][index]] = do(args[2], env)


def do_array(args, env):
    assert len(args) == 1
    return {
        "name": "array",
        "size": do(args[0], env),
        "array": [],
        "get": get_index,
        "set": set_index,
    }


def do_dictionary(args, env):
    assert len(args) == 0
    return {
        "name": "dictionary",
        "dictionary": {},
        "get": get_keyval,
        "set": set_keyval,
        "merge": merge_dict,
    }


def do_setzen(args, env):
    assert len(args) == 2
    assert isinstance(args[0], str)
    env[args[0]] = do(args[1], env)

def do_setzen_klasse(args, env):
    assert(len(args)) == 3
    assert isinstance(args[0], str)
    assert isinstance(args[1], str)
    env[args[0]][args[1]] = do(args[2], env)
def do_abrufen_klasse(args, env):
    assert len(args) == 2
    assert isinstance(str,args[0])
    assert args[0] in env
    assert args[1] in env[args[0]]
    return env[args[0]][1]



# ToDo: pruefen ob in liste of local frames
def do_abrufen(args, env):
    assert len(args) == 1
    assert isinstance(args[0], str)
    assert args[0] in env or args[0] in env["local_frame_of"]
    return (
        do(env[args[0]], env)
        if args[0] in env
        else do(env["local_frame_of"][args[0]], env)
    )


def get_keyval(args, env):
    assert len(args) == 2
    assert args[0] in env
    key = do(args[1], env)
    return env[args[0]["dictionary"][key]]


def set_keyval(args, env):
    assert len(args) == 3
    assert args[0] in env
    key = do(args[1], env)
    env[args[0]["dictionary"][key]] = do(args[2], env)


def merge_dict(args, env):
    assert len(args) == 2
    d = do(args[0], env)
    od = do(args[1], env)
    assert isinstance(d, dict) and isinstance(od, dict)
    return d | od

# ToDo: aufrufen nested functions, ideas for putting functionscope in env , myb list of dictionaries
def do_aufrufen(args, env):
    assert len(args) >= 1
    name = args[0]
    arguments = args[1:]
    # eager evaluation
    values = [do(arg, env) for arg in arguments]
    func = env[name]
    assert isinstance(func, dict)
    assert func["name"] == "funktion"
    func_params = func["parameter"]
    assert len(func_params) == len(values)

    local_frame = dict(zip(func_params, values))
    curr = "local_frame_of"
    env[curr] = local_frame
    body = func["aufruf"]
    result = do(body, env)
    env[curr] = None

    return result


def do_abfolge(args, env):
    assert len(args) > 0
    for operation in args:
        result = do(operation, env)
    return result


def do_subtrahieren(args, env):
    assert len(args) == 2
    return do(args[0], env) - do(args[1], env)


operations = {
    name.replace("do_", ""): func
    for (name, func) in globals().items()
    if name.startswith("do_")
}
print(len(operations))

def do(expr, env):
    if isinstance(expr, int) or isinstance(expr, float) or isinstance(expr, tuple):
        return expr

    assert expr[0] in operations or expr[0].endswith("_new")
    return operations[expr[0]](expr[1:], env)


def main():
    assert len(sys.argv) == 2, "Usage: expr-demo.py filename.gsc"
    with open(sys.argv[1], "r") as source_file:
        program = json.load(source_file)
    assert isinstance(program, list)
    env = {}
    result = do(program, env)

    print(f"=> {env}")


if __name__ == "__main__":
    main()
