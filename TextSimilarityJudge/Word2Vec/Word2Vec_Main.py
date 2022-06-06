import gensim
import TrainingModel
import Trans_and_Split
import config

'''
输入两个txt文件，比较扩展前与扩展后的文本相似度
判断文本扩增的有效性
@param:original_text
@param:extended_text
@return:返回相似度,用txt存储
'''
def word2vec_main(original_text_name, extended_text_name):
    model = gensim.models.Word2Vec.load('zhwiki.model')
    original_lines = TrainingModel.train_add(original_text_name)
    extended_lines = TrainingModel.train_add(extended_text_name)


    #字典存储结果
    result = {}
    similarity = []
    count = 0
    for i in range(len(original_lines)):
        try:
            similarity.append(model.wv.similarity(original_lines[i],extended_lines[i]))
            count += 1
        except Exception as e:
            print("error: %s" % e)
    result = zip(original_lines,extended_lines,similarity)

    #输出结果
    f = open('result.txt', 'a', encoding='utf-8')
    f.write("原始数据  扩展数据  相似度\n")
    ave = 0.0
    for element in result:
        ave += element[2]
        for i in range(len(element)):
            value_str = str(element[i])
            f.write(value_str + '  ')
        f.write("\n")
    ave /= count
    f.write("平均相似度：%d" % ave)
    f.close()


if __name__ == '__main__':
    for  i in range(len(config.original_date_files)):
        original_text_name = config.data_source_path + '/' + config.original_date_files[i]
        extended_text_name = config.data_source_path + '/' + config.extended_data_files[i]
        # word2vec_main(original_text_name=original_text_name, extended_text_name=extended_text_name)
        try:
            word2vec_main(original_text_name=original_text_name,extended_text_name=extended_text_name)
        except Exception as e:
            print('error:%s' % e)

