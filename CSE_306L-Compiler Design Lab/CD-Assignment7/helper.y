%
{
	#include "types.h"
	using namespace std;

	int scope = 0;
	int function_level = 0;
	int yylex(void);
	int undeclared = 0;
	extern int yylex();
	vector<string> ic;
	vector<vector<map<string, symbol_table_entry>>> big_symbol_table;
	map<string, function_table_entry> function_table;

	string active_function_name;
	string active_caller_function;
	function_table_entry temp_stack;

	void yyerror(char const *s)
	{
		printf("Parse error on line no.\n");
		exit(0);
	}

	bool is_already_declared(string name, map<string, function_table_entry> & function_table)
	{
		bool r = false;

		if (function_table.find(name) != function_table.end())
			r = true;

		return r;
	}

	bool is_symbol_already_declared(string name, int scope, int function_level, vector<vector<map<string, symbol_table_entry>>> &big_symbol_table)
	{
		bool r = false;
		vector<map<string, symbol_table_entry>>::iterator itr;
		if (big_symbol_table.size() > scope && big_symbol_table[scope].size() > function_level)
		{
			if (big_symbol_table[scope][function_level].find(name) != big_symbol_table[scope][function_level].end())
			{
				r = true;
			}
		}
		return r;
	}

	%
}

% union
{
	sidentifier *sid;
	sconstant *sconst;
	char charcter;
	int integer;
	float floating_point;
	str *sstr;
	SFUNCTION *FUNC_NAME;
	vec *svec;
}

	% token<sid> ID;
% token<sconst> VAL_INT VAL_FLOAT VAL_CHAR;
% token<integer> TOK_INT % token<charcter> TOK_CHAR % token<floating_point> TOK_FLOAT % token VOID % token IF % token WHILE % token ELSE % token STRUCT % token<str> LOGICAL_OR;
% token<str> LOGICAL_AND;
% token<str> LOGICAL_NOT;
% token<str> IS_EQUAL_TO;
% token<str> IS_NOT_EQUAL_TO;
% token<str> BITWISE_NOT % token<str> BITWISE_AND % token<str> BITWISE_OR % token<str> ASSIGN;
% token<charcter> GREATER_EQUAL;
% token<charcter> GREATER_THAN;
% token<charcter> LESS_EQUAL;
% token<charcter> LESS_THAN;
% token<charcter> OPEN_BRACKET;
% token<charcter> CLOSE_BRACKET;
% token<charcter> OPEN_PAR;
% token<charcter> CLOSE_PAR;

% type<FUNC_NAME> func_name;
% type<sstr> type;
% type<svec> param_list;
% type<sid> expression;
% type<sid> term;
% type<sid> sub_expression;
% type<FUNC_NAME> func_decl_body;

% left BITWISE_OR BITWISE_AND BITWISE_NOT % left '*' '/' % left '+' '-'

	% start S;

% %
		S : afunction
	| global_variables;

afunction : func_decl_body blocked_body{

			}

			;

func_decl_body : type ID
{

	//fill the function_table_entry that this sfunction needs
	function_table_entry temp;
	temp.type_returned = $1->x;
	temp.function_scope_number = scope;
	scope++; // to store the next function

	active_function_name = ($2)->name;

	if (is_already_declared(($2)->name, function_table))
	{
		cout << "the function has alredy been declared in the scope" << endl;
	}
	else // add the function to the function table
	{

		function_table[($2)->name] = temp;
	}
}

'(' eps param_list ')';

blocked_body : '{' func_body '}';
eps : {

	  };

;

param_list : type ID
{
	symbol_table_entry temp;
	temp.is_init = false;
	temp.level = function_level;

	if (is_symbol_already_declared(($2)->name, scope, function_level, big_symbol_table))
	{
		cout << "The symbol has already been declared in this scope" << endl;
	}
	else
	{
		big_symbol_table[scope][function_level][($2)->name] = temp;

		map<string, symbol_table_entry>::iterator itr;
		itr = big_symbol_table[scope][function_level].find(($2)->name);
		($$)->parameters_list.push_back(itr);

		function_table[active_function_name].params.push_back(itr);
	}
}
| param_list ',' type ID
{
	symbol_table_entry temp;
	temp.is_init = false;
	temp.level = function_level;

	if (is_symbol_already_declared(($4)->name, scope, function_level, big_symbol_table))
	{
		cout << "The symbol has already been declared in this scope" << endl;
	}
	else
	{
		big_symbol_table[scope][function_level][($4)->name] = temp;
		symbol_table_pointer itr;
		itr = big_symbol_table[scope][function_level].find(($4)->name);
		($$)->parameters_list = ($1)->parameters_list;
		($$)->parameters_list.push_back(itr);

		function_table[active_function_name].params.push_back(itr);
	}
};

