class PushSaveDispatcher:
    def __init__(self):
        self._subscribers = []

    def add_subscriber(self, subscriber: object) -> None:
        self._subscribers.append(subscriber)

    def dispatch_save(self, state: map) -> None:
        for subscriber in self._subscribers:
            subscriber.dump_saves(state)
