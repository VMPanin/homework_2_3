import chardet
import json


def load_json():
    file_name = input('Введи название файла (newsafr.json, newscy.json, '
                      'newsfr.json, newsit.json):')
    with open(file_name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        result_encoding = result['encoding']
        decoded_data = data.decode(result_encoding)
        data = json.loads(decoded_data)
    return data['rss']['channel']['items']


def get_list_all_words():
    items = load_json()
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
        word = ''
        for k, v in dict_words.items():
            max_word = max(dict_words.values())
            if v == max_word:
                max_word_dict[k] = v
                word = k
        del dict_words[word]
    return max_word_dict


def main():
    result_top10 = get_top10_words()
    print('Топ-10 слов по упоминаемости с указанием числа упоминаний: ',
          result_top10)

main()

