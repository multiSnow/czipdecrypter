from distutils.core import setup

try:
    from Cython.Build import cythonize
except ImportError:
    print('Cython is required.')
    exit(1)

setup_info={
    'name':'cZipDecrypter',
    'version':'0.0.1',
    'description':'Drip-in replacement of zipfile._ZipDecrypter for python 3.7+',
    'url':'https://github.com/multiSnow/czipdecrypter',
    'author':'multiSnow',
    'author_email':'infinity.blick.winkel@gmail.com',
    'classifiers':[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: C',
        'Programming Language :: Cython',
    ],
    'keywords':['zipfile','zip','decryption'],
}

if __name__=='__main__':
    setup_info['ext_modules']=cythonize('czipdecrypter.pyx')
    setup(**setup_info)
