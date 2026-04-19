"""
Test cases for TyC Static Semantic Checker

This module contains test cases for the static semantic checker.
100 test cases covering all error types and comprehensive scenarios.
"""

from tests.utils import Checker
from src.utils.nodes import (
    Program,
    FuncDecl,
    BlockStmt,
    VarDecl,
    AssignExpr,
    ExprStmt,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    Identifier,
    BinaryOp,
    MemberAccess,
    FuncCall,
    StructDecl,
    MemberDecl,
    Param,
    ReturnStmt,
)


# ============================================================================
# Valid Programs (test_001 - test_020)
# ============================================================================


def test_001():
    source = """
void main() {
    int x = 5;
    int y = x + 1;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_002():
    source = """
void main() {
    auto x = 10;
    auto y = 3.14;
    auto z = x + y;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_003():
    source = """
int add(int x, int y) {
    return x + y;
}
void main() {
    int sum = add(5, 3);
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_004():
    source = """
struct Point {
    int x;
    int y;
};
void main() {
    Point p;
    p.x = 10;
    p.y = 20;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_005():
    source = """
void main() {
    int x = 10;
    {
        int y = 20;
        int z = x + y;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_006():
    source = """
    void main() {
        auto x;
        auto y = x + 5; 
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_007():
    source = """
    struct Point { int x; float y; };
    void main() {
        Point p = {10, 3.14};
        p.x = 20;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_008():
    source = """
    struct Point { int x; int y; };
    struct Circle { Point center; float radius; };
    void main() {
        Circle c = {{0, 0}, 5.5};
        c.center.x = 10;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_009():
    source = """
    void main() {
        int i = 0;
        while(i < 10) {
            if (i % 2 == 0) { i++; continue; }
            i++;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_010():
    source = """
    void main() {
        int x = 2;
        switch(x) {
            case 1+1: break;
            case 3: 
            default: break;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_011():
    source = """
    void main() {
        int a; int b; int c;
        a = b = c = 10;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_012():
    source = "get_val() { return 42; } void main() { int x = get_val(); }"
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_013():
    source = """
    void main() {
        for(auto i = 0; i < 5; i++) {
            int x = i;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_014():
    source = """
    void main() {
        float f = 10 + 3.14;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_015():
    source = """
    int fact(int n) {
        if (n <= 1) return 1;
        return n * fact(n - 1);
    }
    void main() {}
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_016():
    source = "struct Point { int x; }; void main() { Point p = {10}; }"
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_017():
    source = "struct P { int x; }; void foo(P p) { int y = p.x + 1; } void main() { P p = {10}; foo(p); }"
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_018():
    source = "get_num() { return 3.14; } void main() { auto x = get_num(); }"
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_019():
    source = "void main() { int x = 10; { int x = 20; int y = x + 5; } }" 
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_020():
    source = """
    void main() {
        int x = 3;
        switch(x) {
            case 1: break;
            case 2: break;
            case 3: break;
            default: break;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected
# ============================================================================
# Declare (test_021 - test_040)
# ============================================================================

def test_021():
    source = """
    void func(int x) {
        int x = 10; 
    }
    """
    # Cần check chính xác message từ file static_error.py
    expected = "Redeclared(Variable, x)" 
    assert Checker(source).check_from_source() == expected

def test_022():
    source = """void main() { int x; float x; }"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_023():
    source = """void foo(){} int foo(){ return 1; }"""
    expected = "Redeclared(Function, foo)"
    assert Checker(source).check_from_source() == expected

def test_024():
    source = """struct A{int x;}; struct A{float y;};"""
    expected = "Redeclared(Struct, A)"
    assert Checker(source).check_from_source() == expected

def test_025():
    source = """struct A{int x; float x;};"""
    expected = "Redeclared(Member, x)"
    assert Checker(source).check_from_source() == expected

def test_026():
    source = """void func(int a, float a) {}"""
    expected = "Redeclared(Parameter, a)"
    assert Checker(source).check_from_source() == expected

def test_027():
    source = """void main() { a = 10; }"""
    expected = "UndeclaredIdentifier(a)"
    assert Checker(source).check_from_source() == expected

def test_028():
    source = """void main() { int x = y + 1; }"""
    expected = "UndeclaredIdentifier(y)"
    assert Checker(source).check_from_source() == expected

def test_029():
    source = """void main() { foo(); }"""
    expected = "UndeclaredFunction(foo)"
    assert Checker(source).check_from_source() == expected

def test_030():
    source = """void main() { Point p; }"""
    expected = "UndeclaredStruct(Point)"
    assert Checker(source).check_from_source() == expected

def test_031():
    source = """struct Node { Node next; };"""
    expected = "UndeclaredStruct(Node)"
    assert Checker(source).check_from_source() == expected

def test_032():
    source = """struct A { B x; };"""
    expected = "UndeclaredStruct(B)"
    assert Checker(source).check_from_source() == expected

def test_033():
    source = """
    struct Point { int x; };
    void main() {
        Point p;
        p.y = 10;
    }
    """
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(p).y))"
    assert Checker(source).check_from_source() == expected

def test_034():
    source = """
    struct Point { int x; };
    void main() {
        Point p = {10, 20};
    }
    """
    expected = "TypeMismatchInExpression(StructLiteral({IntLiteral(10), IntLiteral(20)}))"
    assert Checker(source).check_from_source() == expected

def test_035():
    source = """
    struct Point { int x; };
    struct Circle { Point center; };
    void main() {
        Circle c = {{10, 20}};
    }
    """
    expected = "TypeMismatchInExpression(StructLiteral({IntLiteral(10), IntLiteral(20)}))"
    assert Checker(source).check_from_source() == expected

def test_036():
    source = """
    struct Point { int x; };
    struct Circle { Point center; };
    void main() {
        Circle c;
        c.center.y = 10;
    }
    """
    expected = "TypeMismatchInExpression(MemberAccess(MemberAccess(Identifier(c).center).y))"
    assert Checker(source).check_from_source() == expected

def test_037():
    source = """
    struct Point { int x; };
    void foo(Point p) {}
    void main() {
        foo({10, 20});
    }
    """
    expected = "TypeMismatchInExpression(StructLiteral({IntLiteral(10), IntLiteral(20)}))"
    assert Checker(source).check_from_source() == expected

def test_038():
    source = """
    struct Point { int x; };
    Point foo() { return {10, 20}; }
    void main() {}
    """
    expected = "TypeMismatchInExpression(StructLiteral({IntLiteral(10), IntLiteral(20)}))"
    assert Checker(source).check_from_source() == expected

def test_039():
    source = """
    struct Point { int x; };
    void main() {
        Point p;
        p.y = 10;
    }
    """
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(p).y))"
    assert Checker(source).check_from_source() == expected

def test_040():
    source = """
    struct Point { int x; };
    void main() {
        Point p;
        int y = p.y + 1;
    }
    """
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(p).y))"
    assert Checker(source).check_from_source() == expected

# ============================================================================
# Control Flow (test_041 - test_050)
# ============================================================================

def test_041():
    source = """
    void main() {
        int x = 1;
        switch(x) {
            case 1: continue;
        }
    }
    """
    expected = "MustInLoop(ContinueStmt())" 
    assert Checker(source).check_from_source() == expected

def test_042():
    source = """void main() { break; }"""
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_043():
    source = """void main() { if (1) { break; } }"""
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_044():
    source = """void main() { continue; }"""
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_045():
    source = """
    void helper() { continue; }
    void main() { while(1) { helper(); } }
    """
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_046():
    source = """
    void helper() { break; }
    void main() { while(1) { helper(); } }
    """
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_047():
    source = """
    void main() {
        int x = 1;
        switch(x) {
            case 1: break; continue;
        }
    }
    """
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_048():
    source = """
    void main() {
        int x = 1;
        switch(x) {
            case 1: break; continue;
        }
    }
    """    
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_049():
    source = """
    void helper() { break; }
    void main() {
        int x = 1;
        switch(x) {
            case 1: helper();
        }
    }
    """
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_050():
    source = """
    void helper() { continue; }
    void main() {
        int x = 1;
        switch(x) {
            case 1: helper();
        }
    }
    """
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected


# ============================================================================
# Type Mismatch Expression (test_051 - test_070)
# ============================================================================

def test_051():
    source = """
    void main() {
        int x = 5 + "hello";
    }
    """
    expected = "TypeMismatchInExpression(BinaryOp(IntLiteral(5), +, StringLiteral('hello')))"
    assert Checker(source).check_from_source() == expected

def test_052():
    source = """void main() { 5 % 3.14; }"""
    expected = "TypeMismatchInExpression(BinaryOp(IntLiteral(5), %, FloatLiteral(3.14)))"
    assert Checker(source).check_from_source() == expected

def test_053():
    source = """void main() { !3.14; }"""
    expected = "TypeMismatchInExpression(PrefixOp(!FloatLiteral(3.14)))"
    assert Checker(source).check_from_source() == expected

def test_054():
    source = """void main() { float f = 1.0; ++f; }"""
    expected = "TypeMismatchInExpression(PrefixOp(++Identifier(f)))"
    assert Checker(source).check_from_source() == expected

def test_055():
    source = """
    void foo(int x) {}
    void main() { foo(1, 2); }
    """
    expected = "TypeMismatchInExpression(FuncCall(foo, [IntLiteral(1), IntLiteral(2)]))"
    assert Checker(source).check_from_source() == expected

def test_056():
    source = """
    void foo(int x) {}
    void main() { foo("hello"); }
    """
    expected = "TypeMismatchInExpression(FuncCall(foo, [StringLiteral('hello')]))"
    assert Checker(source).check_from_source() == expected

def test_057():
    source = """void main() { int x; x.y; }"""
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(x).y))"
    assert Checker(source).check_from_source() == expected

