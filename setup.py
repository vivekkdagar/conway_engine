from setuptools import setup, find_packages

setup(
    name='conway_engine',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pygame',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'game-of-life=conway_engine.simulation:main',
        ],
    },
    author='Vivek Dagar',
    author_email='vivekdagar2017@gmail.com',
    description="Conway Engine is a Python package offering a sophisticated implementation"
                " of Conway's Game of Life, featuring the iconic Gosper Glider Gun for dynamic"
                " and explosive cellular automaton growth.",
    url='https://github.com/vivekkdagar/game-of-life',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    license='GNU General Public License v3.0',
)
