from tomarkdown import py_source_to_token, token_line_to_str, token_line_to_yaml, yaml_to_md

import pathlib


def display(row: dict, indent = 0) -> None:
    if 'name' in row:
        print(f'{" "*indent}{row["name"]} (kind: {row["kind"]})')
        indent += 2
        for key, val in row.items():
            if key in ('functions', 'classes', 'name', 'kind', 'child_of'): continue
            print(f'{" "*indent}{key}: {val}')
        if 'child_of' in row:
            child = None
            if not (row['child_of'] is None): child = row['child_of']['name']
            print(f'{" "*indent}child_of: {child}')
        if 'functions' in row:
            print(f'{" "*indent}functions:')
            for row_func in row['functions']: display(row_func, indent + 2)
        if 'classes' in row:
            print(f'{" "*indent}classes:')
            for row_clas in row['classes']: display(row_clas, indent + 2)
    else:
        print(f'{" "*indent}docstring')
        indent += 2
        for key, val in row.items():
            if key in ('kind', 'note'): continue
            print(f'{" "*indent}{key}: {val}')
        if 'note' in row:
            print(f'{" "*indent}note: {repr(row["note"])}')


def main():
    name: str = 'my_script'

    path = pathlib.Path(f'{name}').with_suffix('.py')

    py_lines = py_source_to_token(path_from = path)
    # for py_line in py_lines:
    #     print(py_line)
    #     print(token_line_to_str(py_line))

    struct = token_line_to_yaml(py_lines)
    for row in struct: display(row)

    mds = yaml_to_md(name_of_md_file = name, struct = struct)
    for idx, (name, md) in enumerate(mds.items()):
        _path = pathlib.Path(f'../../docs/pages/demo1/')
        _path.mkdir(parents = True, exist_ok = True)
        _path /= f'{name}.md'
        # print(f'{idx}:{"="*20}')
        # print(f'{idx}:{name} // {_path}')
        # print(md)
        with open(_path, mode = 'w') as out_stream:
            out_stream.write(md)


if __name__ == '__main__': main()
