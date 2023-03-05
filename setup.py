from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='TextBooster',
    version='0.1',
    description='Data augmentation techniques for text data using back translation and synonym replacement',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    readme = "README.md",
    url='https://github.com/hachemsfar/TextBooster',
    author='Hachem Sfar',
    author_email='hachem.sfar@supcom.tn',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='text data augmentation back translation synonym replacement',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'deep_translator',
        'nltk',
        'spacy',
        'textblob',
    ],
    extras_require={
        'dev': [
            'pytest',
        ]
    },
    project_urls={
        'Bug Reports': 'https://github.com/hachemsfar/TextBooster/issues',
        'Source': 'https://github.com/hachemsfar/TextBooster',
    },
)
