from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Example sentence
text = "Hello, my dog is cute"

# Encode text
inputs = tokenizer(text, return_tensors="pt")

# Load pre-trained model (weights)
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

# Forward pass, calculate logit predictions
with torch.no_grad():
    outputs = model(**inputs)

# Since we have a binary classification, we use a sigmoid to get probabilities
probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

# Print sentence and predicted probabilities
print("Text:", text)
print("Probability distribution:", probs)
