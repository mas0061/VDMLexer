# -*- coding: utf-8 -*-
"""
    pygments_plugin.lexers.vdm
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for VDM languages.

    :copyright: Copyright 2011 by Masayuki Ueki.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

class VDMLexer(RegexLexer):
    name = 'VDM'
    aliases = ['vdm']
    filenames = ['*.vpp', '*.vdmpp', '*.vdm', '*.vdmsl']
    mimetypes = ['text/x-vdm']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'--.*?$', Comment),
            (r'/\*', Comment, 'comment'),
            (r'\b(#act|#active|#fin|#req|#waiting|RESULT|abs|all|always|and|as|async|atomic|be|break|by|card|cases|class|comp|'
             r'compose|conc|cycles|dcl|def|definitions|dinter|div|dlclass|dlmodule|do|dom|dunion|duration|elems|else|elseif|'
             r'end|error|errs|exists|exists1|exit|export|exports|ext|extern|for|forall|from|functions|hd|if|imports|in|'
             r'inds|init|inmap|input|instance|inter|inv|inverse|iota|is not yet specified|is subclass of|is subclass responsibility|'
             r'is_|is_bool|is_char|is_int|is_nat|is_nat1|is_rat|is_real|is_token|isofbaseclass|isofclass|lambda|len|let|map|'
             r'measure|merge|mg|mk_|mod|module|mu|munion|mutex|new|not|of|operations|or|others|per|periodic|post|power|pre|'
             r'psubset|rd|rem|renamed|return|reverse|rng|samebaseclass|sameclass|self|seq|seq1|set|sizeof|skip|st|start|'
             r'startlist|state|struct|subset|sync|system|then|thread|threadid|time|tixe|tl|to|token|traces|trap|types|'
             r'undefined|union|uselib|values|variables|while|with|wr)\b', Keyword),
            (r'\b(private|protected|public|static)\b', Keyword.Declaration),
            (r'\b(bool|char|floor|int|nat|nat1|rat|real)\b', Keyword.Type),
            (r'\b(true|false|nil)\b', Keyword.Constant),
            (r"'[^']*'", String),
            (r"\"[^\"]*\"", String),
            (r'.', Text),
        ],
        'comment': [
            (r'[^*/]', Comment),
            (r'/\*', Comment, '#push'),
            (r'\*/', Comment, '#pop'),
            (r'[*/]', Comment)
        ],
    }
