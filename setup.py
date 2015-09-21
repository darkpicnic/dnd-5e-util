from setuptools import setup

setup(
    name='dnd-5e-util',
    version='0.1',
    py_modules=['random_npc'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        random_npc=random_npc:run
    ''',
)
