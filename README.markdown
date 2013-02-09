#Updates

## Just updated for Spring 2013

I have updated the Makefile to use as31, and also changed all python to be python 3 compatible.

Note: This toolchain was made for me, and is very hackish. If there is interest in me improving it, or you yourself have ideas
on how to improve it, pleas let me know, fork away, and share the software...


I recently added code from Isaac Evan's preprocessor. To get the update, do a normal pull/clone

<pre>
git pull
</pre>
Followed by 
<pre>
git submodule init
git submodule update
</pre>

This wil get you all the sweet features.

If the pull complains about changes to Makefile, come bother me, or read about git. Sorry, I don't have time to write  too much.

#A few notes

These instructions have been tested on Mac and Ubuntu (donlanes). You will need some kind of a serial port to them to work. If you have questions, please ask me (isaac).

I will likely continue to work on the toolchain, and will send out an email if I add something notable. prog8051 is a bit sketchy. I haven't tested it much. I will add version numbers to my toolchain if I release more than a few versions.

A usb-serial dongle that works on Linux is: http://www.amazon.com/TRENDnet-Serial-Converter-TU-S9-White/dp/B0007T27H8/ref=sr_1_1?ie=UTF8&qid=1328853484&sr=8-1
#Ubuntu Instructions
<pre>
sudo apt-get install dosbox python-serial python-argparse
cd ~
git clone git://github.com/igutekunst/6.115-Toolchain.git 6.115
echo  "export PATH=~/6.115/tools/bin:\$PATH" >> ~/.bashrc
source ~/.bashrc
</pre>

Test this by typing rasm test.asm

It should print something like this:
<pre>
as31 test.p.asm
Begin Pass #1
Begin Pass #2
</pre>

Additionally, you can type
<pre>
make program
</pre>
To upload the program on the R31JP
##Serial Port Settings
For this to work, edit the Makefile and change the serial port to be the correct one for you machine. To find out, first type
<pre>
ls /dev/tty*
</pre>
Now plug in your serial port, and repeat the command. The item that shows up is the serial port.
##Modifying the Makefile for your own code
You can modify the Makefile to change which asm file it assembles by changing the SRC variable.

Just open the file and replace SRC := test with SRC := myfile  (without the asm). Your file must be named myfile.asm
##Plain Old rasm
If you want, you can also just use rasm as documented in the lab


##prog8051
If have also included a program I wrote, prog8051 which will upload an .obj file the the board if it is in monitor mode.
To use it, type prog8051myfile.obj --serial-port /dev/thecorrectserialport

For example,

<pre>
prog8051  myfile.obj --serial-port /dev/ttyUSB0
</pre>

To see the prog8051 syntax, type
<pre>
prog8051 --help 
</pre> 


If you want to avoid typing the serial port each time, edit the file prog8051_config.ini in the 6.115 directory to reflect 
the correct port.

#Mac Instructions
* Follow the general instructions above, but Instead install pyserial, and argparse with the following command
<pre>
sudo easy_install pyserial
sudo easy_install argparase
</pre>

##Problems

#Getting Involved / I fixed something

If you find something broken, or want to improve the toolchain, go ahead and fork it on GitHub. If you don't want to learn git, just send me 
a modified file, and I'll merge it if it looks ok. 

I can also make you a collaborator on GitHub if you are intersted enough.

# Things I want to change
* Make this a software package that uses some packaging system, either pip or python egg format, or 
* Use GNU Build System (Make, autoconf, etc)
* make prog8051 cleaner
* Perhaps use the C preprocessor somehow
* Make the Makefile not terrible. I had no idea how Makefiles worked when I created this, and know slightly more now
* Make a linker??
