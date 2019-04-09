from pytorch_pretrained_bert import OpenAIGPTModel
import pickle
from pytorch_pretrained_bert import OpenAIGPTTokenizer
import torch

#read corpus data first

tokenizer = OpenAIGPTTokenizer.from_pretrained('openai-gpt')

dic = {}


def convert(corpus):
    for index, text in enumerate(corpus.dictionary.idx2word):
        tokenized_text = tokenizer.tokenize(text)
        # indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
        dic[index] = tokenized_text  # [indexed_tokens[0],indexed_tokens[-1]]

    with open('GPT_index.pkl', 'wb') as handle:
        pickle.dump(dic, handle, protocol=pickle.HIGHEST_PROTOCOL)
fn = '/home/yh1844/Documents/NLU/NLU2019/ON/corpus.e15022e5794bc6f5de6639fcbac6670b.data'
corpus = torch.load(fn)
convert(corpus)