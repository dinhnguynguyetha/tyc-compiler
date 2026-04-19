"""
Static Semantic Checker for TyC Programming Language

This module implements a comprehensive static semantic checker using visitor pattern
for the TyC procedural programming language. It performs type checking,
scope management, type inference, and detects all semantic errors as
specified in the TyC language specification.
"""
from functools import reduce
from typing import (
    Dict,
    List,
    Set,
    Optional,
    Any,
    Tuple,
    NamedTuple,
    Union,
    TYPE_CHECKING,
)
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    ASTNode,
    Program,
    StructDecl,
    MemberDecl,
    FuncDecl,
    Param,
    VarDecl,
    IfStmt,
    WhileStmt,
    ForStmt,
    BreakStmt,
    ContinueStmt,
    ReturnStmt,
    BlockStmt,
    SwitchStmt,
    CaseStmt,
    DefaultStmt,
    Type,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    BinaryOp,
    PrefixOp,
    PostfixOp,
    AssignExpr,
    MemberAccess,
    FuncCall,
    Identifier,
    StructLiteral,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    ExprStmt,
    Expr,
    Stmt,
    Decl,
)

# Type aliases for better type hints
TyCType = Union[IntType, FloatType, StringType, VoidType, StructType]
from .static_error import (
    StaticError,
    Redeclared,
    UndeclaredIdentifier,
    UndeclaredFunction,
    UndeclaredStruct,
    TypeCannotBeInferred,
    TypeMismatchInStatement,
    TypeMismatchInExpression,
    MustInLoop,
)

#support class
class UnknownType(Type):
    def __str__(self):
        return "Unknown"

class Symbol:
    def __init__(self, name: str, typ: Type, kind: str):
        self.name = name
        self.typ = typ
        self.kind = kind 


class StaticChecker(ASTVisitor):
    
    # --- HELPER METHODS ---
    
    def lookup(self, name: str, o: List[Dict], stop_at_func: bool = False) -> Symbol:
        """Tìm kiếm symbol từ scope trong cùng ra ngoài cùng"""
        for scope in reversed(o):
            if name in scope:
                return scope[name]
            if stop_at_func and scope.get("___is_func_scope___"):
                break
        return None

    def __init__(self, ast):
        self.ast = ast
        self.o = [{
            "readInt": Symbol("readInt", IntType(), "Function"),
            "readFloat": Symbol("readFloat", FloatType(), "Function"),
            "readString": Symbol("readString", StringType(), "Function"),
            "printInt": Symbol("printInt", VoidType(), "Function"),
            "printFloat": Symbol("printFloat", VoidType(), "Function"),
            "printString": Symbol("printString", VoidType(), "Function"),
        }]
        self.loop_depth = 0
        self.switch_depth = 0

    def check(self):
        return self.visit(self.ast, self.o)

    def visit_program(self, node: "Program", o: Any = None):
        for decl in node.decls:
            name = decl.name
            if isinstance(decl, FuncDecl):
                if name in o[0]:
                    raise Redeclared("Function", name) 
                o[0][name] = Symbol(name, decl.return_type, "Function")
            elif isinstance(decl, StructDecl):
                if name in o[0]:
                    raise Redeclared("Struct", name) 
                o[0][name] = Symbol(name, StructType(name), "Struct")

        for decl in node.decls:
            self.visit(decl, o)
            
        return "Static checking passed"

    def visit_struct_decl(self, node: "StructDecl", o: Any = None):
        

    def visit_member_decl(self, node: "MemberDecl", o: Any = None):
        pass

    def visit_func_decl(self, node: "FuncDecl", o: Any = None):
        local_o = o + [{"___is_func_scope___": True}] 
        
        for param in node.params:
            self.visit(param, local_o)
            
        self.visit(node.body, local_o)

    def visit_param(self, node: "Param", o: Any = None):
        if node.name in o[-1]:
            raise Redeclared("Parameter", node.name) #
        o[-1][node.name] = Symbol(node.name, node.typ, "Parameter")

    # Type system
    def visit_int_type(self, node: "IntType", o: Any = None):
        pass

    def visit_float_type(self, node: "FloatType", o: Any = None):
        pass

    def visit_string_type(self, node: "StringType", o: Any = None):
        pass

    def visit_void_type(self, node: "VoidType", o: Any = None):
        pass

    def visit_struct_type(self, node: "StructType", o: Any = None):
        pass

    # Statements
    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        block_env = o + [{}]
        for stmt in node.stmts:
            self.visit(stmt, block_env)

    def visit_var_decl(self, node: "VarDecl", o: Any = None):
        param_check = self.lookup(node.name, o, stop_at_func=True)
        if param_check and param_check.kind == "Parameter":
            raise Redeclared("Variable", node.name)
            
        if node.name in o[-1]:
            raise Redeclared("Variable", node.name) #

        var_type = node.typ if node.typ else UnknownType()
        
        if node.init:
            init_type = self.visit(node.init, o)
            if not isinstance(var_type, UnknownType):
                if type(var_type) != type(init_type):
                    raise TypeMismatchInStatement(node)
            else:
                var_type = init_type 

        o[-1][node.name] = Symbol(node.name, var_type, "Variable")

    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        cond_type = self.visit(node.cond, o)
        if not isinstance(cond_type, IntType):
            raise TypeMismatchInStatement(node) #
        
        self.visit(node.tstmt, o)
        if node.fstmt:
            self.visit(node.fstmt, o)

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        pass

    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        pass

    def visit_switch_stmt(self, node: "SwitchStmt", o: Any = None):
        pass

    def visit_case_stmt(self, node: "CaseStmt", o: Any = None):
        pass

    def visit_default_stmt(self, node: "DefaultStmt", o: Any = None):
        pass

    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        pass

    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        pass

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        pass

    def visit_expr_stmt(self, node: "ExprStmt", o: Any = None):
        self.visit(node.expr, o)

    # Expressions
    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        pass

    def visit_prefix_op(self, node: "PrefixOp", o: Any = None):
        pass

    def visit_postfix_op(self, node: "PostfixOp", o: Any = None):
        pass

    def visit_assign_expr(self, node: "AssignExpr", o: Any = None):
        pass

    def visit_member_access(self, node: "MemberAccess", o: Any = None):
        pass

    def visit_func_call(self, node: "FuncCall", o: Any = None):
        pass

    def visit_identifier(self, node: "Identifier", o: Any = None):
        pass

    def visit_struct_literal(self, node: "StructLiteral", o: Any = None):
        pass

    # Literals
    def visit_int_literal(self, node: "IntLiteral", o: Any = None):
        pass

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        pass

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        pass