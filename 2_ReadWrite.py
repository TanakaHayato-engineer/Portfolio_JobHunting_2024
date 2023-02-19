import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['figure.max_open_warning'] = 0
import os


"""

研究室に問い合わせたところ，
--------------------------------------------------------------
・実際に ”アルゴリズムを用いて” テキストファイルに時間配列を記入する
--------------------------------------------------------------
許可が降りませんでした．

ですので，今回の就活においるGitHubのポートフォリオは
--------------------------------------------------------------
・"乱数による"時間配列の生成
--------------------------------------------------------------
に変更して提出させてもらいます．

実際にやっている研究内容と若干のズレが生じますが，
ご理解していただけると幸いです．


◆このPythonファイルでやっていること
    1.相関ごとの発火回数を配列に21パターン（相関：-1.0~1.0を0.1刻み）格納
    2.MPP・LPPの時間配列の中で一致した時間を格納するリスト（MPP_LPP_match_list）作成
    3.ラスター図（棒グラフ）作成
    4.平均発火率のグラフ（散布図）作成

"""


# --------------------------------------------------------------------------------------------------- #


# テキストファイルを保存する場所を指定する
# 既存ディレクトリ
dir_path1 = 'C:/GitHubPortfolio_JobHunting_2024/RandomGenerate'
dir_path2 = '/Save_GC_TimeList_TextFile'
dir_path3 = '/Save_MPP_TimeList_TextFile'
dir_path4 = '/Save_LPP_TimeList_TextFile'
dir_path5 = '/Save_MPP_LPP_match_TimeList_TextFile'
# 新しく作るディレクトリ
make_dir_path6 = 'C:/GitHubPortfolio_JobHunting_2024/Analysis&Graph'
make_dir_path7 = '/Raster_Graph'
make_dir_path8 = '/FireingRate_ScatterPlot'

# ディレクトリが存在しない場合、作成する
# 相関係数ごとの写真を保存
if not os.path.exists(make_dir_path6+make_dir_path7):
    os.makedirs(make_dir_path6+make_dir_path7)
# 平均発火率のグラフ（散布図）を保存
if not os.path.exists(make_dir_path6+make_dir_path8):
    os.makedirs(make_dir_path6+make_dir_path8)


# --------------------------------------------------------------------------------------------------- #


# 相互相関
corrcoef = [h/10 for h in range (10, -11, -1)]

# 初期化宣言
GC_TimeList = []
GC_peak_Count = []

MPP_TimeList = []
MPP_peak_Count = []

LPP_TimeList = []
LPP_peak_Count = []

