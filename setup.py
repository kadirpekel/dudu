from setuptools import setup

setup(
    name='todo.py',
    scripts=['todo'],
    version='0.0.1',
    description='get things done!',
    author='Kadir Pekel',
    author_email='kadirpekel@gmail.com',
    url='https://github.com/kadirpekel/todo.py',
    install_requires=[
        'komandr>=0.1.1'
    ],
)
