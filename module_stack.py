class Stack:
    """
    isEmpty - проверка стека на пустоту. Метод возвращает True или False.
    push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    size - возвращает количество элементов в стеке.
    """

    def __init__(self):
        self.stack = []

    def is_Empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_Empty():
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        if self.is_Empty():
            return
        return self.stack[-1]

    def size(self):
        return len(self.stack)



