import json
import logging
from datetime import datetime
import os
from scrapy import signals

from fake_useragent import UserAgent

logger = logging.getLogger("django")


class EnvironmentIP:
    _env = None

    def __init__(self):
        self.IP = 0

    # 单例模式
    @classmethod
    def get_instance(cls):
        if EnvironmentIP._env is None:
            cls._env = cls()

        return cls._env

    def set_ip(self, IP):
        self.IP = IP

    def get_ip(self):
        return self.IP


# 可切换使用的代理
env_var_ip = EnvironmentIP()


class EnvironmentFlag:

    _env = None

    def __init__(self):
        self.falg = False

    # 单例模式
    @classmethod
    def get_instance(cls):
        if EnvironmentFlag._env is None:
            cls._env = cls()

        return cls._env

    def set_flag(self, flag):
        self.falg = flag

    def get_flag(self):
        return self.flag


env_var_flag = EnvironmentFlag()


class Environment:

    _env = None

    def __init__(self):
        self.count_time = datetime.now()

    # 单例模式
    @classmethod
    def get_instance(cls):
        if Environment._env is None:
            cls._env = cls()

        return cls._env

    def set_count_time(self, count_time):
        self.count_time = count_time

    def get_count_time(self):
        return self.count_time


env_var = Environment()


class RandomUserAgent:
    @classmethod
    def from_crawler(cls, crawler):

        s = cls()

        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)

        return s

    def process_request(self, request, spider):

        ua = UserAgent()

        request.headers.update({"User-Agent": ua.random})

        return None

    def process_response(self, request, response, spider):
        html = response.body.decode("utf-8")

        try:
            if html.find("code") != -1:
                return response

        except Exception as e:

            logger.exception("网络不好，正在重新请求", e)

        try:

            temp = json.loads(html)

            if temp["code"] == 406:
                return request  # 重新发给调度器，重新请求

        except Exception as e:

            logger.exception("请求失败", e)

        return response


class ProxyMiddleware:
    def __init__(self) -> None:

        from redis import StrictRedis, ConnectionPool

        pool = ConnectionPool(host=os.environ.get("REDIS_HOST_SPIDER"), port=6379)

        self.redis = StrictRedis(connection_pool=pool)

    @classmethod
    def from_crawler(cls, crawler):

        s = cls()

        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)

        return s
