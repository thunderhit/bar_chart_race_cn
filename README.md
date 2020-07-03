# bar_char_race_cn库

解决[bar_chart_race库](https://github.com/dexplo/bar_chart_race)不支持中文的问题

<video id="video" controls="" preload="none">
    <source id="mp4" src="test/近20年各省财政收入.mp4" type="video/mp4">
</video>







### 安装

```
pip install bar_char_race_cn
```



### 注意:

使用前需提前安装ffmpeg



### 使用

准备测试数据

```
import pandas as pd

df = pd.read_csv('data/财政收入.csv')

def year2timestamp(year):
    #转为可比较大小的日期格式
    return pd.Timestamp(str(year))

df['year'] = df['year'].apply(year2timestamp)
df.set_index('year', inplace=True)
df.sort_index(inplace=True) #日期从小到大排序
```

可视化代码

```python
import bar_chart_race_cn as bcr

bcr.bar_chart_race(df=df,
                   filename='近20年各省财政收入.mp4',
                   title='近20年各省财政收入(单位: 亿元)'
                  )
```

效果

<video id="video" controls="" preload="none">
    <source id="mp4" src="test/近20年各省财政收入.mp4" type="video/mp4">
</video>





## 更多

- [B站:大邓和他的python](https://space.bilibili.com/122592901/channel/detail?cid=66008)

- 公众号：大邓和他的python

- [知乎专栏：数据科学家](https://zhuanlan.zhihu.com/dadeng)

    ​    

## 支持一下

![](../shreport/img/my_zanshang_qrcode.jpg)