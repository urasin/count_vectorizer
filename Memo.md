
# sklearnのCountVectorizerの使い方
- https://www.haya-programming.com/entry/2018/02/25/044525

```
## 出現頻度の近すぎる・高すぎる単語を消す
　全文章中に1回,2回しか出てこない単語、いらないですよね。逆に、全文章にまんべんなく
出現する単語もいらない気がします。

　CountVectorizerにはmin_df, max_dfというパラメーターがあります。dfはDocument Frequency,
のことで、tf-idfのあれです。要するに(何回出てくるかはおいといて)全文書中の何％にその単語が出現
するかの指標です。それを使って特徴をフィルタリングできます。

  今回は8文章なので、うっかり変な数字を指定すると全く効果がなかったり、なにも残らなかったりするのが
難しいところです。とりあえずは出現する文章が2文章以上、6文章以下くらいの特徴をとってみます。
min_df=2/8=0.25, max_df=6/8=0.75とすれば良さそうですが、比較がgreater | less than or equal
なのか単にgreater | less than なのかよくわからないので、安全をみてmin_df=0.24, max_df=0.76と
しておきます。

## stop wordの除去
 byとかforとかthatとか要らないですよね。stop_wordsというパラメーターがあり、「こんなのいらないよ」と
 単語のりすとをわたすと除去してくます。また、もじ'english'渡すこともでき、その場合は「built-in stop list for English」を使ってくれます
```

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

