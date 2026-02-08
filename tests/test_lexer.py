"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


# ========== Simple Test Cases (10 types) ==========
def test_keyword_auto():
    """1. Keyword"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"


def test_operator_assign():
    """2. Operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_separator_semi():
    """3. Separator"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"


def test_integer_single_digit():
    """4. Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"


def test_float_decimal():
    """5. Float literal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"


def test_string_simple():
    """6. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"


def test_identifier_simple():
    """7. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_line_comment():
    """8. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_integer_in_expression():
    """9. Mixed: integers and operator"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"


def test_complex_expression():
    """10. Complex: variable declaration"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"

# ========== Additional Test Cases (100 types) ==========
#Keyword Tests
def test_001_keyword_void():
    tokenizer = Tokenizer("void")
    assert tokenizer.get_tokens_as_string() == "void,<EOF>"

def test_002_keyword_int():
    tokenizer = Tokenizer("int")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"

def test_003_keyword_float():
    tokenizer = Tokenizer("float")
    assert tokenizer.get_tokens_as_string() == "float,<EOF>"

def test_004_keyword_struct():
    tokenizer = Tokenizer("struct")
    assert tokenizer.get_tokens_as_string() == "struct,<EOF>"

def test_005_keyword_if():
    tokenizer = Tokenizer("if")
    assert tokenizer.get_tokens_as_string() == "if,<EOF>"

def test_006_keyword_else():
    tokenizer = Tokenizer("else")
    assert tokenizer.get_tokens_as_string() == "else,<EOF>"

def test_007_keyword_while():
    tokenizer = Tokenizer("while")
    assert tokenizer.get_tokens_as_string() == "while,<EOF>"

def test_008_keyword_for():
    tokenizer = Tokenizer("for")    
    assert tokenizer.get_tokens_as_string() == "for,<EOF>"

def test_009_keyword_return():
    tokenizer = Tokenizer("return")
    assert tokenizer.get_tokens_as_string() == "return,<EOF>"

def test_010_keyword_break():
    tokenizer = Tokenizer("break")
    assert tokenizer.get_tokens_as_string() == "break,<EOF>"

def test_011_keyword_string():
    tokenizer = Tokenizer("string")
    assert tokenizer.get_tokens_as_string() == "string,<EOF>"

def test_012_keyword_switch():
    tokenizer = Tokenizer("switch")
    assert tokenizer.get_tokens_as_string() == "switch,<EOF>"

def test_013_keyword_case():
    tokenizer = Tokenizer("case")
    assert tokenizer.get_tokens_as_string() == "case,<EOF>"

def test_014_keyword_continue():
    tokenizer = Tokenizer("continue")
    assert tokenizer.get_tokens_as_string() == "continue,<EOF>"

def test_015_keyword_default():
    tokenizer = Tokenizer("default")
    assert tokenizer.get_tokens_as_string() == "default,<EOF>"

def test_016_keywords_case_sensitivity():
    tokenizer = Tokenizer("If While Return")
    assert tokenizer.get_tokens_as_string() == "If,While,Return,<EOF>"

# Operator Tests
def test_017_operator_equal():
    tokenizer = Tokenizer("==")
    assert tokenizer.get_tokens_as_string() == "==,<EOF>"

def test_018_operator_not_equal():
    tokenizer = Tokenizer("!=")
    assert tokenizer.get_tokens_as_string() == "!=,<EOF>"

def test_019_operator_greater_equal():
    tokenizer = Tokenizer(">=")
    assert tokenizer.get_tokens_as_string() == ">=,<EOF>"

def test_020_operator_less_equal():
    tokenizer = Tokenizer("<=")
    assert tokenizer.get_tokens_as_string() == "<=,<EOF>"

def test_021_operator_logical_and():
    tokenizer = Tokenizer("&&")
    assert tokenizer.get_tokens_as_string() == "&&,<EOF>"

def test_022_operator_logical_or():
    tokenizer = Tokenizer("||")
    assert tokenizer.get_tokens_as_string() == "||,<EOF>"

def test_023_operator_increment():
    tokenizer = Tokenizer("++")
    assert tokenizer.get_tokens_as_string() == "++,<EOF>"

def test_024_operator_decrement():
    tokenizer = Tokenizer("--")
    assert tokenizer.get_tokens_as_string() == "--,<EOF>"

def test_025_operator_addition():
    tokenizer = Tokenizer("+")
    assert tokenizer.get_tokens_as_string() == "+,<EOF>"

