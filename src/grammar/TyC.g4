grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// TODO: Define grammar rules here
program: (structDecl | funcDecl)* EOF;

structDecl: STRUCT ID LBRACE structMem* RBRACE SEMI;
structMem: typeType ID SEMI;

varDecl: 
    AUTO ID ASSIGN expr SEMI
  | AUTO ID SEMI
  | typeType ID (ASSIGN expr)? SEMI
  ;

funcDecl: (typeType | VOID)? ID LP (paramList)? RP stmtBlock;

paramList: paramDecl (COMMA paramDecl)*;
paramDecl: typeType ID;

typeType: INT | FLOAT | STRING | ID; 

stmt: 
    varDecl
  | stmtBlock
  | ifStmt
  | whileStmt
  | forStmt
  | switchStmt
  | breakStmt
  | continueStmt
  | returnStmt
  | exprStmt
  ;

stmtBlock: LBRACE stmt* RBRACE;

ifStmt: IF LP expr RP stmt (ELSE stmt)?;

whileStmt: WHILE LP expr RP stmt;

forStmt: FOR LP (scalarVarDecl | assignExpr | ) SEMI (expr)? SEMI (assignExpr | expr)? RP stmt;
scalarVarDecl: (AUTO | typeType) ID (ASSIGN expr)?; 

switchStmt: SWITCH LP expr RP LBRACE (caseStmt | defaultStmt)* RBRACE;
caseStmt: CASE expr COLON stmt*;
defaultStmt: DEFAULT COLON stmt*;

breakStmt: BREAK SEMI;
continueStmt: CONTINUE SEMI;
returnStmt: RETURN expr? SEMI;
exprStmt: expr SEMI;

expr: expr1;

expr1: expr2 (ASSIGN expr1)?; 
assignExpr: expr2 ASSIGN expr1; 

expr2: expr3 (OR expr3)*;

expr3: expr4 (AND expr4)*;

expr4: expr5 ((EQUAL | NOT_EQUAL) expr5)*;

expr5: expr6 ((LESS | LESS_EQUAL | GREATER | GREATER_EQUAL) expr6)*;

expr6: expr7 ((ADD | SUB) expr7)*;

expr7: expr8 ((MUL | DIV | MOD) expr8)*;

expr8: 
    (SUB | ADD | NOT) expr8
  | (INC | DEC) expr8
  | expr9
  ;

expr9: 
    LP expr RP            
  | ID                 
  | literal                
  | expr9 DOT ID             
  | expr9 LP exprList? RP     
  | expr9 (INC | DEC)       
  ;

exprList: expr (COMMA expr)*;

literal: INTLIT | FLOATLIT | STRINGLIT | structLiteral;
structLiteral: LBRACE exprList? RBRACE;
AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
RETURN: 'return';
STRING: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
GREATER: '>';
LESS_EQUAL: '<=';
GREATER_EQUAL: '>=';
OR: '||';
AND: '&&';
NOT: '!';
INC: '++';
DEC: '--';
ASSIGN: '=';
DOT: '.';

LBRACE: '{';
RBRACE: '}';
LP: '(';
RP: ')';
SEMI: ';';
COMMA: ',';
COLON: ':';

FLOATLIT: 
    [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)?
  | '.' [0-9]+ ([eE] [+-]? [0-9]+)?
  | [0-9]+ [eE] [+-]? [0-9]+
  ;

INTLIT: [0-9]+; 

STRINGLIT: '"' ( ~["\\\r\n] | '\\' [bfnrt"\\] )* '"' { self.text = self.text[1:-1] };

ID: [a-zA-Z_] [a-zA-Z0-9_]*;

BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

WS : [ \t\r\n]+ -> skip ;

ERROR_CHAR: .;
ILLEGAL_ESCAPE: '"' ( ~["\\\r\n] | '\\' [bfnrt"\\] )* '\\' ~[bfnrt"\\];
UNCLOSE_STRING: '"' ( ~["\\\r\n] | '\\' [bfnrt"\\] )* [\r\n] | EOF;
