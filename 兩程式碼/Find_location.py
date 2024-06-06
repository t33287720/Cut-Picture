#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 尋找座標
# 下方圖片名稱改為自己的圖片
# 左鍵 & 右鍵 選取想擷取之範圍
# 跳出擷取後的畫面 並另存為output.jpg
# 可重新選取左鍵/右鍵 (另一點會固定不變)
# Enter 關閉 output 
# 任意鍵結束程式
import cv2

# 定義全局變數
w1, h1 = -1, -1
w2, h2 = -1, -1
output = None

# 讀取圖像
img = cv2.imread('0.jpg') # 圖片名稱
point = img

# 定義回傳函數
def click_event(event, x, y, flags, param):
   global w1, w2 ,h1 ,h2
   
   if event == cv2.EVENT_LBUTTONDOWN: # 滑鼠左鍵動作
       w1, h1 = x, y
       print('第一點座標：x:',w1 , ', y:', h1)
       crop_and_save_image(img, h1, h2, w1, w2)
   
   elif event == cv2.EVENT_RBUTTONDOWN: # 滑鼠右鍵動作
       w2, h2 = x, y
       print('第二點座標：x:',w2 , ', y:', h2)
       crop_and_save_image(img, h1, h2, w1, w2)

# 定義裁切圖片的函數
def crop_and_save_image(img, h1, h2, w1, w2):

   point = img.copy()  # 複製原始圖像
   cv2.circle(point, (w1, h1), 3, (0, 0, 255), -1) # 繪製左鍵紅點
   cv2.circle(point, (w2, h2), 3, (255, 0, 0), -1) # 繪製右鍵藍點
   cv2.imshow('image', point) 
   if h1 > 0 and h2 > 0 and w1 > 0 and w2 > 0:
       if h1 > h2:
           # 將 h1 和 h2 的值對調
           h1, h2 = h2, h1
       if w1 > w2:
           # 將 w1 和 w2 的值對調
           w1, w2 = w2, w1
       crop_img = img[h1:h2, w1:w2]  # 取出陣列的範圍
       cv2.imwrite('output.jpg', crop_img)  # 儲存圖片
       cv2.imshow('output', crop_img)


cv2.imshow('image', img)
while True:
   cv2.setMouseCallback('image', click_event)
   key = cv2.waitKey(0)  # 等待按鍵輸入以確認座標
   if key == 13:  # 等待 Enter 鍵輸入
       cv2.destroyWindow('output')  # 關閉 "output" 窗口
       break


cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




