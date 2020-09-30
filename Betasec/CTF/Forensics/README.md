# Forensics

Detective work.

### General forensics
Magic Numbers: The starting values that identify a file format. These are often crucial for programs to properly read a certain file type, so they must be correct. If some files are acting strangely, try verifying their magic number with a trusted list of file signatures.
https://en.wikipedia.org/wiki/List_of_file_signatures

command-line tool to carve files out of another file:
binwalk
`binwalk e file`

command-line tool, used to recover deleted files from a file system image. Handy to use if given a .dd and .img file etc:

TestDisk
>https://www.cgsecurity.org/wiki/TestDisk_Download

`readelf -s BINARY`

disk image:
`sudo losetup -f -P disk.img`
`sudo mount /dev/loop0 /mnt/temp`