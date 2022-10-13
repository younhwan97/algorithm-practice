SELECT PRODUCT_CODE, SUM((SALES_AMOUNT * PRICE)) AS SALES
FROM OFFLINE_SALE O
JOIN PRODUCT P
ON O.PRODUCT_ID = P.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE