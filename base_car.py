from abc import ABC, abstractmethod

# 【抽象類別(介面) 1】測試
class CarInterface(ABC):
    """抽象類別(介面)"""

    @abstractmethod
    def get_price(self):
        min_price = min(self.__models)
        return min_price

    @abstractmethod
    def get_model(self):
        pass
    
    @abstractmethod
    def get_spec(self):
        pass