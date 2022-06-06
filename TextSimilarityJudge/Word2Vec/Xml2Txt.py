
from gensim.corpora import WikiCorpus

def Xml2Txt_main():
    input_file_name = 'zhwiki-latest-pages-articles.xml.bz2'
    output_file_name = 'zhwiki-latest-pages-articles.txt'
    #读入数据，解析
    input_file = WikiCorpus(input_file_name,dictionary={})
    output_file = open(output_file_name,'w',encoding='utf-8')

    for text in input_file.get_texts():
        output_file.write(' '.join(text)+'\n')

    output_file.close()

if __name__ == '__main__':
    Xml2Txt_main()