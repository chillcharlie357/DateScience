import jieba
import gensim
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import string
import zhon.hanzi
import re
import config

def train_model(train_txt_name,model_file_name):
    #训练模型
    model = Word2Vec(LineSentence(train_txt_name),
                     vector_size=200,
                     window=5,
                     min_count=5)
    #保存模型
    model.save(model_file_name)

#追加训练
def train_add(input_file_name):
    input_file = open(input_file_name,'r',encoding="utf-8")
    lines = input_file.readlines()
    #给新文件分词
    new_sentences = []
    for line in lines:
        #去除标点符号
        line = re.sub('[{}]'.format(string.punctuation),' ',line)
        line = re.sub('[{}]'.format(zhon.hanzi.punctuation),' ',line)
        line = re.sub('[\n]',' ',line)
        sentences = line.split(" ")
        for sentence in sentences:
            #分词
            # new_sentences.append(' '.join(jieba.cut(sentence)))
            new_sentences.extend(jieba.cut(sentence))
            # print(sentence)
    # #保存分词结果
    # with open(input_file_name.replace(".txt","-split.txt"),'w',encoding="utf-8") as f:
    #     for i in range(len(new_sentences)):
    #         f.write("".join(new_sentences[i]))
    #追加训练模型
    old_model =  gensim.models.Word2Vec.load('../Model/zhwiki.model')
    old_model.build_vocab(new_sentences,update=True)
    old_model.train(new_sentences,total_examples=old_model.corpus_count,epochs=10)

    input_file.close()
    #返回分词结果
    return new_sentences


if __name__ == '__main__':
    # 加载经过分词的训练数据,初次训练
    train_txt_name = config.data_source_path + '/Init/' + 'zhwiki-simple-ch.txt'
    model_file_name = '../Model/' + 'zhwiki.model'
    train_model(train_txt_name=train_txt_name,model_file_name=model_file_name)
