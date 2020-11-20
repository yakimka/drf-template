from typing import Type

from model_bakery import baker


class CycleFactory:
    def __init__(self, factory: Type['Factory'], count: int):
        self.factory = factory
        self.count = count

    def __getattr__(self, name):
        if hasattr(self.factory, name):
            return lambda *args, **kwargs: [getattr(self.factory, name)(*args, **kwargs) for _ in
                                            range(0, self.count)]


class Factory:
    @classmethod
    def cycle(cls, count) -> CycleFactory:
        """
        Run given method X times:
            Factory.cycle(5).orderItem()  # gives 5 orders
        """
        return CycleFactory(cls, count)

    @classmethod
    def example_model(cls, **kwargs):
        return baker.make('example_app.ExampleModel', **kwargs)
