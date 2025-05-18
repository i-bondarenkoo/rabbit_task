from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from abc import ABC, abstractmethod
import csv
import json
import xml.etree.ElementTree as ET


class Report(ABC):
    @abstractmethod
    def generate(self, type: str, headres: list, data: list):
        pass


class ExcelReport(Report):
    def generate(self, headers, data, filename):
        # новый файл
        wb = Workbook()
        # новый лист в excel файле
        sheet = wb.active

        # Первая строчка - заголовки
        for i in range(len(headers)):
            # преобразует номер столбца в букву 1-а 2-б
            string = get_column_letter(i + 1)
            # [Буква]1 - все заголовки пишутся в первую строку А1 В1 С1 и тд
            sheet[f"{string}1"] = headers[i]
        # данные
        # индекс j перебирает строку данных
        for j in range(len(data)):
            # индекс i значение внутри строки
            for i in range(len(data[i])):
                column = get_column_letter(i + 1)
                sheet[f"{column}{j + 2}"] = data[j][i]
        wb.save(filename)


class CSVReport(Report):
    def generate(self, headers, data, filename):
        # открываем файл для записи и указываем кодировку
        with open("report.csv", mode="w", encoding="utf-8") as file:
            # объект для записи информации в файл csv.writer
            file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
            file_writer.writerow(headers)
            for row in data:
                file_writer.writerow(row)


class JSONReport(Report):
    def generate(self, headers, data, filename):
        new_list = []
        for row in data:
            new_dict = {}
            for i in range(len(headers)):
                new_dict[headers[i]] = row[i]
            new_list.append(new_dict)
        with open(filename, mode="w", encoding="utf-8") as file:
            json.dump(new_list, file, ensure_ascii=False, indent=4)


class XMLReport(Report):
    def generate(self, headers, data, filename):
        root = ET.Element("Data")

        for row in data:
            row_elem = ET.SubElement(root, "Row")
            for i, header in enumerate(headers):
                col_elem = ET.SubElement(row_elem, "Column", name=header)
                col_elem.text = str(row[i])

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)


headers = ["Заголовок 1", "Заголовок 2", "Заголовок 3"]
data = [[1, "a", True], [2, "b", True], [3, "c", False]]
csv_report = CSVReport()
csv_report.generate(headers, data, "C:/Users/i.bondarenko/Desktop/report.csv")
json_report = JSONReport()
json_report.generate(headers, data, "C:/Users/i.bondarenko/Desktop/report.json")
xml_report = XMLReport()
xml_report.generate(headers, data, "C:/Users/i.bondarenko/Desktop/report.xml")
