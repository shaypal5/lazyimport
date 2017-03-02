"""Errors for lazyimport."""


class IllegalUseOfScopeReplacer(Exception):
    """Raised when an illegal use of ScopeReplacer is made."""

    _fmt = ("ScopeReplacer object %(name)r was used incorrectly:"
            " %(msg)s%(extra)s")

    def __init__(self, name, msg, extra=None):
        Exception.__init__(self)
        self.name = name
        self.msg = msg
        if extra:
            self.extra = ': ' + str(extra)
        else:
            self.extra = ''


class InvalidImportLine(Exception):
    """Raised when an non-valid import statement is given to lazyimport."""

    _fmt = "Not a valid import statement: %(msg)\n%(text)s"

    def __init__(self, text, msg):
        Exception.__init__(self)
        self.text = text
        self.msg = msg


class ImportNameCollision(Exception):
    """Raised when an already imported object import was attempted."""

    _fmt = ("Tried to import an object to the same name as"
            " an existing object. %(name)s")

    def __init__(self, name):
        Exception.__init__(self)
        self.name = name
