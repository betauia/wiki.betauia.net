# Betasec
> Skrive om BETASEC

# UIACTF
> Skrive om UIACTF


# What is CTF?
In computer security, Capture the Flag (CTF), a type of wargame, is a computer security competition. CTF contests are usually designed to serve as an educational exercise to give participants experience in securing a machine, as well as conducting and reacting to the sort of attacks found in the real world (i.e., bug bounty programs in professional settings). Reverse-engineering, network sniffing, protocol analysis, system administration, programming, and cryptanalysis are all skills which have been required by prior CTF contests at DEF CON. There are three main styles of capture the flag competitions: attack/defense, hardware challenges and Jeopardy!.


In an attack/defense style competition, each team is given a machine (or a small network) to defend on an isolated network. Teams are scored on both their success in defending their assigned machine and on their success in attacking the other team's machines. Depending on the nature of the particular CTF game, teams may either be attempting to take an opponent's flag from their machine or teams may be attempting to plant their own flag on their opponent's machine. Two of the more prominent attack/defense CTF's are held every year at DEF CON, the largest hacker conference, and the NYU-CSAW (Cyber Security Awareness Week), the largest student cyber-security contest.


Hardware challenges usually involve getting a unknown piece of hardware and having to figure out how to bypass part of the security, e.g. using debugging ports or using a Side-channel attack.


Jeopardy!-style competitions usually involve multiple categories of problems, each of which contains a variety of questions of different point values and difficulties. Teams attempt to earn the most points in the competition's time frame (for example 24 hours), but do not directly attack each other. Rather than a race, this style of game play encourages taking time to approach challenges and prioritizes quantity of correct submissions over the timing.


There is a fourth type of CTF, most commonly referred to as King of the Hill (KotH). King of the Hill is similar to Attack/Defend, but instead of everyone having their own machine (or small network) to defend, there are only preconfigured ones, which require all teams to exploit them. Once your team has successfully taken over the machine, the focus shifts to defending the machine from other teams attacks. Score is usually determined by a score reporting service on the machine, that reports a team token. When one team is able to gain access, they will remove the other teams token, and insert their own, thus making them the King of the Hill.

###### source\\\\[wikipedia](https://en.wikipedia.org/wiki/Capture_the_flag#Software_and_games)

# Categories
---

## Web Exploitation
> In the web tasks, you have to discover weaknesses in different web sites and services. Most of the tasks are done in your web browser. Common web tasks include SQL-injections, XSS, input sanitation.

### SITES
- https://trailofbits.github.io/ctf/web/exploits.html

### PDFS
- https://picoctf.org/learning_guides/Book-3-Web-Exploitation.pdf

### TOOLS
DevTools in web browser
- https://portswigger.net/burp
- https://www.telerik.com/fiddler
- https://beautifier.io/
- https://github.com/swisskyrepo/PayloadsAllTheThings
- https://csp-evaluator.withgoogle.com/
- https://requestbin.com/

---

## Steganography
> Steganography or "stego" is essentially just hiding information in another file, where both the file used to hide and the information hidden can be whatever you want.

### SITES
- https://ctf101.org/forensics/what-is-stegonagraphy/

### PDFS

### TOOLS
- https://www.audacityteam.org/
- https://www.sonicvisualiser.org/
- https://academo.org/demos/spectrum-analyzer/
- https://github.com/zardus/ctf-tools/tree/master/stegsolve
- https://github.com/zed-0xff/zsteg
- https://github.com/DominicBreuker/stego-toolkit

---

## Cryptography
> Crypto is short for cryptography, where information is protected by encrypting it (some kind of transformation) into an unreadable format, also referred to as the cipher text. The cipher text may only be read by the ones possessing the secret key to decipher or decrypt it.

### SITES
- https://tghack.no/page/crypto-tutorial

### PDFS
- https://kopimi.datapor.no/books/applied_cryptography_protocols_algorithms_and_source_code_in_c.pdf
- https://kopimi.datapor.no/books/Understanding_Cryptography.pdf
- https://picoctf.org/learning_guides/Book-2-Cryptography.pdf

### TOOLS
- Sagemath
- https://github.com/Legrandin/pycryptodome
- https://github.com/Gallopsled/pwntools
- https://gchq.github.io/CyberChef/

---

## Binary Exploitation (pwn)
> Binary exploitation or often called "pwn" is the art of abusing and exploiting binaries to do unintended things.  You have to discover vulnerabilities and leverage them to gain remote code execution.

### SITES
- https://tghack.no/page/shellcoding-tutorial
- https://github.com/r0hi7/BinExp

### PDFS
- https://www.uio.no/studier/emner/matnat/ifi/IN5290/h18/lectures/inf5290-2018-l08-binary-exploitation_1.pdf
- https://www.uio.no/studier/emner/matnat/ifi/IN5290/h18/lectures/inf5290-2018-l09-binary-exploitation_2.pdf
- https://picoctf.org/learning_guides/Book-5-Binary-Exploitation.pdf

### TOOLS
- gdb
- https://github.com/longld/peda
- ltrace
- strace
- https://github.com/Gallopsled/pwntools

---
## Reverse Engineering
> Reverse engineering is the act of picking apart a system to figure out how it works. In this category you will have to discover how different programs work to recover hidden flags and other information.


### SITES
- https://tghack.no/page/re-tutorial
- https://ctf101.org/reverse-engineering/overview/
- https://medium.com/@amustaque97/demystify-reverse-engineering-ctf-challenge-blade-40c45e7933c0

### PDFS
- https://kopimi.datapor.no/books/Reversing_Secrets_of_Reverse_Engineering.pdf
- https://kopimi.datapor.no/books/practical_reverse_engineering_x86_x64_arm_windows_kernel_reversing_tools_and_obfuscation.pdf
- https://kopimi.datapor.no/books/Practical_Malware_Analysis.pdf
- https://picoctf.org/learning_guides/Book-6-Reversing.pdf

### TOOLS
- https://ghidra-sre.org/
- https://www.hex-rays.com/products/ida/support/download/
- https://onlinedisassembler.com/static/home/
- https://retdec.com/
- https://binary.ninja/demo/
- https://x64dbg.com/#start
- https://github.com/radareorg/cutter
- https://angr.io/
- strings


## Forensics
> In forensics, you must investigate the files to find hiddes clues and messages. The files can be packet captures from network traffic, or any other file such as pictures, zipped files, or text files.

### SITES
- https://www.amanhardikar.com/mindmaps/ForensicChallenges.html
- https://trailofbits.github.io/ctf/forensics/

### PDFS
- https://kopimi.datapor.no/books/art_of_memory_forensics_detecting_malware_and_threats_in_windows_linux_and_mac_memory.pdf
- https://picoctf.org/learning_guides/Book-4-Forensics.pdf

### TOOLS
- https://www.wireshark.org/docs/man-pages/wireshark.html
- https://www.wireshark.org/docs/man-pages/tshark.html
- https://www.tcpdump.org/manpages/tcpdump.1.html
- https://scapy.readthedocs.io/en/latest/introduction.html
- https://tools.kali.org/forensics/foremost
- https://www.sleuthkit.org/sleuthkit/download.php
- https://github.com/volatilityfoundation/volatility

---

## Misc
> Miscellaneous or "misc" is often just tasks that don't fit into one of the other more established categories. These tasks often require a little programming knowledge and can be a good start if you have a programming background.

### SITES

### PDFS
https://picoctf.org/learning_guides/Book-1-General-Skills.pdf

### TOOLS
- https://github.com/Z3Prover/z3
- https://github.com/Gallopsled/pwntools
- https://www.wolframalpha.com/