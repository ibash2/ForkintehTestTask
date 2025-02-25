from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import (
    Any,
    Generic,
    TypeVar,
)

from domain.events.base import BaseEvent
# from infrastructure.message_brokers.base import BaseMessageBroker


ET = TypeVar("ET", bound=BaseEvent)
ER = TypeVar("ER", bound=Any)


@dataclass
class IntegrationEvent(BaseEvent, ABC): ...


@dataclass
class EventHandler(ABC, Generic[ET, ER]):
    # message_broker: BaseMessageBroker
    # broker_topic: str

    @abstractmethod
    def handle(self, event: ET) -> ER: ...
