import csv

input_file = open("corpus.txt", "r")
output_file = open("model.csv", "w")

n = 8

ngram_table = {}

corpus_text = input_file.read()

for i in range(0, len(corpus_text) - n):

    ngram = corpus_text[i:i+n]
    if ngram in ngram_table:
        ngram_table[ngram] += 1
    else:
        ngram_table[ngram] = 1

ngram_list = sorted(ngram_table.items(), key=lambda x: x[1], reverse=True)
writer = csv.writer(output_file, delimiter='\t')
writer.writerows(ngram_list)