func_body : statements;

statements : statement | statements statement;


statement : decl_statement ';' | assign_statement ';' | if_statement | while_statement | '{' statement '}';

decl_statement : type identifier_list;

type : TOK_INT { $$->x = "int"; }
| TOK_FLOAT { $$->x = "float"; }
| TOK_CHAR { $$->x = "char"; }
| VOID { $$->x = "void"; };

identifier_list : is_equal_to_stmt{

				  } |
				  identifier_list ',' is_equal_to_stmt | ID array_list;

is_equal_to_stmt : ID '=' expression
{

	// //check if the ID is already defined ridicously

	if (is_symbol_already_declared(($1)->name, scope, function_level, big_symbol_table))
	{
		cout << "The symbol has already been declared in this scope" << endl;
	}
	else
	{

		*($1) = *($3);
		//add this vairable in symbol table
		symbol_table_entry temp;
		temp.is_init = false;
		temp.level = function_level;
		//add value also to the symbol table entry
		if (($3)->is_int == true)
		{
			temp.type = "int";
			temp.val = ($3)->int_val;
		}
		else if ($3->is_char == true)
		{
			temp.type = "char";
			temp.val = ($3)->char_val;
		}
		else if ($3->is_float == true)
		{
			temp.type = "float";
			temp.val = ($3)->float_val;
		}
		big_symbol_table[scope][function_level][($1)->name] = temp;
	}
}

|
	;

array_list : '[' VAL_INT ']' | '[' VAL_INT ']' array_list;

// for assign_statement
assign_statement : single_assignment | single_assignment ',' assign_statement;

single_assignment : ID '=' expression | ID array_list '=' expression | ID structure_referencing '=' expression;

structure_referencing : '.' ID | '.' ID structure_referencing;

// writing expression without ambiguity
expression : expression '*' term
{
	//check the coercibility
	int t1 = 0, t2 = 0;
	if (($1)->is_int == true)
		t1 = 1;
	if (($1)->is_char == true)
		t1 = 2;
	if (($1)->is_float == true)
		t1 = 3;

	if (($3)->is_int == true)
		t2 = 1;
	if (($3)->is_char == true)
		t2 = 2;
	if (($3)->is_float == true)
		t2 = 3;

	if (t1 != t2)
	{
		cout << "Type mismatch during the multiplication of" << ($1)->val << "and" << ($3)->val << endl;
	}
	else
	{
		//do the semantic analysis
		$$ = new sidentifier;
		*($$) = *($1);
		if (t1 == 1)
		{
			($$)->int_val = ($1)->int_val * ($3)->int_val;
		}

		if (t1 == 2)
		{
			yyerror("Two charcters cannot be multiplied \n");
		}
		else if (t1 == 3)
		{
			($$)->float_val = ($1)->float_val * ($3)->float_val;
		}
	}
}
| expression '/' term
{
	//check the coercibility
	int t1 = 0, t2 = 0;
	if (($1)->is_int == true)
		t1 = 1;
	if (($1)->is_char == true)
		t1 = 2;
	if (($1)->is_float == true)
		t1 = 3;

	if (($3)->is_int == true)
		t2 = 1;
	if (($3)->is_char == true)
		t2 = 2;
	if (($3)->is_float == true)
		t2 = 3;

	if (t1 != t2)
	{
		cout << "Type mismatch during the division of" << ($1)->val << "and" << ($3)->val << endl;
	}
	else
	{
		//do the semantic analysis
		$$ = new sidentifier;
		*($$) = *($1);
		if (t1 == 1)
		{
			($$)->int_val = int((($1)->int_val) / (($3)->int_val));
		}

		if (t1 == 2)
		{
			($$)->char_val = char(int(($1)->char_val) + int(($3)->char_val));
		}
		else if (t1 == 3)
		{
			($$)->float_val = ($1)->float_val + ($3)->float_val;
		}
	}
}
| expression '+' term
{
	//check the coercibility
	int t1 = 0, t2 = 0;
	if (($1)->is_int == true)
		t1 = 1;
	if (($1)->is_char == true)
		t1 = 2;
	if (($1)->is_float == true)
		t1 = 3;

	if (($3)->is_int == true)
		t2 = 1;
	if (($3)->is_char == true)
		t2 = 2;
	if (($3)->is_float == true)
		t2 = 3;

	if (t1 != t2)
	{
		cout << "Type mismatch during the addition of" << ($1)->val << "and" << ($3)->val << endl;
	}
	else
	{
		//do the semantic analysis
		$$ = new sidentifier;
		*($$) = *($1);
		if (t1 == 1)
		{
			($$)->int_val = ($1)->int_val + ($3)->int_val;
		}

		if (t1 == 2)
		{
			($$)->char_val = char(int(($1)->char_val) + int(($3)->char_val));
		}
		else if (t1 == 3)
		{
			($$)->float_val = ($1)->float_val + ($3)->float_val;
		}
	}
}