def test_026_operator_subtract():
    tokenizer = Tokenizer("-")
    assert tokenizer.get_tokens_as_string() == "-,<EOF>"

def test_027_operator_multiply():
    tokenizer = Tokenizer("*")
    assert tokenizer.get_tokens_as_string() == "*,<EOF>"

def test_028_operator_divide():
    tokenizer = Tokenizer("/")
    assert tokenizer.get_tokens_as_string() == "/,<EOF>"

def test_029_operator_modulus():
    tokenizer = Tokenizer("%")
    assert tokenizer.get_tokens_as_string() == "%,<EOF>"

def test_030_operator_logical_NOT():
    tokenizer = Tokenizer("!")
    assert tokenizer.get_tokens_as_string() == "!,<EOF>"

def test_031_operator_less_than():
    tokenizer = Tokenizer("<")
    assert tokenizer.get_tokens_as_string() == "<,<EOF>"

def test_032_operator_greater_than():
    tokenizer = Tokenizer(">")
    assert tokenizer.get_tokens_as_string() == ">,<EOF>"

def test_033_compound_assignment_split():
    tokenizer = Tokenizer("x += 5")
    assert tokenizer.get_tokens_as_string() == "x,+,=,5,<EOF>"

# Separator Tests
def test_034_separator_comma():
    tokenizer = Tokenizer(",")
    assert tokenizer.get_tokens_as_string() == ",,<EOF>"

def test_035_separator_dot():
    tokenizer = Tokenizer(".")
    assert tokenizer.get_tokens_as_string() == ".,<EOF>"

def test_036_separator_colon():
    tokenizer = Tokenizer(":")
    assert tokenizer.get_tokens_as_string() == ":,<EOF>"

def test_037_separator_open_brace():
    tokenizer = Tokenizer("{")
    assert tokenizer.get_tokens_as_string() == "{,<EOF>"

def test_038_separator_close_brace():
    tokenizer = Tokenizer("}")
    assert tokenizer.get_tokens_as_string() == "},<EOF>"

def test_039_separator_open_paren():
    tokenizer = Tokenizer("(")
    assert tokenizer.get_tokens_as_string() == "(,<EOF>"

def test_040_separator_close_paren():
    tokenizer = Tokenizer(")")
    assert tokenizer.get_tokens_as_string() == "),<EOF>"

def test_041_separator_newline():
    tokenizer = Tokenizer("\n")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_042_separator_whitespace():
    tokenizer = Tokenizer("   ")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

# Literal Tests
def test_043_integer_multiple_digits():
    tokenizer = Tokenizer("12345")
    assert tokenizer.get_tokens_as_string() == "12345,<EOF>"

def test_044_float_scientific_notation():
    tokenizer = Tokenizer("1.23e4")
    assert tokenizer.get_tokens_as_string() == "1.23e4,<EOF>"

def test_045_float_no_leading_digit():
    tokenizer = Tokenizer(".75")
    assert tokenizer.get_tokens_as_string() == ".75,<EOF>"

def test_046_float_no_trailing_digit():
    tokenizer = Tokenizer("12.")
    assert tokenizer.get_tokens_as_string() == "12.,<EOF>"

def test_047_float_with_E():
    tokenizer = Tokenizer("6.02E+23")
    assert tokenizer.get_tokens_as_string() == "6.02E+23,<EOF>"

def test_048_float_E_with_sign():
    tokenizer = Tokenizer("9.81e-2")
    assert tokenizer.get_tokens_as_string() == "9.81e-2,<EOF>"

def test_049_float_zero_variations():
    tokenizer = Tokenizer("0.0")
    assert tokenizer.get_tokens_as_string() == "0.0,<EOF>"

def test_050_float_multiple_dots():
    tokenizer = Tokenizer("1.2.3")
    assert tokenizer.get_tokens_as_string() == "1.2,.3,<EOF>"

def test_051_float_exponent_no_dot():
    tokenizer = Tokenizer("2E-3")
    assert tokenizer.get_tokens_as_string() == "2E-3,<EOF>"

def test_052_float_dot_start_exponent():
    tokenizer = Tokenizer(".5e-2")
    assert tokenizer.get_tokens_as_string() == ".5e-2,<EOF>"

def test_053_string_with_escaped_quotes_1():
    tokenizer = Tokenizer('"JLPT \\"N3\\"!"')
    assert tokenizer.get_tokens_as_string() == 'JLPT \\"N3\\"!,<EOF>'

def test_054_string_with_escape_sequences():
    tokenizer = Tokenizer('"Sousou\\nno\\nFrieren"')
    assert tokenizer.get_tokens_as_string() == r"Sousou\nno\nFrieren,<EOF>"

