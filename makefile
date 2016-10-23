

build:
	cd ./source && make all
	rm -f output/*.pyc output/*.aux output/*.log output/*.out
	rm -f source/*.pyc source/*.aux source/*.log source/*.out source/*.pdf
clean:
	rm -rf output
	rm -rf source/__pycache__