from setuptools import setup, find_packages

setup(
    name='decipher',
    url='https://https://github.com/tidusete/decipher',
    author='dsymbol',
    install_requires=[
        'openai-whisper @ git+https://github.com/openai/whisper.git@b91c907694f96a3fb9da03d4bbdc83fbcd3a40a4',
        'click==8.1.3',
        'ffpb==0.4.1',
        'tqdm'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'decipher = decipher.__main__:main'
        ]
    }
)
