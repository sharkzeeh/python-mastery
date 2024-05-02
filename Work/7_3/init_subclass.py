class Philosopher:
    def __init_subclass__(cls, **kwargs):
        # super().__init_subclass__(**kwargs)   # does nothing in this example
        print(f"Called __init_subclass({cls})")
        if 'default_name' in kwargs:    # overrides cls.default_name
            cls.default_name = kwargs['default_name']
            print(f'Changed cls.default_name to {cls.default_name}')

class AustralianPhilosopher(Philosopher, default_name="Bruce"):
    pass

class GermanPhilosopher(Philosopher, default_name="Nietzsche"):
    default_name = "Hegel"
    print("Set name to Hegel")


if __name__ == '__main__':
    Bruce = AustralianPhilosopher()
    print(Bruce.default_name)

    Mistery = GermanPhilosopher()
    print(Mistery.default_name)
