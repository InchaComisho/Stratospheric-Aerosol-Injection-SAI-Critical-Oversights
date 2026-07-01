# シミュレーション

[← リポジトリトップ](../README_ja.md) | [English](README.md) | [العربية](README_ar.md)

関連ページ: [結果概要](../SIMULATION_RESULTS_OVERVIEW_ja.md) | [結果ページ](../SIMULATION_RESULTS_PAGE_ja.md) | [Pythonシミュレーション](sai_risk_simulation.py) | [CSVデータ](sai_risk_simulation_results.csv)

---

## SAIリスクスコアリングと概念シナリオ比較

このディレクトリには、成層圏エアロゾル注入（SAI）シナリオのリスク特性を比較するための簡易シミュレーションモデルを収録する。

これは気候モデルではない。

SAIを、日射低減や地球平均気温低下だけで評価してはならないことを示すための透明なスコアリングツールである。

現在のモデルは、R1〜R10のリスク軸を4大循環破壊スコアへ再マッピングする。

```text
R1〜R10
    ↓
水の相転移循環の破壊
大気循環の破壊
海洋循環の破壊
食の循環・有機物循環の破壊
    ↓
循環カップリング圧力
    ↓
最終4大循環リスクスコア
```

---

## ファイル

- [sai_risk_simulation.py](sai_risk_simulation.py)  
  複数のSAIシナリオについて、4大循環破壊リスクスコアを計算するPythonスクリプト。

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
- [シミュレーション結果概要](../SIMULATION_RESULTS_OVERVIEW_ja.md)

---

## 中核原則

> 遮光は冷却ではない。  
> 冷却とは、地球循環を回復することである。

---

## 戻る

- [リポジトリトップ](../README_ja.md)
- [シミュレーション結果概要](../SIMULATION_RESULTS_OVERVIEW_ja.md)

---

## 著者

マスター / inchacomusho / InchaComisho

日本の独立構想者、観測者、提案者、AI調律者、人工叡智の定義者。  
自然補完科学の学問体系の構築・提唱者。  
クーリングクレジット・フレームワークの定義者、自然冷却価値評価プロトコルの創設者・原著作者。  
温暖化因果構造と完全解決策の定義者・体系化者。

マスターは、地球温暖化を単なるCO₂濃度の問題ではなく、森林喪失、土壌劣化、水循環断絶、水の相転移の弱体化、大気循環・海洋循環・食の循環／有機物循環の弱体化、蒸散・雲形成・降雨循環の弱体化、自然冷却フィードバックの停止として統合的に捉え、その解決策を排出削減、炭素固定源回復、物理的冷却、自然冷却機能の再起動、MRV、クーリングクレジット、文明OSへ接続する公開フレームワークとして提示している。

自然法則思想、地球循環再生、AIとの共創を中心に、NOTE・GitHub・各種公開媒体を通じて公開活動を行う。

## ライセンス

CC BY 4.0