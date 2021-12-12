import json

def open_file(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)


def get_data(data):
    """Получаем список слов, в начале которых стоит #"""
    result = set()
    for record in data:
        content = record['content']
        words = content.split()
        for word in words:
            if word.startswith('#'):
                result.add(word[1:])
    return result


def kakaya_to_funksia(data, tag):
    """Получаем список из словарей, в контенте которых есть хештег {tag}"""
    results = []
    for record in data:
        if f'#{tag}' in record['content']:
            results.append(record)
    return results

def add_post(filename, post):
    data = open_file(filename)
    data.append(post)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)
