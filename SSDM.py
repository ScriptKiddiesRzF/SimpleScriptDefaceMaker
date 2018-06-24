#!/system/bin/python
"""
Author: ./RzFNymous33
Date  : 24-06-2018
Name  : Rizal Afrizal Freeze
Tools : Script Deface Maker
"""
import os
import sys
import time

if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
print ("+-----------------------------------------+")
print ("|--------------Script Deface Maker v1.0--------------|")
print ("+-----------------------------------------+")
print ("| [+] Author : ./RzFNymous33 A.K.A R.A Freeze  |")
print ("| [+] Date  : 24-06-2018 (20:19)          |")
print ("| [+] Team  : XPLOITER HACKER TEAM     |")
print ("| [+] Simple Script Deface Maker          |")
print ("| [+] Free and Easy To Use            |")
print ("+-----------------------------------------+")
print
print "[1] Start"
print "[2] About"
print "[0] Exit"
print
aa = '"'
menu = raw_input("{Script Deface Maker}:> ")

try:
   file = open("index.html", 'w')
except(IOError):
   print ("ERROR")
   sys.exit()
  
if menu == '1':
  print "Simple Script Deface Maker"
  print
  defstyletitle_simple = raw_input("Title: ")
  defstyleimage_src = raw_input("Link/Image: ")
  defstyleimage_width = raw_input("Lebar/Width: ")
  defstyleimage_height = raw_input("Tinggi/Height: ")
  defstylehacked_simple = raw_input("Touched By: ")
  defstylemessage_simple = raw_input("Message: ")
  defstyleteam_simple = raw_input("Nama Team: ")
  time.sleep(1)
  print "[+] Success ea jancokkk"
  print "[!] Script is save as index.html"
  print "Thanks To:"
  print "[+] ALLAH SWT "
  print "[+] HellMe "
  print "[+] ./R41N53 "
  print "[+] BlackDeath "
  print "[+] NRT101"
  print "[+] e90x "
  print "[+] ./FL45H3R.33 "
  print "[+] PatrickCibel "
  print "[+] Xuner "
  print "[+] And All Mem Xploiter Hacker Team"
  print "For the support..."
  a = '"center"'
  aaa = '"#111111"'
  b = '"100%"'
  bb = '""'
  c = '"0"'
  d = '"align"'
  e = '"#000000"'
  f = '"10"'
  gg = '"1"'
  h = '"#ffffff"'
  hh = '"#b21f25"'
  hhh = '"#333333"'
  
  file.write(" <body bgcolor=black>\n")
  file.write("\n")
  file.write("<br><title>"+defstyletitle_simple+"</title></br>\n")
  file.write("<td><div align="+a+">\n")
  file.write("</div>        <table width="+b+" border="+c+" cellpadding="+c+" cellspacing="+c+">\n")
  file.write("          <tbody><tr>\n")
  file.write("     <center><img src="+aa+""+defstyleimage_src+""+aa+" alt="+bb+" width="+aa+""+defstyleimage_width+""+aa+" height="+aa+""+defstyleimage_height+""+aa+" align="+d+"></a></center>\n")
  file.write("          </tr>\n")
  file.write("        </tbody></table>\n")
  file.write("<table width="+b+" bgcolor="+e+" border="+c+" cellpadding="+f+" cellspacing="+gg+">\n")
  file.write("\n")
  file.write("  <tbody><tr bgcolor="+h+">\n")
  file.write("    <td bgcolor="+h+"><center><b><font color="+hh+">Touched By "+defstylehacked_simple+"</font></b></center></td>\n")
  file.write("\n")
  file.write("  </tr>\n")
  file.write("\n")
  file.write("  <tr bgcolor="+hhh+">\n")
  file.write("    <td bgcolor="+aaa+"><center><center><font color="+hh+"><b><br>"+defstylemessage_simple+"</center>\n")
  file.write("      <br><center>"+defstyleteam_simple+"</b></center>\n")
  file.write("\n")
  file.write("\n")
  file.write("   </td></tr><tr bgco")
  sys.exit()
  
if menu == '2':
  print "Simple Script Deface Maker v1.0 24-06-2018 (20:19)"
  print "Author: ./RzFNymous33"
  print "Coded By : ./RzFNymous33 A.K.A Rizal Afrizal Freeze"
  print "Team  : Xploiter Hacker Team"
  print "Disclaimer: This tool is for educational purpose only."
  print "Thanks To:"
  print "[+] ALLAH SWT "
  print "[+] HellMe "
  print "[+] ./R41N53 "
  print "[+] BlackDeath "
  print "[+] NRT101"
  print "[+] e90x "
  print "[+] ./FL45H3R.33 "
  print "[+] PatrickCibel "
  print "[+] Xuner "
  print "[+] And All Mem Xploiter Hacker Team"
  print "For the support..."
  
if menu == '0':
  print "Thanks To:"
  print "[+] ALLAH SWT "
  print "[+] HellMe "
  print "[+] ./R41N53 "
  print "[+] BlackDeath "
  print "[+] NRT101"
  print "[+] e90x "
  print "[+] ./FL45H3R.33 "
  print "[+] PatrickCibel "
  print "[+] Xuner "
  print "[+] And All Mem Xploiter Hacker Team"
  print "For the support..."
  print "Exiting..."
  sys.exit()