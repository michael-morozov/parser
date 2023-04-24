rebuild-l: clean-l build

rebuild-w: clean-w build

build:
	pyinstaller --onefile main.py
	
clean-l:
	rm main.spec
	rm -r ./dist
	rm -r ./build

clean-w:
	del main.spec
	rd /s /q dist
	rd /s /q build