import zhconv
import jieba
import config

def Trans_and_Split(input_file_name,output_file_name):

    lines = open(input_file_name,'r',encoding='utf-8').readlines()
    output_file = open(output_file_name,'w',encoding='utf-8')
    for line in lines:
        #繁体转简体
        line = zhconv.convert(line,'zh-hans')
        #分词
        output_file.write(' '.join(jieba.cut(line.split('\n')[0].replace(' ', ''))) + '\n')

if __name__ == '__main__':
    #用wikich测试
    input_file_name = config.data_source_path + '/Init/' + 'zhwiki-latest-pages-articles.txt'
    output_file_name = config.data_source_path + '/Init/' + 'zhwiki-simple-ch.txt'
    Trans_and_Split(input_file_name=input_file_name,output_file_name=output_file_name)