| expression '-' term

{
	//check the coercibility
	int t1 = 0, t2 = 0;
	if (($1)->is_int == true)
		t1 = 1;
	if (($1)->is_char == true)
		t1 = 2;
	if (($1)->is_float == true)
		t1 = 3;

	if (($3)->is_int == true)
		t2 = 1;
	if (($3)->is_char == true)
		t2 = 2;
	if (($3)->is_float == true)
		t2 = 3;

	if (t1 != t2)
	{
		cout << "Type mismatch during the subtraction of" << ($1)->val << "and" << ($3)->val << endl;
	}
	else
	{
		//do the semantic analysis
		$$ = new sidentifier;
		*($$) = *($1);
		if (t1 == 1)
		{
			($$)->int_val = ($1)->int_val + ($3)->int_val;
		}

		if (t1 == 2)
		{
			($$)->char_val = char(int(($1)->char_val) - int(($3)->char_val));
		}
		else if (t1 == 3)
		{
			($$)->float_val = ($1)->float_val + ($3)->float_val;
		}
	}
}
| '(' expression ')'

{
	$$ = new sidentifier;
	*($$) = *($2);
}

| term
{
	// 					just allocate the attributes of term to expression
	$$ = new sidentifier;
	*($$) = *($1);
}

;

term : VAL_INT
{
	$$ = new sidentifier;
	$$->is_int = true;
	$$->type = "int";
	$$->int_val = ($1)->int_val;
}

| VAL_FLOAT
{
	$$ = new sidentifier;
	$$->is_float = true;
	$$->type = "float";
	$$->float_val = ($1)->float_val;
}

| VAL_CHAR
{
	$$ = new sidentifier;
	$$->is_char = true;
	$$->type = "char";
	$$->char_val = ($1)->char_val;
}

| ID
{
	$$ = new sidentifier;
	*$$ = *$1;
}
| function_call
{
	$$ = new sidentifier;
	$$->type = function_table[active_caller_function].type_returned;
	if ($$->type == "int ")
		$$->is_int = true;
	else if ($$->type == "float")
		$$->is_float = true;
	else if ($$->type == "char")
		$$->is_char = true;
};

// expression : term
// 				{
// 					just allocate the attributes of term to expression
// 					$$.sid = new sid;
// 					*($$.sid) = *($1.sid);
// 				}

// 			|expression '+' term

// 				{
// 					//check the coercibility
// 					 int t1=0 , t2=0;
// 					 if(($1.sid)->is_int == true)	t1=1;
// 					 if(($1.sid)->is_char == true)	t1=2;
// 					 if(($1.sid)->is_float == true)	t1=3;

// 					if(($3.sid)->is_int == true)	t2=1;
// 					 if(($3.sid)->is_char == true)	t2=2;
// 					 if(($3.sid)->is_float == true)	t2=3;

// 					 if(t1!=t2)
// 					 {
// 					 	cout << "Type mismatch during the addition of" << ($1.sid)->val << "and" << ($3.sid)->val << endl;
// 					 }
// 					 else
// 					 {
// 					 	//do the semantic analysis
// 					 	$$.sid = new sid;
// 					 	*($$.sid) = *($1.sid);
// 						if(t1==1)
// 						{
// 							($$.sid)-> int_val = ($1.sid)->int_val + ($3.sid)->int_val ;
// 						}

// 						if(t1==2)
// 						{
// 							($$.sid)-> char_val = char(int(($1.sid)->char_val) + int(($3.sid)->char_val)) ;
// 						}
// 						else if(t1==3)
// 						{
// 							($$.sid)-> float_val = ($1.sid)->float_val + ($3.sid)->flaot_val ;
// 						}

// 					 }

// 				}

// 			;

// term :  sub_expression
// 		{
// 			//just allocate the attributes of term to expression
// 			$$.sid = new sid;
// 			*($$.sid) = *($1.sid);
// 		}

// 		|term '*' sub_expression
// 		{
// 			 int t1=0 , t2=0;
// 					 if(($1.sid)->is_int == true)	t1=1;
// 					 if(($1.sid)->is_char == true)	t1=2;
// 					 if(($1.sid)->is_float == true)	t1=3;

