模块名：Dastor
版本：1.0.0
发布日期：2024.10.15
语言：Python

用途：
更方便地存储数据到本地硬盘中
用于小型网站开发、单机游戏开发、企业业务管理系统等

基础教程：

下载好后移动到您的项目文件夹下并解压

1 导入模块
from dastor import *

2 创建对象

dastor = Dastor() ---------------------------

我们创建了一个名为dastor的数据读写器对象
这个对象会自动创建一个名为data.dtr的dtr数据库文件，用来存放您的数据
dtr数据库文件以键值对方式存放数据
KEY = VALUE
由于数据是以明文方式储存，所以可能会有安全隐患
您可以创建一个加密的数据读写器对象，方法如下
dastor = DastorEncrypt()
DastorEncrypt对象能够自动将存储的数据进行加密

3 写入数据
语法

dastor.write(key, value) ----------------------

利用write方法可以将数据以键值对方式写入dtr数据库
此方法用两个参数，分别是key、value
参数key是数据名称，也就是变量名
参数value是数据值，也就是变量值
示例

dastor.write("name", "Donald Trump")
dastor.write("age", 82)
dastor.write("color", "blue")

在这个示例中dastor向dtr内存储了name、age、color三个数据
它们的值分别为Donald Trump、82、blue
打开 data.dtr 文件应该可以看到以下内容
-----------------------
| name=Donald Trump   |
| age=82              |
| color=blue          |
-----------------------

4 更改数据
更改数据和写入数据的方法是相同的
如果我们想将上述示例中变量age的值改为40，可以按下列方法编写

dastor.write("age", 40)

更改数据并不会将dtr数据库中的原值直接修改
而是在数据库的末尾新增一条键值对
所以修改 age 数据值后的 data.dtr 会显示以下内容
-----------------------
| name=Donald Trump   |
| age=82              |
| color=blue          |
| age=40              |
-----------------------
不过不必担心，
Dastor对象读取数据时会自动忽略旧的键值对，从而读取新建立的数据

5 读取数据
语法

value = dastor.read(key) ------------------------

read方法会根据参数key在dtr数据库中从后向前匹配第一个与key相同的数据名称并返回相应的数据值给变量value
示例
color = dastor.read("color")
age   = dastor.read("age")
print(color, age)
输出结果如下
blue 40
示例中我们读取了data.dtr数据库中的color和age两条数据，并将数据值返回给变量并打印在了屏幕上
可以看到，age的值为40，而非82
说明Dastor读写器自动忽略了被覆盖的旧值

进阶操作教程：
1 数据加密
创建DastorEncrypt加密读写器对象
dastor = DastorEncrypt()

读写方法与Dastor对象一样，依旧为

value = dastor.read(key)
和
dastor.write(key, value)

写入的数据会被DastorEncrypt加密成由0和1组成的二进制密文
示例

dastor = DastorEncrypt()
dastor.write("Animal": "cat")

打开data.dtr文件可以看到下列内容
10000011000000011011101000000011010011000000011011011000000011000011000000011011001000000011111110110001110000000110000110000000111010010000000
这就是将Animal=cat加密后的数据



反馈邮箱：
sjx20011225@outlook.com