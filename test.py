from gensim.models import KeyedVectors
wv = KeyedVectors.load_word2vec_format("model.txt", binary=False)
print(wv.most_similar("ひろゆき", topn=30))

