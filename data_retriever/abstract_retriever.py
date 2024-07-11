
from abc import ABC, abstractmethod

class DataRetriever(ABC):

    def __init__(self, llm, data_repo):
        self.llm = llm
        self.data_repo = data_repo

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_data(self, atomic_query):
        pass

    def process_query(self, atomic_query):
        if self.data_repo.contains_data(atomic_query):
            return self.data_repo.get_data(atomic_query)
        else:
            return get_data(atomic_query)
