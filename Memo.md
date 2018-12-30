- https://www.haya-programming.com/entry/2018/02/25/044525

## csr_matrix
- http://hamukazu.com/2014/12/03/internal-data-structure-scipy-sparse/
- 疎行列(sparse matrix) => 成分の殆どが0の行列
- sparse[スパース] => まばらな、わずかな、薄い


## 疎行列とは
- http://hamukazu.com/2014/09/26/scipy-sparse-basics/
```
要素の殆どが0であるような行列を疎行列と呼ぶ。そうでない普通の行列を区別したい時は密行列
と呼ぶ。疎行列では、非ゼロ要素だけおぼえておけばよいので、メモリ、計算時間ともに大幅な
節約になる。とくに非ゼロようその割合が小さい場合はその節約は大きくなる。

## 使い方
`scipy.sparse`には、疎行列を表すクラスがいくつかあるが、一般の行列について演算したいのなら、
lil_matrix, csc_matrix, csr_matrixだけを覚えれば良い

典型的な使い方としては
1. lil_matrixを用意する
2. 値をセットする
3. csr_matrix(またはcsc_matrix)に変換する(どちらを使うべきかの判断は後述)
4. 演算をする
という流れになる。

つまりまとめると、
* 値をセットする時はlil_matrixを使う
* 計算する時はcsr_matrixまたはcsc_matrixつかう

lil_matrixでも演算はできるが、計算効率を考えるとそれは避けたほうが良い
```

