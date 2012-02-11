#A few notes
this is running the real 16bit DOS rasm executable inside of DOSBox. This means DOS limitations apply. Make your filenames really short (8 characters or less). To read more about the restrictions, visit [http://en.wikipedia.org/wiki/8.3_filename]

These instructions have been tested on Mac and Ubuntu (donlanes). You will need some kind of a serial port to them to work. If you have questions, please ask me (isaac).

I will likely continue to work on the toolchain, and will send out an email if I add something notable. prog8051 is a bit sketchy. I haven't tested it much. I will add version numbers to my toolchain if I release more than a few versions.

A usb-serial dongle that works on Linux is: http://www.amazon.com/TRENDnet-Serial-Converter-TU-S9-White/dp/B0007T27H8/ref=sr_1_1?ie=UTF8&qid=1328853484&sr=8-1
#Instructions
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
Executing DOSBox...

Rasm51E 1.32 (c) Rigel Corporation 1990-1995
Assembling file t:temp.asm
opening file t:temp.asm
pass 1

4 lines of source code read

pass 2
  assembly time :   0.000 seconds
writing file t:temp.lst to disk
writing file t:temp.obj to disk
disk write time :   0.000 seconds

no errors found...Rasm51E terminates...

-rw-r--r--  1 isaac   26 Feb  9 17:55 test.err
-rw-r--r--  1 isaac  132 Feb  9 17:55 test.lst
-rw-r--r--  1 isaac   44 Feb  9 17:55 test.obj
</pre>

Additionally, you can type
<pre>
make program
</pre>
To upload the program on the RJ31P (is that what it's called). 
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

To see the prog8051 syntax, type
<pre>
prog8051 --help 
</pre> 


<pre>
prog8051 -o myfile.obj
</pre>

#Mac Instructions
* Copy DOSBox.app into /Applications
* Make a symlink  to /Applications/DOSBox.app/Contents/MacOS/DOSBox from ~/6.115/tools/bin/dosbox
<pre>
ln -s /Applications/DOSBox.app/Contents/MacOS/DOSBox ~/Dropbox/Classes/6.115/tools/bin/dosbox 
</pre>
* Follow the general instructions above, but Instead install pyserial with the following command
<pre>
sudo easy_install pyserial
</pre>

##Problems
If you get something like
<pre>
isaac$:~/6.115$ rasm test.asm
Executing DOSBox...
Sorry, DOSBox failed.  Full output follows:
DOSBox version 0.74
Copyright 2002-2010 DOSBox Team, published under GNU GPL.
---
CONFIG: Generating default configuration.
Writing it to /home/isaac/.dosbox/dosbox-0.74.conf
CONFIG:Loading primary settings from config file
/home/isaac/.dosbox/dosbox-0.74.conf
MIXER:Got different values from SDL: freq 44100, blocksize 512
ALSA:Can't subscribe to MIDI port (65:0) nor (17:0)
MIDI:Opened device:none
SHELL:Redirect output to t:LOG
Illegal command: r:\rasm51e.exe.
isaac$:~/6.115$
</pre>

You should modify tools/bin/rasm and adjust the indicated line to point at the rasm directory.
