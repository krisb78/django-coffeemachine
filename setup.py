from setuptools import (
    setup,
    find_packages
)

import coffeemachine

setup(
    name='coffeemachine',
    author="Krzysztof Bandurski",
    author_email="krzysztof.bandurski@gmail.com",
    version=coffeemachine.__version__,
    description='Simple compilation of coffeescript for Django',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    requires=[
        'django (>1.2.0)',
    ],
    packages=find_packages(exclude=["example", "example.*"]),
    include_package_data=True,
    zip_safe=False
)