for corrcoef in corrcoef:

    # 顆粒細胞(GC：Granul Cells)について
    f_GC = open('{}/GC_TimeList_CorrCoef={}.txt'.format(dir_path1+dir_path2, str(corrcoef)))

    GC_TimeList = [s.strip() for s in f_GC.readlines()]
    GC_TimeList_Count = len(GC_TimeList)
    GC_TimeList_ChangeInt = [int(s) for s in GC_TimeList]       # 文字列を整数に直す
    GC_TimeList_sec = [x/1000 for x in GC_TimeList_ChangeInt]   # msecからsecへ
    GC_peak_Count.append(GC_TimeList_Count)

    f_GC.close()


    # MPPについて
    f_MPP = open('{}/MPP_TimeList_CorrCoef={}.txt'.format(dir_path1+dir_path3, str(corrcoef)))

    MPP_TimeList = [s.strip() for s in f_MPP.readlines()]
    MPP_TimeList_Count = len(MPP_TimeList)
    MPP_TimeList_ChangeInt = [int(s) for s in MPP_TimeList]       # 文字列を整数に直す
    MPP_TimeList_sec = [x/1000 for x in MPP_TimeList_ChangeInt]   # msecからsecへ
    MPP_peak_Count.append(MPP_TimeList_Count)

    f_MPP.close()


    # LPPについて
    f_LPP = open('{}/LPP_TimeList_CorrCoef={}.txt'.format(dir_path1+dir_path4, str(corrcoef)))

    LPP_TimeList = [s.strip() for s in f_LPP.readlines()]
    LPP_TimeList_Count = len(LPP_TimeList)
    LPP_TimeList_ChangeInt = [int(s) for s in LPP_TimeList]       # 文字列を整数に直す
    LPP_TimeList_sec = [x/1000 for x in LPP_TimeList_ChangeInt]   # msecからsecへ
    LPP_peak_Count.append(LPP_TimeList_Count)

    f_LPP.close()


    # MPP/LPPで時間が一致している部分をリストにする
    MPP_LPP_match_list_sec = []

    # MPPの時間配列を使って，LPPと時間が一致している部分を抜き出す
    for MPP_num in MPP_TimeList_sec:
        if MPP_num in LPP_TimeList_sec:
            MPP_LPP_match_list_sec.append(MPP_num)

    # MPPとLPPが一致している部分をmsecになおして
    # テキストファイル(MPP_LPP_match_TimeList_CorrCoef=?.txt)に保存する
    MPP_LPP_match_list_msec = [int(x*1000) for x in MPP_LPP_match_list_sec]  # secからmsecへ

    # テキストファイルを格納
    for i in range (len(MPP_LPP_match_list_msec)):
        with open ('{}/MPP_LPP_match_TimeList_CorrCoef={}.txt'.format(dir_path1+dir_path5, str(corrcoef)), 'w') as f_match:
            for j in MPP_LPP_match_list_msec:
                f_match.write("%s\n" % j)


    # --------------------------------------------------------------------------------------------------- #


    # ラスター図（棒グラフ）を記入
    # L(縦)M(横)N(番目)の順に指定
    # グラフの見やすい色 → https://contents-open.hatenablog.com/entry/2021/08/19/231157
    GC_color = '#03AF7A'                # 重厚な青みの緑
    MPP_color = '#FF4B00'               # 鮮やかな黄みの赤
    LPP_color = '#005AFF'               # 鮮やかな青
    MPP_LPP_match_color1 = '#FFF100'    # 鮮やかな黃(MPPの補色)
    MPP_LPP_match_color2 = '#F6AA00'    # 鮮やかなオレンジ(LPPの補色)

    # 画像の範囲を決める．
    fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(8, 12))

    # bar(x軸, y軸, 色)
    axs[0].bar(GC_TimeList_sec, 1, width=0.05, color=GC_color)
    axs[1].bar(MPP_TimeList_sec, 1, width=0.05, color=MPP_color)
    axs[2].bar(LPP_TimeList_sec, 1, width=0.05, color=LPP_color)

    # MPP/LPPが一致している部分を黄色で塗りつぶす
    for match_time in MPP_LPP_match_list_sec:
    # MPPのグラフ
        if match_time in MPP_TimeList_sec:
            axs[1].axvspan(match_time, match_time+0.05, color=MPP_LPP_match_color1, alpha=1)
        # LPPのグラフ
        if match_time in LPP_TimeList_sec:
            axs[2].axvspan(match_time, match_time+0.05, color=MPP_LPP_match_color2, alpha=1)

    # バーの高さを1.0に設定
    axs[0].set_ylim([0, 1.0])
    axs[1].set_ylim([0, 1.0])
    axs[2].set_ylim([0, 1.0])

    axs[0].set_title('GC')
    axs[1].set_title('MPP')
    axs[2].set_title('LPP')

    # y軸の目盛りを削除
    axs[0].set_yticks([])
    axs[1].set_yticks([])
    axs[2].set_yticks([])


    # サブプロットの間隔を調整
    fig.tight_layout()

    # 画像を保存するファイルパスの作成
    file_path = os.path.join(make_dir_path6+make_dir_path7, 'raster_graph_CorrCoef={}.png'.format(str(corrcoef)))

    # 画像を保存する
    fig.savefig(file_path)


# --------------------------------------------------------------------------------------------------- #


# 発火率を計算する
firing_rate_list = []

for i in range (len(GC_peak_Count)):
    firing_rate = (GC_peak_Count[i] / MPP_peak_Count[i]) * 100
    firing_rate_list.append(firing_rate)


# x軸とy軸のデータを用意
# 相互相関
corrcoef_list = [h/10 for h in range (10, -11, -1)]
x = [corrcoef for corrcoef in reversed(corrcoef_list)]
y = [rate for rate in reversed(firing_rate_list)]

# グラフのサイズを指定
plt.figure(figsize=(10,6))

# 散布図を描画
plt.scatter(x, y, color='red')  # 散布図の描画
plt.plot(x, y, color='red')     # 線の描画

# x軸とy軸にラベルを追加
plt.xlabel('Correlation Coefficient')
plt.ylabel('Firing Rate (%)')

# グリッド線を表示
plt.grid()

plt.savefig("{}/FiringRate_ScatterPlot.png".format(make_dir_path6+make_dir_path8))

