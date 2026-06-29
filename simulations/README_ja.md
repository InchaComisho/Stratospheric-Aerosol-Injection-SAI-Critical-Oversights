# シミュレーション

## SAIリスクスコアリングと概念シナリオ比較

このディレクトリには、成層圏エアロゾル注入（SAI）シナリオのリスク特性を比較するための簡易シミュレーションモデルを収録する。

これは気候モデルではない。

SAIを、日射低減や地球平均気温低下だけで評価してはならないことを示すための透明なスコアリングツールである。

---

## ファイル

- [sai_risk_simulation.py](sai_risk_simulation.py)  
  複数のSAIシナリオについて、重み付きリスクスコアを計算するPythonスクリプト。

- [sai_risk_simulation_results.csv](sai_risk_simulation_results.csv)  
  既定シナリオの出力結果CSV。

---

## 評価項目

```text
R1 既存の大気粒子負荷
R2 鉛直エアロゾル層の不確実性
R3 湿潤沈着の弱体化
R4 地表固定機能の喪失
R5 粒子再揚起リスク
R6 雲・降雨かく乱
R7 放熱・赤外相互作用リスク
R8 自然冷却フィードバック損傷
R9 ガバナンス・地域対立リスク
R10 停止ショックリスク
```

各項目は0.0から1.0で評価される。

---

## 実行方法

```bash
python sai_risk_simulation.py
```

実行すると、コンソールに結果を表示し、次のCSVを出力する。

```text
sai_risk_simulation_results.csv
```

---

## 結果ページ

表とグラフをまとめたページはこちら。

- [SAIリスクシミュレーション結果ページ](../SIMULATION_RESULTS_PAGE_ja.md)
- [SAI Risk Simulation Results Page](../SIMULATION_RESULTS_PAGE.md)
- [صفحة نتائج محاكاة مخاطر SAI](../SIMULATION_RESULTS_PAGE_ar.md)

---

## 中核原則

> 遮光は冷却ではない。  
> 冷却とは、地球循環を回復することである。

---

## ライセンス

CC BY 4.0