def test_058():
    source = """
    struct Point { int x; };
    void main() { Point p = {1, 2}; }
    """
    expected = "TypeMismatchInExpression(StructLiteral({IntLiteral(1), IntLiteral(2)}))"
    assert Checker(source).check_from_source() == expected

def test_059():
    source = """void main() { int x; (x = 5.5) + 1; }"""
    expected = "TypeMismatchInExpression(AssignExpr(Identifier(x) = FloatLiteral(5.5)))"
    assert Checker(source).check_from_source() == expected

def test_060():
    source = """void main() { "A" && "B"; }"""
    expected = "TypeMismatchInExpression(BinaryOp(StringLiteral('A'), &&, StringLiteral('B')))"
    assert Checker(source).check_from_source() == expected

def test_061():
    source = """void main() { "A" < "B"; }"""
    expected = "TypeMismatchInExpression(BinaryOp(StringLiteral('A'), <, StringLiteral('B')))"
    assert Checker(source).check_from_source() == expected

def test_062():
    source = """void main() { "A" + "B"; }"""
    expected = "TypeMismatchInExpression(BinaryOp(StringLiteral('A'), +, StringLiteral('B')))"
    assert Checker(source).check_from_source() == expected

def test_063():
    source = """void main() { -"hello"; }"""
    expected = "TypeMismatchInExpression(PrefixOp(-StringLiteral('hello')))"
    assert Checker(source).check_from_source() == expected

