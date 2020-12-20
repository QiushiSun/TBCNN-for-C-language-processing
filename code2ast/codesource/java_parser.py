import json
import pickle
from java_ast import JavaAST

def gen_ast(source):
    if 'root' in source:
        return gen_ast(source['root'])
    elif 'type' in source:
        if not source['type'] == 'Javadoc':
            # ast_node = {
            #     'name': source['type'],
            #     'value': source['value'] if 'value' in source else '',
            #     'child': [],
            # }
            ast_node = JavaAST(source['type'], value=source['value'] if 'value' in source else '', child=[])
            if 'children' not in source:
                print "ERROR, no children", source
            else:
                for child in source['children']:
                    ast_child = gen_ast(child)
                    if ast_child is not None:
                        ast_node.child.append(ast_child)
            return ast_node
    else:
        print "ERROR, no root or type", source

def print_ast(ast):
    print ast['name'], ast['value']
    for child in ast['child']:
        print_ast(child)

label_word = [u'method', u'method.', u'methods', u'Module', u'modules', u'class']

def read_java_json(infile, outfile=None):
    data = []
    count1=0
    with open(infile, 'r') as file_handler:
        java = json.load(file_handler)
        for code in java[0:100]:
            label = '0'
            for lw in label_word:
                if lw in code['comment']:
                    label = '1'
                    count1 += 1
            data.append({
                'tree': gen_ast(code), 'metadata': {'label': label}
            })

    print count1

    if outfile is not None:
        print('Dumping scripts')
        with open(outfile, 'wb') as file_handler:
            pickle.dump(data, file_handler, -1)

    return data
