# NODE_LIST = [
#     'Module','Interactive','Expression','FunctionDef','ClassDef','Return',
#     'Delete','Assign','AugAssign','Print','For','While','If','With','Raise',
#     'TryExcept','TryFinally','Assert','Import','ImportFrom','Exec','Global',
#     'Expr','Pass','Break','Continue','attributes','BoolOp','BinOp','UnaryOp',
#     'Lambda','IfExp','Dict','Set','ListComp','SetComp','DictComp',
#     'GeneratorExp','Yield','Compare','Call','Repr','Num','Str','Attribute',
#     'Subscript','Name','List','Tuple','Load','Store','Del',
#     'AugLoad','AugStore','Param','Ellipsis','Slice','ExtSlice','Index','And','Or',
#     'Add','Sub','Mult','Div','Mod','Pow','LShift','RShift','BitOr','BitXor',
#     'BitAnd','FloorDiv','Invert','Not','UAdd','USub','Eq','NotEq','Lt',
#     'LtE','Gt','GtE','Is','IsNot','In','NotIn','comprehension','ExceptHandler',
#     'arguments','keyword','alias']

NODE_LIST = [
'Typedef', 'ParamList', 'For', 'UnaryOp', 'TernaryOp', 'Label', 'InitList', 'IdentifierType', 'FuncDef', 'DeclList', 'Struct', 'PtrDecl', 'Return', 'FuncCall', 'Assignment', 'FuncDecl', 'Enum', 'ID', 'Break', 'DoWhile', 'StructRef', 'BinaryOp', 'Compound', 'ArrayDecl', 'Case', 'TypeDecl', 'Default', 'Cast', 'While', 'Continue', 'ArrayRef', 'Enumerator', 'Typename', 'ExprList', 'Goto', 'Decl', 'Constant', 'FileAST', 'Switch', 'EmptyStatement', 'EnumeratorList', 'If'
]

# NODE_LIST = ['Typedef', 'Struct', 'For', 'UnaryOp', 'Union', 'CompoundLiteral', 'TernaryOp', 'Label', 'InitList', 'IdentifierType', 'FuncDef', 'TypeDecl', 'Return', 'FuncCall', 'Assignment', 'FuncDecl', 'Enum', 'ExprList', 'Break', 'DoWhile', 'StructRef', 'BinaryOp', 'Compound', 'ArrayDecl', 'Case', 'DeclList', 'Default', 'PtrDecl', 'While', 'Continue', 'ParamList', 'Enumerator', 'Typename', 'ID', 'Goto', 'Decl', 'Constant', 'Cast', 'ArrayRef', 'root', 'Switch', 'EmptyStatement', 'EnumeratorList', 'If']


#NODE_LIST = [u'PostfixExpression', u'WildcardType', u'CastExpression', u'ExpressionStatement', u'InfixExpression', u'SuperMethodInvocation', u'PrimitiveType', u'ClassInstanceCreation', u'NormalAnnotation', u'VariableDeclarationStatement', u'ParameterizedType', u'EnhancedForStatement', u'DoStatement', u'TypeParameter', u'QualifiedName', u'SimpleType', u'MemberValuePair', u'ArrayAccess', u'Assignment', u'SwitchStatement', u'CatchClause', u'ForStatement', u'BreakStatement', u'SynchronizedStatement', u'ThisExpression', u'MarkerAnnotation', u'NumberLiteral', u'BooleanLiteral', u'ParenthesizedExpression', u'ArrayCreation', u'NullLiteral', u'SimpleName', u'TryStatement', u'MethodInvocation', u'ArrayType', u'MethodDeclaration', u'SwitchCase', u'Modifier', u'Block', u'ConditionalExpression', u'TypeLiteral', u'VariableDeclarationFragment', u'FieldAccess', u'PrefixExpression', u'ThrowStatement', u'WhileStatement', u'StringLiteral', u'VariableDeclarationExpression', u'SingleMemberAnnotation', u'SingleVariableDeclaration', u'ReturnStatement', u'IfStatement']
# NODE_LIST =[u'Typedef', u'ParamList', u'For', u'UnaryOp', u'TernaryOp', u'Label', u'InitList', u'IdentifierType', u'FuncDef', u'DeclList', u'Struct', u'Return', u'FuncCall', u'Assignment', u'FuncDecl', u'Enum', u'ID', u'Break', u'DoWhile', u'StructRef', u'BinaryOp', u'Compound', u'ArrayDecl', u'Case', u'Cast', u'TypeDecl', u'Default', u'PtrDecl', u'While', u'Continue', u'ArrayRef', u'Enumerator', u'Typename', u'ExprList', u'Goto', u'Decl', u'Constant', u'FileAST', u'Switch', u'EmptyStatement', u'EnumeratorList', u'If']

NODE_MAP = {x: i for (i, x) in enumerate(NODE_LIST)}
