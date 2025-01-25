from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import pandas as pd

df1 = pd.read_csv('llama_hd_eval.tsv', sep='\t')
df2 = pd.read_csv('llama_hd_train.tsv', sep='\t')

third_column = df1.iloc[:, 2].to_list()
third_column.extend(df2.iloc[:, 2].to_list())
# Example data
sentences = third_column

# Preprocess: Tokenize sentences
tokenized_sentences = [sentence.lower().split() for sentence in sentences]
print("tokenized_sentences={}".format(tokenized_sentences))

# Train Word2Vec model
# Parameters:
# - vector_size: Dimensionality of the word vectors (100 as per realistic implementation).
# - window: Context window size (5 words to the left and right).
# - min_count: Ignores words with total frequency less than this.
# - sg: Skip-gram (1) vs CBOW (0); skip-gram often works better for smaller datasets.
model = Word2Vec(sentences=tokenized_sentences, vector_size=2, window=5, min_count=1, sg=1)

# Save the trained model
model.save("word2vec.model")
