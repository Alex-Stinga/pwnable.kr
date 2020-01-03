# pwnable.kr

'pwnable.kr' is a wargame site which provides various pwn challenges regarding system exploitation. While playing pwnable.kr, you could learn/improve system hacking skills.

The challenges are divided into four categories.  

[Toddler's Bottle]  -  very easy challenges with simple mistakes.  
[Rookiss]  -  typical bug exploitation challenges for rookies.  
[Grotesque]  -  these challenges are grotesque-y. painful to solve it, but very tasty flag  
[Hacker's Secret]  -  intended solution for these challenges involves special techniques.  

Here are  my writeups of the challenges, starting with the easiest ones.

## Toddler's Bottle

#### fd
Mommy! what is a file descriptor in Linux?  
ssh fd@pwnable.kr -p 2222   
(pw:guest)  

We are given a hint, the file descriptor and the ssh login info.

According to wikipedia, a filed descriptor is a handler used to acces a file or other input/output resource. 
A file descriptor is a non-negative integer, generally represented in the C programming language as the type int (negative values being reserved  to indicate an error condition).
There are 3 types of file descriptors:  

| File          | Stram         | Int   |
| ------------- |:-------------:| -----:|
|standard input    |stdin    | 0
|standard output   | stdout |   1 |
|standard error| stderr |    2 |

