from setuptools import setup, find_packages

setup(
    name='safeurl_decoder',
    version='2.0.0',
    packages=find_packages(),
    # url='https://github.com/renisac/safeurl_decoder',
    url='https://github.com/purusoni/safeurl_decoder_and_opener',
    author='REN-ISAC',
    author_email='soc@ren-isac.net',
    description='',
    entry_points = {
              'console_scripts': ['safeurl-decode=safeurl_decoder.__init__:main'],
    }
)
