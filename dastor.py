# -*- coding: utf-8 -*-
from decimal import Decimal, getcontext

"""
数据存储器
"""

def encrypt(a, delimiter="10000000"):
    """
    加密算法
    """
    new_a = ""
    for i in str(a):
        b = ord(i)               # 将字符转为编码
        c = bin(b)               # 转二进制
        c = str(c).lstrip("0b")  # 去掉0b
        new_a += c + delimiter   # 加入分隔符
    return new_a



def decrypt(a, delimiter="10000000"):
    """
    解密算法
    """
    new_a = ""
    for i in str(a).split(delimiter):
        if i.isdigit():
            b = int(i, 2)           # ��二进制转为整数
            c = chr(b)              # ��编码转为字符
            new_a += c
    return new_a



class Dastor():
    """
    数据存储类
    用法：
        创建存储器：
        dastorname = Dastor(文件名)
        读取数据：read(键)
        添加或更改数据：write(键, 值)
    """



    def __init__(self, filename:str = "data", delimiter="=", suffix:str=".dtr") -> None:
        self.filename = filename + suffix
        self.delimiter = delimiter
        with open(self.filename, 'a+') as file:
            pass
    


    def read(self, key:str)->str|float:
        """
        读取数据
        """
        with open(self.filename, 'r') as file:
            data = file.readlines()
            data.reverse()
            for i in data:
                i = i.strip("\n")
                if i.split(self.delimiter)[0] == str(key):
                    ret = i.split(self.delimiter)[1]
                    if ret.isdigit():
                        return Decimal(ret)
                    else:
                        return ret
    


    def write(self, key:str, value:str|int|float):
        """
        写入数据
        """
        with open(self.filename, 'a') as file:
            file.write(f"\n{key}{self.delimiter}{value}")



    def get_all_keys(self)->list:
        pass


    def read_all(self)->dict:
        pass


    def write_by_dict(self):
        pass


    def read_by_list(self)->list:
        pass




class DastorEncrypt(Dastor):
    """
    加密数据存储器
    """

    def __init__(self, filename: str = "data", delimiter="11111110") -> None:
        super().__init__(filename, delimiter)



    def read(self, key: str) -> str | float:
        ord_key = encrypt(key)
        ore_value = super().read(ord_key)
        return decrypt(ore_value)
    


    def write(self, key: str, value: str | int | float):
        ord_key = encrypt(key)
        ord_value = encrypt(value)
        super().write(ord_key, ord_value)