// 					if(($3.sid)->is_int == true)	t2=1;
// 					 if(($3.sid)->is_char == true)	t2=2;
// 					 if(($3.sid)->is_float == true)	t2=3;

// 					 if(t1!=t2)
// 					 {
// 					 	cout << "Type mismatch during the addition of" << ($1.sid)->val << "and" << ($3.sid)->val << endl;
// 					 }
// 					 else
// 					 {
// 					 	//do the semantic analysis
// 					 	$$.sid = new sid;
// 					 	*($$.sid) = *($1.sid);
// 						if(t1==1)
// 						{
// 							($$.sid)-> int_val = ($1.sid)->int_val + ($3.sid)->int_val ;
// 						}

// 						if(t1==2)
// 						{
// 							cout << "two charcters cannot be multiplied " <<endl;
// 						}
// 						else if(t1==3)
// 						{
// 							($$.sid)-> float_val = ($1.sid)->float_val + ($3.sid)->float_val ;
// 						}

// 					}
// 			}

// 		| function_call
// 		{
// 			$$ = new sid;
// 			$$->type = function_table[active_caller_function].type_returned;
// 		}
// 		;

// sub_expression : '(' expression ')'
// 				{
// 					$$.sid = new sid;
// 					*($$.sid) = *($1.sid);
// 				}

// 			 | BITWISE_NOT expression
// 			 | expression BITWISE_OR expression
// 			 | expression BITWISE_AND expression
// 			 | ID
// 			 | VAL_INT
// 			 {
// 			 	$$ = new sid;
// 			 	$$.is_int= true;
// 			 	$$.int_val = ($1.sconst).int_val;
// 			 }

// 			 | VAL_FLOAT
// 			 {
// 			 	$$ = new sid;
// 			 	$$.is_float = true;
// 			 	$$.float_val = ($1.sconst).float_val;
// 			 }

// 			 | VAL_CHAR
// 			 {
// 			 	$$ = new sid;
// 			 	$$.is_char = true;
// 			 	$$.char_val = ($1.sconst).char_val;
// 			 }
// 			 ;

// for ifstatement
if_statement : IF '(' expression ')' '{' statements '}' else_expression;

else_expression : ELSE '{' statements '}' |
	;

// while statement
while_statement : WHILE '(' expression ')' '{' statements '}';

//for function call
function_call : ID '(' function_call_parameters ')' ';'
{
	// check if the function exists in the function table
	active_caller_function = ($1)->name;

	if (function_table.find(active_caller_function) == function_table.end())
	{
		cout << "the function has not been declared" << endl;
	}
	else
	{
		//match details of function_call_parameter and function_table_entry
		for (int i = 0; i < temp_stack.params.size(); i++)
		{
			if (temp_stack.params[i]->second.type != function_table[active_caller_function].params[i]->second.type)
			{
				yyerror("parameters passed mismatch with function declaration \n");
			}
		}
	}
}

;

function_call_parameters : ID
{
	if (big_symbol_table[scope][function_level].find($1->name) ==
		big_symbol_table[scope][function_level].end())
	{
		cout << " The parameter is not declared" << endl;
		yyerror("-");
	}
	else
	{
		map<string, symbol_table_entry>::iterator itr;
		itr = big_symbol_table[scope][function_level].find($1->name);
		temp_stack.params.push_back(itr);
	}
}
| function_call_parameters ',' ID
{
	if (big_symbol_table[scope][function_level].find($3->name) ==
		big_symbol_table[scope][function_level].end())
	{
		cout << " The parameter is not declared" << endl;
		yyerror("-");
	}
	else
	{
		map<string, symbol_table_entry>::iterator itr;
		itr = big_symbol_table[scope][function_level].find($3->name);
		temp_stack.params.push_back(itr);
	}
}

;

// for declaring structres
// later consider assiging structs also in assign_statement

astructure : STRUCT struct_name '{' structure_body '}' ';';

struct_name : ID;

structure_body : structure_statements;

structure_statements : structure_statement | structure_statement structure_statements

													 structure_statement : decl_statement ';'

																		   //declaring global variables

																		   global_variables : decl_statement ';'

																							  %
																							  %
																							  int main(int argc, char *argv[])
{
	return yyparse();

	;
}

== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
#include <bits/stdc++.h>
#include "types.h"
																																								using namespace std;

bool is_already_declared(string name, map<string, func_table_entry> &function_table)
{
	bool r = false;

	if (function_table.find(name) != function_table.end())
		r = true;

	return r;
}

