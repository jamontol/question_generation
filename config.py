# experiment ID
exp = "qg-1"

environment = 'local'
# data directories
#newsqa_data_dir = "/Users/gdamien/Data/newsqa/newsqa-data-v1"
if (environment=='local'):

    squad_data_dir = "C:/Users/jrml/Documents/Chatbot/Bankia.es/datos/json/squad_es"
    mlqa_data_dir = "C:/Users/jrml/Documents/Chatbot/Bankia.es/datos/json/mlqa_es"
    out_dir = "C:/Users/jrml/Documents/Chatbot/Bankia.es/datos/qg/"
    # model paths
    spacy_es ="C:/Users/jrml/Documents/Chatbot/Bankia.es/datos/spacy/es_core_news_md/en_core_news_md-2.3.0"
    glove = "C:/Users/jrml/Documents/Chatbot/Bankia.es/datos/glove/"
    squad_models = "C:/Users/jrml/Documents/Chatbot/Bankia.es/datos/models/"

elif (environment=='colab'):

    squad_data_dir = "/content/drive/My Drive/Colab Notebooks/QG/data/json/squad_es"
    mlqa_data_dir = "/content/drive/My Drive/Colab Notebooks/QG/data/json/mlqa_es" 
    out_dir = "/content/drive/My Drive/Colab Notebooks/QG/data/qg/" 
    # model paths
    spacy_es = "/content/drive/My Drive/Colab Notebooks/QG/data/spacy/es_core_news_md/en_core_news_md-2.3.0"  
    glove = "/content/drive/My Drive/Colab Notebooks/QG/data/glove/" 
    squad_models = "/content/drive/My Drive/Colab Notebooks/QG/models/"

train_dir = squad_data_dir + "train/"
dev_dir = squad_data_dir + "dev/"

# model paths
# spacy_es = "/content/drive/My Drive/Colab Notebooks/QG/data/spacy/es_core_news_md/en_core_news_md-2.3.0"  #"C:/Users/jrml/Documents/Chatbot/Bankia.es/datos/spacy/es_core_news_md/en_core_news_md-2.3.0"
# glove = "/content/drive/My Drive/Colab Notebooks/QG/data/glove/" #"C:/Users/jrml/Documents/Chatbot/Bankia.es/datos/glove/"
# squad_models = "/content/drive/My Drive/Colab Notebooks/QG/data/models/" # "C:/Users/jrml/Documents/Chatbot/Bankia.es/json/models/"

# preprocessing values
paragraph = False
min_len_context = 5
max_len_context = 100 if not paragraph else 1000
min_len_question = 5
max_len_question = 20
word_embedding_size = 300
answer_embedding_size = 2
in_vocab_size = 45000
out_vocab_size = 28000

# training hyper-parameters
num_epochs = 15
batch_size = 32
learning_rate = 1.0
hidden_size = 600
n_layers = 2
drop_prob = 0.3
start_decay_epoch = 8
decay_rate = 0.5
use_answer = True
cuda = True
pretrained = False

# eval hyper-parameters
eval_batch_size = 1
min_len_sentence = 5
top_k = 0.
top_p = 0.9
temperature = 0.7
decode_type = "topk"
