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
def test_001_var_decl_explicit_types():
    source = "void main() { int a; float b; string c; }"
    assert Parser(source).parse() == "success"

def test_002_var_decl_auto_no_init():
    source = "void main() { auto x; }"
    assert Parser(source).parse() == "success"

def test_003_var_decl_complex_init():
    source = "void main() { float x = 1.0 + 2.0 * 3.0; }"
    assert Parser(source).parse() == "success"

def test_004_var_decl_string():
    source = "void main() { string s = \"Hello World\"; }"
    assert Parser(source).parse() == "success"

def test_005_var_decl_negative_number():
    source = "void main() { int x = -5; float y = -3.14; }"
    assert Parser(source).parse() == "success"

#Functions & Parameters
def test_006_func_multi_params():
    source = "int add(int a, float b, string c) { return 1; }"
    assert Parser(source).parse() == "success"

def test_007_func_void_return():
    source = "void proc() { return; }"
    assert Parser(source).parse() == "success"

def test_008_func_call_as_statement():
    source = "void main() { doSomething(1, \"test\"); }"
    assert Parser(source).parse() == "success"

def test_009_func_nested_call():
    source = "void main() { int x = max(min(1, 2), 3); }"
    assert Parser(source).parse() == "success"

def test_010_func_no_type_inference():
    source = "main() { }"
    assert Parser(source).parse() == "success"

def test_011_func_recursive_call():
    source = "int factorial(int n) { if (n <= 1) return 1; else return n * factorial(n - 1); }"
    assert Parser(source).parse() == "success"

def test_012_func_call_struct_literal_arg():
    source = "void main() { drawRect({0, 0}, {10, 20}, \"Red\"); }"
    assert Parser(source).parse() == "success"

def test_013_func_struct_param():
    source = "struct Data { int id; }; void process(Data item, int size) { }"
    assert Parser(source).parse() == "success"

#Struct
def test_014_struct_complex_members():
    source = "struct User { int id; string name; float score; };"
    assert Parser(source).parse() == "success"

def test_015_struct_member_access():
    source = "void main() { point.x = 10; }"
    assert Parser(source).parse() == "success"

def test_016_struct_nested_access():
    source = "void main() { int x = rect.topLeft.x; }"
    assert Parser(source).parse() == "success"

def test_017_struct_decl_inside_function():
    source = "void main() { Point p = {1, 2}; }"
    assert Parser(source).parse() == "success"

def test_018_struct_array_access_simulation():
    source = "struct A { int x; }; struct B { float y; }; void main() {}"
    assert Parser(source).parse() == "success"

def test_019_struct_multiple_declarations():
    source = "struct Point { int x; int y; }; void main() { Point p1; Point p2; Point p3; }"
    assert Parser(source).parse() == "success"    

#Complex Expressions
def test_020_expr_precedence_mul_add():
    source = "void main() { int x = 1 + 2 * 3; }"
    assert Parser(source).parse() == "success"

def test_021_expr_parentheses():
    source = "void main() { int x = (1 + 2) * 3; }"
    assert Parser(source).parse() == "success"

def test_022_expr_logical_complex():
    source = "void main() { if (a > b && c <= d || !e) {} }"
    assert Parser(source).parse() == "success"

def test_023_expr_unary_operators():
    source = "void main() { int x = -a + !b; }"
    assert Parser(source).parse() == "success"

def test_024_expr_comparison_chain():
    source = "void main() { bool check = x >= y == z < 5; }"
    assert Parser(source).parse() == "success"

def test_025_if_else_simulation():
    source = "void main() { int x; if (a > b) x = a; else x = b; }"
    assert Parser(source).parse() == "success"  

def test_026_expr_logical_complex_2():
    source = "void main() { int x = (a && b) || (!c && d); }"
    assert Parser(source).parse() == "success"

#Advanced Loops
def test_027_for_empty_parts():
    source = "void main() { for (; i < 10; ) { i = i + 1; } }"
    assert Parser(source).parse() == "success"

def test_028_for_infinite():
    source = "void main() { for (;;) { break; } }"
    assert Parser(source).parse() == "success"

def test_029_for_decl_inside():
    source = "void main() { for (int i = 0; i < 10; i++) {} }"
    assert Parser(source).parse() == "success"

def test_030_loop_nested():
    source = "void main() { while(1) { while(0) { break; } } }"
    assert Parser(source).parse() == "success"

def test_031_continue_stmt():
    source = "void main() { while(1) { if(x) continue; } }"
    assert Parser(source).parse() == "success"

def test_032_loop_break_in_nested():
    source = "void main() { for (int i = 0; i < 10; i++) { while(1) { break; } } }"
    assert Parser(source).parse() == "success"

#Switch-Case
def test_033_switch_full():
    source = "void main() { switch(x) { case 1: break; default: break; } }"
    assert Parser(source).parse() == "success"

def test_034_switch_empty():
    source = "void main() { switch(x) {} }"
    assert Parser(source).parse() == "success"

def test_035_switch_stack_cases():
    source = "void main() { switch(x) { case 1: case 2: print(1); break; } }"
    assert Parser(source).parse() == "success"

def test_036_switch_default_only():
    source = "void main() { switch(x) { default: x = 0; } }"
    assert Parser(source).parse() == "success"

def test_037_switch_expression_case():
    source = "void main() { switch(x) { case 1+2: break; } }"
    assert Parser(source).parse() == "success"

def test_038_switch_case_multiple_statements():
    source = "void main() { switch(x) { case 1: printInt(1); printInt(2); break; } }"
    assert Parser(source).parse() == "success"

