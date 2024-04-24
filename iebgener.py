import configparser
import argparse


parser = argparse.ArgumentParser(
description='--- iebgener.py command line parameters ---')
parser.add_argument('--sysut1', help='input file to copy', required=True)
parser.add_argument('--sysut2', help='output file to copy into', required=True)
args = parser.parse_args()

sysut1 = args.sysut1
sysut2 = args.sysut2

print('Copying from:', sysut1)
print('to:', sysut2)
reccounter = 0

fi = open(sysut1,'rt')
fo = open(sysut2,'wt')

databuf = fi.readline()
while databuf:
    fo.write(databuf)
    databuf = fi.readline()
    reccounter +=1

print('Copied', reccounter, 'records')
fi.close()
fo.close()

