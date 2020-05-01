SELECT W1.ID FROM WEATHER W1, WEATHER W2
WHERE TO_DATE(W1.RecordDate)-TO_DATE(W2.RecordDate) = 1
AND W1.Temperature > W2.Temperature

