# flacbittolower
I wrote this script to auto convert my music library so that all music is below a specified frequency. The reason is that I use a Raspberry Pi as a music server and when using a Squeezebox V3 that is only capable of playing back 24-bit, 48khz, the server has to downsample the music on fly, something the Raspberry Pi isn't able to cope with. [Read more at why I need to downsample here](http://www.jackenhack.com/raspberry-pi-squeezebox-logitech-server/)

**WARNING! Replaces original files, so do a backup before use!**

## prerequisites
You need to install the following and maybe change the path in the script:
* [FLAC](http://flac.sourceforge.net/)
* [sox](http://sox.sourceforge.net/)

This is one of my first Python scripts so put on darkened glasses to shield yourself if your a Python expert. Or even better, fix it!