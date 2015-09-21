from setuptools import setup

setup(
    name='dnd-5e-util',
    version='0.1',
    py_modules=['dnd_util'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        dnd_util=dnd_util:run
    ''',
)
