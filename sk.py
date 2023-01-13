#!/usr/bin/python3
import pexpect
import time
import sys
import re
def setup(fw_ip):
		fw = pexpect.spawn("ssh -o StrictHostKeyChecking=no admin@%s" %fw_ip)
		fw.logfile = open("output-%s.log" % fw_ip, "wb")
		fw.expect("word: ")
		fw.sendline("PaloAlto123!\r")
		fw.expect("> $")
		fw.sendline("set cli pager off\r")
		fw.expect("> $")
		fw.sendline("set cli scripting-mode on\r")
		fw.expect("> $")
		return fw

def collect_data(fw):
		fw.sendline("show clock\r")
		fw.expect("> $")
		fw.sendline("show counter global filter packet-filter yes delta yes\r")
		print (fw.sendline)
		fw.expect("> $")

def main():
		fw1 = setup("10.46.34.153")
		while True:
				collect_data(fw1)
				time.sleep(1)
if __name__ == "__main__":
		main()