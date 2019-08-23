install:
	sudo pip -r install -U requirements.txt
clean:
	find . -name \*.pyc -type f -delete
	find . -name __pycache__  -type d -delete
	rm -rf .pytest_cache/
