from pygments.lexer import RegexLexer
from pygments.token import Text, Name, Number, String, Operator, Keyword, Punctuation, Comment


class HclLexer(RegexLexer):
    name = 'HCL'
    aliases = ['hcl']
    filenames = ['*.hcl', '*.tf']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'#.*$', Comment.Single),
            (r'\b(resource|provider|variable|output|module)\b', Keyword),
            (r'\b(true|false|null)\b', Keyword.Constant),
            (r'\b[0-9]+\b', Number),
            (r'"(\\\\|\\"|[^"])*"', String),
            (r'[-a-zA-Z0-9_]+', Name),
            (r'[{}()\[\],.:]', Punctuation),
            (r'[=]', Operator),
        ]
    }
