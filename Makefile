rebuild-l: clean-l linux_build

rebuild-w: clean-w win_build

rebuild-w:

win_build:
	pyinstaller main.py

linux_build:
	pyinstaller --onefile main.py

clean-l:
	rm main.spec
	rm -r ./dist
	rm -r ./build

clean-w:
	del main.spec
	rd /s /q dist
	rd /s /q build