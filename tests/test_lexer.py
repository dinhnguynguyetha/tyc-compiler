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
def test_keyword_void():
    """11. Keyword void"""
    tokenizer = Tokenizer("void")
    assert tokenizer.get_tokens_as_string() == "void,<EOF>"

def test_keyword_int():
    """12. Keyword int"""
    tokenizer = Tokenizer("int")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"

def test_keyword_float():
    """13. Keyword float"""
    tokenizer = Tokenizer("float")
    assert tokenizer.get_tokens_as_string() == "float,<EOF>"

def test_keyword_struct():
    """14. Keyword struct"""
    tokenizer = Tokenizer("struct")
    assert tokenizer.get_tokens_as_string() == "struct,<EOF>"

def test_keyword_if():
    """15. Keyword if"""
    tokenizer = Tokenizer("if")
    assert tokenizer.get_tokens_as_string() == "if,<EOF>"

def test_keyword_else():
    """16. Keyword else"""
    tokenizer = Tokenizer("else")
    assert tokenizer.get_tokens_as_string() == "else,<EOF>"

def test_keyword_while():
    """17. Keyword while"""
    tokenizer = Tokenizer("while")
    assert tokenizer.get_tokens_as_string() == "while,<EOF>"

def test_keyword_for():
    """18. Keyword for"""
    tokenizer = Tokenizer("for")    
    assert tokenizer.get_tokens_as_string() == "for,<EOF>"

def test_keyword_return():
    """19. Keyword return"""
    tokenizer = Tokenizer("return")
    assert tokenizer.get_tokens_as_string() == "return,<EOF>"

def test_keyword_break():
    """20. Keyword break"""
    tokenizer = Tokenizer("break")
    assert tokenizer.get_tokens_as_string() == "break,<EOF>"

def test_keyword_string():
    """21. Keyword string"""
    tokenizer = Tokenizer("string")
    assert tokenizer.get_tokens_as_string() == "string,<EOF>"

def test_keyword_switch():
    """22. Keyword switch"""
    tokenizer = Tokenizer("switch")
    assert tokenizer.get_tokens_as_string() == "switch,<EOF>"

def test_keyword_case():
    """23. Keyword case"""
    tokenizer = Tokenizer("case")
    assert tokenizer.get_tokens_as_string() == "case,<EOF>"

# Operator Tests
def test_operator_equal():
    """24. IsEqual operator"""
    tokenizer = Tokenizer("==")
    assert tokenizer.get_tokens_as_string() == "==,<EOF>"

def test_operator_not_equal():
    """25. NotEqual operator"""
    tokenizer = Tokenizer("!=")
    assert tokenizer.get_tokens_as_string() == "!=,<EOF>"

def test_operator_greater_equal():
    """26. GreaterEqual operator"""
    tokenizer = Tokenizer(">=")
    assert tokenizer.get_tokens_as_string() == ">=,<EOF>"

def test_operator_less_equal():
    """27. LessEqual operator"""
    tokenizer = Tokenizer("<=")
    assert tokenizer.get_tokens_as_string() == "<=,<EOF>"

def test_operator_logical_and():
    """28. LogicalAnd operator"""
    tokenizer = Tokenizer("&&")
    assert tokenizer.get_tokens_as_string() == "&&,<EOF>"

def test_operator_logical_or():
    """29. LogicalOr operator"""
    tokenizer = Tokenizer("||")
    assert tokenizer.get_tokens_as_string() == "||,<EOF>"

def test_operator_increment():
    """30. Increment operator"""
    tokenizer = Tokenizer("++")
    assert tokenizer.get_tokens_as_string() == "++,<EOF>"

def test_operator_decrement():
    """31. Decrement operator"""
    tokenizer = Tokenizer("--")
    assert tokenizer.get_tokens_as_string() == "--,<EOF>"

def test_operator_addition():
    """32. Add operator"""
    tokenizer = Tokenizer("+")
    assert tokenizer.get_tokens_as_string() == "+,<EOF>"

def test_operator_subtract():
    """33. Subtract operator"""
    tokenizer = Tokenizer("-")
    assert tokenizer.get_tokens_as_string() == "-,<EOF>"

def test_operator_multiply():
    """34. Multiply operator"""
    tokenizer = Tokenizer("*")
    assert tokenizer.get_tokens_as_string() == "*,<EOF>"

def test_operator_divide():
    """35. Divide operator"""
    tokenizer = Tokenizer("/")
    assert tokenizer.get_tokens_as_string() == "/,<EOF>"

# Separator Tests
def test_separator_comma():
    """36. Separator comma"""
    tokenizer = Tokenizer(",")
    assert tokenizer.get_tokens_as_string() == ",,<EOF>"

