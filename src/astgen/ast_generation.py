"""
AST Generation module for TyC programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from functools import reduce
from build.TyCVisitor import TyCVisitor
from build.TyCParser import TyCParser
from src.utils.nodes import *


class ASTGeneration(TyCVisitor):
    """AST Generation visitor for TyC language."""
    def visitProgram(self, ctx: TyCParser.ProgramContext):
        decls = []
        for i in range(ctx.getChildCount() - 1):
            decls.append(self.visit(ctx.getChild(i)))
        return Program(decls)
    
    def visitStructDecl(self, ctx: TyCParser.StructDeclContext):
        name = ctx.ID().getText()
        members = [self.visit(mem) for mem in ctx.structMem()]
        return StructDecl(name, members)
    
    def visitStructMem(self, ctx: TyCParser.StructMemContext):
        mtype = self.visit(ctx.typeType())
        name = ctx.ID().getText()
        return MemberDecl(mtype, name)
    
    def visitVarDecl(self, ctx: TyCParser.VarDeclContext):
        name = ctx.ID().getText()
        if ctx.AUTO():
            typ = None
        else:
            typ = self.visit(ctx.typeType())
        init = self.visit(ctx.expr()) if ctx.expr() else None
        
        return VarDecl(typ, name, init)
    
    def visitFuncDecl(self, ctx: TyCParser.FuncDeclContext):
        name = ctx.ID().getText()
        
        if ctx.VOID():
            return_type = VoidType()
        elif ctx.typeType():
            return_type = self.visit(ctx.typeType())
        else:
            return_type = None
            
        params = self.visit(ctx.paramList()) if ctx.paramList() else []
        body = self.visit(ctx.stmtBlock())
        return FuncDecl(return_type, name, params, body)
    
    def visitParamList(self, ctx: TyCParser.ParamListContext):
        params = [self.visit(param) for param in ctx.paramDecl()]
        return params
    
    def visitParamDecl(self, ctx: TyCParser.ParamDeclContext):
        param_type = self.visit(ctx.typeType())
        param_name = ctx.ID().getText()
        return Param(param_type, param_name)
    
    def visitTypeType(self, ctx: TyCParser.TypeTypeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.ID():
            return StructType(ctx.ID().getText())
        
    def visitStmt(self, ctx: TyCParser.StmtContext):
        return self.visit(ctx.getChild(0))
    
    def visitStmtBlock(self, ctx: TyCParser.StmtBlockContext):
        stmts = [self.visit(stmt) for stmt in ctx.stmt()]
        return BlockStmt(stmts)
    
    def visitReturnStmt(self, ctx: TyCParser.ReturnStmtContext):
        expr = self.visit(ctx.expr()) if ctx.expr() else None
        return ReturnStmt(expr)
        
    def visitLiteral(self, ctx: TyCParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.structLiteral():
            return self.visit(ctx.structLiteral())
        
    def visitExpr1(self, ctx: TyCParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2())
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr1()) 
        return AssignExpr(left, right)
    
    def visitExpr2(self, ctx: TyCParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3(0))
        left = self.visit(ctx.expr3(0))
        for i in range(1, len(ctx.expr3())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.expr3(i))
            left = BinaryOp(left, op, right)
        return left
    
    def visitExpr3(self, ctx: TyCParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4(0))
        left = self.visit(ctx.expr4(0))
        for i in range(1, len(ctx.expr4())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.expr4(i))
            left = BinaryOp(left, op, right)
        return left
    
    def visitExpr4(self, ctx: TyCParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5(0))
        left = self.visit(ctx.expr5(0))
        for i in range(1, len(ctx.expr5())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.expr5(i))
            left = BinaryOp(left, op, right)
        return left
    
    def visitExpr5(self, ctx: TyCParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6(0))
        left = self.visit(ctx.expr6(0))
        for i in range(1, len(ctx.expr6())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.expr6(i))
            left = BinaryOp(left, op, right)
        return left
    
    def visitExpr6(self, ctx: TyCParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7(0))
        left = self.visit(ctx.expr7(0))
        for i in range(1, len(ctx.expr7())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.expr7(i))
            left = BinaryOp(left, op, right)
        return left
        
    def visitExpr7(self, ctx: TyCParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8(0))
        left = self.visit(ctx.expr8(0))
        for i in range(1, len(ctx.expr8())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.expr8(i))
            left = BinaryOp(left, op, right)
        return left
    
    def visitExpr8(self, ctx: TyCParser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr9())
        op = ctx.getChild(0).getText()
        operand = self.visit(ctx.expr8())
        return PrefixOp(op, operand)
    
    def visitExpr9(self, ctx: TyCParser.Expr9Context):
        if ctx.ID() and ctx.getChildCount() == 1:
            return Identifier(ctx.ID().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.LP() and ctx.expr() and not ctx.exprList():
            return self.visit(ctx.expr())
        elif ctx.DOT():
            obj = self.visit(ctx.expr9())
            field = ctx.ID().getText()
            return MemberAccess(obj, field) 
        elif ctx.INC() or ctx.DEC():
            operand = self.visit(ctx.expr9())
            op = ctx.INC().getText() if ctx.INC() else ctx.DEC().getText()
            return PostfixOp(op, operand) 
        elif ctx.LP() and (ctx.exprList() or ctx.getChildCount() == 3):
            func_name = self.visit(ctx.expr9())
            args = self.visit(ctx.exprList()) if ctx.exprList() else []
            return FuncCall(func_name, args)
        
    def visitExpr(self, ctx: TyCParser.ExprContext):
        return self.visit(ctx.expr1())
    
    def visitIfStmt(self, ctx: TyCParser.IfStmtContext):
        condition = self.visit(ctx.expr())
        then_stmt = self.visit(ctx.stmt(0))
        else_stmt = self.visit(ctx.stmt(1)) if ctx.ELSE() else None
        return IfStmt(condition, then_stmt, else_stmt)

    def visitSwitchStmt(self, ctx: TyCParser.SwitchStmtContext):
        expr = self.visit(ctx.expr())
        cases = [self.visit(case) for case in ctx.caseStmt()] if ctx.caseStmt() else []
        default_case = self.visit(ctx.defaultStmt()) if ctx.defaultStmt() else None
        return SwitchStmt(expr, cases, default_case)

    def visitCaseStmt(self, ctx: TyCParser.CaseStmtContext):
        expr = self.visit(ctx.expr())
        stmts = [self.visit(stmt) for stmt in ctx.stmt()]
        return CaseStmt(expr, stmts)

    def visitDefaultStmt(self, ctx: TyCParser.DefaultStmtContext):
        stmts = [self.visit(stmt) for stmt in ctx.stmt()]
        return DefaultStmt(stmts)
    
    def visitWhileStmt(self, ctx: TyCParser.WhileStmtContext):
        condition = self.visit(ctx.expr())
        body = self.visit(ctx.stmt())
        return WhileStmt(condition, body)

    def visitForStmt(self, ctx: TyCParser.ForStmtContext):
        semi_indices = [i for i in range(ctx.getChildCount()) if ctx.getChild(i).getText() == ';']
        semi1, semi2 = semi_indices[0], semi_indices[1]
        init = None
        if semi1 > 2: 
            init_ctx = ctx.getChild(2)
            if isinstance(init_ctx, TyCParser.ScalarVarDeclContext):
                init = self.visit(init_ctx)
            else:
                init = ExprStmt(self.visit(init_ctx)) 
                
        condition = None
        if semi2 > semi1 + 1:
            condition = self.visit(ctx.getChild(semi1 + 1))
        update = None
        rp_index = ctx.getChildCount() - 2
        if rp_index > semi2 + 1:
            update = self.visit(ctx.getChild(semi2 + 1))
            
        body = self.visit(ctx.stmt())
        return ForStmt(init, condition, update, body)
    
    def visitBreakStmt(self, ctx: TyCParser.BreakStmtContext):
        return BreakStmt()

    def visitContinueStmt(self, ctx: TyCParser.ContinueStmtContext):
        return ContinueStmt()
    
    def visitExprStmt(self, ctx: TyCParser.ExprStmtContext):
        expr = self.visit(ctx.expr())
        return ExprStmt(expr)
    def visitStructLiteral(self, ctx: TyCParser.StructLiteralContext):
        exprs = self.visit(ctx.exprList()) if ctx.exprList() else []
        return StructLiteral(exprs)
    
    def visitScalarVarDecl(self, ctx: TyCParser.ScalarVarDeclContext):
        name = ctx.ID().getText()
        typ = None if ctx.AUTO() else self.visit(ctx.typeType())
        init = self.visit(ctx.expr()) if ctx.expr() else None
        return VarDecl(typ, name, init)

    def visitAssignExpr(self, ctx: TyCParser.AssignExprContext):
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr1())
        return AssignExpr(left, right)
    
    def visitExprList(self, ctx: TyCParser.ExprListContext):
        return [self.visit(expr) for expr in ctx.expr()]