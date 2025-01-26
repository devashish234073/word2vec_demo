# word2vec_demo

Train and create a model using the datasets available in https://github.com/facebookresearch/llama-hd-dataset/tree/main/data

Download the two .tsv files from above location or just run word2vec_download.py to do the same.

Run "word2vec_train.py" to train the model.

![image](https://github.com/user-attachments/assets/f405864a-90d4-4371-8417-1c3c4c827af8)

Once trained run word2vec_run.py it will find similar words. 

![image](https://github.com/user-attachments/assets/7c491cea-16c0-4456-a4b3-a90538dc0649)

The dimension of the vector is set in word2vec_train.py you can tweak that and train again to change it.
In the above screenshot you can see teh dimention of the vector is 2 and for dimention of 2 I have added logic to also plot the word in graph.
