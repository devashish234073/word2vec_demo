from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import random

# Load the trained model
model = Word2Vec.load("word2vec.model")
sentence = input("Enter a sentence: ")
word_array = sentence.split()
print("Array of words:", word_array)

def get_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

x_coords = []
y_coords = []
point_colors = []
word_color_map = {}

for word in word_array:
    if word in model.wv:
        # Example: Find similar words
        similar_words = model.wv.most_similar(word, topn=5)
        print("\nWords similar to '{}':".format(word))
        for similar_word, similarity in similar_words:
            print(f"{similar_word}: {similarity:.4f}")
        print(f"Vector for '{word}':\n{model.wv[word]}")
        if(model.wv[word].shape == (2,)):
            x_coords.append(model.wv[word][0])
            y_coords.append(model.wv[word][1])
            if word not in word_color_map:
              word_color_map[word] = get_random_color()
            point_colors.append(word_color_map[word])
            #plt.plot(model.wv[word][0], model.wv[word][1], 'ro')
            #plt.show()
    else:
        print(f"Word '{word}' not in vocabulary")

if len(x_coords) > 0:
    plt.scatter(x_coords, y_coords, c=point_colors, s=100)
    for word, color in word_color_map.items():
        plt.scatter([], [], color=color, label=word)
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.title("Random Colored Points with Words")
    plt.legend(title="Word Legend")
    plt.grid(True)
    plt.show()