def test_064():
    source = """
    void main() {
        auto x = 10;
        x = "hello";
    }
    """
    expected = "TypeMismatchInExpression(AssignExpr(Identifier(x) = StringLiteral('hello')))"
    assert Checker(source).check_from_source() == expected

def test_065():
    source = "void main() { auto x; auto y; int z = x == y; }"
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), ==, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_066():
    source = "foo() { return 3.14; } void main() { int x = foo(); }"
    expected = "TypeMismatchInStatement(VarDecl(IntType(), x = FuncCall(foo, [])))"
    assert Checker(source).check_from_source() == expected

def test_067():
    source = "void foo(int x) {} void main() { foo(3.14); }"
    expected = "TypeMismatchInExpression(FuncCall(foo, [FloatLiteral(3.14)]))"
    assert Checker(source).check_from_source() == expected

def test_068():
    source = "struct Point { int x; }; void main() { Point p; float y = p.x; }"
    expected = "TypeMismatchInStatement(VarDecl(FloatType(), y = MemberAccess(Identifier(p).x)))"
    assert Checker(source).check_from_source() == expected

def test_069():
    source = "void main() { auto p; int y = p.x; }"
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(p).x))"
    assert Checker(source).check_from_source() == expected

def test_070():
    source = "struct Point { int x; }; void main() { Point p = {3.14}; }"
    expected = "TypeMismatchInExpression(StructLiteral({FloatLiteral(3.14)}))"
    assert Checker(source).check_from_source() == expected


# ============================================================================
# Type Mismatch Statement (test_071 - test_085)
# ============================================================================

def test_071():
    source = """void main() { if (3.14) {} }"""
    expected = "TypeMismatchInStatement(IfStmt(if FloatLiteral(3.14) then BlockStmt([])))"
    assert Checker(source).check_from_source() == expected

def test_072():
    source = """void main() { while ("true") {} }"""
    expected = "TypeMismatchInStatement(WhileStmt(while StringLiteral('true') do BlockStmt([])))"
    assert Checker(source).check_from_source() == expected

def test_073():
    source = """void main() { int x = 3.14; }"""
    expected = "TypeMismatchInStatement(VarDecl(IntType(), x = FloatLiteral(3.14)))"
    assert Checker(source).check_from_source() == expected

def test_074():
    source = """void main() { int x; x = "str"; }"""
    expected = "TypeMismatchInExpression(AssignExpr(Identifier(x) = StringLiteral('str')))" 
    assert Checker(source).check_from_source() == expected

def test_075():
    source = """void main() { return 1; }"""
    expected = "TypeMismatchInStatement(ReturnStmt(return IntLiteral(1)))"
    assert Checker(source).check_from_source() == expected

