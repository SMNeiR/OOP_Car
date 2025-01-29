from car import Car

# 【繼承】測試，繼承 Car 父類別方法
class HybridCar(Car):
    """油電款"""

    def __init__(self):
        # 【覆寫】測試，覆寫 Car 父類別屬性 _models 和 _specs
        self._models = {845_000:'1.8L Hybrid油電豪華', 885_000:'1.8L Hybrid油電尊爵', 930_000:'1.8L Hybrid GR Sport'}
        self._specs = {
            '1.8L Hybrid油電豪華':[
                '1.8 升油電混合動力', '綜效 140 匹馬力', 'E-CVT 無段變速', '雙 A 臂後懸吊', '新式樣 16 吋鋁圈',
                '橫柵式水箱護罩', '鹵素頭燈', 'LED 尾燈', '後座出風口', '皮質座椅', 
                '恆溫空調', '9吋主機', '無線 Apple CarPlay/Android Auto', '雙環式指針儀表與 4.2 吋資訊幕', 'Smart Entry / 按鈕啟動',
                '6 支喇叭', 'TSS 2.0 自動駕駛輔助系統', 'VSC + TRC + HAC', 'ACA 主動過彎輔助', 'ECB 電子式煞車控制',
                'PBC車身起伏控制系統', 'EBS緊急煞車警示', '倒車雷達', '倒車顯影','7 氣囊'
                ],
            '1.8L Hybrid油電尊爵':[
                '格紋式水箱護罩', '真皮方向排及排檔頭', 'LED前霧燈', 'LED光條尾燈'
                ],
            '1.8L Hybrid GR Sport':[
                '運動化懸吊系統', '底盤空力套件', 'GR Sport外觀套件', 'LED頭燈組', '17吋勁黑切削鋁圈 + Dunlop跑車胎',
                '勁黑車外後視鏡', '紅黑雙色內裝'
                ]
            }

    def update_spec(self, model_name):
        spec_info = ['']
        for model, spec in self._specs.items():
            spec_info[0] = model
            if model == '1.8L Hybrid油電豪華':
                spec_info += spec
            elif model == '1.8L Hybrid油電尊爵':
                for update_spec in spec:
                    if update_spec == '格紋式水箱護罩':
                        spec_info[spec_info.index('橫柵式水箱護罩')] = f'> {update_spec}'
                    elif update_spec == 'LED光條尾燈':
                        spec_info[spec_info.index('LED 尾燈')] = f'> {update_spec}'
                    else:
                        spec_info.append(f'+ {update_spec}')
            elif model == '1.8L Hybrid GR Sport':
                for update_spec in spec:
                    if update_spec == 'LED頭燈組':
                        spec_info[spec_info.index('鹵素頭燈')] = f'>> {update_spec}'
                    elif update_spec == '17吋勁黑切削鋁圈 + Dunlop跑車胎':
                        spec_info[spec_info.index('新式樣 16 吋鋁圈')] = f'>> {update_spec}'
                    else:
                        spec_info.append(f'++ {update_spec}')
            if model_name == model:
                break
        return spec_info