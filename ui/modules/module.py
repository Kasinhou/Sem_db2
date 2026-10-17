from abc import ABC, abstractmethod

class Module(ABC):
    def __init__(self, root):
        self.root = root
        self.values = []
        self.selected = False
        self.des = []

    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def edit(self,tree):
        pass
    @abstractmethod
    def delete(self):
        pass
    @abstractmethod
    def load(self):
        return self.values