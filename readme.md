![alt text](https://github.com/N0nent1ty/AutoBuildInMineCraft/blob/master/screen_shot/1.png)

# Getting Start:
You have to know how to set up a evironment for python in minecraft first.
it is recommented to follow the tutorial(URL is list bellow) to complete evironment settings.
### [Python Coding for Minecraft](http://www.instructables.com/id/Python-coding-for-Minecraft/)


# Python prerequisites dependencies.
## [sklearn](http://scikit-learn.org/stable/). 
#### for kd_tree algorithm.

## [Pillow](https://pillow.readthedocs.io/en/4.3.x/) 
#### for image procceing.

##### Windows user:
``
You can download whl file from following link to install pillow.
``
[Unofficial Windows Binaries ](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
##### Linux & Mac user:
``
pip3 install pillow 
``


# Running test:
Once you finsh the above step, move the file main.py to %appdata%/.minecraft/mcpicy 
and modify the code in line number 126th, change the line to the path of your image file.
im = Image.open(r"your/picture/path)")
</br>
I know this approach like change the the path maually is terrible but I will amend this function one day when I have somehow more free time,
or you can change the image dynamiclly by adding a feature by yourself.
If every thing above is setted up correctlly,
start minecraft and run the source code, the building should show up in your world.

