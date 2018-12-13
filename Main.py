import Preprocessing as pr
import Crossvalidation as cr

input_path = './input/insurance_awal.csv'
output_path = './input/insurance_bersih.csv'

data = pr.load_praproses(input_path, output_path)
rata_precision, rata_recall, rata_fmeasure = cr.crossvalidation(data)

print("Precision    : ", round(rata_precision*100, 2),"%")
print("Recall       : ", round(rata_recall*100, 2),"%")
print("F-Measure    : ", round(rata_fmeasure*100, 2),"%")
