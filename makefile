install:
	sudo pip -r install -U requirements.txt
clean:
	rm -rf .pytest_cache
	rm -rf ./*/__pycache__/
	rm -rf ./*/*.pyc
