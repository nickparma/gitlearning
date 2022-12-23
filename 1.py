punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(str_x):
    for punChars in punctuation_chars:
        str_x = str_x.replace(punChars, "")
    return str_x

def get_neg(neg_word):
    new_neg_word = strip_punctuation(neg_word)
    split_neg_word = new_neg_word.lower().split()
    
    count = 0
    for word in split_neg_word:
        for wrd in negative_words:
            if word == wrd:
                count += 1
    return count

def get_pos(pos_word):
    new_pos_word = strip_punctuation(pos_word)
    lst_pos_word = new_pos_word.lower().split()
    
    count = 0
    for word in lst_pos_word:
        for wrd in positive_words:
            if word == wrd:
                count += 1
    return count

project = open('project_twitter_data.csv', 'r')
resultdata = open('resulting_data.csv', 'w')
resultdata.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
projectrd = project.readlines()[1:]
for p in projectrd:
    positive_score = get_pos(p)
    negative_score = get_neg(p)
    net_score = positive_score - negative_score
    split_p = p.split(',')
    retweets = int(split_p[1])
    replies = int(split_p[2])
    formatting = f"{retweets},{replies},{positive_score},{negative_score},{net_score}"
    resultdata.write(formatting + '\n')

resultdata.close()
project.close()

































