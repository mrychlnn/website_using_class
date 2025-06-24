from abc import ABC, abstractmethod

class BaseWebPage(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass