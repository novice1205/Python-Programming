class Sample:
    def __init__(self):
        print("lalalala")
    def __del__(self):
        print("destroying...................")


s = Sample()

s.__del__()

