arr = list(
    map(
        lambda x: list(
            map(
                lambda y: int(y), x.split(','))
        ), 
        s.replace('},', '|').replace('{', '').replace('}', '').split('|')
    )
)