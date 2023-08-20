import os
from transformers import GPT2Tokenizer, GPT2Model
import torch
import faiss 
import numpy as np

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')
model_outputs = []
index_filename = 'faiss_index.index'

def store_db(content):
		try:
			encoded_input = tokenizer(content, return_tensors="pt", truncation=True, max_length=tokenizer.model_max_length)
			with torch.no_grad():
				output = model(**encoded_input)
				model_outputs.append(output)
			
			#Flatten the model outputs into embeddings
			flattened_embeddings = np.concatenate([output.last_hidden_state.view(output.last_hidden_state.size(0), -1).numpy() for output in model_outputs])

			# Initialize Faiss index
			index_dimension = flattened_embeddings.shape[1]

			index = faiss.IndexFlatL2(index_dimension)

			# Insert embeddings into the index
			index.add(flattened_embeddings)
			faiss.write_index(index, "faiss_index.index")
		except Exception as e:
			print("Exception occured", e)
			return False
		return True