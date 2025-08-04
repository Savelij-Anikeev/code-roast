from ..core.lib.extension import Extension

from ..core.config import settings

class ConfigExtension(Extension):
    def init(self):
        self.instance = settings

    def action(self):
        return self.instance
