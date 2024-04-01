# Context Managers

# For resources, consider the use of the 'with' 
# statement instead of relying on __del__()
# Allows you to customize entry/exit steps

# with obj as val: ... > val = obj.__enter__()
    # statements
    # statements
    # statements
                #  ... > obj.__exit__(type, value, traceback)

class Manager:
    def __enter__(self):
        print('Entering')
        return self
    def __exit__(self, type, value, traceback):
        print('Leaving')
        if type:
            print('An exception occured')


if __name__ == '__main__':
    m = Manager()
    with m:
        print('Hello world')
    # Entering
    # Hello World
    # Leaving
