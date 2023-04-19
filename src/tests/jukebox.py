from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("openai/jukebox-1b-lyrics")

model = AutoModel.from_pretrained("openai/jukebox-1b-lyrics")