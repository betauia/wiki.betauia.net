# python

### inline (can be used as an argument to another program):
./program.c `python -c "print 0x1234+1"`

virtualenv:
`pip install virtualenv` or `apt install virtualen` (pipenv masterrace)
create virtualenv: virtualenv PATH
activate: `source PATH/bin/activate`
remove: `deactivate` and remove folder

web server: `python -m SimpleHTTPServer`
websever python3 : `python3 -m http.server`

convert python2 to python3: 2to3-3.7 `file.py -w`  (replace with version)

binary to int:
`int("01110101", 2)`   // base 2

int to hex:
`hex("3453453453")`   // [2:-1]  to remove zero at start

hex to string:
`hexstring.decode("hex")`

base32 decode:
`import base64`
`base64.b32decode("STRING")`