def test_separator_dot():
    """37. Separator dot"""
    tokenizer = Tokenizer(".")
    assert tokenizer.get_tokens_as_string() == ". ,<EOF>"

def test_separator_colon():
    """38. Separator colon"""
    tokenizer = Tokenizer(":")
    assert tokenizer.get_tokens_as_string() == ": ,<EOF>"

def test_separator_open_brace():
    """39. Separator open brace"""
    tokenizer = Tokenizer("{")
    assert tokenizer.get_tokens_as_string() == "{ ,<EOF>"

def test_separator_close_brace():
    """40. Separator close brace"""
    tokenizer = Tokenizer("}")
    assert tokenizer.get_tokens_as_string() == "} ,<EOF>"

def test_separator_open_paren():
    """41. Separator open parenthesis"""
    tokenizer = Tokenizer("(")
    assert tokenizer.get_tokens_as_string() == "( ,<EOF>"

def test_separator_close_paren():
    """42. Separator close parenthesis"""
    tokenizer = Tokenizer(")")
    assert tokenizer.get_tokens_as_string() == ") ,<EOF>"

def test_separator_newline():
    """43. Separator newline"""
    tokenizer = Tokenizer("\n")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_separator_whitespace():
    """44. Separator whitespace"""
    tokenizer = Tokenizer("   ")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

# Literal Tests
def test_integer_multiple_digits():
    """45. Integer literal multiple digits"""
    tokenizer = Tokenizer("12345")
    assert tokenizer.get_tokens_as_string() == "12345,<EOF>"

def test_float_scientific_notation():
    """46. Float literal scientific notation"""
    tokenizer = Tokenizer("1.23e4")
    assert tokenizer.get_tokens_as_string() == "1.23e4,<EOF>"

def test_string_with_escape_sequences():
    """47. String literal with escape sequences"""
    tokenizer = Tokenizer('"Sousou\\nno\\nFrieren"')
    assert tokenizer.get_tokens_as_string() == "Sousou\nno\nFrieren,<EOF>"

# Identifier Tests
def test_identifier_with_underscore():
    """48. Identifier with underscore"""
    tokenizer = Tokenizer("my_variable")
    assert tokenizer.get_tokens_as_string() == "my_variable,<EOF>"

def test_identifier_with_digits():
    """49. Identifier with digits"""
    tokenizer = Tokenizer("Kanji1500")
    assert tokenizer.get_tokens_as_string() == "Kanji1500,<EOF>"
    
# Comment Tests
def test_line_comment_with_code():
    """50. Line comment with code after"""
    tokenizer = Tokenizer("// This is a number\nint x;")
    assert tokenizer.get_tokens_as_string() == "int,x,;,<EOF>"

