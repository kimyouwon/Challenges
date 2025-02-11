#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void admin_shell(){ 
printf("Access granted! Admin shell activated.\n"); 
char*args[] = {"/bin/sh", NULL}; 
execv(args[0], args); 
// 쉘 실행
}

void operation() {
 printf("You thought this was useful? Try again.\n");
}

int main() { 
	char buffer[64]; 
	void (*func)();
	 char key[16];
	 func = operation;

	 printf("KEY?: \n");
	 gets(buffer);
	 printf("You entered: %s\n", buffer);
	 if (strchr(key, 'A') == NULL) {
		 if (strlen(key) > 8){
			 if (key[strlen(key) - 1] != '1') {
				 printf("Authentication successful!\n");
				 func = admin_shell;
			 }
		 }
	 }
 func();
 return 0;
}

