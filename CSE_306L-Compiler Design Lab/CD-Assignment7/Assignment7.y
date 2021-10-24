%{
#include <stdio.h>

int yylex();
int yyerror(char *s);

%}


$token STRING NUM OTHER SEMICOLON PIC