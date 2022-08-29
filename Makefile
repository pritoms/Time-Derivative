all:
	python3 setup.py install --user

clean:
	rm -rf build dist *.egg-info

test:
	./test.sh
