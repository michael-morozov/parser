rebuild-l: clean-l linux_build

rebuild-w:

windows_build:
	pyinstaller main.py
linux_build:
	pyinstaller --onefile main.py

clean-l:
	rm main.spec
	rm -r ./dist
	rm -r ./build