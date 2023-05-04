import builtins
def all_thing_is_obj(object: any) -> int:

    match type(object):
        case builtins.list:
            print("list")
        case builtins.tuple:
            print("tuple")
        case builtins.dict:
            print("dict")
        case builtins.set:
            print("set")
        case builtins.str:
            print("string")
        case _:
            print("did not match any type")
    return(42)

