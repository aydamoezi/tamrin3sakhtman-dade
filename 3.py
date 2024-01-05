class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def add_term(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.exponent}", end=" ")
            current = current.next
        print()

# Example usage
p = Polynomial()
p.add_term(3, 2)
p.add_term(4, 1)
p.add_term(2, 0)
p.display()

