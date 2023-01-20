# causal induction cognitive experiment
## explanation
- This is an experiment to reproduce (JOHN R.ANDERSON & CHING-FAN SHEU 1995).
- JOHN R.ANDERSON & CHING-FAN SHEU 1995 [http://act-r.psy.cmu.edu/?post_type=publications&p=13747](http://act-r.psy.cmu.edu/?post_type=publications&p=13747)

## set up
```
python3 -m venv as95_venv
```
```
source as95_venv/bin/activate
```
```
pip install Django==3.0
```

## set up Analysis Scripts
```
pip install numpy
```
```
pip install pandas
```
```
pip install matplotlib
```
```
pip install seaborn
```

## run experiment
```
python manage.py collectstatic
```
```
python manage.py runserver
```

## run Analysis Scripts
```
python stat.py
```
```
python fixedeffectsmodel.py
```

# data
## Files
- res_user_data_exp*.csv
- res_predictions_exp*.csv
- res_estimations_exp*.csv

## Columns
user_data
- user_id 参加者ID
- start_time 実験開始時刻
- end_time 実験終了時刻
- user_agent ユーザーの使用デバイス、使用ブラウザなどの詳細情報

predictions
- user_id 参加者ID
- number カバーストーリーの薬の種類
- frequency 刺激の種類
- pred_i 提示するセルのインデックス
- stimulation 提示したセルの種類 {a,b,c,d}
- cause 原因事象か真 {0,1}
- effect 結果事象が真 {0,1}
- prediction 予測の判断 {0,1}

estimation
- user_id 参加者ID
- number カバーストーリーの薬の種類
- frequency 刺激の種類
- est_i 推定タイミングのインデックス
- estimation 因果関係の強さの推定値

# Analysis Scripts
- analysis/src/corr.py 相関係数
- analysis/src/plot.py グラフプロット用
- analysis/src/stat.py 基本統計量
- analysis/src/test-of-no-corr.py 無相関検定