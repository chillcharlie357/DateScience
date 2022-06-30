from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import zhon.hanzi #汉语标点符号集合

import config
import string
import re
import numpy
import scipy.stats as stats

def split_file(file_name,file_path,encoding):
    '''

    :param file_name:
    :param file_path:
    :return:a list contain split sentences
    '''
    with open(file_path+file_name,mode='r',encoding=encoding) as f:
        lines_list = f.readlines()
        lines = []
        for ele in lines_list:
            temp = ele.split('。')
            #删除标点符号
            for i in range(len(temp)):
                temp[i] = re.sub('[{}]'.format(string.punctuation),'',temp[i])
                temp[i] = re.sub('[{}]'.format(zhon.hanzi.punctuation),'',temp[i])
                temp[i] = re.sub('[\n]','',temp[i])

            if temp.count('') != 0:
                temp.remove('')

            lines.extend(temp)

        return lines



def get_weights(elements):
    lengths = []
    for ele in elements:
        lengths.append(len(ele))
    return lengths

def significance_test(original,extended):
    '''

    :param original: original embeddings
    :param extended: extended embeddings
    :return: boolean significant or not
    '''
    original_average = numpy.average(original)
    extended_average = numpy.average(extended)
    original_var = numpy.var(original)
    extended_var = numpy.var(extended)
    n1 = len(original)
    n2 = len(extended)
    T = (original_average - extended_average) / numpy.sqrt(original_var / n1 + extended_var / n2)
    if T > 1.96 or T < -1.96:
        return True
    return False




def get_split_sentences_list(source_file_list,source_file_path,encoding):
    result = []
    for file_name in source_file_list:
        temp = split_file(file_name=file_name,file_path=source_file_path,encoding=encoding)
        result.extend(temp)
    return result

def Tex2Vec_main():
    # Load source files
    source_files = []
    extended_files = []
    for i in range(config.file_count):
        source_files.append('{}.txt'.format(i))
        extended_files.append('{}back.txt'.format(i))
    # Load pretrained model from web
    model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    for i in range(len(source_files)):
        # split file into sentences and remove
        sentences_original = split_file(source_files[i],config.Original_path,'utf-8')
        sentences_extended = split_file(extended_files[i],config.Extended_path,'gbk')

        # embedding
        embeddings_original = model.encode(sentences_original)
        embeddings_extended = model.encode(sentences_extended)
        # significant test
        is_different = significance_test(embeddings_original,embeddings_extended)
        # Compute cosine similarity
        # Matrix with res[i][j]  = cos_sim(a[i], b[j])
        similarity_matrix =  cos_sim(embeddings_original,embeddings_extended)

        # print(similarity_matrix)

        with open(config.Reslut_path+'{}out.txt'.format(i),mode='w',encoding='utf-8') as f:
            f.write('\n{}.txt and {}back.txt is different: {}\n'.format(i, i, is_different))
            f.write(' Matrix with similarity[i][j]  = cos_sim(original[i], extended[j])\n\n')

            temp = similarity_matrix.numpy()
            for i in range(len(temp[0])):
                f.write('{: >10d}'.format(i))
            for i in range(len(temp)):
                f.write('{: >10}: '.format(i))
                for j in range(len(temp[0])):
                    f.write(str(temp[i][j]))
                    f.write(' |')
                f.write('\n')



if __name__ == '__main__':
    Tex2Vec_main();
    # split_file(config.Extended_file[0],config.Extended_path)