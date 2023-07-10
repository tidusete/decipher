from setuptools import setup, find_packages

setup(
    name='decipher',
    url='https://https://github.com/tidusete/decipher',
    author='dsymbol',
    install_requires=[
        'openai-whisper @ git+https://github.com/openai/whisper.git',
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
