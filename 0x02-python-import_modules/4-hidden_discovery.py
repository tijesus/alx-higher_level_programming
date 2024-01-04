#!/usr/bin/python3

if __name__ == "_main_":
    """Print all the names in hidden modulese"""
    import hidden_4

    names = dir(hidden_4)

    for name in names:
        if name[:2] != "__":
            print(name)