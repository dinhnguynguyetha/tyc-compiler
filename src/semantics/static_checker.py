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
    def __init__(self, symbol=None):
        self.symbol = symbol
        
    def __str__(self):
        return "Unknown"

class Symbol:
    def __init__(self, name: str, typ: Type, kind: str, extra=None):
        self.name = name
        self.typ = typ
        self.kind = kind 
        self.extra = extra or {}


class StaticChecker(ASTVisitor):
    def lookup_var(self, name: str, o: List[Dict[str, Any]], stop_at_func: bool = False) -> Symbol:
        for scope in reversed(o):
            if name in scope:
                return scope[name]
            if stop_at_func and scope.get("___is_func_scope___"):
                break
        return None

    def match_type(self, t1: Type, t2: Type) -> bool:
        if type(t1) != type(t2): 
            return False
        if isinstance(t1, StructType) and isinstance(t2, StructType):
            return t1.name == t2.name
        return True

    def __init__(self, ast=None):
        self.ast = ast
        self.o = [{
            "func_readInt": Symbol("readInt", IntType(), "Function", {"params": []}),
            "func_readFloat": Symbol("readFloat", FloatType(), "Function", {"params": []}),
            "func_readString": Symbol("readString", StringType(), "Function", {"params": []}),
            "func_printInt": Symbol("printInt", VoidType(), "Function", {"params": [IntType()]}),
            "func_printFloat": Symbol("printFloat", VoidType(), "Function", {"params": [FloatType()]}),
            "func_printString": Symbol("printString", VoidType(), "Function", {"params": [StringType()]}),
        }]
        self.loop_depth = 0
        self.switch_depth = 0

    def check(self, ast=None):
        if ast is not None:
            self.ast = ast
        return self.visit(self.ast, self.o)

    def visit_program(self, node: "Program", o: Any = None):
        for decl in node.decls:
            if isinstance(decl, FuncDecl):
                if "func_" + decl.name in o[0]:
                    raise Redeclared("Function", decl.name)
                param_types = [p.typ for p in decl.params]
                func_sym = Symbol(decl.name, decl.return_type, "Function", {"params": param_types})
                o[0]["func_" + decl.name] = func_sym
                self.visit(decl, o)
                
            elif isinstance(decl, StructDecl):
                if "struct_" + decl.name in o[0]:
                    raise Redeclared("Struct", decl.name)
                struct_sym = Symbol(decl.name, StructType(decl.name), "Struct", {"members": {}})
                o[0]["struct_" + decl.name] = struct_sym
                self.visit(decl, o)
                
        return "Static checking passed"

    def visit_struct_decl(self, node: "StructDecl", o: Any = None):
        struct_sym = o[0]["struct_" + node.name]
        members_dict = {}
        for mem in node.members:
            if mem.name in members_dict:
                raise Redeclared("Member", mem.name)
            if not mem.typ:
                raise TypeCannotBeInferred(node)
                
            mem_type = self.visit(mem.typ, o)
            if isinstance(mem_type, StructType) and mem_type.name == node.name:
                raise UndeclaredStruct(mem_type.name)
                
            members_dict[mem.name] = mem_type
        
        struct_sym.extra["members"] = members_dict

    def visit_member_decl(self, node: "MemberDecl", o: Any = None):
        pass

    def visit_func_decl(self, node: "FuncDecl", o: Any = None):
        local_o = o + [{"___is_func_scope___": True, "___expected_return___": node.return_type}] 
        
        for param in node.params:
            self.visit(param, local_o)
            
        self.visit(node.body, local_o)
        
        expected_ret = local_o[-1]["___expected_return___"]
        if not expected_ret:
            expected_ret = VoidType()
        o[0]["func_" + node.name].typ = expected_ret

    def visit_param(self, node: "Param", o: Any = None):
        if node.name in o[-1]:
            raise Redeclared("Parameter", node.name)
        
        param_type = self.visit(node.typ, o)
        o[-1][node.name] = Symbol(node.name, param_type, "Parameter")

    # Type system
    def visit_int_type(self, node: "IntType", o: Any = None):
        return IntType()

    def visit_float_type(self, node: "FloatType", o: Any = None):
        return FloatType()

    def visit_string_type(self, node: "StringType", o: Any = None):
        return StringType()

    def visit_void_type(self, node: "VoidType", o: Any = None):
        return VoidType()

    def visit_struct_type(self, node: "StructType", o: Any = None):
        if "struct_" + node.name not in o[0]:
            raise UndeclaredStruct(node.name)
        return StructType(node.name)

    # Statements
    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        block_o = o + [{}]
        for stmt in node.stmts:
            self.visit(stmt, block_o)
            
        for key, sym in block_o[-1].items():
            if isinstance(sym, Symbol) and isinstance(sym.typ, UnknownType):
                raise TypeCannotBeInferred(node)

    def visit_var_decl(self, node: "VarDecl", o: Any = None):
        param_check = self.lookup_var(node.name, o, stop_at_func=True)
        if param_check and param_check.kind == "Parameter":
            raise Redeclared("Variable", node.name)
            
        if node.name in o[-1]:
            raise Redeclared("Variable", node.name)

        var_type = self.visit(node.typ, o) if node.typ else None
        
        if node.init:
            if var_type:
                o[-1]["___expected_type___"] = var_type
                
            init_type = self.visit(node.init, o)
            
            if "___expected_type___" in o[-1]:
                del o[-1]["___expected_type___"]

            if var_type:
                if not self.match_type(var_type, init_type):
                    raise TypeMismatchInStatement(node)
            else:
                var_type = init_type 

        symbol = Symbol(node.name, var_type, "Variable")
        if not var_type:
            symbol.typ = UnknownType(symbol)
            
        o[-1][node.name] = symbol

    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        cond_type = self.visit(node.cond, o)
        if not isinstance(cond_type, IntType):
            raise TypeMismatchInStatement(node)
        self.visit(node.tstmt, o)
        if node.fstmt:
            self.visit(node.fstmt, o)

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        cond_type = self.visit(node.cond, o)
        if not isinstance(cond_type, IntType):
            raise TypeMismatchInStatement(node)
        self.loop_depth += 1
        self.visit(node.stmt, o)
        self.loop_depth -= 1

    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        if node.init:
            self.visit(node.init, o)
        if node.cond:
            cond_type = self.visit(node.cond, o)
            if not isinstance(cond_type, IntType):
                raise TypeMismatchInStatement(node)
        if node.upd:
            self.visit(node.upd, o)
            
        self.loop_depth += 1
        for_o = o + [{}]
        self.visit(node.stmt, for_o)
        self.loop_depth -= 1

    def visit_switch_stmt(self, node: "SwitchStmt", o: Any = None):
        expr_type = self.visit(node.expr, o)
        if not isinstance(expr_type, IntType):
            raise TypeMismatchInStatement(node)
            
        self.switch_depth += 1
        for case_stmt in node.cases:
            self.visit(case_stmt, o)
        if node.default_stmt:
            self.visit(node.default_stmt, o)
        self.switch_depth -= 1

    def visit_case_stmt(self, node: "CaseStmt", o: Any = None):
        expr_type = self.visit(node.expr, o)
        if not isinstance(expr_type, IntType):
            raise TypeMismatchInStatement(node) # TypeMismatch theo Statement Rule
        for stmt in node.stmts:
            self.visit(stmt, o)

    def visit_default_stmt(self, node: "DefaultStmt", o: Any = None):
        for stmt in node.stmts:
            self.visit(stmt, o)

    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        if self.loop_depth == 0 and self.switch_depth == 0:
            raise MustInLoop(node)

    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        if self.loop_depth == 0:
            raise MustInLoop(node)

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        func_scope = None
        for scope in reversed(o):
            if scope.get("___is_func_scope___"):
                func_scope = scope
                break
                
        expected = func_scope["___expected_return___"]
        
        if expected and node.expr:
            o[-1]["___expected_type___"] = expected
        ret_type = self.visit(node.expr, o) if node.expr else VoidType()
        
        if "___expected_type___" in o[-1]:
            del o[-1]["___expected_type___"]
            
        if not expected:
            func_scope["___expected_return___"] = ret_type
        else:
            if not self.match_type(expected, ret_type):
                raise TypeMismatchInStatement(node)

    def visit_expr_stmt(self, node: "ExprStmt", o: Any = None):
        self.visit(node.expr, o)

    # Expressions
    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        left_type = self.visit(node.left, o)
        right_type = self.visit(node.right, o)
        
        if isinstance(left_type, UnknownType) and isinstance(right_type, IntType) and isinstance(node.right, IntLiteral):
            if left_type.symbol: left_type.symbol.typ = IntType()
            left_type = IntType()
        elif isinstance(right_type, UnknownType) and isinstance(left_type, IntType) and isinstance(node.left, IntLiteral):
            if right_type.symbol: right_type.symbol.typ = IntType()
            right_type = IntType()
            
        if isinstance(left_type, UnknownType) or isinstance(right_type, UnknownType):
            raise TypeCannotBeInferred(node)

        op = node.op
        if op in ['+', '-', '*', '/']:
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()
            if type(left_type) in [IntType, FloatType] and type(right_type) in [IntType, FloatType]:
                return FloatType()
            raise TypeMismatchInExpression(node)
        elif op == '%':
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()
            raise TypeMismatchInExpression(node)
        elif op in ['<', '<=', '>', '>=', '==', '!=']:
            if type(left_type) in [IntType, FloatType] and type(right_type) in [IntType, FloatType]:
                return IntType()
            raise TypeMismatchInExpression(node)
        elif op in ['&&', '||']:
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()
            raise TypeMismatchInExpression(node)

        raise TypeMismatchInExpression(node)

    def visit_prefix_op(self, node: "PrefixOp", o: Any = None):
        operand_type = self.visit(node.operand, o)
        if node.op in ['!', '+', '-']:
            if isinstance(operand_type, UnknownType): raise TypeCannotBeInferred(node)
            if node.op == '!':
                if not isinstance(operand_type, IntType): raise TypeMismatchInExpression(node)
                return IntType()
            else:
                if type(operand_type) not in [IntType, FloatType]: raise TypeMismatchInExpression(node)
                return operand_type
        elif node.op in ['++', '--']:
            if not isinstance(node.operand, (Identifier, MemberAccess)):
                raise TypeMismatchInExpression(node)
            if not isinstance(operand_type, IntType):
                raise TypeMismatchInExpression(node)
            return IntType()

    def visit_postfix_op(self, node: "PostfixOp", o: Any = None):
        operand_type = self.visit(node.operand, o)
        if not isinstance(node.operand, (Identifier, MemberAccess)):
            raise TypeMismatchInExpression(node)
        if not isinstance(operand_type, IntType):
            raise TypeMismatchInExpression(node)
        return IntType()

    def visit_assign_expr(self, node: "AssignExpr", o: Any = None):
        if not isinstance(node.left, (Identifier, MemberAccess)):
            raise TypeMismatchInExpression(node)
            
        left_type = self.visit(node.left, o)
        if not isinstance(left_type, UnknownType):
            o[-1]["___expected_type___"] = left_type
            
        right_type = self.visit(node.right, o)
        if "___expected_type___" in o[-1]:
            del o[-1]["___expected_type___"]

        if isinstance(left_type, UnknownType) and isinstance(right_type, UnknownType):
            raise TypeCannotBeInferred(node)
            
        if isinstance(left_type, UnknownType) and left_type.symbol:
            left_type.symbol.typ = right_type
            left_type = right_type
            
        if not self.match_type(left_type, right_type):
            raise TypeMismatchInExpression(node)
            
        return left_type

    def visit_member_access(self, node: "MemberAccess", o: Any = None):
        obj_type = self.visit(node.obj, o)
        if not isinstance(obj_type, StructType):
            raise TypeMismatchInExpression(node)
            
        struct_sym = o[0].get("struct_" + obj_type.name)
        if not struct_sym or node.field not in struct_sym.extra["members"]:
            raise TypeMismatchInExpression(node)
            
        return struct_sym.extra["members"][node.field]

    def visit_func_call(self, node: "FuncCall", o: Any = None):
        symbol = o[0].get("func_" + node.name)
        if not symbol:
            raise UndeclaredFunction(node.name)
            
        expected_params = symbol.extra["params"]
        if len(node.args) != len(expected_params):
            raise TypeMismatchInExpression(node)
            
        for arg, param_type in zip(node.args, expected_params):
            o[-1]["___expected_type___"] = param_type
            arg_type = self.visit(arg, o)
            
            if "___expected_type___" in o[-1]:
                del o[-1]["___expected_type___"]
            
            if isinstance(arg_type, UnknownType) and arg_type.symbol:
                arg_type.symbol.typ = param_type
                arg_type = param_type
                
            if not self.match_type(arg_type, param_type):
                raise TypeMismatchInExpression(node)
                
        return symbol.typ

    def visit_identifier(self, node: "Identifier", o: Any = None):
        symbol = self.lookup_var(node.name, o)
        if not symbol:
            raise UndeclaredIdentifier(node.name)
        return symbol.typ

    def visit_struct_literal(self, node: "StructLiteral", o: Any = None):
        expected_type = o[-1].get("___expected_type___")
        
        if not expected_type or not isinstance(expected_type, StructType):
            raise TypeMismatchInExpression(node) 
        struct_sym = o[0].get("struct_" + expected_type.name)
        if not struct_sym:
            raise UndeclaredStruct(expected_type.name)
            
        expected_members = list(struct_sym.extra["members"].values())
        
        if len(node.exprs) != len(expected_members):
            raise TypeMismatchInExpression(node)
            
        for expr, expected_mem_type in zip(node.exprs, expected_members):
            old_expected = o[-1].get("___expected_type___")
            o[-1]["___expected_type___"] = expected_mem_type
            
            expr_type = self.visit(expr, o)
            
            if old_expected is not None:
                o[-1]["___expected_type___"] = old_expected
            else:
                del o[-1]["___expected_type___"]
                
            if isinstance(expr_type, UnknownType) and expr_type.symbol:
                expr_type.symbol.typ = expected_mem_type
                expr_type = expected_mem_type
                
            if not self.match_type(expr_type, expected_mem_type):
                raise TypeMismatchInExpression(node)
                
        return expected_type

    # Literals
    def visit_int_literal(self, node: "IntLiteral", o: Any = None):
        return IntType()

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        return FloatType()

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        return StringType()