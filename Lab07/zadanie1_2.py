with open('input.txt', 'r', encoding='utf-8') as input_file:
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            line_number = 1     
            for line in input_file:
                words_count = len(line.split())
                output_file.write(f"Строка {line_number}: {words_count} слов(а)\n")
                line_number += 1
            
            print("Обработка завершена! Результат записан в output.txt")