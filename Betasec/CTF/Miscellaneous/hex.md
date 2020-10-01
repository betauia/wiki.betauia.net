# Hex
decode hex in bash:
`echo "HEXVALUE" | xxd -r -p`

decode hex to ascii in python:
`"57".decode("hex")`

xxd - make a hexdump or do the reverse
hexdump to binary
`xxd -r FILE > out`

binary to hexdump
`xxd FILE`
then check which filetype the file is

hexedit (view and edit hexdump)
`hexedit FILE`

online tool that allows you to modify the hexadecimal and binary values of an uploaded file. This is a good tool for correcting files with a corrupt magic number
https://hexed.it/