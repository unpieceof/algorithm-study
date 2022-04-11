# 9498. 시험 성적
import math

score = int(input())
grade = {10:"A", 9:"A", 8:"B", 7:"C", 6:"D"}

score = math.trunc(score/10)
if score > 5:
  print(grade[score])
else:
  print("F")