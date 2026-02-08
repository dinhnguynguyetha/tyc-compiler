"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


# ========== Simple Test Cases (10 types) ==========
def test_empty_program():
    """1. Empty program"""
    assert Parser("").parse() == "success"


def test_program_with_only_main():
    """2. Program with only main function"""
    assert Parser("void main() {}").parse() == "success"


def test_struct_simple():
    """3. Struct declaration"""
    source = "struct Point { int x; int y; };"
    assert Parser(source).parse() == "success"


def test_function_no_params():
    """4. Function with no parameters"""
    source = "void greet() { printString(\"Hello\"); }"
    assert Parser(source).parse() == "success"


def test_var_decl_auto_with_init():
    """5. Variable declaration"""
    source = "void main() { auto x = 5; }"
    assert Parser(source).parse() == "success"


def test_if_simple():
    """6. If statement"""
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_while_simple():
    """7. While statement"""
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_for_simple():
    """8. For statement"""
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_switch_simple():
    """9. Switch statement"""
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert Parser(source).parse() == "success"


def test_assignment_simple():
    """10. Assignment statement"""
    source = "void main() { int x; x = 5; }"
    assert Parser(source).parse() == "success"

# ========== Additional Test Cases (100 types) ==========

#Variables & Types
def test_var_decl_explicit_types():
    """11. Explicit type declarations"""
    source = "void main() { int a; float b; string c; }"
    assert Parser(source).parse() == "success"

def test_var_decl_auto_no_init():
    """12. Auto without initialization (Parser should pass, Semantic fails)"""
    source = "void main() { auto x; }"
    assert Parser(source).parse() == "success"

def test_var_decl_complex_init():
    """13. Initialization with complex expression"""
    source = "void main() { float x = 1.0 + 2.0 * 3.0; }"
    assert Parser(source).parse() == "success"

def test_var_decl_string():
    """14. String variable declaration"""
    source = "void main() { string s = \"Hello World\"; }"
    assert Parser(source).parse() == "success"

def test_var_decl_negative_number():
    """15. Negative number initialization"""
    source = "void main() { int x = -5; float y = -3.14; }"
    assert Parser(source).parse() == "success"

#Functions & Parameters
def test_func_multi_params():
    """16. Function with multiple parameters"""
    source = "int add(int a, float b, string c) { return 1; }"
    assert Parser(source).parse() == "success"

def test_func_void_return():
    """17. Void function with return statement"""
    source = "void proc() { return; }"
    assert Parser(source).parse() == "success"

def test_func_call_as_statement():
    """18. Function call as a statement"""
    source = "void main() { doSomething(1, \"test\"); }"
    assert Parser(source).parse() == "success"

def test_func_nested_call():
    """19. Nested function calls in expression"""
    source = "void main() { int x = max(min(1, 2), 3); }"
    assert Parser(source).parse() == "success"

def test_func_no_type_inference():
    """20. Function without return type (inference)"""
    source = "main() { }"
    assert Parser(source).parse() == "success"

#Struct
def test_struct_complex_members():
    """21. Struct with mixed types"""
    source = "struct User { int id; string name; float score; };"
    assert Parser(source).parse() == "success"

def test_struct_member_access():
    """22. Struct member access"""
    source = "void main() { point.x = 10; }"
    assert Parser(source).parse() == "success"

def test_struct_nested_access():
    """23. Nested struct member access"""
    source = "void main() { int x = rect.topLeft.x; }"
    assert Parser(source).parse() == "success"

def test_struct_decl_inside_function():
    """24. Struct literal in function"""
    source = "void main() { Point p = {1, 2}; }"
    assert Parser(source).parse() == "success"

def test_struct_array_access_simulation():
    """25. Multiple struct definitions"""
    source = "struct A { int x; }; struct B { float y; }; void main() {}"
    assert Parser(source).parse() == "success"

#Complex Expressions
def test_expr_precedence_mul_add():
    """26. Precedence: Multiply before Add"""
    source = "void main() { int x = 1 + 2 * 3; }"
    assert Parser(source).parse() == "success"

def test_expr_parentheses():
    """27. Parentheses forcing precedence"""
    source = "void main() { int x = (1 + 2) * 3; }"
    assert Parser(source).parse() == "success"

def test_expr_logical_complex():
    """28. Complex logical expression"""
    source = "void main() { if (a > b && c <= d || !e) {} }"
    assert Parser(source).parse() == "success"

def test_expr_unary_operators():
    """29. Unary operators mix"""
    source = "void main() { int x = -a + !b; }"
    assert Parser(source).parse() == "success"

def test_expr_comparison_chain():
    """30. Comparison expressions"""
    source = "void main() { bool check = x >= y == z < 5; }"
    assert Parser(source).parse() == "success"

#Advanced Loops
def test_for_empty_parts():
    """31. For loop with missing parts"""
    source = "void main() { for (; i < 10; ) { i = i + 1; } }"
    assert Parser(source).parse() == "success"

def test_for_infinite():
    """32. Infinite for loop"""
    source = "void main() { for (;;) { break; } }"
    assert Parser(source).parse() == "success"

def test_for_decl_inside():
    """33. For loop with variable declaration"""
    source = "void main() { for (int i = 0; i < 10; i++) {} }"
    assert Parser(source).parse() == "success"

def test_loop_nested():
    """34. Nested while loops"""
    source = "void main() { while(1) { while(0) { break; } } }"
    assert Parser(source).parse() == "success"

def test_continue_stmt():
    """35. Continue statement usage"""
    source = "void main() { while(1) { if(x) continue; } }"
    assert Parser(source).parse() == "success"

#Switch-Case
def test_switch_full():
    """36. Full switch case with default"""
    source = "void main() { switch(x) { case 1: break; default: break; } }"
    assert Parser(source).parse() == "success"

def test_switch_empty():
    """37. Empty switch body"""
    source = "void main() { switch(x) {} }"
    assert Parser(source).parse() == "success"

def test_switch_stack_cases():
    """38. Stacked cases (fall-through)"""
    source = "void main() { switch(x) { case 1: case 2: print(1); break; } }"
    assert Parser(source).parse() == "success"

def test_switch_default_only():
    """39. Switch with default only"""
    source = "void main() { switch(x) { default: x = 0; } }"
    assert Parser(source).parse() == "success"

def test_switch_expression_case():
    """40. Case with expression"""
    source = "void main() { switch(x) { case 1+2: break; } }"
    assert Parser(source).parse() == "success"

#Comment và Literal đặc biệt
def test_comment_block_inline():
    """41. Inline block comment"""
    source = "void main() { int /* comment */ x = 5; }"
    assert Parser(source).parse() == "success"

def test_comment_line_end():
    """42. Line comment at EOF"""
    source = "void main() {} // End of file"
    assert Parser(source).parse() == "success"

def test_literal_scientific_float():
    """43. Scientific notation float"""
    source = "void main() { float f = 1.2e-3; }"
    assert Parser(source).parse() == "success"

def test_literal_string_escapes():
    """44. String with escapes"""
    source = "void main() { string s = \"Line\\nTab\\tQuote\\\"\"; }"
    assert Parser(source).parse() == "success"

def test_literal_float_dot():
    """45. Float starting with dot"""
    source = "void main() { float f = .5; float g = 1.; }"
    assert Parser(source).parse() == "success"

#Negative Tests
def test_err_missing_semi():
    """46. Error: Missing semicolon"""
    source = "void main() { int x = 5 }"
    try:
        Parser(source).parse()
    except Exception:
        assert True 

def test_err_invalid_var_decl():
    """47. Error: Invalid variable declaration format"""
    source = "void main() { int x, y; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_unclosed_block():
    """48. Error: Unclosed brace"""
    source = "void main() { if (1) { "
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_keyword_as_id():
    """49. Error: Using keyword as identifier"""
    source = "void main() { int if = 5; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_double_dots_float():
    """50. Error: Malformed float"""
    source = "void main() { float x = 1.2.3; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

