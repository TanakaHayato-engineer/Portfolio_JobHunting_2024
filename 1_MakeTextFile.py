import numpy as np
import random
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
    1.アルゴリズムから生成された時間配列の数だけ抽出し，乱数で再現
    2.GC,MPP,LPP分のテキストファイルを作成

"""

# テキストファイルを保存する場所を指定する
make_dir_path1 = 'C:/GitHubPortfolio_JobHunting_2024/RandomGenerate'
make_dir_path2 = '/Save_GC_TimeList_TextFile'
make_dir_path3 = '/Save_MPP_TimeList_TextFile'
make_dir_path4 = '/Save_LPP_TimeList_TextFile'
make_dir_path5 = '/Save_MPP_LPP_match_TimeList_TextFile'

# ディレクトリが存在しない場合、作成する
# GC（顆粒細胞）の時間配列を保存
if not os.path.exists(make_dir_path1+make_dir_path2):
    os.makedirs(make_dir_path1+make_dir_path2)
# MPP（内側貫通路）の時間配列を保存
if not os.path.exists(make_dir_path1+make_dir_path3):
    os.makedirs(make_dir_path1+make_dir_path3)
# LPP（外側貫通路）の時間配列を保存
if not os.path.exists(make_dir_path1+make_dir_path4):
    os.makedirs(make_dir_path1+make_dir_path4)
# MPPとLPPが一致したときの時間配列を保存
if not os.path.exists(make_dir_path1+make_dir_path5):
    os.makedirs(make_dir_path1+make_dir_path5)


# 実際の顆粒細胞（GC : Granull Cells）のデータ数をリスト化
GC_Model_timeCountList = [25, 24, 23, 22, 23, 21, 23, 19, 19, 16, 21, 18, 23, 21, 22, 20, 24, 25, 23, 25, 37]
# 相互相関
corrcoef = 1.0

GC_Random_TimeList = []

for GC_Model_timeCount in GC_Model_timeCountList:

    # 0から25秒までをms単位で乱数を生成
    GC_Random_TimeList = [int(random.uniform(0, 25000)) for i in range (GC_Model_timeCount)]
    GC_Random_TimeList = sorted(GC_Random_TimeList)

    with open ('{}/GC_TimeList_CorrCoef={}.txt'.format(make_dir_path1+make_dir_path2, str(corrcoef)), 'w') as f_GC:
        for d in GC_Random_TimeList:
            f_GC.write("%d\n" % d)

    corrcoef -= 0.1
    corrcoef = np.round(corrcoef, 1)
    GC_Random_TimeList = []


# 実際のMPP（Medial Parforant Path：内側貫通路）のデータ数をリスト化
MPP_Model_timeCountList = [464, 499, 497, 529, 539, 571, 591, 608, 599, 599, 593, 591, 590, 581, 582, 597, 594, 613, 598, 591, 608]
# 相互相関
corrcoef = 1.0

MPP_Random_TimeList = []

for MPP_Model_timeCount in MPP_Model_timeCountList:

    # 0から25秒までをms単位で乱数を生成
    MPP_Random_TimeList = [int(random.uniform(0, 25000)) for i in range (MPP_Model_timeCount)]
    MPP_Random_TimeList = sorted(MPP_Random_TimeList)

    with open ('{}/MPP_TimeList_CorrCoef={}.txt'.format(make_dir_path1+make_dir_path3, str(corrcoef)), 'w') as f_MPP:
        for d in MPP_Random_TimeList:
            f_MPP.write("%d\n" % d)

    corrcoef -= 0.1
    corrcoef = np.round(corrcoef, 1)
    MPP_Random_TimeList = []


# 実際のLPPのデータ数をリスト化
LPP_Model_timeCountList = [779, 734, 675, 650, 592, 555, 509, 501, 508, 495, 509, 511, 527, 539, 566, 573, 616, 635, 661, 691, 704]
# 相互相関
corrcoef = 1.0

LPP_Random_TimeList = []

for LPP_Model_timeCount in LPP_Model_timeCountList:

    # 0から25秒までをms単位で乱数を生成
    LPP_Random_TimeList = [int(random.uniform(0, 25000)) for i in range (LPP_Model_timeCount)]
    LPP_Random_TimeList = sorted(LPP_Random_TimeList)

    with open ('{}/LPP_TimeList_CorrCoef={}.txt'.format(make_dir_path1+make_dir_path4, str(corrcoef)), 'w') as f_LPP:
        for d in LPP_Random_TimeList:
            f_LPP.write("%d\n" % d)

    corrcoef -= 0.1
    corrcoef = np.round(corrcoef, 1)
    LPP_Random_TimeList = []