def test_055_string_with_escaped_backslash():
    tokenizer = Tokenizer('"This is a backslash: \\\\"')
    assert tokenizer.get_tokens_as_string() == r'This is a backslash: \\,<EOF>'

def test_056_string_with_escaped_tab():
    tokenizer = Tokenizer('"Before\\tAfter"')
    assert tokenizer.get_tokens_as_string() == r'Before\tAfter,<EOF>'

def test_057_string_with_escaped_backspace():
    tokenizer = Tokenizer('"Text with backspace\\b here"')
    assert tokenizer.get_tokens_as_string() == r'Text with backspace\b here,<EOF>'

def test_058_string_with_escaped_formfeed():
    tokenizer = Tokenizer('"Formfeed character here\\f end"')
    assert tokenizer.get_tokens_as_string() == r'Formfeed character here\f end,<EOF>'

def test_059_string_with_escaped_carriage_return():
    tokenizer = Tokenizer('"Line1\\rLine2"')
    assert tokenizer.get_tokens_as_string() == r'Line1\rLine2,<EOF>'

def test_060_string_with_multiple_escape_sequences():
    tokenizer = Tokenizer('"Line1\\nLine2\\tTabbed\\\\"')
    assert tokenizer.get_tokens_as_string() == r'Line1\nLine2\tTabbed\\,<EOF>'

def test_061_string_empty():
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"

def test_062_string_escaped_backslash_path():
    tokenizer = Tokenizer(r'"C:\\Windows\\System32"')
    result = tokenizer.get_tokens_as_string()
    assert r"C:\\Windows\\System32" in result

def test_063_string_with_symbols():
    tokenizer = Tokenizer('"@#$%^&*(){}"')
    assert tokenizer.get_tokens_as_string() == "@#$%^&*(){},<EOF>"

# Identifier Tests
def test_064_identifier_with_underscore():
    tokenizer = Tokenizer("my_variable")
    assert tokenizer.get_tokens_as_string() == "my_variable,<EOF>"

def test_065_identifiers_case_sensitivity():
    tokenizer = Tokenizer("MyVar myvar MYVAR")
    assert tokenizer.get_tokens_as_string() == "MyVar,myvar,MYVAR,<EOF>"

def test_066_identifier_with_digits():
    tokenizer = Tokenizer("Kanji1500")
    assert tokenizer.get_tokens_as_string() == "Kanji1500,<EOF>"

def test_067_identifier_complex_underscore():
    tokenizer = Tokenizer("__init__123")
    assert tokenizer.get_tokens_as_string() == "__init__123,<EOF>"
    
def test_068_identifier_beginning_with_underscore():
    tokenizer = Tokenizer("_privateVar")
    assert tokenizer.get_tokens_as_string() == "_privateVar,<EOF>"

def test_069_identifier_with_mixed_characters():
    tokenizer = Tokenizer("var_123Name")
    assert tokenizer.get_tokens_as_string() == "var_123Name,<EOF>"

def test_070_identifier_containing_keyword():
    tokenizer = Tokenizer("autoPilot format whileLoop")
    assert tokenizer.get_tokens_as_string() == "autoPilot,format,whileLoop,<EOF>"

def test_071_identifier_end_with_underscore():
    tokenizer = Tokenizer("variable_")
    assert tokenizer.get_tokens_as_string() == "variable_,<EOF>"

# Comment Tests
def test_072_line_comment_with_code():
    tokenizer = Tokenizer("// This is a number\nint x;")
    assert tokenizer.get_tokens_as_string() == "int,x,;,<EOF>"

