# http://hamukazu.com/2014/09/26/scipy-sparse-basics/
from scipy.sparse import lil_matrix, csr_matrix

# 疎行列aを用意する(3x3のすべて0の行列)
# return <class 'scipy.sparse.lil.lil_matrix'>
# a = lil_matrix([3, 3])
a = lil_matrix((3, 3)) # 引数がlistだと値をセットしたときエラーが出る、tupleを渡す

# 非ゼロ要素を設定する
a[0, 0]=1;a[0, 2]=2

# lil_matrixをcsr_matrixに変換する
# return <class 'scipy.sparse.csr.csr_matrix'>
a = a.tocsr()

# 疎行列bを用意する
b = lil_matrix((3, 3))

# 非ゼロようそを追加する
b[1, 1] = 3; b[2, 0] = 4; b[2, 2] = 5

# lil_matrixをcsr_matrixに変換する
b = b.tocsr()

# aとbの積を計算する
# なぜdotか？https://qiita.com/masafumi_miya/items/640800cef813acf70caf
c = a.dot(b)

# # aとbの和を計算する
d = a + b

print(d.toarray())
# toarrayでvisualize できる, cast できる
# return <class 'numpy.ndarray'>
# print(c.toarray())
