# Deep Neural Networks for Job Recommendations 實作
# 人力銀行「配對信」職缺推薦應用

</br>

Job recommendation (YouTube DNN recommendation)

參考論文 [Deep Neural Networks for YouTube Recommendations (RecSys 2016)](https://research.google.com/pubs/archive/45530.pdf) 的兩階段推薦架構，應用在人力銀行的兩個場景：

1. **職缺搜尋頁排序（Ranking）**：依照求職者的偏好，重新排序搜尋結果
2. **配對信推薦**：根據求職者的行為與背景，找出他們最可能主動應徵的職缺並寄送推薦

第一頁點擊率（CTR）從 16% 提升到 35%，每天平均多出 47.3 次面試邀約。

---

## 專案內容

- 建立 **粗排（Candidate Generation）+ 精排（Ranking）** 兩階段的職缺推薦流程
- 建立 **用戶畫像** 與 **物件（職缺）畫像**，作為模型的輸入特徵
- 考慮商業邏輯、求職情境對資料做 **特徵工程**，決定特徵重要性，與模型考慮程度。
- 用 **Word2Vec** 把職缺、職務類別、工作地點轉成 embedding，作為 DNN 的預訓練向量
- 把模型包成 **API**，提供配對信即時取得推薦結果

---

## 模型架構

```
        所有職缺
           │
           ▼
 ┌─────────────────────┐
 │ 粗排                 │  用戶畫像 → DNN → 選出數百個候選職缺
 │ Candidate Generation│
 └─────────────────────┘
           │
           ▼
 ┌─────────────────────┐
 │ 精排 Ranking         │  用戶畫像 + 物件畫像 → DNN → 預測應徵機率
 └─────────────────────┘
           │
           ▼
      配對信推薦結果
```

---

## 資料與特徵工程

### 資料處理流程

1. 取得用戶畫像
2. 取得物件畫像
3. Encoding：把類別特徵轉成 token，拼成訓練資料，輸入 DNN
4. 輸出 sigmoid 分數（0：沒有應徵，1：主動應徵）

---


## 參考資料

- Paul Covington, Jay Adams, Emre Sargin. *Deep Neural Networks for YouTube Recommendations*. RecSys 2016.
