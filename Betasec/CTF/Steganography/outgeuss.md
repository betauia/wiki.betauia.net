# outguess (encrypt/decrypt embeded image)
* To embed the message hidden.txt into the monkey.jpg image:
```bash
outguess -k  "my secret pass phrase" -d hidden.txt monkey.jpg out.jpg
```
* retrieve the hidden	message	from the image:
```bash
outguess -k "my secret pass phrase" -r out.jpg message.txt
```