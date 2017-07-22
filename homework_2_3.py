import chardet
import json


file_name = input('Введи название файла (newsafr.json, newscy.json, newsfr.json, newsit.json):')
def decode_file():
    with open(file_name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        result = (result['encoding'])
    return result

def load_json():
    result_encoding = str(decode_file())
    with open(file_name, encoding = result_encoding) as f:
        data = json.load(f)
    return data['rss']['channel']['items']

def get_list_all_words():
    items = (load_json())
    all_words = []
    for item in items:
        words = item['title'].split(' ') + item['description'].split(' ')
        all_words += words
    return all_words

def get_dict_count_words():
    all_words = get_list_all_words()
    dict_words = {}
    for word in all_words:
        if len(word) > 6:
            dict_words[word] = all_words.count(word)
    return dict_words

def get_top10_words():
    max_word_dict = {}
    dict_words = get_dict_count_words()
    num = 10
    while num >= 1:
        num = num - 1
        for k, v in dict_words.items():
            max_word = max(dict_words.values())
            if v == max_word:
                max_word_dict[k] = v
                word = k
        del dict_words[word]
    return max_word_dict

def main():
    result_top10 = get_top10_words()
    print('Топ-10 слов по упоминаемости в новостях с указанием числа упоминаний: ', result_top10)

main()
