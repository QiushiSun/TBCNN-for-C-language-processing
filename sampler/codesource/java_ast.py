class JavaAST:

    name = None
    value = None
    child = []

    def __init__(self, name, value, child):
        self.name = name
        self.value = value
        self.child = child

    def children(self):
        # for convience of sampler
        return zip(self.child, self.child)
