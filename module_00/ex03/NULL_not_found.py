def NULL_not_found(object: any) -> int:
    object_type = object.__class__

    types_names = {
        type(None): "Nothing: None",
        float: "Cheese: nan",
        int: "Zero: 0",
        str: "Empty:",
        bool: "Fake: False"
    }

    # print 'none type'

    # 'not' covers all none cases but floats;
    # for floats we compare the object with itself
    if not object or (object != object):
        print(f"{types_names.get(object_type)} {object_type}")
        return (0)
    else:
        print("Type not Found")
        return (1)
