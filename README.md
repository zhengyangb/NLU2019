# NLU2019 Code  

The model we propose in the paper uses ON-LSTM and OpenAI GPT models. Instead of replicate from scratch, we use the code from the  following repositories. 

- [OpenAI GPT](https://github.com/huggingface/pytorch-pretrained-BERT)
- [ON-LSTM](https://github.com/yikangshen/Ordered-Neurons)



<!--
run with `--cuda --mode GPT --learning_rate 1e-6 --lr 10 --batch_size 20 --dropoute 0.0 --dropout 0.45 --dropouth 0.3 --dropouti 0.0 --wdrop 0.45 --chunk_size 10 --seed 141 --epoch 1000`  
- Distinguish GPT optimizer 
- Return GPT LM result
- Weighted loss
- Hyper-parameter
  - Turn off embedding drop out
  - decrease learning rate  

April 8  
tools/id2gptid  
util.get_batch_gpt  
GPT_model  
main_gpt  
  
TODO:  
Resume setting
Check accuracy   
Inprove efficiency  
Experiments design  
-->

