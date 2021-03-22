import json


with open("txt7.txt", "r", encoding="utf 8") as f7:
    with open("result_txt7.txt", "w", encoding="utf 8") as fw:
        profit = {el.split()[0]: int(el.split()[2]) - int(el.split()[3]) for el in f7}
        average_profit = [profit, {"Средняя прибыль": round((sum([int(i) for i in profit.values() if int(i)>0])) /
                         len([int(n) for n in profit.values() if int(n)>0]))}]
        json.dump(average_profit, fw, ensure_ascii=False)