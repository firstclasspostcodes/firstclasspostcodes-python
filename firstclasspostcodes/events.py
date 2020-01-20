class Events:
    def __init__(self):
        self.events = {}

    def on(self, event_name, handler):
        if event_name not in self.events:
            self.events[event_name] = []
        self.events[event_name].append(handler)
        handler_id = len(self.events[event_name]) - 1
        return handler_id

    def off(self, event_name, handler_id):
        if event_name in self.events and handler_id in self.events[event_name]:
            del self.events[event_name][handler_id]
            return True
        return False

    def emit(self, event_name, *args, **keywargs):
        for handler in self.events[event_name]:
            handler(*args, **keywargs)