def test_block_comment():
    """51. Block comment"""
    tokenizer = Tokenizer("/* This is a \n block comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_block_comment_with_code():
    """52. Block comment with code after"""
    tokenizer = Tokenizer("/* Comment */ float y;")
    assert tokenizer.get_tokens_as_string() == "float,y,;,<EOF>"

def test_nested_block_comments():
    """53. Nested block comments"""
    tokenizer = Tokenizer("/* Outer comment /* Inner comment */ End of outer */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_mixed_code_and_comments():
    """54. Mixed code and comments"""
    tokenizer = Tokenizer("int x; // variable x\n/* block comment */ float y;")
    assert tokenizer.get_tokens_as_string() == "int,x,;,float,y,;,<EOF>"

def test_expression_with_all_operators():
    """55. Expression with all operators"""
    tokenizer = Tokenizer("a = b + c - d * e / f == g != h >= i <= j && k || l++;")
    assert tokenizer.get_tokens_as_string() == "a,=,b,+,c,-,d,*,e,/,f,==,g,!=,h,>=,i,<=,j,&&,k,||,l,++,;,<EOF>"

#Error Tests
def test_unterminated_string():
    """56. Unterminated string literal"""
    tokenizer = Tokenizer('"This is an unterminated string')
    with pytest.raises(Exception):
        tokenizer.get_tokens_as_string()

def test_invalid_character():
    """57. Invalid character"""
    tokenizer = Tokenizer("@")
    with pytest.raises(Exception):
        tokenizer.get_tokens_as_string()

def test_unterminated_block_comment():
    """58. Unterminated block comment"""
    tokenizer = Tokenizer("/* This is an unterminated block comment")
    with pytest.raises(Exception):
        tokenizer.get_tokens_as_string()
    
def test_invalid_number_format():
    """59. Invalid number format"""
    tokenizer = Tokenizer("12.34.56")
    with pytest.raises(Exception):
        tokenizer.get_tokens_as_string()

def test_identifier_starting_with_digit():
    """60. Identifier starting with digit"""
    tokenizer = Tokenizer("1variable")
    with pytest.raises(Exception):
        tokenizer.get_tokens_as_string()

def test_malformed_operator():
    """61. Malformed operator"""
    tokenizer = Tokenizer("===")
    with pytest.raises(Exception):
        tokenizer.get_tokens_as_string()

def test_error_char():
    """62. Error character 1"""
    tokenizer = Tokenizer("#")
    with pytest.raises(Exception):
        tokenizer.get_tokens_as_string()

def test_error_char_2():
    """63. Error character 2"""
    tokenizer = Tokenizer("$")
    with pytest.raises(Exception):
        tokenizer.get_tokens_as_string()

def test_error_char_3():
    """64. Error character 3"""
    tokenizer = Tokenizer("^")
    with pytest.raises(Exception):
        tokenizer.get_tokens_as_string()

def test_error_char_4():
    """65. Error character 4"""
    tokenizer = Tokenizer("`")
    with pytest.raises(Exception):
        tokenizer.get_tokens_as_string()

#Forgotten Test
def test_operator_modulus():
    """66. Modulus operator"""
    tokenizer = Tokenizer("%")
    assert tokenizer.get_tokens_as_string() == "%,<EOF>"

def test_operator_logical_NOT():
    """67. Logical NOT operator"""
    tokenizer = Tokenizer("!")
    assert tokenizer.get_tokens_as_string() == "!,<EOF>"

def test_operator_less_than():
    """68. LessThan operator"""
    tokenizer = Tokenizer("<")
    assert tokenizer.get_tokens_as_string() == "<,<EOF>"

def test_operator_greater_than():
    """69. GreaterThan operator"""
    tokenizer = Tokenizer(">")
    assert tokenizer.get_tokens_as_string() == ">,<EOF>"

def test_float_no_leading_digit():
    """70. Float literal with no leading digit"""
    tokenizer = Tokenizer(".75")
    assert tokenizer.get_tokens_as_string() == ".75,<EOF>"

def test_float_no_trailing_digit():
    """71. Float literal with no trailing digit"""
    tokenizer = Tokenizer("12.")
    assert tokenizer.get_tokens_as_string() == "12.,<EOF>"

def test_float_with_E():
    """72. Float literal with E and plus sign"""
    tokenizer = Tokenizer("6.02E+23")
    assert tokenizer.get_tokens_as_string() == "6.02E+23,<EOF>"

def test_float_E_with_sign():
    """73. Float literal with e and minus sign"""
    tokenizer = Tokenizer("9.81e-2")
    assert tokenizer.get_tokens_as_string() == "9.81e-2,<EOF>"

def test_string_with_escaped_quotes_1():
    """74. String literal with escaped quotes"""
    tokenizer = Tokenizer('"Hello \\"World\\"!"')
    assert tokenizer.get_tokens_as_string() == 'Hello \\"World\\"!,<EOF>'

def test_keyword_continue():
    """75. Keyword continue"""
    tokenizer = Tokenizer("continue")
    assert tokenizer.get_tokens_as_string() == "continue,<EOF>"

def test_keyword_default():
    """76. Keyword default"""
    tokenizer = Tokenizer("default")
    assert tokenizer.get_tokens_as_string() == "default,<EOF>"

def test_string_with_escaped_backslash():
    """77. String literal with escaped backslash"""
    tokenizer = Tokenizer('"This is a backslash: \\\\"')
    assert tokenizer.get_tokens_as_string() == 'This is a backslash: \\,<EOF>'

def test_string_with_escaped_tab():
    """78. String literal with escaped tab"""
    tokenizer = Tokenizer('"Column1\\tColumn2"')
    assert tokenizer.get_tokens_as_string() == 'Column1\tColumn2,<EOF>'

def test_string_with_escaped_backspace():
    """79. String literal with escaped backspace"""
    tokenizer = Tokenizer('"Text with backspace\\b here"')
    assert tokenizer.get_tokens_as_string() == 'Text with backspace\b here,<EOF>'

def test_string_with_escaped_formfeed():
    """80. String literal with escaped formfeed"""
    tokenizer = Tokenizer('"Formfeed character here\\f end"')
    assert tokenizer.get_tokens_as_string() == 'Formfeed character here\f end,<EOF>'

def test_string_with_escaped_carriage_return():
    """81. String literal with escaped carriage return"""
    tokenizer = Tokenizer('"Line1\\rLine2"')
    assert tokenizer.get_tokens_as_string() == 'Line1\rLine2,<EOF>'

def test_string_with_multiple_escape_sequences():
    """82. String literal with multiple escape sequences"""
    tokenizer = Tokenizer('"Line1\\nLine2\\tTabbed\\\\"')
    assert tokenizer.get_tokens_as_string() == 'Line1\nLine2\tTabbed\\,<EOF>'

def test_identifier_beginning_with_underscore():
    """83. Identifier beginning with underscore"""
    tokenizer = Tokenizer("_privateVar")
    assert tokenizer.get_tokens_as_string() == "_privateVar,<EOF>"

def test_identifier_with_mixed_characters():
    """84. Identifier with mixed characters"""
    tokenizer = Tokenizer("var_123Name")
    assert tokenizer.get_tokens_as_string() == "var_123Name,<EOF>"

def test_illegal_escape_sequence():
    """85. Illegal escape sequence"""
    tokenizer = Tokenizer('"Bad escape \\q"')
    with pytest.raises(Exception):
        tokenizer.get_tokens_as_string()

def test_float_zero_variations():
    """86. Float literal zero variations"""
    tokenizer = Tokenizer("0.0")
    assert tokenizer.get_tokens_as_string() == "0.0,<EOF>"

def test_string_empty():
    """87. Empty string literal"""
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"

def test_string_with_symbols():
    """88. String with special symbols"""
    tokenizer = Tokenizer('"@#$%^&*(){}"')
    assert tokenizer.get_tokens_as_string() == "@#$%^&*(){},<EOF>"

def test_sticky_operators_parens():
    """87. Sticky tokens: Parens and identifiers"""
    tokenizer = Tokenizer("func(a,b)")
    assert tokenizer.get_tokens_as_string() == "func,(,a,,,b,),<EOF>"

def test_sticky_arithmetic():
    """88. Sticky tokens: Arithmetic without spaces"""
    tokenizer = Tokenizer("1+2*3-4")
    assert tokenizer.get_tokens_as_string() == "1,+,2,*,3,-,4,<EOF>"

def test_sticky_relational():
    """89. Sticky tokens: Relational operators"""
    tokenizer = Tokenizer("a>=b")
    assert tokenizer.get_tokens_as_string() == "a,>=,b,<EOF>"

def test_sticky_member_access():
    """90. Sticky tokens: Struct member access"""
    tokenizer = Tokenizer("person.name")
    assert tokenizer.get_tokens_as_string() == "person,.,name,<EOF>"

def test_sticky_semicolon():
    """91. Sticky tokens: Semicolon after literal"""
    tokenizer = Tokenizer("return 0;")
    assert tokenizer.get_tokens_as_string() == "return,0,;,<EOF>"

def test_identifier_containing_keyword():
    """92. Identifier containing keyword text"""
    tokenizer = Tokenizer("autoPilot format whileLoop")
    assert tokenizer.get_tokens_as_string() == "autoPilot,format,whileLoop,<EOF>"

def test_keywords_case_sensitivity():
    """93. Keywords are case sensitive (should be identifiers)"""
    tokenizer = Tokenizer("If While Return")
    assert tokenizer.get_tokens_as_string() == "If,While,Return,<EOF>"

def test_identifier_end_with_underscore():
    """94. Identifier ending with underscore"""
    tokenizer = Tokenizer("variable_")
    assert tokenizer.get_tokens_as_string() == "variable_,<EOF>"

def test_fragment_struct_declaration():
    """95. Struct declaration fragment"""
    tokenizer = Tokenizer("struct Point { int x; int y; };")
    assert tokenizer.get_tokens_as_string() == "struct,Point,{,int,x,;,int,y,;,},;,<EOF>"

def test_fragment_array_access_simulation():
    """96. Function call fragment"""
    tokenizer = Tokenizer("printInt(arr);")
    assert tokenizer.get_tokens_as_string() == "printInt,(,arr,),;,<EOF>"

def test_fragment_increment_loop():
    """97. Increment in loop context"""
    tokenizer = Tokenizer("i++;")
    assert tokenizer.get_tokens_as_string() == "i,++,;,<EOF>"

def test_illegal_escape_sequence_x():
    """98. Illegal escape sequence (hex not supported)"""
    tokenizer = Tokenizer(r'"Hex \x01"')
    with pytest.raises(Exception):
        tokenizer.get_tokens_as_string()

def test_illegal_escape_quote():
    """99. Illegal escape inside string"""
    tokenizer = Tokenizer(r'"Bad \q escape"')
    with pytest.raises(Exception):
        tokenizer.get_tokens_as_string()

def test_float_multiple_dots():
    """100. Malformed float (multiple dots)"""
    tokenizer = Tokenizer("1.2.3")
    assert tokenizer.get_tokens_as_string() == "1.2,.,3,<EOF>"