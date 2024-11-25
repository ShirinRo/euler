import numpy as np

words_list = open('p098_words.txt', 'r')
lines = words_list.readlines()
input_words = [x.strip('"') for x in lines[0].split(',')]

should_reverse = True


def is_anagram(w1: str, w2: str):
    return sorted(list(w1)) == sorted(list(w2))


def get_anagrams(words):
    all_anagrams_dict = {}
    for i in range(len(words)):
        w1 = words[i]
        cur = [w1]
        for j in range(i + 1, len(words)):
            w2 = words[j]
            if is_anagram(w1, w2):
                cur += [w2]
        if len(cur) > 1:
            cur_len = len(w1)
            if cur_len in all_anagrams_dict:
                all_anagrams_dict[cur_len] += [cur]
            else:
                all_anagrams_dict[cur_len] = [cur]
    all_anagrams_sorted = []
    all_keys = list(all_anagrams_dict.keys())
    all_keys.sort(reverse=should_reverse)
    for key in all_keys:
        all_anagrams_sorted += all_anagrams_dict[key]
    return all_anagrams_sorted


def get_squares_dics(anagrams):
    longest_word_len = 0
    for anagram_arr in anagrams:
        for word in anagram_arr:
            if len(word) > longest_word_len:
                longest_word_len = len(word)

    largest_number = int('9' * longest_word_len)
    squares = {}
    cur_square = 1
    while cur_square ** 2 < largest_number:
        key = len(str(cur_square ** 2))
        if key in squares:
            squares[key] += [cur_square ** 2]
        else:
            squares[key] = [cur_square ** 2]
        cur_square += 1
    return squares


def find_permutation(word1, word2):
    first_list = list(word1)
    letters_set = set(first_list)
    second_list = list(word2)
    res_dict = {}
    for letter in letters_set:
        indices = [i for i in range(len(second_list)) if second_list[i] == letter]
        res_dict[letter] = [10 ** (len(first_list) - 1 - i) for i in indices]
    res = []
    for letter in first_list:
        possible_result = res_dict[letter]
        if len(possible_result) == 1:
            res += res_dict[letter]
        else:
            val = min(possible_result)
            res += [val]
            possible_result.remove(val)
            res_dict[letter] = possible_result
    return res


def dot_prod(v1, v2):
    return sum([int(v1[i]) * int(v2[i]) for i in range(len(v1))])


def is_num_word_match_legal(str1, str2):
    def inner(s1, s2):
        dic = {}
        for i, l in enumerate(s1):
            if l not in dic:
                dic[l] = s2[i]
            else:
                if dic[l] != s2[i]:
                    return False
        return True
    return inner(str1, str2) and inner(str2, str1)


anagrams = get_anagrams(input_words)
squares_dict = get_squares_dics(anagrams)



max_num = 0
curr_len = 0
for anagram_group in anagrams:
    first_word = anagram_group[0]
    group_len = len(first_word)
    curr_len = group_len
    possible_squares = squares_dict[group_len]
    for i in range(1, len(anagram_group)):
        second_word = anagram_group[i]
        permutation = find_permutation(first_word, second_word)
        for number in possible_squares:
            if not is_num_word_match_legal(str(number), first_word):
                continue
            perm_num = dot_prod(list(str(number)), permutation)
            if perm_num in possible_squares:
                if number > max_num or perm_num > max_num:
                    max_num = max([max_num, number, perm_num])
print(max_num)