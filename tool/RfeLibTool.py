# encoding=utf-8
import re
import base64
from jsonpath_rw import parse
import hashlib
import time
import uuid
import random
import os
from unittest.util import safe_repr


class RfeLibTool:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = '1.0'
    ROBOT_LIBRARY_DOC_FORMAT = 'TEXT'

    def __init__(self):
        pass

    def getValueFromJson(self, str_json, jsonpath):
        """
        获取json中某个key对应的value \n
        :param str_json: str json \n
        :param jsonpath: str jsonpath \n
        :return: obj 通过jsonpath在json中得到的value 可能是 int str obj ...\n
        """
        jsonxpr = parse(jsonpath)
        return jsonxpr.find(json.loads(str_json))[0].value

    def getFile(self, path):
        """
        读出文本中的内容 \n
        :param path: 文件路径 \n
        :return:  文件内容 \n
        """
        try:
            with open(path, 'r') as fin:
                data = fin.read()
                return data
        except Exception, e:
            raise safe_repr(e)

    def toBase64(self, img_path):
        """
        将图片转为base64编码  \n
        :param img_path: 图片路径  \n
        :return:  \n
        """
        try:
            with open(img_path, 'rb') as fin:  # 二进制方式打开图片
                image_data = fin.read()
                base64_data = base64.b64encode(image_data)
                return base64_data
        except Exception, e:
            raise safe_repr(e)

    def toMD5(self, str_content):
        """
        将传入字符串进行md5加密  \n
        :param str: 要加密的字符串  \n
        :return: \n
        """
        m = hashlib.md5()
        m.update(str_content)
        str_encoding = m.hexdigest()
        return str_encoding

    def getTimestamp(self):
        """
        返回毫秒级时间戳 \n
        :return: 时间戳 \n
        """
        return int(round(time.time() * 1000))

    def getRandInt(self, min, max):
        """
        返回一个[min,max]区间的数
        :return:
        """
        return random.randint(int(min), int(max))

    def getRandStr(self, n=7, type=0):
        """
        生成一个指定长度为 n 的随机字符串，  \n
        :param n: 要返回的字符串长度
        :param type: type=0时（n<=10），为纯数字，type=0时(n<=36)，为字母数字混合 \n
        :return: str
        """
        str0 = "012345678901234567890123456789"
        str1 = "abcdefghijklmnopqrstuvwxyz"
        list_rs = []
        if int(type) == 0:
            list_rs = random.sample(str0, int(n))
        else:
            list_rs = random.sample(str0 + str1, int(n))
        return "".join(list_rs)

    def listUUID(self, n=1):
        """
        批量返回全球唯一的32位字符串 \n
        :param n: 要返回字符串的个数,默认为1
        :return: list[str1,str2]
        """
        try:
            list = [self.toMD5(str(uuid.uuid1()).replace("-", "")) for i in range(int(n))]
        except Exception, e:
            raise safe_repr(e)
        return list

    def listRandFileName(self, path, n=1):
        """
        随机返回n个path路径下的文件名 \n
        :param path: 存放文件的路径 \n
        :param n: 要返回的文件名数量 \n
        :return: list[str1,str2,...]
        """
        list_file = os.listdir(path)
        return random.sample(list_file, int(n))

    def listAllFileName(self, path):
        """
        返回path路径下所有文件名称  \n
        :param path: 存放文件的路径 \n
        :return: list[str1,str2,...]
        """
        return os.listdir(path)

    def appendList(self,res_list,obj):
        """
        将对象obj添加到list中
        :param list: old list
        :param obj: object
        :return: new list
        """
        if isinstance(res_list,list):
            res_list.append(obj)
            return res_list