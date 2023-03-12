from decorator import decorator


@decorator
def surprise(*args, **kwargs):
    """Decorator that replaces the decorated function with a 'surprise!' print statement."""
    print("surprise!")


@decorator
def execute_twice(func, *args, **kwargs):
    """Decorator that executes the decorated function twice when it is called."""
    func(*args)
    func(*args)


