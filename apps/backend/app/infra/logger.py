import logging

from ..core.lib.extension import Extension

class LoggerExtension(Extension):
    def init(self):
        self.instance = logging.getLogger("infra")

    def action(self):
        return self.instance