def test_073_block_comment():
    tokenizer = Tokenizer("/* This is a \n block comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_074_block_comment_with_code():
    tokenizer = Tokenizer("/* Comment */ float y;")
    assert tokenizer.get_tokens_as_string() == "float,y,;,<EOF>"

def test_075_nested_block_comments():
    tokenizer = Tokenizer("/* Outer comment /* Inner comment */ End of outer */")
    assert tokenizer.get_tokens_as_string() == "End,of,outer,*,/,<EOF>"

def test_076_mixed_code_and_comments():
    tokenizer = Tokenizer("int x; // variable x\n/* block comment */ float y;")
    assert tokenizer.get_tokens_as_string() == "int,x,;,float,y,;,<EOF>"

def test_077_expression_with_all_operators():
    tokenizer = Tokenizer("a = b + c - d * e / f == g != h >= i <= j && k || l++;")
    assert tokenizer.get_tokens_as_string() == "a,=,b,+,c,-,d,*,e,/,f,==,g,!=,h,>=,i,<=,j,&&,k,||,l,++,;,<EOF>"

#Error Tests
def test_078_string_error_precedence():
    tokenizer = Tokenizer('"This has bad escape \\z and is unclosed')
    result = tokenizer.get_tokens_as_string()
    assert "Illegal Escape" in result and "Unclosed String" not in result

def test_079_unterminated_string():
    tokenizer = Tokenizer('"This is an unterminated string')
    result = tokenizer.get_tokens_as_string()
    assert "Error Token" in result or "Unclosed String" in result or "UncloseString" in result

def test_080_invalid_character():
    tokenizer = Tokenizer("@")
    assert "Error Token" in tokenizer.get_tokens_as_string()

def test_081_error_char():
    tokenizer = Tokenizer("#")
    assert "Error Token" in tokenizer.get_tokens_as_string()

def test_082_error_char_2():
    tokenizer = Tokenizer("$")
    assert "Error Token" in tokenizer.get_tokens_as_string()

def test_083_error_char_3():
    tokenizer = Tokenizer("^")
    assert "Error Token" in tokenizer.get_tokens_as_string()

def test_084_error_char_4():
    tokenizer = Tokenizer("`")
    assert "Error Token" in tokenizer.get_tokens_as_string()

def test_085_illegal_escape_sequence():
    tokenizer = Tokenizer('"Bad escape \\q"')
    result = tokenizer.get_tokens_as_string()
    assert "Illegal Escape" in result and "Bad escape \\q" in result

def test_086_illegal_escape_sequence_x():
    tokenizer = Tokenizer(r'"Hex \x01"')
    result = tokenizer.get_tokens_as_string()
    assert "Illegal Escape" in result and "Hex \\x" in result

def test_087_illegal_escape_quote():
    tokenizer = Tokenizer(r'"Bad \q escape"')
    result = tokenizer.get_tokens_as_string()
    assert "Illegal Escape" in result and "Bad \\q" in result

#Boundary / Sticky Tests
def test_088_sticky_operators_parens():
    tokenizer = Tokenizer("func(a,b)")
    assert tokenizer.get_tokens_as_string() == "func,(,a,,,b,),<EOF>"

def test_089_sticky_arithmetic():
    tokenizer = Tokenizer("1+2*3-4")
    assert tokenizer.get_tokens_as_string() == "1,+,2,*,3,-,4,<EOF>"

def test_090_sticky_relational():
    tokenizer = Tokenizer("a>=b")
    assert tokenizer.get_tokens_as_string() == "a,>=,b,<EOF>"

def test_091_sticky_member_access():
    tokenizer = Tokenizer("person.name")
    assert tokenizer.get_tokens_as_string() == "person,.,name,<EOF>"

def test_092_sticky_semicolon():
    tokenizer = Tokenizer("return 0;")
    assert tokenizer.get_tokens_as_string() == "return,0,;,<EOF>"

#Integration / Fragments Tests
def test_093_fragment_struct_declaration():
    tokenizer = Tokenizer("struct Point { int x; int y; };")
    assert tokenizer.get_tokens_as_string() == "struct,Point,{,int,x,;,int,y,;,},;,<EOF>"

def test_094_fragment_array_access_simulation():
    tokenizer = Tokenizer("printInt(arr);")
    assert tokenizer.get_tokens_as_string() == "printInt,(,arr,),;,<EOF>"

def test_095_fragment_increment_loop():
    tokenizer = Tokenizer("i++;")
    assert tokenizer.get_tokens_as_string() == "i,++,;,<EOF>"

def test_096_whitespace_form_feed():
    tokenizer = Tokenizer("int\fx") 
    assert tokenizer.get_tokens_as_string() == "int,x,<EOF>"

#Looking wrong but true
def test_097_unterminated_block_comment():
    tokenizer = Tokenizer("/* This is an unterminated block comment")
    res = tokenizer.get_tokens_as_string()
    assert "/" in res and "*" in res
    
def test_098_invalid_number_format():
    tokenizer = Tokenizer("12.34.56")
    assert tokenizer.get_tokens_as_string() == "12.34,.56,<EOF>"

def test_099_identifier_starting_with_digit():
    tokenizer = Tokenizer("1variable")
    assert tokenizer.get_tokens_as_string() == "1,variable,<EOF>"

def test_100_malformed_operator():
    tokenizer = Tokenizer("===")
    assert tokenizer.get_tokens_as_string() == "==,=,<EOF>"
