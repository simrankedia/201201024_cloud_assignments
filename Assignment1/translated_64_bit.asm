extern printf
section .text
global  _start
_start:
push rbp
mov rdi,fmt
mov rsi,msg
mov rax,0
call printf
pop rbp
mov rax,0
ret
section .data
msg:  db "Hello world", 0
fmt:  db "%s", 10, 0
