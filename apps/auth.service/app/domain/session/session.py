class Session:
    def __init__(self, props):
        self.props = props

    @staticmethod
    def of(data):
        return Session(data)