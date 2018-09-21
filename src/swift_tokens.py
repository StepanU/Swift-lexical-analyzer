keywords = {}
operators = {}
delimiters = {}

# DECLARATIONS
keywords['associatedtype'] = 'D_ASSOCIATED_TYPE'
keywords['class'] = 'D_CLASS'
keywords['deinit'] = 'D_DEINIT'
keywords['enum'] = 'D_ENUM'
keywords['extension'] = 'D_EXTENSION'
keywords['fileprivate'] = 'D_FILE_PRIVATE'
keywords['func'] = 'D_DEFINE_FUNCTION'
keywords['import'] = 'D_IMPORT'
keywords['init'] = 'D_INIT'
keywords['inout'] = 'D_INOUT'
keywords['let'] = 'D_LET'
keywords['open'] = 'D_OPEN'
keywords['operator'] = 'D_OPERATOR'
keywords['private'] = 'D_PRIVATE'
keywords['protocol'] = 'D_PROTOCOL'
keywords['public'] = 'D_PUBLIC'
keywords['static'] = 'D_STATIC'
keywords['struct'] = 'D_STRUCT'
keywords['subscript'] = 'D_SUBSCRIPT'
keywords['typealias'] = 'D_TYPE_ALIAS'
keywords['var'] = 'D_VAR'
# STATEMENTS
keywords['break'] = 'S_BREAK'
keywords['case'] = 'S_CASE'
keywords['continue'] = 'S_CONTINUE'
keywords['default'] = 'S_DEFAULT'
keywords['defer'] = 'S_DEFER'
keywords['do'] = 'S_DO'
keywords['else'] = 'S_ELSE'
keywords['fallthrough'] = 'S_FALLTHROUGH'
keywords['for'] = 'S_FOR'
keywords['guard'] = 'S_GUARD'
keywords['if'] = 'S_IF'
keywords['in'] = 'S_IN'
keywords['repeat'] = 'S_REPEAT'
keywords['return'] = 'S_RETURN'
keywords['switch'] = 'S_SWITCH'
keywords['where'] = 'S_WHERE'
keywords['while'] = 'S_WHILE'
# EXPRESSIONS
keywords['as'] = 'E_AS'
keywords['Any'] = 'E_ANY'
keywords['catch'] = 'E_CATCH'
keywords['false'] = 'E_FALSE'
keywords['true'] = 'E_TRUE'
keywords['try'] = 'E_TRY'
keywords['is'] = 'E_IS'
keywords['nil'] = 'E_NIL'
keywords['rethrows'] = 'E_RETHROWS'
keywords['super'] = 'E_SUPER'
keywords['self'] = 'E_SELF'
keywords['Self'] = 'E_SELF_CAPITAL'
keywords['throw'] = 'E_THROW'
keywords['throws'] = 'E_THROWS'
# PATTERNS
keywords[' _ '] = 'P_UNDERSCORE'
# KEYWORD WITH A NUMBER SIGN
keywords['#available'] = '#_AVAILABLE'
keywords['#colorLiteral'] = '#_COLOR_LITERAL'
keywords['#column'] = '#_COLUMN'
keywords['#else'] = '#_ELSE'
keywords['#elseif'] = '#_ELSE_IF'
keywords['#endif'] = '#_END_IF'
keywords['#error'] = '#_ERROR'
keywords['#file'] = '#_FILE'
keywords['#fileLiteral'] = '#_FILE_LITERAL'
keywords['#function'] = '#_FUNCTION'
keywords['#if'] = '#_IF'
keywords['#imageLiteral'] = '#_IMAGE_LITERAL'
keywords['#line'] = '#_LINE'
keywords['#selector'] = '#_SELECTOR'
keywords['#sourceLocation'] = '#_SOURCE_LOCATION'
keywords['#warning'] = '#_WARNING'
# KEYWORDS RESERVED IN PARTICULAR CONTEXTS
keywords['associativity'] = 'C_ASSOCIATIVITY'
keywords['convenience'] = 'C_CONVENIENCE'
keywords['dynamic'] = 'C_DYNAMIC'
keywords['didSet'] = 'C_DID_SET'
keywords['final'] = 'C_FINAL'
keywords['get'] = 'C_GET'
keywords['infix'] = 'C_INFIX'
keywords['indirect'] = 'C_INDIRECT'
keywords['lazy'] = 'C_LAZY'
keywords['left'] = 'C_LEFT'
keywords['mutating'] = 'C_MUTATING'
keywords['none'] = 'C_NONE'
keywords['nonmutating'] = 'C_NONMUTATING'
keywords['optional'] = 'C_OPTIONAL'
keywords['override'] = 'C_OVERRIDE'
keywords['postfix'] = 'C_POSTFIX'
keywords['precedence'] = 'C_PRECEDENCE'
keywords['prefix'] = 'C_PREFIX'
keywords['Protocol'] = 'C_PROTOCOL'
keywords['required'] = 'C_REQUIRED'
keywords['right'] = 'C_RIGHT'
keywords['Type'] = 'C_TYPE'
keywords['set'] = 'C_SET'
keywords['unowned'] = 'C_UNOWNED'
keywords['weak'] = 'C_WEAK'
keywords['willSet'] = 'C_WILDSET'
# DELIMETERS
delimiters['('] = 'DEL_LP'  # Left Parenthesis
delimiters[')'] = 'DEL_RP'
delimiters['{'] = 'DEL_LCP'  # Left Curve Parenthesis
delimiters['}'] = 'DEL_RCP'
delimiters['['] = 'DEL_LSP'  # Left Square Parenthesis
delimiters[']'] = 'DEL_RSP'
delimiters[','] = 'DEL_COMMA'
delimiters['.'] = 'DEL_DOT'
delimiters[':'] = 'DEL_COLON'
delimiters[';'] = 'DEL_SEMICOLON'
delimiters['='] = 'DEL_EQUAL'
delimiters['@'] = 'DEL_AT'
delimiters['#'] = 'DEL_SHARP??'
delimiters['&'] = 'DEL_AMPERSAND'
delimiters['->'] = 'DEL_ARROW'
delimiters['`'] = 'DEL_APOSTROPH'
delimiters['?'] = 'DEL_QUEST_CONSUMER'
delimiters['!'] = 'DEL_QUEST_GIVER'
# OPERATORS
operators['+'] = 'O_PLUS'
operators['*'] = 'O_MULT'
operators['*'] = 'O_POWER'
operators['-'] = 'O_MINUS'
operators['/'] = 'O_DIV'
operators['%'] = 'O_MOD'  # 'O_REMINDER_OF_BETTER_DAYS'

# TO ADD + - = etc.