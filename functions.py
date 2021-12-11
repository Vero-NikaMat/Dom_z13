import json

def open_file(file):
    with open(file, encoding='utf-8') as f:
        return json.load(f)


def get_data(data):
    result = set()

    for record in data:
        content = record['content']
        words = content.split()
        for word in words:
            if word.startswith('#'):
                result.add(word[1:])
    return result

def kakaya_to_funksia(data, tag):
    results = []
    for record in data:
        if f'#{tag}' in record['content']:
            results.append(record)
    return results