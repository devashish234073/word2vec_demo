from gensim.models import Word2Vec
import matplotlib.pyplot as plt
# Load the trained model
model = Word2Vec.load("word2vec.model")
# Example: Get vector for a word
for word in ["my","your","the","class","not"]:
    if word in model.wv:
        # Example: Find similar words
        similar_words = model.wv.most_similar(word, topn=5)
        print("\nWords similar to '{}':".format(word))
        for similar_word, similarity in similar_words:
            print(f"{similar_word}: {similarity:.4f}")
        print(f"Vector for '{word}':\n{model.wv[word]}")
        if(model.wv[word].shape == (2,)):
            plt.plot(model.wv[word][0], model.wv[word][1], 'ro')
            plt.show()
    else:
        print(f"Word '{word}' not in vocabulary")