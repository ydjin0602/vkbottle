from abc import ABC, abstractmethod
from .views import ABCView
from .middlewares import BaseMiddleware
from typing import List, Dict, Callable, Type, NoReturn, Any
from vkbottle.api.abc import ABCAPI


class ABCRouter(ABC):
    """ Abstract Router
    Documentation:
    """

    views: Dict[str, "ABCView"]
    middlewares: List["BaseMiddleware"]

    @abstractmethod
    async def route(self, event: dict, ctx_api: "ABCAPI"):
        pass

    def add_view(self, name: str, view: "ABCView") -> NoReturn:
        self.views[name] = view

    def add_middleware(self, middleware: "BaseMiddleware") -> NoReturn:
        self.middlewares.append(middleware)

    def view(self, name: str) -> Callable[..., Type["ABCView"]]:
        def decorator(view: Type["ABCView"]):
            self.add_view(name, view())
            return view

        return decorator

    def middleware(self) -> Callable[..., Type["BaseMiddleware"]]:
        def decorator(middleware: Type["BaseMiddleware"]):
            self.add_middleware(middleware())
            return middleware

        return decorator
