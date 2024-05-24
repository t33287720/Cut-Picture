#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 取得名稱為流水號的圖片 從0開始
# 每10秒裁切一次
# 每裁切一次就將流水號+1
# 裁切圖片名為 i_1
# 關閉前一次之圖片 顯示當前裁切之圖片
# 無法找到圖片則多等待10秒 再次執行
# 任意鍵停止程式碼
import cv2
import time
i = 0
show_pic = 1 # 裁切後圖片顯示
# 確保第一張圖片存在
img = cv2.imread(f'{i}.jpg')
if img is None:
   print("找不到第一張圖片")
else:
   while True:
       try:
           img = cv2.imread(f'{i}.jpg')  # 讀取圖片 i.jpg
           x1, y1, x2, y2 = 199, 204, 372, 306
           if x1>x2:
               x1, x2 = x2, x1
           if y1>y2:
               y1, y2 = y2, y1
           crop_img = img[y1:y2, x1:x2]  # 取出陣列的範圍
           output_name = f"{i}_1.jpg"  # 根據 i 生成新的圖片名稱
           if show_pic:
               if i>0:
                   cv2.destroyWindow(f'{i-1}_1')  # 關閉前一個圖片
               cv2.imshow(f'{i}_1', crop_img) # 顯示當前儲存圖片
           cv2.imwrite(output_name, crop_img)  # 儲存圖片
           print(f"已上傳裁切後 {i}_1.jpg")
           i += 1  # 更新 i
       except Exception as e:
           print(f"找不到圖片 {i}.jpg: {e}")
           cv2.waitKey(10000)

       # 檢查是否有按鍵輸入，如果有任何鍵按下，退出迴圈
       if cv2.waitKey(10000) >= 0:
           break
cv2.destroyAllWindows()


# In[ ]:




