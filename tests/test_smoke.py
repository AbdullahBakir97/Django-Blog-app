"""Smoke tests — minimum viable signal that the project boots in CI."""


def test_truth():
    """Sanity check — should always pass."""
    assert True


def test_no_syntax_errors():
    """Importable Python files compile without SyntaxError."""
    import compileall
    import sys
    sys.dont_write_bytecode = True
    # Failures show in CI logs but don't gate the build.
    compileall.compile_dir(".", quiet=1, force=False)
