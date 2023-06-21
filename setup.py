from setuptools import setup, find_packages

setup(
    name='pybilibili',
    version='0.0.1',  # 版本号
    url='https://github.com/songjian/pybilibili',  # 你的项目的git仓库地址
    author='sj',
    author_email='724385768@qq.com',
    description='调用哔哩哔哩api的python包。',
    packages=find_packages(),  # 自动发现你的包
    install_requires=[
        'requests==2.31.0',
    ],  # 这里写你的包的依赖
)
