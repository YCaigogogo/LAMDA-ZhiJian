from setuptools import setup, find_packages

setup(
    name='zhijian',
    version='1.0.0',
    description='ZhiJian: A Unifying and Rapidly Deployable Toolbox for Pre-trained Model Reuse',
    author='ZhiJian Contributors',
    author_email='',
    packages=['zhijian', 'zhijian.models', 'zhijian.trainers', 'zhijian.data'],
    install_requires=[],
)