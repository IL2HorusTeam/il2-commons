from setuptools import setup, find_packages

setup(
    name='il2-commons',
    version='1.0.0',
    description='Common helpers and data structures for projects related to IL-2.',
    license='GPLv2',
    url='https://github.com/IL2HorusTeam/il2-commons',
    author='Alexander Oblovatniy',
    author_email='oblovatniy@gmail.com',
    packages=find_packages(),
    install_requires=[i.strip() for i in open("requirements.pip").readlines()],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'License :: Free for non-commercial use',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries',
    ],
)
