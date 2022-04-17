from abc import abstractmethod
from typing import Generic, List, Optional, TypeVar

# Type definition for Model
M = TypeVar('M')

# Type definition for Unique Id
K = TypeVar('K')

###############################
# Abstract Class for Services #
###############################
class ServiceMeta(Generic[M, K]):

  # Create a new instance of the Model
  @abstractmethod
  def create(self, instance: M) -> M:
    pass

  # Delete an existing instance of the Model
  @abstractmethod
  def delete(self, id: K) -> None:
    pass

  # Fetch an existing instance of the Model by it's unique Id
  @abstractmethod
  def get(self, id: K) -> M:
    pass

  # Lists all existing instance of the Model
  @abstractmethod
  def index(self, pageSize: Optional[int] = 100, startIndex: Optional[int] = 0) -> List[M]:
    pass

  # Updates an existing instance of the Model
  @abstractmethod
  def update(self, id: K, instance: M) -> M:
    pass
