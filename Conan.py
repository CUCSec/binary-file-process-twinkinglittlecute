import struct
import string 

def tamper(student_id):
  with open('lenna.bmp','r+b') as f:
    list=[]
    student_id=int(student_id)
    f.seek(54)
    for i in range(12):
      list.append(student_id%10)
      student_id=int(student_id/10)
    list.reverse()
    for j in range(12):
      step=list[j]
      print(step)
      if step==0:
        f.seek(10,1)
        f.write(b'\x00\x00\x00')
     
      else:
        f.seek(step,1)
        f.write(b'\x00\x00\x00')
     
      
      
    



def detect():
  with open('lenna.bmp', 'rb') as f:
    f.seek(54)
    count = 12
    offset = 0
    last_offset = 0
    while count > 0:
      color = f.read(3)
      if color!=b'\x00\x00\x00':
        f.seek(-2,1)
      if color == b'\x00\x00\x00':

        if offset - last_offset == 10:
          print(0)
        else:
          print(offset - last_offset)

        last_offset = offset+1
        count -= 1

      offset += 1

      


if __name__ == '__main__':
  import sys
  tamper(sys.argv[1])

  detect()