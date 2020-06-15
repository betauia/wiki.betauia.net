# Caesar's Cipher
Also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift. It's a substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.i

## Examples
A Caesar cipher using a left rotation of three places, equivalent to a right shift of 23 (the shift parameter is used as the key):

```
Plain:    ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cipher:   XYZABCDEFGHIJKLMNOPQRSTUVW
```

## Usage
Can easily be scripted in any language. Package bsdgames includes a easy-to-use tool.

```
sudo apt install bsdgames
echo hello | caesar 10
```

## Misc
One-liner to check all rotations:

```bash
cipher='entertexthere' ; for i in {0..25}; do echo $cipher | caesar $i; done
```

Remember to also check with all ascii characters (255).
