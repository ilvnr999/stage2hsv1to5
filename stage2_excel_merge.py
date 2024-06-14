import pandas as pd
import numpy as np

# 共生藻數量excel與找片顏色空間數據excel合併成一個新的excel
# 讀取color_space、symbiodinium
# 輸出marge_data
#target_list = ['PD',] #'PD','SP',
def main(target_list):
    for target in target_list:
        symbiodinium_excel = pd.read_excel("stage2_excels/all_symbiodinium.xlsx", engine='openpyxl')        # 讀取共生藻excel檔案
        x1 = symbiodinium_excel.iloc[1:,:].values.tolist()      # 讀取共生藻檔案除了column名稱以外的資料
        #x2 = symbiodinium_excel.iloc[1:,-1:].values.tolist()       
        #list_x_all = []

        color_space_excel = pd.read_excel(f"stage2_excels/{target}/{target}_color_space.xlsx")      # 讀取color space的工作表
        y = color_space_excel.iloc[:,:].values       # 讀取所有column與roll的資料
        list_y = y.tolist()     # 將資料轉成list型態    
        list_excel = []     # 建立一個空list 後面要加入新的excel檔
        # 搜索共生藻與色彩空間兩檔案中相同的相片
        for i in x1:        # 瀏覽共生藻檔案
            for j in list_y:        # 瀏覽color space檔案
                if i[0] == j[0]:        # 比對相同的名稱
                    #print(i,j)
                    if i[8] == 0:       # 共生藻數量平均為0
                        nor = 0         # 將nor設為0
                    else:       # 共生藻數量平均不為0    
                        nor = i[8] / j[1]       # 共生藻數量平均/area
                    list_excel.append([j[0],i[8],j[1],nor,
                                        j[2], j[3], j[4], j[5], j[6], j[7],
                                        j[8], j[9], j[10], j[11], j[12], j[13],
                                        j[14], j[15], j[16], j[17], j[18], j[19]])

        df = pd.DataFrame(list_excel, columns=["name","symbiodinium", "area", "nor",
                                            "hsv_h_mean","hsv_h_median","hsv_h_variance","hsv_h_std_dev","hsv_h_percentile_25","hsv_h_percentile_75",
                                                "hsv_s_mean","hsv_s_median","hsv_s_variance","hsv_s_std_dev","hsv_s_percentile_25","hsv_s_percentile_75",
                                                "hsv_v_mean","hsv_v_median","hsv_v_variance","hsv_v_std_dev","hsv_v_percentile_25","hsv_v_percentile_75"]) # 設定資料為dataframe column名稱設定
        excel_file = f'stage2_excels/{target}/{target}_merge_data.xlsx'     # 輸出excel檔案名稱

        with pd.ExcelWriter(excel_file, engine='openpyxl', mode='w') as writer:     # 設定？
            df.to_excel(writer, index=False)       # 將資料寫入excel
            print(f"{target} Excel file saved.") 