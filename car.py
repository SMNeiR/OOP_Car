from base_car import CarInterface

class Car(CarInterface):
    """汽油款"""

    def __init__(self):
        self._models = {725_000:'1.8L 汽油經典', 780_000:'1.8L 汽油豪華', 795_000:'1.8L 汽油豪華 +', 885_000:'1.8L GR Sport'}
        self._specs = {
            '1.8L 汽油經典':[
                '1.8 升自然進氣引擎', '140 匹馬力', 'CVT 無段變速', '扭力標後懸吊', '15 吋鐵圈',
                '鹵素頭燈', 'LED 尾燈', '後座出風口', '皮質座椅', 'CD 音響',
                '電摺後視鏡', '4 支喇叭', 'TSS 2.0 自動駕駛輔助系統', 'VSC + TRC + HAC', 'ACA 主動過彎輔助',
                'EBS 緊急煞車警示', '7 氣囊'
                ],
            '1.8L 汽油豪華':[
                '新式樣 16 吋鋁圈', 'LED 前霧燈', '網格紋式水箱護罩', '免鑰矢進入與啟動', '9 吋主機',
                '恆溫空調', '倒車雷達', '倒車顯影', '6 支喇叭', '電摺車外後視鏡',
                '無線 Apple CarPlay/Android Auto'
                ],
            '1.8L 汽油豪華+':[
                'BSM 盲點偵測'
                ],
            '1.8L GR Sport':[
                '17 吋勁黑切削鋁圈 + Dunlop 跑車胎', '雙 A 臂後懸吊', '運動化懸吊系統', '底盤空力套件', '光條式 LED 尾燈',
                'GR Sport 外觀套件', '勁黑車外後視鏡', '真皮包裹方向盤及排檔頭', '方向盤換檔撥片', '車速連結車門上鎖',
                '紅黑雙色內裝', '12.3 吋數位儀表'
                ]
            }


    def get_price(self):
        """取得車款最低價格"""
        min_price = min(self._models)
        return min_price

    def get_model(self, budget=None):
        """
        取得車款

        參數：
            budget(int): 有無預算

        返回：
            model_info(string): 回傳車款 1. $725,000  1.8L 汽油經典 
        """
        model_info = ""
        for index, (price, model) in enumerate(self._models.items(), start=1):
            if budget is None or budget >= price: # 篩選出符合預算的車款，budget is None 等於全部顯示
                model_info += f"{index}. ${price:,}  {model}\n"
        return model_info
        
    # 【抽象類別(介面) 2】測試，未實作 get_spec() 建立物件會報錯
    # TypeError: Can't instantiate abstract class Car without an implementation for abstract method 'get_spec'
    def get_spec(self, index):
        """
        取得車款詳細規格 (配件)

        參數：
            index(int): 推薦車款順序
        
        返回：
            spec_info(string): 車款詳細規格
        """
        spec_info = ""
        items = list(self._models.items())

        # 檢查索引是否有效
        if index < 1 or index > len(items):
            return "索引無效"

        # 取得指定索引的鍵值對
        price, model = items[index - 1]     # 索引從 0 開始，所以減 1
        for index, (spec) in enumerate(self.update_spec(model), start=1):
            spec_info += f"{index:2}. {spec}\n" 

        return spec_info
    
    def update_spec(self, model_name):
        """
        取得車款配件清單

        參數：
            model_name(string): 車款名稱
        
        返回：
            spec_info(list): 車款配件清單
        """
        spec_info = ['']
        # 從基本款逐步升級配件，至選取車款名稱 (model_name)
        for model, spec in self._specs.items():     # 所有車款
            spec_info[0] = model
            if model == '1.8L 汽油經典':        # 取得基本款配件 '1.8L 汽油經典'
                spec_info += spec
            elif model == '1.8L 汽油豪華':      # 升級配件 '1.8L 汽油豪華'
                for update_spec in spec:
                    if update_spec == '新式樣 16 吋鋁圈':
                        spec_info[spec_info.index('15 吋鐵圈')] = f'> {update_spec}'
                    elif update_spec == 'LED 前霧燈':
                        spec_info[spec_info.index('鹵素頭燈')] = f'> {update_spec}'
                    elif update_spec == '6 支喇叭':
                        spec_info[spec_info.index('4 支喇叭')] = f'> {update_spec}'
                    elif update_spec == '電摺車外後視鏡':
                        spec_info[spec_info.index('電摺後視鏡')] = f'> {update_spec}'
                    else:
                        spec_info.append(f'+ {update_spec}')
            elif model == '1.8L 汽油豪華+':     # 升級配件 '1.8L 汽油豪華+'
                for update_spec in spec:
                    spec_info.append(f'++ {update_spec}')
            elif model == '1.8L GR Sport':      # 升級配件 '1.8L GR Sport'
                for update_spec in spec:
                    if update_spec == '17 吋勁黑切削鋁圈 + Dunlop 跑車胎':
                        spec_info[spec_info.index('> 新式樣 16 吋鋁圈')] = f'>>> {update_spec}'
                    elif update_spec == '雙 A 臂後懸吊':
                        spec_info[spec_info.index('扭力標後懸吊')] = f'>>> {update_spec}'
                    elif update_spec == '光條式 LED 尾燈':
                        spec_info[spec_info.index('LED 尾燈')] = f'>>> {update_spec}'
                    elif update_spec == '勁黑車外後視鏡':
                        spec_info[spec_info.index('> 電摺車外後視鏡')] = f'>>> {update_spec}'
                    else:
                        spec_info.append(f'+++ {update_spec}')
            if model_name == model: # 符合車款名稱 (model_name)，回傳車款配件清單
                break
        return spec_info