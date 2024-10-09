from setuptools import setup, find_packages


setup(
    name='hot-cosby',
    packages=find_packages(),
    install_requires=['sqlalchemy', 'fastapi', 'click', 'click-log', 'celery[redis]', 'python-dotenv', 'pandas',
                      'matplotlib', 'rauth', 'xmltodict', 'pyhumps', 'pymongo', 'pydantic', 'pg8000']
)
