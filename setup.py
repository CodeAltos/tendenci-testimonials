from setuptools import setup, find_packages

longdesc = \
'''
A Tendenci testimonials app.
'''

setup(
    name='tendenci-testimonials',
    author='Tendenci',
    author_email='programmers@tendenci.com',
    version='6.0.0',
    license='GPL3',
    description='Testimonials app for Tendenci',
    long_description=longdesc,
    url='https://github.com/tendenci/tendenci-testimonials',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    include_package_data=True,
    packages=find_packages(),
    install_requires=['tendenci>=6.0'],
)