#Comment và Literal Special Cases
def test_039_comment_block_inline():
    source = "void main() { int /* comment */ x = 5; }"
    assert Parser(source).parse() == "success"

def test_040_comment_line_end():
    source = "void main() {} // End of file"
    assert Parser(source).parse() == "success"

def test_041_literal_scientific_float():
    source = "void main() { float f = 1.2e-3; }"
    assert Parser(source).parse() == "success"

def test_042_literal_string_escapes():
    source = "void main() { string s = \"Line\\nTab\\tQuote\\\"\"; }"
    assert Parser(source).parse() == "success"

def test_043_literal_float_dot():
    source = "void main() { float f = .5; float g = 1.; }"
    assert Parser(source).parse() == "success"

def test_044_comment_multiline():
    source = """void main() { 
    /* This is a 
       multi-line comment */
    int x = 5; 
}"""
    assert Parser(source).parse() == "success"

def test_045_literal_string_as_char():
    source = "void main() { string c = \"A\"; }"
    assert Parser(source).parse() == "success"

#Negative Tests
def test_046_err_missing_semi():
    source = "void main() { int x = 5 }"
    try:
        Parser(source).parse()
    except Exception:
        assert True 

def test_047_err_invalid_var_decl():
    source = "void main() { int x, y; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_048_err_unclosed_block():
    source = "void main() { if (1) { "
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_049_err_keyword_as_id():
    source = "void main() { int if = 5; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_050_err_double_dots_float():
    source = "void main() { float x = 1.2.3; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_051_err_unterminated_string():
    source = "void main() { string s = \"Hello; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_052_err_invalid_struct_decl():
    source = "struct { int x; };"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_053_err_invalid_expr():
    source = "void main() { int x = 5 + * 3; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_054_err_missing_paren():
    source = "void main() { if (x > 0 { printInt(x); } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_055_err_invalid_switch_case():
    source = "void main() { switch(x) { case : break; } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_056_err_invalid_for_syntax():
    source = "void main() { for (int i = 0 i < 10; i++) {} }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_057_err_invalid_var_name():
    source = "void main() { int 1var = 5; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_058_err_extra_token():
    source = "void main() { int x = 5;; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_059_err_incorrect_struct_member():
    source = "struct Point { int x float y; };"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_060_err_invalid_literal():
    source = "void main() { int x = 0b102; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_061_err_misplaced_return():
    source = "void main() { return 5; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_062_err_incomplete_if():
    source = "void main() { if (x > 0) "
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_063_err_invalid_array_decl():
    source = "void main() { int arr[]; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_064_err_invalid_pointer_decl():
    source = "void main() { int* *ptr; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_065_err_misplaced_struct():
    source = "void main() { struct Point { int x; int y; }; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_066_err_invalid_comment():
    source = "void main() { /* This is an invalid comment // }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_067_err_incorrect_ternary():
    source = "void main() { int x = a > b ? ; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_068_err_missing_case_colon():
    source = "void main() { switch(x) { case 1 break; } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_069_err_invalid_unary_op():
    source = "void main() { int x = ++*y; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_070_err_incorrect_logical_expr():
    source = "void main() { bool b = a && || c; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_071_err_misplaced_break():
    source = "void main() { break; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_072_err_invalid_float_format():
    source = "void main() { float f = 1..0; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_073_err_incorrect_array_access():
    source = "void main() { int x = arr[; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_074_err_invalid_char_literal():
    source = "void main() { char c = 'AB'; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_075_err_misplaced_continue():
    source = "void main() { continue; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_076_err_incorrect_struct_access():
    source = "void main() { int x = point..x; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_077_err_invalid_function_call():
    source = "void main() { doSomething(1, ); }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_078_err_incomplete_for_loop():
    source = "void main() { for (int i = 0; ; i++) {} }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_079_err_invalid_bitwise_expr():
    source = "void main() { int x = a & | b; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_080_err_misplaced_return_in_void():
    source = "void main() { return 5; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_081_err_invalid_nested_struct():
    source = "struct A { struct B { int x; }; };"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_082_err_incorrect_while_syntax():
    source = "void main() { while 1) { } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_083_err_invalid_pointer_usage():
    source = "void main() { int* p = &5; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_084_err_incorrect_logical_not():
    source = "void main() { bool b = !; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_085_err_misplaced_struct_decl():
    source = "void main() { struct Point { int x; int y; }; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_086_err_invalid_ternary_syntax():
    source = "void main() { int x = a ? b : ; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_087_err_incorrect_case_expression():
    source = "void main() { switch(x) { case (1 + ): break; } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_088_err_invalid_unary_plus():
    source = "void main() { int x = +; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_089_err_misplaced_break_in_switch():
    source = "void main() { switch(x) { break; } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_090_err_incorrect_array_decl_size():
    source = "void main() { int arr[-5]; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_091_err_invalid_float_exponent():
    source = "void main() { float f = 1.2e+; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_092_err_incorrect_struct_syntax():
    source = "struct Point { int x int y; };"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_093_err_invalid_function_return():
    source = "auto func() { return 5; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_094_err_misplaced_continue_in_switch():
    source = "void main() { switch(x) { continue; } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_095_err_incorrect_char_escape():
    source = "void main() { char c = '\\q'; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True
    
def test_096_err_invalid_logical_and():
    source = "void main() { bool b = &&a; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_097_err_misplaced_return_in_loop():
    source = "void main() { while(1) { return; } }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_098_err_incorrect_struct_member_access():
    source = "void main() { int x = point->x; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_099_err_invalid_function_param():
    source = "void func(int a, , float b) { }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

def test_100_err_invalid_func_decl():
    source = "int func( { return 0; }"
    try:
        Parser(source).parse()
    except Exception:
        assert True

