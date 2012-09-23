### Goal

`Ctrl+S` --> Save and compile.

### Supported compilers

* [Coco](https://github.com/satyr/coco/)
* [Lessc](http://lesscss.org/)

### Tested only on Windows XP!

### Installation

	git clone https://github.com/jan-swiecki/sublime-text-2-save-and-compile-coco
	cd sublime-text-2-save-and-compile-coco

Select `SaveAndCompile.py` and `my_exec.py` and press `Ctrl+C`.

Open Sublime Text 2.

Go to `Preferences -> Browse Packages`. Go into `User` folder.

Press `Ctrl+V`.

Go to `Preferences -> Key Bindings - User`. Add following key binding:

	{ "keys": ["ctrl+s"], "command": "save_and_compile" }

When you save coco file the output view will appear only on compile error.

And keep in mind that I'm no Python guru!