SRC_DIR = src
 
run: $(SRC_DIR)/main.py
	python3 src/main.py src/test.c
 
format:
	git ls-files '*.py' | xargs autopep8 --in-place
