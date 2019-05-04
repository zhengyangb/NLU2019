import numpy as np

import torch


def embedded_dropout(embed, words, dropout=0.1, scale=None, fixemb=None):
  if dropout:
    mask = embed.weight.data.new().resize_((embed.weight.size(0), 1)).bernoulli_(1 - dropout).expand_as(embed.weight) / (1 - dropout)
    masked_embed_weight = mask * embed.weight
  else:
    masked_embed_weight = embed.weight
  if scale:
    masked_embed_weight = scale.expand_as(masked_embed_weight) * masked_embed_weight

  padding_idx = embed.padding_idx
  if padding_idx is None:
      padding_idx = -1

  X = torch.nn.functional.embedding(words, masked_embed_weight,
    padding_idx, embed.max_norm, embed.norm_type,
    embed.scale_grad_by_freq, embed.sparse
  )
  if fixemb:
    m = np.zeros(shape=(1, 1, 400))
    m = torch.FloatTensor(m)
    m[:, :, 300:] = 1
    m[:,:, [0,2]] = 1
    if X.is_cuda:
      m = m.cuda()
    X = m * X + (1 - m) * X.clone().detach()
  return X

def embedded_dropout_gpt(embed, dropout=0.1, scale=None):
  if dropout:
    # embed: SL * BS * GPT_ES
    mask = embed.weight.data.new().resize_((embed.weight.size(0), 1)).bernoulli_(1 - dropout).expand_as(
      embed.weight) / (1 - dropout)
    embed.weight = torch.nn.Parameter(mask * embed.weight)
  if scale:
    embed.weight = torch.nn.Parameter(scale.expand_as(embed.weight) * embed.weight)
  return embed


if __name__ == '__main__':
  V = 50
  h = 4
  bptt = 10
  batch_size = 2


  embed = torch.nn.Embedding(V, h)

  words = np.random.random_integers(low=0, high=V-1, size=(batch_size, bptt))
  words = torch.LongTensor(words)

  origX = embed(words)
  X = embedded_dropout(embed, words)

  print(origX)
  print(X)
