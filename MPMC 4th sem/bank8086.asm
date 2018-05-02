include 'emu8086.inc'
data segment
    
    password db '12345h';
    message1 db 10,13,10,13, 'Enter the 5 characters long pin to proceed: $';
    amt dw ?
data ends

stack segment 
    dw 100 dup(0);
    topPtr label word;
stack ends

display macro message
    mov ah, 09h
    lea dx, message
    int 21h       
endm 

currentAmt macro amt 
        mov cx, 04h
        mov dx, amt
        rol dl, 04h
        rol dh, 04h
        ror dx, 08h
        mov amt, dx
    printWhole: 
        mov dx, amt
        and dl, 0Fh
        add dl, 30h
        mov ah, 02h
        int 21h  
        mov dx, amt
        shr dx, 04h
        mov amt, dx
        loop printWhole 
        print 10
        print 13
        
endm

code segment
    assume cs:code, ds:data, ss:stack
    
    start:
        
        mov ax, data
        mov ds, ax
        mov es, ax  
        
        mov ax, stack
        mov ss, ax
        mov sp, offset topPtr
        print 'WELCOME TO THE BANK'
        display message1
        
        mov cx, 05h
        mov bx, offset password


    again:
        mov ah, 08h
        int 21h
        cmp al, [bx]
        jne l1
        inc bx
        loop again
        cmp cx, 00h
        jz passwordMatched
    
    l1:
        print 'Password did not match'
        mov dx, 0bedah;
        jmp didntMatch
        
    passwordMatched:
        print 'Password matched'
        print 10
        print 13
        print 'Choose from given options:'
        mov ax, 0000h
        jmp bankActions   
        
    didntMatch:
        mov     al, 182         ; meaning that we're about to load
        out     43h, al         ; a new countdown value
    
        mov     ax, 9999h        ; countdown value is stored in ax. It is calculated by 
                                ; dividing 1193180 by the desired frequency (with the
                                ; number being the frequency at which the main system
                                ; oscillator runs
        out     42h, al         ; Output low byte.
        mov     al, ah          ; Output high byte.
        out     42h, al               
    
        in      al, 61h         
                                ; to connect the speaker to timer 2
        or      al, 00000011b  
        out     61h, al         ; Send the new value   
    
    bankActions:
        print 10
        print 13
        print 'Your current balance is: '
        mov amt, ax
        currentAmt amt
    
        print 10
        print 13
        print 'Press 1 to withdraw'
        print 10
        print 13
        print 'Press 2 to deposit'
        print 10
        print 13
        print 'Press 0 to quit'
        
        
        mov ah, 01h
        int 21h       
        sub al, 30h
        cmp al, 01h
        jz withdraw
        cmp al, 02h
        jz deposit
        cmp al, 00h
        jz quitBank
 
           
    notValid:
        print 10
        print 13
        print 'You didnt choose a valid option, try again.'
        jmp bankActions:
        
        
    withdraw:
        print 10
        print 13
        print 'Enter amount to withdraw: '
        mov ah, 01h
        int 21h
        sub al, 30h
        mov bl, al
        mov ax, amt
        sub al, bl     
        mov amt, ax
        jmp bankActions
        
        
        
    deposit:
        print 10
        print 13
        print 'Enter amount to add: '
        mov ah, 01h
        int 21h
        sub al, 30h
        mov bl, al
        mov ax, amt
        add al, bl     
        mov amt, ax
        jmp bankActions
    
    quitBank:
        print 'Bye '    
     
        
            
code ends
    end start