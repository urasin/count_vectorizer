from sklearn.feature_extraction.text import CountVectorizer
file_path = "./data/wiki_python.txt"

with open(file_path, 'r') as f:
  text_list = [line.rstrip() for line in f]  # remove empty line

# https://qiita.com/makopo/items/35c103e2df2e282f839a
# https://qiita.com/asatohan/items/7a247eb533a5adba9e87
# http://nonbiri-tereka.hatenablog.com/entry/2015/06/04/070933
cv = CountVectorizer()
# return <class 'scipy.sparse.csr.csr_matrix'>
matrix = cv.fit_transform(text_list)

# Can get matrx shape
# Can get dimensons number (ndim) => 2 
# `dimV =n` n次元
# About dimension in math: https://oguemon.com/study/linear-algebra/basis-dimension/#toc4
# About dimensions https://deepage.net/features/numpy-axis.html
# size => 全要素数(8 * 98 = 784)
# Apis: https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html
# print(matrix.toarray().size)

# 2/8 = 0.25 6/8 = 0.75 
cv = CountVectorizer(min_df=0.24, max_df=0.76, stop_words='english')
matrix = cv.fit_transform(text_list)
# decrese 14 dimentions(14 word)
# print(matrix.shape)
# cvが破壊的に変更されてる？ 気持ち悪い感がする。
print(matrix.toarray())
print(cv.get_feature_names())

# 1/8(sentence) = 0.125
cv = CountVectorizer(min_df=0.12, max_df=0.76, stop_words='english')
matrix = cv.fit_transform(text_list)
# print(cv.get_feature_names())

# ngramの特徴量にする
# ngram_rangeというパラメーターがあります。これはtupleで渡す必要があり、(1,1),(1,2)とかで
# 指定します。





