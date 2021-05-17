from dubbo.utils import DubboClient


class BaseService:
    """基础服务"""

    def __init__(self):
        self.dubbo_client = DubboClient("211.103.136.244", 6502)
