## Note:
figures and illustration source by:
> McCormick, C. (2016, April 19).  _Word2Vec Tutorial - The Skip-Gram Model_. Retrieved from  [http://www.mccormickml.com](http://www.mccormickml.com/)
# **Word Vectors**

Word Vectors are often used as a fundamental component for downstream NLP tasks, e.g. question answering, text generation, translation, etc., so it is important to build some intuitions as to their strengths and weaknesses. Here, you will explore two types of word vectors: those derived from *co-occurrence matrices*, and those derived via *GloVe*. 

# **1- Skip Gram**

The continuous skip-gram model learns by predicting the surrounding words given a current word. In other words, the Continuous Skip-Gram Model predicts words within a certain range before and after the current word in the same sentence.

## **1.1 Model architecture**
![image](https://user-images.githubusercontent.com/61620007/179069325-9c6a6c81-1d5a-4285-ab53-71ce88e7f4f6.png)

## **1.2- Training of Skip-Gram**

### The Fake Task
We’re going to train the neural network to do the following. Given a specific word in the middle of a sentence (the input word), look at the words nearby and pick one at random. The network is going to tell us the probability for every word in our vocabulary of being the “nearby word” that we chose.
<br>
<br>
We’ll train the neural network to do this by feeding it word pairs found in our training documents. 
> The below example shows some of the training samples (word pairs) we would take from the sentence “The quick brown fox jumps over the lazy dog.” I’ve used a small window size of 2 just for the example. The word highlighted in blue is the input word.

![image](https://user-images.githubusercontent.com/61620007/179070545-5fe788a1-1d01-4e3e-a3aa-2b9cecdc43a6.png)

## **1.3- Architecture Details**

We’re going to represent an input word like “ants” as a one-hot vector. This vector will have 10,000 components (one for every word in our vocabulary) and we’ll place a “1” in the position corresponding to the word “ants”, and 0s in all of the other positions.
<br>
<br>
The output of the network is a single vector (also with 10,000 components) containing, for every word in our vocabulary, the probability that a randomly selected nearby word is that vocabulary word.
![image](https://user-images.githubusercontent.com/61620007/179070841-7261bb3b-855f-45d4-9bb1-e9f14be24042.png)
There is no activation function on the hidden layer neurons, but the output neurons use softmax. We’ll come back to this later.

## **1.4- The Hidden Layer**

we’re going to say that we’re learning word vectors with 300 features. So the hidden layer is going to be represented by a weight matrix with 10,000 rows (one for every word in our vocabulary) and 300 columns (one for every hidden neuron).
![image](https://user-images.githubusercontent.com/61620007/179070926-8b07af87-770b-456a-8e26-aaa736be4bed.png)

The hidden layer of this model is really just operating as a lookup table. The output of the hidden layer is just the “word vector” for the input word.

![image](https://user-images.githubusercontent.com/61620007/179070954-22271bb1-3691-4892-bfdb-e749baa00fe0.png)

## **1.5- The output layer**

Specifically, each output neuron has a weight vector which it multiplies against the word vector from the hidden layer, then it applies the function exp(x) to the result. Finally, in order to get the outputs to sum up to 1, we divide this result by the sum of the results from all 10,000 output nodes.

![image](https://user-images.githubusercontent.com/61620007/179070994-af77c5bb-ae29-4b81-9cee-e75bddb5a1ae.png)

## **1.6- Math of the Skip-Gram**

### **Feed Forward**
![image](https://user-images.githubusercontent.com/61620007/179069768-22977015-f853-465f-a8c2-ab14d52a141a.png)

### **Loss Function**

![image](https://user-images.githubusercontent.com/61620007/179069831-7f37bfc3-c01b-4186-add5-3fdfe7523443.png)

### **Back Propagation**

![image](https://user-images.githubusercontent.com/61620007/179069965-dc0a8f42-53fc-48a1-90b9-7987a6e41a45.png)

## **1.7: Skip-Gram abstract look**
![image](https://user-images.githubusercontent.com/61620007/179070128-2ad5c794-e070-40f8-a0ff-bc45bf395e34.png)

