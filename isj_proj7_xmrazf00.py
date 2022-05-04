#!/usr/bin/env python3

# Decorator factory
def log_and_count(*args1, **kwargs1):
    # Decorator
    def decorating(fn):
        # Inner decorator
        def inner(*args2, **kwargs2):
            if "key" in kwargs1:
                kwargs1["counts"][kwargs1["key"]] += 1
            elif args1:
                kwargs1["counts"][list(args1)[0]] += 1
            else:
                kwargs1["counts"][fn.__name__] += 1
            # Tisk konecneho formatovaneho retezce
            print("called {0} with {1} and {2}".format(fn.__name__, args2, kwargs2))
            return fn(*args2, **kwargs2)
        return inner
    return decorating
