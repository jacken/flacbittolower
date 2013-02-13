#!/usr/bin/env python
import os, sys, traceback, fnmatch, subprocess, shlex, pipes
from optparse import OptionParser

def all_files(root, patterns='*', single_level=False, yield_folders=False):
    # Expand patterns from semicolon-separated string to list
    patterns = patterns.split(';')
    for path, subdirs, files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)
        files.sort( )
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    yield os.path.join(path, name)
                    break
        if single_level:
            break

def samplerate(s):
	command = '/usr/local/bin/soxi -r '.split()
	command.append(s)
	try:
		samplerate = subprocess.Popen(command,stdout=subprocess.PIPE)
	except:
		print "----------------"
		print "Error when reading file: " + s
		print "----------------"
		pass
	else:
		return samplerate.communicate()
	
def downsample(s, freq):
	tmpname = s + '_tmp.flac'
	command = ['/usr/local/bin/sox',s , tmpname, 'rate','-v' ,freq]
	#print command
	try:
		p = subprocess.check_call(command, stderr=subprocess.PIPE)
		os.rename(tmpname, s)
	except:
		print "----------------"
		print "Error when converting file: " + s
		print "----------------"
		pass
	print
	print
	
def main():	
	usage = "Downsamples FLAC music files recursivly in a folder to a lower sampling frequency: %prog [options] arg foldername.\n \
WARNING! Replaces original files, so do a backup before use!"
	parser = OptionParser(usage=usage, version="%prog 0.2")
	parser.add_option('-f', '--freq',
					type='choice',
					action='store',
					dest='freq',
					choices=['22050', '32000', '44100', '48000', '88200', '96000',],
					default='48000',
					help="Choose the sampling frequency to downsample if higher, for example 48000. All FLAC files higher will be downsampled to 48000. Default value = [%default]",)
	(options, args) = parser.parse_args()
	if len(args) != 1:
		parser.error("wrong number of arguments")
	for path in all_files(str(args[0]), '*.flac;*.FLAC'):
		filerate =  samplerate(path)
		print "filerate = " + str(filerate)
		if filerate:
			filerate =  int(samplerate(path)[0])
			if (filerate > int(options.freq)):
				print str(path)
				print "Sample rate: " + str(filerate)
				downsample(path, options.freq)
if __name__ == '__main__':
    main()

