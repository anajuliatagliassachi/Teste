#include <stdio.h>
#include <stdlib.h>

int main(){

char linha1[256];
char linha2[256];

FILE *fd;

fd = fopen("arq.txt","r");

if (fd==NULL){ 
  printf("Não foi possivel abrir o arquivo.\n"); 
  exit(1); 
}

fgets(linha1, 255, fd);
fgets(linha2, 255, fd);

int entrada;

scanf("%d",&entrada);
if (entrada == 1){
     printf("%s", linha1);
  } else {
    if (entrada == 2) {
       printf("%s", linha2);
      }
  else{
      printf("Entrada Invalida\n");
  }
  }
  
  printf("Bom dia!\n");

}
