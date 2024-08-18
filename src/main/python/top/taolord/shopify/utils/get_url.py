import requests
import json

from top.taolord.jet.common import YamlRead


class GetUrl:
    def __init__(self, ):
        self.yamlRead = YamlRead()
        self.proxy = self.yamlRead.read_yaml('keygen.req.proxy')

    def getUrl(self, url: str) -> str:
        """
        请求目标地址
        :param url: 地址
        :return:  返回请求参数
        """
        try:
            req = requests.get(url=url)
            req.encoding = "utf-8"
            urlLabelText = req.text
            return urlLabelText
        except Exception as e:
            print(f"getUrl：请求:{url}。失败开启轮调", )
            print(f"getUrl：{e}", )
            self.getUrl(url)

    def getUrlHeaders(self, url: str, headers: dict) -> str:
        """
        请求目标地址
        :param headers: 请求头
        :param url: 地址
        :return:  返回请求参数
        """
        try:
            req = requests.get(url=url, headers=headers)
            req.encoding = "utf-8"
            urlLabelText = req.text
            return urlLabelText
        except Exception as e:
            print(f"getUrlHeaders：请求:{url}。失败开启轮调", )
            print(f"getUrlHeaders：{e}", )
            self.getUrlHeaders(url, headers)

    def getUrlProxies(self, url: str, headers: dict, proxies: dict) -> str:
        """
        请求目标地址
        :param proxies: 代理
        :param headers: 请求头
        :param url: 地址
        :return:  返回请求参数
        """
        try:
            req = requests.get(url=url, headers=headers, proxies=proxies)
            req.encoding = "utf-8"
            urlLabelText = req.text
            return urlLabelText
        except Exception as e:
            print(f"getUrlProxies：请求:{url}。失败开启轮调", )
            print(f"getUrlProxies：{e}", )
            self.getUrlProxies(url, headers, proxies)

    def getUrlVpn(self, url: str) -> str:
        """
        请求目标地址
        :param url: 地址
        :return:  返回请求参数
        """
        try:
            req = requests.get(url=url, proxies=self.proxy)
            req.encoding = "utf-8"
            urlLabelText = req.text
            return urlLabelText
        except Exception as e:
            print(f"getUrl：请求:{url}。失败开启轮调", )
            print(f"getUrl：{e}", )
            self.getUrlVpn(url)

    def getUrlHeadersVpn(self, url: str, headers: dict) -> str:
        """
        请求目标地址
        :param headers: 请求头
        :param url: 地址
        :return:  返回请求参数
        """
        try:
            req = requests.get(url=url, headers=headers, proxies=self.proxy)
            req.encoding = "utf-8"
            urlLabelText = req.text
            return urlLabelText
        except Exception as e:
            print(f"getUrlHeaders：请求:{url}。失败开启轮调", )
            print(f"getUrlHeaders：{e}", )
            self.getUrlHeadersVpn(url, headers)

    def postUrlVpn(self, url: str, data: dict, headers: dict) -> str:
        """
        请求目标地址
        :param headers: 请求头
        :param data: 请求参数
        :param url: 地址
        :return:  返回请求参数
        """
        try:
            req = requests.post(url, data=json.dumps(data), headers=headers, proxies=self.proxy)
            req.encoding = "utf-8"
            urlLabelText = req.text
            return urlLabelText
        except Exception as e:
            print(f"getUrl：请求:{url}。失败开启轮调", )
            print(f"getUrl：{e}", )
            self.getUrl(url)
