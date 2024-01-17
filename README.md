# S28ERAV1 - Capstone Project: Part 1
## Train LLM from scratch. ##

* You need to select a model that is less than 3B parameters (can be Microsoft's Phi 2 as well, but with random weights, hence training logs are MUST for capstone)
* Data:
  * It would be close to impossible to collect ALL the datasets required to train your model. Hence:
  * You are going to use Microsoft's Phi-2 or any other model and generate data. Recommend you generate this data in parallel, don't generate and store everything as that would be a very very large dataset
  * You are going to collect "some" clean data (100MB when zipped). This data CAN be generated from Phi-2 and stored.
* Training
  * You are going to use the same tokenizer and other data structures to keep your life simple
  * You are going to use AWS (or an equvalent system) where you are going to train YOUR model. 
  * You are going to train YOUR model (let's say that starts at 10). Train it somehow to reach the "initial loss - 1" value. Compare it with the final Microsoft's Phi 2's value and see how much more you have to train!!!

