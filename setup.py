from os import path,listdir,system,makedirs
from appdirs import AppDirs
from setuptools import setup

cache_path=AppDirs('tdwnsv3','Simatwa').user_cache_dir

if not path.isdir(cache_path):
	makedirs(cache_path)
	
def get_file(fnm):
	main=path.join(cache_path,'main.txt')
	if not path.isfile(main):
		dirpath = path.abspath(path.dirname(__file__))
		with open(main,'w',encoding='utf-8') as fp:
			fp.write(dirpath)
	return path.join(open(main).readlines()[0],fnm)

setup (
   name='tdwnsv3',
   packages=['tdwnsv3'],
   version='1.0.8',
   install_requires=open(get_file('requirements.txt')).readlines(),
   url='https://github.com/Simatwa/tdwnsv3',
   license='MIT',
   author='Simatwa Caleb',
   author_email='simatwaclb@gmail.com',
   description="Simple local-file's server with security as main priority!",
   long_description=open(get_file('README.md')).read(),
   long_description_content_type='text/markdown',
       classifiers=[
        "License :: OSI Approved :: MIT",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
  )
def install_module():
	installable=listdir(get_file('dist'))[0]
	installable_file_path=get_file(f"dist/{installable}")
	system(f'pip install {installable_file_path}')

install_module()