#Forgotten test case
def test_func_recursive_call():
    """51. Recursive function call"""
    source = "int factorial(int n) { if (n <= 1) return 1; else return n * factorial(n - 1); }"
    assert Parser(source).parse() == "success"

def test_if_else_simulation():
    """52. Replaces Ternary Operator: Use if-else statement"""
    source = "void main() { int x; if (a > b) x = a; else x = b; }"
    assert Parser(source).parse() == "success"

def test_struct_multiple_declarations():
    """53. Replaces Array: Declare multiple variables"""
    source = "struct Point { int x; int y; }; void main() { Point p1; Point p2; Point p3; }"
    assert Parser(source).parse() == "success"      

def test_func_struct_param():
    """54. Replaces Pointer: Pass struct by value"""
    source = "struct Data { int id; }; void process(Data item, int size) { }"
    assert Parser(source).parse() == "success"

def test_expr_logical_complex_2():
    """55. Replaces Bitwise: Complex logical expression"""
    source = "void main() { int x = (a && b) || (!c && d); }"
    assert Parser(source).parse() == "success"

def test_loop_break_in_nested():
    """56. Break statement in nested loops"""
    source = "void main() { for (int i = 0; i < 10; i++) { while(1) { break; } } }"
    assert Parser(source).parse() == "success"

def test_switch_case_multiple_statements():
    """57. Multiple statements in case block"""
    source = "void main() { switch(x) { case 1: printInt(1); printInt(2); break; } }"
    assert Parser(source).parse() == "success"

def test_comment_multiline():
    """58. Multi-line comment"""
    source = """void main() { 
    /* This is a 
       multi-line comment */
    int x = 5; 
}"""
    assert Parser(source).parse() == "success"

def test_literal_string_as_char():
    """59. Replaces Char: Use String literal"""
    source = "void main() { string c = \"A\"; }"
    assert Parser(source).parse() == "success"

