class Node:
    def __init__(self, value, state, children = []):
        self.value = value
        self.children = children
        self.state = state

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, list_of_children):
        for child in list_of_children:
            self.add_child(child)