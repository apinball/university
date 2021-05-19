from tkinter import*
from tkinter import messagebox

import random



a=Tk()
a.title("오늘의 메뉴 선택 프로그램")
a.geometry("400x300")
menu=["bread","macaron","pancake","pumpkin_soup"]

bread_img = PhotoImage(file = "bread.png")
macaron_img = PhotoImage(file = "macaron.png")
pancake_img = PhotoImage(file = "pancake.png")
pumkin_soup_img = PhotoImage(file = "pumpkin_soup.png")

def choice():
    c_menu=random.choice(menu)
    
    if c_menu=="bread":
        la2.configure(text = "선택 메뉴 : 빵")
        im1.configure(image = bread_img)
        messagebox.showinfo("준비 재료","다목적 밀가루 6컵, 소금 한 작은술, 따뜻한 물 2컵, 활성 건조 효모 3 작은술 또는 한 봉지")
    elif c_menu=="macaron":
        la2.configure(text = "선택 메뉴 : 마카롱")
        im1.configure(image = macaron_img)
        messagebox.showinfo("준비 재료","달걀흰자 2개, 소금 아주 약간, 설탕 1/4컵, 슈가파우더 1컵, 아몬드가루 1컵, 코코아가루 2Ts")
    elif c_menu=="pancake":
        la2.configure(text = "선택 메뉴 : 팬 케이크")
        im1.configure(image = pancake_img) 
        messagebox.showinfo("준비 재료", "설탕, 박력분, 소금, 베이킹파우더, 계란, 유유, 버터7g")
    else:
        la2.configure(text = "선택 메뉴 : 호박수프")
        im1.configure(image = pumkin_soup_img)
        messagebox.showinfo("준비 재료","단호박 1개, 버터 1큰술, 우유 1컵, 올리고당 2큰술, 양파1/2개, 물 1컵, 생크림2/3컵, 소금 1꼬집")
        

la1=Label(a, text="<오늘의 메뉴 이미지 보이기>",font=("",20))
la2=Label(a, text="메뉴 미정")
la3=Label(a, text="요리사: 2171313 최현우",fg="blue")
im1=Label(a, image="")
bt1=Button(a, text="오늘의 메뉴 선택하기",command=choice,bg="cyan")


la1.pack();
la2.pack();
bt1.pack();
im1.pack();
la3.place(x=120 ,y=200);
a.mainloop()