def test_076():
    source = """int foo() { return; }"""
    expected = "TypeMismatchInStatement(ReturnStmt(return))"
    assert Checker(source).check_from_source() == expected

def test_077():
    source = """void main() { switch("a") { case 1: break; } }"""
    expected = "TypeMismatchInStatement(SwitchStmt(switch StringLiteral('a') cases [CaseStmt(case IntLiteral(1): [BreakStmt()])]))"
    assert Checker(source).check_from_source() == expected

def test_078():
    source = "foo(int x) { if (x) return 1; return 3.14; }"
    expected = "TypeMismatchInStatement(ReturnStmt(return FloatLiteral(3.14)))"
    assert Checker(source).check_from_source() == expected

def test_079():
    source = "void main() { int x; x = 3.14; }"
    expected = "TypeMismatchInExpression(AssignExpr(Identifier(x) = FloatLiteral(3.14)))"
    assert Checker(source).check_from_source() == expected

def test_080():
    source = "struct Point { int x; }; void main() { Point p; p.x = 3.14; }"
    expected = "TypeMismatchInExpression(AssignExpr(MemberAccess(Identifier(p).x) = FloatLiteral(3.14)))"
    assert Checker(source).check_from_source() == expected

def test_081():
    source = """
    void main() {
        auto x;
        x = 10;
        x = "hello";
    }
    """
    expected = "TypeMismatchInExpression(AssignExpr(Identifier(x) = StringLiteral('hello')))"
    assert Checker(source).check_from_source() == expected

def test_082():
    source = """
    void main() {
        auto x;
        int y = x + 1;
        float z = x + 1.0;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_083():
    source = "foo() { return 1; return 3.14; } void main() {}"
    expected = "TypeMismatchInStatement(ReturnStmt(return FloatLiteral(3.14)))"
    assert Checker(source).check_from_source() == expected

def test_084():
    source = "void foo(int x) { return; } void main() {}"
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_085():
    source = "struct P { int x; }; void main() { P p = {\"str\"}; }"
    expected = "TypeMismatchInExpression(StructLiteral({StringLiteral('str')}))"
    assert Checker(source).check_from_source() == expected
# ============================================================================
# Type Cannot Be Inferred (test_086 - test_100)
# ============================================================================

def test_086():
    source = """
    void main() {
        auto a; auto b;
        a = b;
    }
    """
    expected = "TypeCannotBeInferred(AssignExpr(Identifier(a) = Identifier(b)))"
    assert Checker(source).check_from_source() == expected

def test_087():
    source = """void main() { auto x; }"""
    expected = "TypeCannotBeInferred(BlockStmt([VarDecl(auto, x)]))"
    assert Checker(source).check_from_source() == expected

def test_088():
    source = "foo() { auto x; return x; } void main() {}"
    expected = "TypeCannotBeInferred(BlockStmt([VarDecl(auto, x), ReturnStmt(return Identifier(x))]))"
    assert Checker(source).check_from_source() == expected

def test_089():
    source = """
    void main() {
        auto a; auto b;
        int c = a * b;
    }
    """
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(a), *, Identifier(b)))"
    assert Checker(source).check_from_source() == expected

def test_090():
    source = "void main() { auto x; !x; }"
    expected = "TypeCannotBeInferred(PrefixOp(!Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_091():
    source = "void main() { auto x; ++x; }"
    expected = "TypeMismatchInExpression(PrefixOp(++Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_092():
    source = "void main() { auto x; x++; }"
    expected = "TypeMismatchInExpression(PostfixOp(Identifier(x)++))"
    assert Checker(source).check_from_source() == expected

def test_093():
    source = "void main() { auto x; -x; }"
    expected = "TypeCannotBeInferred(PrefixOp(-Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_094():
    source = "void main() { auto x; auto y; int z = x < y; }"
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), <, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_095():
    source = "void main() { auto x; auto y; int z = x && y; }"
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), &&, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_096():
    source = "void main() { auto x; x = x + x; }"
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), +, Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_097():
    source = "void main() { auto x; { auto y = x; } }"
    expected = "TypeCannotBeInferred(BlockStmt([VarDecl(auto, y = Identifier(x))]))"
    assert Checker(source).check_from_source() == expected

def test_098():
    source = "void main() { auto x; auto y; int z = x - y; }"
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), -, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_099():
    source = """
    void main() {
        auto x;
        x = x;
    }
    """
    expected = "TypeCannotBeInferred(AssignExpr(Identifier(x) = Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_100():
    source = "void main() { auto x; auto y; int z = x / y; }"
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), /, Identifier(y)))"
    assert Checker(source).check_from_source() == expected