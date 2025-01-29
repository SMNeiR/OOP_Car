from car import Car
from hybridcar import HybridCar

if __name__ == '__main__':
    
    while True:
        print("請選擇車款【1. 汽油】或【2. 油電款】")
        type = input("請輸入數字 '1', '2', 或 'q' 結束： ")

        if type == 'q':
            break

        new_car = Car()     # 預設 汽油
        if type == '2':
            new_car = HybridCar()

        # 【封裝(屬性)】測試，Python 無實際封裝，__models 只是被改成 _Car__models
        # AttributeError: 'Car' object has no attribute '_models'.
        # print(f"Model: {new_car._Car__models}")
        
        while True:
            print("\n請輸入購車預算： ")
            budget = input("'a' 全車款, 'q' 結束： ")

            if budget == 'q':
                break

            if budget == 'a':
                #【多載 1】測試，無參數 get_model()
                print(f"\n推薦車款:\n{new_car.get_model()}")
            elif budget.isdigit() and int(budget) >= new_car.get_price():
                #【多載 2】測試，有參數 get_model(int(budget))    
                print(f"推薦車款:\n{new_car.get_model(int(budget))}")

                number = int(input("請選擇車款： "))
                print(f"\n詳細規格:\n{new_car.get_spec(number)}")
            else:
                print("\n無預算內車款!\n")

