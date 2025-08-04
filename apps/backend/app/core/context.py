class Context:
    def __init__(self, props):
        for prop in ['user', 'metadata', 'session']:
            val = props if props.get(prop, None) else None

            self.__setattr__(prop, val)

