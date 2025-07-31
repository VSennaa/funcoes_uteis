from setuptools import setup, find_packages

setup(
    name='funcoes_uteis',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'scikit-learn',
    ],
    author='VSennaa',
    description='Funções úteis para análise de dados, como o método do cotovelo.',
)