bool is_symbol_already_declared(string name, int scope, int function_level, vector<vector<map<string, symbol_table_entry>>> &big_symbol_table)
{
	bool r = false;
	vector<map<string, symbol_table_entry>>::iterator itr;
	//check if scope and function level are reached to not get segmentation fault -_-
	if (big_symbol_table.size() > scope && big_symbol_table[scope].size() > function_level)
	{
		if (big_symbol_table[scope][function_level].find(name) != big_symbol_table[scope][function_level].end())
		{
			r = true;
		}
	}
	return r;
}

== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
#include <bits/stdc++.h>
																																							 using namespace std;

typedef struct str
{
	string x;
} str;

typedef struct symbol_table_entry
{
	string val; // dont use this

	int int_val;
	char char_val;
	float float_val;

	bool is_init;
	int level; //scope
	string type;

} symbol_table_entry;

#define symbol_table_pointer map<string, symbol_table_entry>::iterator

typedef struct function_table_entry
{
	vector<symbol_table_pointer> params;
	vector<int> variables;
	string type_returned;
	int function_scope_number;
} function_table_entry;

#define function_table_pointer vector<map<string, function_table_entry>>::iterator

struct sidentifier
{
	string type;

	string name;
	bool is_int;
	bool is_char;
	bool is_float;

	int int_val;
	char char_val;
	float float_val;

	string val; // this stores any value

	bool is_array;
	int array_inset;
	int array_offset;
	symbol_table_pointer st_ptr;

	sidentifier()
	{
		is_int = false;
		is_char = false;
		is_float = false;
	}
};
// typedef struct sidentifier sidentifier;

struct SFUNCTION
{
	string name;
	function_table_entry func_details;
	int scope_as_fnptr;
};

struct sconstant
{
	string name;
	bool is_int;
	bool is_float;
	bool is_char;

	int int_val;
	char char_val;
	float float_val;

	string val; //to store the value irrespective of the type

	sconstant()
	{
		is_int = false;
		is_float = false;
		is_char = false;
	}
};

struct vec
{
	vector<symbol_table_pointer> parameters_list;
};

== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
s : make clean
make execute
execute : yacc -
d grammar.y
lex parser.l
g++ --std = c++ 11 - g lex.yy.c y.tab.c - o compiler
clean : rm -
rf lex.yy.c y.tab.c y.tab.h compiler
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
%
{
#include <bits/stdc++.h>
#include "types.h"
#include "y.tab.h"
	using namespace std;
	int line_no = 1;
	%
}

digits[0 - 9] +
alpha_numeric[A - Za - z_][A - Za - z_0 - 9] *
float_num[+-]
? [0 - 9] * "."[0 - 9] +
chars[A - Za - z]
% %
"||"
{
	return LOGICAL_OR;
}
"&&" { return LOGICAL_AND; }
"==" { return IS_EQUAL_TO; }
"!=" { return IS_NOT_EQUAL_TO; }
"=" { return ASSIGN; }
">=" { return GREATER_EQUAL; }
">" { return GREATER_THAN; }
"<=" { return LESS_EQUAL; }
"<" { return LESS_THAN; }

"{" { return OPEN_BRACKET; }
"}" { return CLOSE_BRACKET; }
"(" { return OPEN_PAR; }
")" { return CLOSE_PAR; }
[% - +* / (){};
]
{ return yytext[0]; }

"~"
{
	return BITWISE_NOT;
}
"&&" { return BITWISE_AND; }
"||" { return BITWISE_OR; }
not { return LOGICAL_NOT; }
and { return LOGICAL_AND; }
or { return LOGICAL_OR; }
"int"
{
	cout << "read int " << line_no << endl;
	return TOK_INT;
}
"float" { return TOK_FLOAT; }
"char" { return TOK_CHAR; }
"void" { return VOID; }
"if" { return IF; }
"while" { return WHILE; }
"else" { return ELSE; }
"struct" { return STRUCT; }
{
	chars
}
{
	(yylval.sconst)->char_val = yytext[0];
	(yylval.sconst)->is_char = true;
	return VAL_CHAR;
}
{
	alpha_numeric
}
{
	cout << "read identifier " << line_no << endl;
	(yylval.sid)->name = yytext;
	return ID;
}
{
	float_num
}
{
	(yylval.sconst)->float_val = atof(yytext);
	(yylval.sconst)->is_float = true;
	return VAL_FLOAT;
}
{
	digits
}
{
	(yylval.sconst)->int_val = atoi(yytext);
	(yylval.sconst)->is_int = true;
	;
	return VAL_INT;
}
[;:\t\n] "\n" line_no++;
.cout << "Unexpected value at line " << line_no << endl;

% %
	int yywrap(void) { return 1; }

final_Submit.txt
	Displaying final_Submit.txt.