# 리스트를 함수에 전달할 경우
# 전달받은 리스트의 내용 수정됨

def show_list(myList):
    print('show_list함수')
    print(myList)
    print(id(myList))

def modify_list(myList):
    print('modify_list 함수')
    myList.append('new')
    myList = [100,200,300]
    print(myList)
    print('id', id(myList))
    print('-------')

# my_list = [1,2,3,4]
# # show_list(my_list)
# modify_list(my_list)
# print(my_list)
# print('my_list :',id(my_list))

students =[
    {'name': '홍길동','kor' : 87,'math': 98,'eng' : 88,'science' : 95},
    {'name': '이몽룡','kor' : 92,'math': 98,'eng' : 96,'science' : 98},
    {'name': '성춘향','kor' : 76,'math': 92,'eng' : 94,'science' : 90},
    {'name': '변학도','kor' : 98,'math': 96,'eng' : 96,'science' : 92},
    {'name': '박지성','kor' : 95,'math': 98,'eng' : 98,'science' : 98},
    {'name': '류현진','kor' : 64,'math': 88,'eng' : 92,'science' : 92}]

def get_student_info(stdList):
    name = stdList['name']
    print('stdList id: ', id(stdList))
    return {'name':name}

for std in students:
    stdInfo = get_student_info(std)
    print(stdInfo['name'])
    print('std id: ', id(std))




