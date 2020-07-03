from setuptools import setup
import setuptools

setup(
    name='bar_chart_race_cn',     # 包名字
    version='0.11',   # 包版本
    description='解决bar_chart_race无法显示中文的问题',   # 简单描述
    author='thunderhit',  # 作者
    author_email='thunderhit@qq.com',  # 邮箱
    url='https://github.com/thunderhit/bar_chart_race_cn',      # 包的主页
    packages=setuptools.find_packages(),
    install_requires=['matplotlib', 'numpy', 'pandas'],
    python_requires='>=3.5',
    license="MIT",
    keywords=[
        'bar chart race',
        '支持中文',
    ],
    long_description=open('README.md').read(), # 读取的Readme文档内容
    long_description_content_type="text/markdown")  # 指定包文档格式为markdown

