import logging

from ..core.protocols.extension import Extension

class LoggerExtension(Extension):
    def init(self):
        self.instance = logging.getLogger("infra")

    def action(self):
        return self.instance