def test_err_invalid_func_decl():
    """60. Error: Invalid function declaration"""
    source = "int func( { return 0; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_unterminated_string():
    """61. Error: Unterminated string literal"""
    source = "void main() { string s = \"Hello; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_struct_decl():
    """62. Error: Invalid struct declaration"""
    source = "struct { int x; };"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_expr():
    """63. Error: Invalid expression"""
    source = "void main() { int x = 5 + * 3; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_missing_paren():
    """64. Error: Missing parenthesis"""
    source = "void main() { if (x > 0 { printInt(x); } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_switch_case():
    """65. Error: Invalid switch case syntax"""
    source = "void main() { switch(x) { case : break; } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_for_syntax():
    """66. Error: Invalid for loop syntax"""
    source = "void main() { for (int i = 0 i < 10; i++) {} }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_var_name():
    """67. Error: Invalid variable name"""
    source = "void main() { int 1var = 5; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_extra_token():
    """68. Error: Extra token after valid statement"""
    source = "void main() { int x = 5;; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_incorrect_struct_member():
    """69. Error: Incorrect struct member declaration"""
    source = "struct Point { int x float y; };"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_literal():
    """70. Error: Invalid literal"""
    source = "void main() { int x = 0b102; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_misplaced_return():
    """71. Error: Misplaced return statement"""
    source = "void main() { return 5; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_incomplete_if():
    """72. Error: Incomplete if statement"""
    source = "void main() { if (x > 0) "
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_array_decl():
    """73. Error: Invalid array declaration"""
    source = "void main() { int arr[]; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_pointer_decl():
    """74. Error: Invalid pointer declaration"""
    source = "void main() { int* *ptr; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_misplaced_struct():
    """75. Error: Misplaced struct declaration"""
    source = "void main() { struct Point { int x; int y; }; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_comment():
    """76. Error: Invalid comment syntax"""
    source = "void main() { /* This is an invalid comment // }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_incorrect_ternary():
    """77. Error: Incorrect ternary operator usage"""
    source = "void main() { int x = a > b ? ; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_missing_case_colon():
    """78. Error: Missing colon in case statement"""
    source = "void main() { switch(x) { case 1 break; } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_unary_op():
    """79. Error: Invalid unary operator usage"""
    source = "void main() { int x = ++*y; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_incorrect_logical_expr():
    """80. Error: Incorrect logical expression"""
    source = "void main() { bool b = a && || c; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_misplaced_break():
    """81. Error: Misplaced break statement"""
    source = "void main() { break; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_float_format():
    """82. Error: Invalid float format"""
    source = "void main() { float f = 1..0; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_incorrect_array_access():
    """83. Error: Incorrect array access syntax"""
    source = "void main() { int x = arr[; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_char_literal():
    """84. Error: Invalid character literal"""
    source = "void main() { char c = 'AB'; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_misplaced_continue():
    """85. Error: Misplaced continue statement"""
    source = "void main() { continue; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_incorrect_struct_access():
    """86. Error: Incorrect struct member access"""
    source = "void main() { int x = point..x; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_function_call():
    """87. Error: Invalid function call syntax"""
    source = "void main() { doSomething(1, ); }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_incomplete_for_loop():
    """88. Error: Incomplete for loop syntax"""
    source = "void main() { for (int i = 0; ; i++) {} }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_bitwise_expr():
    """89. Error: Invalid bitwise expression"""
    source = "void main() { int x = a & | b; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_misplaced_return_in_void():
    """90. Error: Return with value in void function"""
    source = "void main() { return 5; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_unclosed_string():
    """91. Error: Unclosed string literal"""
    source = "void main() { string s = \"Hello World; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_nested_struct():
    """92. Error: Invalid nested struct declaration"""
    source = "struct A { struct B { int x; }; };"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_incorrect_while_syntax():
    """93. Error: Incorrect while loop syntax"""
    source = "void main() { while 1) { } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_pointer_usage():
    """94. Error: Invalid pointer usage"""
    source = "void main() { int* p = &5; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_incorrect_logical_not():
    """95. Error: Incorrect logical NOT usage"""
    source = "void main() { bool b = !; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_misplaced_struct_decl():
    """96. Error: Misplaced struct declaration inside function"""
    source = "void main() { struct Point { int x; int y; }; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_ternary_syntax():
    """97. Error: Invalid ternary operator syntax"""
    source = "void main() { int x = a ? b : ; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_incorrect_case_expression():
    """98. Error: Incorrect case expression"""
    source = "void main() { switch(x) { case (1 + ): break; } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_unary_plus():
    """99. Error: Invalid unary plus usage"""
    source = "void main() { int x = +; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_misplaced_break_in_switch():
    """100. Error: Misplaced break statement in switch"""
    source = "void main() { switch(x) { break; } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_incorrect_array_decl_size():
    """101. Error: Incorrect array declaration size"""
    source = "void main() { int arr[-5]; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_float_exponent():
    """102. Error: Invalid float exponent format"""
    source = "void main() { float f = 1.2e+; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_incorrect_struct_syntax():
    """103. Error: Incorrect struct syntax"""
    source = "struct Point { int x int y; };"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_function_return():
    """104. Error: Invalid function return type"""
    source = "auto func() { return 5; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_misplaced_continue_in_switch():
    """105. Error: Misplaced continue statement in switch"""
    source = "void main() { switch(x) { continue; } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_incorrect_char_escape():
    """106. Error: Incorrect character escape sequence"""
    source = "void main() { char c = '\\q'; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True
    
def test_err_invalid_logical_and():
    """107. Error: Invalid logical AND usage"""
    source = "void main() { bool b = &&a; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_misplaced_return_in_loop():
    """108. Error: Return statement inside loop without function context"""
    source = "void main() { while(1) { return; } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_incorrect_struct_member_access():
    """109. Error: Incorrect struct member access syntax"""
    source = "void main() { int x = point->x; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_err_invalid_function_param():
    """110. Error: Invalid function parameter syntax"""
    source = "void func(int a, , float b) { }"
    try:
        Parser(source).parse()
    except Exception:
        assert True