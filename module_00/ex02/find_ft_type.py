def all_thing_is_obj(object: any) -> int:
    object_type = object.__class__  # or type(object)
    types = {
        str: "String",
        list: "List",
        set: "Set",
        dict: "Dict",
        tuple: "Tuple"
    }

    # print object type if found

    # specail formatting for strings
    if (object_type == str):
        print(f"{object} is in the kitchen: {object_type}")
    # type not defined in the map
    elif not types.get(object_type):
        print("Type not found")
    else:
        print(f"{types[object_type]} : {object_type}")

    return (42)
