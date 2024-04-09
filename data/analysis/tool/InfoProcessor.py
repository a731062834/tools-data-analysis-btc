#encoding:utf8
import jieba
import re

class InfoProcessor:
    regex_alpha = "[a-zA-Z]+"
    regex_num = "[0-9]+"

    def __init__(self):
        self.tokenizer = jieba.Tokenizer()

    def process_text(self, input_text):
        tokenized_words = self.tokenizer.tokenize(input_text)

        processed_words = []
        for word in tokenized_words:
            if len(word) < 2:
                continue
            if re.match(self.regex_num, word):
                continue
            if re.match(self.regex_alpha, word):
                continue
            processed_words.append(word)
        return processed_words

    def split_text(self, input_text):
        return re.split("。|！|？", input_text)
