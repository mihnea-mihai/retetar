import re

def parse_ing_line (ing):
    m = re.match(r"""
        ((?P<qty>[\d\.\,\/]*)\s
        (de\s)?
        ((?P<unit>\w*)\s)?)?
        (de\s)?
        (?P<name>.*)
        """, ing, flags=re.VERBOSE | re.DOTALL
    )
    return {
        field: m[field] for field in ['name', 'qty', 'unit']
    }

with open('.import_scripts/in.md') as r:
    with open('.import_scripts/out.md', 'w') as w:
        w.write(
            '\n- '.join(str(parse_ing_line(line.strip())).replace("'", '')
            for line in r)
        )
