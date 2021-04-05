import cv2
import boto3
import sudoku3

#click photo
cap = cv2.VideoCapture(0)  
ret , photo = cap.read()   
cv2.imwrite("sudoku.jpg",photo)
print(ret)
cap.release()  

#upload photo in s3
#enter s3 bucket name
bucket_name = "" 
file_name = "sudoku.jpg"

s3 = boto3.resource("s3") 
s3.Bucket(bucket_name).upload_file(file_name , file_name)

# Call Amazon Textract
textract = boto3.client('textract')

response = textract.analyze_document(

 Document={
 'S3Object': {
 'Bucket': bucket_name,
 'Name': "sudoku.jpg"
 }
 },
 FeatureTypes=["TABLES"])

temp_array = []
p = 0
for i in range(1 , 81):
   if p == 81:
       break 
   else: 
      text = response['Blocks'][i]['Text']
      split_text = text.split(" ")
      chunkf = []
      if (len(split_text) == 9):
          for n in split_text:

              try : temp_array.append(int(n)) 
              except: temp_array.append(1)
          p += 9    

      else:
          try : temp_array.append(int(split_text[0])) 
          except: temp_array.append(1)
          p += 1

sudoku_array = [temp_array[9*x:9*(x+1)] for x in range(9)]

#solving the sudoku
solved_array = sudoku3.solve(sudoku_array)
solved_array = [solved_array[9*x:9*(x+1)] for x in range(9)]

for chunk in solved_array:
    print(chunk)