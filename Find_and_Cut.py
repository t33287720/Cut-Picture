#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 尋找座標
# 下方圖片名稱改為自己的圖片
# 左鍵 & 右鍵 選取想擷取之範圍
# 跳出擷取後的畫面 並另存為output.jpg
# 可重新選取左鍵/右鍵 (另一點會固定不變)
# Enter 確認座標
# 取得名稱為流水號的圖片 從0開始
# 每10秒裁切一次
# 每裁切一次就將流水號+1
# 裁切圖片名為 i_1
# 關閉前一次之圖片 顯示當前裁切之圖片
# 無法找到圖片則多等待10秒 再次執行
# 任意鍵停止程式碼
import cv2
import time

# 定義全局變數
i = 0
x1, y1 = -1, -1
x2, y2 = -1, -1
output = None
show_pic = 1 # 裁切後圖片顯示

# 讀取圖像
img_find = cv2.imread('messi5.jpg') # 圖片名稱
point = img_find

# 確保第一張圖片存在
img = cv2.imread(f'{i}.jpg')

# 定義回傳函數
def click_event(event, x, y, flags, param):
   global x1, x2 ,y1 ,y2
   
   if event == cv2.EVENT_LBUTTONDOWN: # 滑鼠左鍵動作
       x1, y1 = x, y
       print('第一點座標：x:',x1 , ', y:', y1)
       crop_and_save_image(img_find, x1, x2, y1, y2)
   
   elif event == cv2.EVENT_RBUTTONDOWN: # 滑鼠右鍵動作
       x2, y2 = x, y
       print('第二點座標：x:',x2 , ', y:', y2)
       crop_and_save_image(img_find, x1, x2, y1, y2)

# 定義裁切圖片的函數
def crop_and_save_image(img_find, x1, x2, y1, y2):

   point = img_find.copy()  # 複製原始圖像
   cv2.circle(point, (x1, y1), 3, (0, 0, 255), -1) # 繪製左鍵紅點
   cv2.circle(point, (x2, y2), 3, (255, 0, 0), -1) # 繪製右鍵藍點
   cv2.imshow('image', point) 
   if y1 > 0 and y2 > 0 and x1 > 0 and x2 > 0:
       if y1 > y2:
           # 將 y1 和 y2 的值對調
           y1, y2 = y2, y1
       if x1 > x2:
           # 將 w1 和 w2 的值對調
           x1, x2 = x2, x1
       crop_img = img_find[y1:y2, x1:x2]  # 取出陣列的範圍
       cv2.imwrite('output.jpg', crop_img)  # 儲存圖片
       cv2.imshow('output', crop_img)
       print('確認座標請按Enter')


cv2.imshow('image', img_find)
while True:
   cv2.setMouseCallback('image', click_event)
   key = cv2.waitKey(0)  # 等待按鍵輸入以確認座標
   if key == 13:  # 等待 Enter 鍵輸入
       print('已確認座標(', x1, ', ', y1,')以及(', x2, ',', y2,')')
       cv2.destroyAllWindows()
       break

if img is None:
   print("找不到第一張圖片")
else:
   while True:
       try:
           img = cv2.imread(f'{i}.jpg')  # 讀取圖片 i.jpg
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
           # 檢查是否有按鍵輸入，如果有任何鍵按下，退出迴圈
           if cv2.waitKey(10000) >= 0:
               break

       # 檢查是否有按鍵輸入，如果有任何鍵按下，退出迴圈
       if cv2.waitKey(10000) >= 0:
           break
cv2.destroyAllWindows()


# In[ ]:




