#========
# name: makefile
# date: 2018DEC11
# prog: pr
# description: 
#       automate the build and clean
#========

#------
# python version
#------
PYVER=python3.5



#-----
# use case: install current version
#-----
build :
	$(PYVER) setup.py install


#-----
# use case: remove current build from installed directory
#-----
clean :
	sudo rm -fr build dist wsd.egg-info __pycache__

