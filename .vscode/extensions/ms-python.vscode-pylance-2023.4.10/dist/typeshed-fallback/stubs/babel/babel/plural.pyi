import decimal
from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from typing import Any

def extract_operands(source: float | decimal.Decimal) -> tuple[decimal.Decimal, int, int, int, int, int, int, int]: ...

class PluralRule:
    abstract: list[Any]
    def __init__(self, rules: Mapping[str, str] | Iterable[tuple[str, str]]) -> None: ...
    @classmethod
    def parse(cls, rules: Mapping[str, str] | Iterable[tuple[str, str]] | PluralRule) -> PluralRule: ...
    @property
    def rules(self) -> Mapping[str, str]: ...
    @property
    def tags(self) -> frozenset[str]: ...
    def __call__(self, n: float | decimal.Decimal) -> str: ...

def to_javascript(rule): ...
def to_python(rule): ...
def to_gettext(rule): ...
def in_range_list(num, range_list): ...
def within_range_list(num, range_list): ...
def cldr_modulo(a, b): ...

class RuleError(Exception): ...

def tokenize_rule(s): ...
def test_next_token(tokens, type_, value: Incomplete | None = ...): ...
def skip_token(tokens, type_, value: Incomplete | None = ...): ...
def value_node(value): ...
def ident_node(name): ...
def range_list_node(range_list): ...
def negate(rv): ...

class _Parser:
    tokens: Any
    ast: Any
    def __init__(self, string) -> None: ...
    def expect(self, type_, value: Incomplete | None = ..., term: Incomplete | None = ...): ...
    def condition(self): ...
    def and_condition(self): ...
    def relation(self): ...
    def newfangled_relation(self, left): ...
    def range_or_value(self): ...
    def range_list(self): ...
    def expr(self): ...
    def value(self): ...

compile_zero: Any

class _Compiler:
    def compile(self, arg): ...
    compile_n: Any
    compile_i: Any
    compile_v: Any
    compile_w: Any
    compile_f: Any
    compile_t: Any
    compile_value: Any
    compile_and: Any
    compile_or: Any
    compile_not: Any
    compile_mod: Any
    compile_is: Any
    compile_isnot: Any
    def compile_relation(self, method, expr, range_list) -> None: ...

class _PythonCompiler(_Compiler):
    compile_and: Any
    compile_or: Any
    compile_not: Any
    compile_mod: Any
    def compile_relation(self, method, expr, range_list): ...

class _GettextCompiler(_Compiler):
    compile_i: Any
    compile_v: Any
    compile_w: Any
    compile_f: Any
    compile_t: Any
    def compile_relation(self, method, expr, range_list): ...

class _JavaScriptCompiler(_GettextCompiler):
    compile_i: Any
    compile_v: Any
    compile_w: Any
    compile_f: Any
    compile_t: Any
    def compile_relation(self, method, expr, range_list): ...

class _UnicodeCompiler(_Compiler):
    compile_is: Any
    compile_isnot: Any
    compile_and: Any
    compile_or: Any
    compile_mod: Any
    def compile_not(self, relation): ...
    def compile_relation(self, method, expr, range_list, negated: bool = ...): ...
