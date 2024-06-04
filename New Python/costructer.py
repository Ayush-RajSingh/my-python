class person:

    def __init__(self) -> None:
        print("constructor called")
        pass
    def __del__(self):
        print("distructor called")

        p = person()