import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter .ttk import *


def user_add_path():
    root.withdraw()
    u_path = filedialog.askopenfilename()
    # u_path = str(entry.get())
    return u_path

def user_save_image():
    root.withdraw()
    u_save_path = filedialog.askdirectory()
    # u_path = str(entry.get())
    return u_save_path

def shik_user_image(y):
    if y == 1:
        dragon = PhotoImage(r'C:\Users\cohenhad\code\shikShuk\dragon\dragongood.png')
    elif y == 2:
        dragon = PhotoImage(r'C:\Users\cohenhad\code\shikShuk\dragon\dragonnn_icon.gif')
    else:
        dragon = PhotoImage(r'C:\Users\cohenhad\code\shikShuk\dragon\dragon_n_icon.gif')
    return dragon


def shuk_user_image(y):
    if y == 1:
        dragon = PhotoImage(r'C:\Users\cohenhad\code\shikShuk\puke\puke_icon.gif')
    elif y == 2:
        dragon = PhotoImage(r'C:\Users\cohenhad\code\shikShuk\puke\pukegood_icon.gif')
    else:
        dragon = PhotoImage(r'C:\Users\cohenhad\code\shikShuk\puke\pukee_icon.gif')
    return dragon


def submit_button():
    picture_path = user_add_path
    save_new_image = user_save_image
    shik_image = shik_user_image
    shuk_image = shuk_user_image
    return picture_path, save_new_image, shik_image, shuk_image


root = tk.Tk()
canvas = tk.Canvas(root, height=650, width=750)
canvas.pack()
root.title('Shik or Shuk')
root.iconbitmap(r'C:\Users\cohenhad\code\shikShuk\title_icon_icon_icon.ico')

background_image = tk.PhotoImage(file='title.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relx=0.15, rely=0.02, relwidth=0.7, relheight=0.2)

# ------------------------------user pick his image for edit------------------------------

frame = tk.Frame(root, bg='#e6e600', bd=5)
frame.place(relx=0.3, rely=0.25, relwidth=0.3, relheight=0.08, anchor='n')
entry1_1 = tk.Button(frame, text='Input Image', font=3, command=user_add_path)
entry1_1.place(relx=0, rely=0, relwidth=1, relheight=1)

# ------------------------------user pick his save folder------------------------------

frame_save = tk.Frame(root, bg='#e6e600', bd=5)
frame_save.place(relx=0.7, rely=0.25, relwidth=0.3, relheight=0.08, anchor='n')
entry_save = tk.Button(frame_save, text='output Image', font=3, command=user_save_image)
entry_save.place(relx=0, rely=0, relwidth=1, relheight=1)

# ------------------------------user pick his shik image------------------------------

frame1 = tk.Frame(root, bd=5)
frame1.place(relx=0.628, rely=0.37, relwidth=1, relheight=0.08, anchor='n')
entry1_1_1 = tk.Label(frame1, text='Pick your Shik logo:', font=4)
entry1_1_1.place(relx=0, rely=0)



# 1
shik1_image = PhotoImage(file = r'C:\Users\cohenhad\code\shikShuk\dragon\dragongood.png')
shik1_image = shik1_image.subsample(3, 3)

frame_shik1 = tk.Frame(root, bd=5, bg='#e6e600')
frame_shik1.place(relx=0.3, rely=0.45, relwidth=0.13, relheight=0.15, anchor='n')
shik1 = Button(frame_shik1, image = shik1_image, command = shik_user_image(1))
shik1.place(relx=0, rely=0, relwidth=1, relheight=1)

# 2
shik2_image = PhotoImage(file = r'C:\Users\cohenhad\code\shikShuk\dragon\dragonnn_icon.gif')
shik2_image = shik2_image.subsample(3, 3)

frame_shik2 = tk.Frame(root, bd=5, bg='#e6e600')
frame_shik2.place(relx=0.5, rely=0.45, relwidth=0.13, relheight=0.15, anchor='n')
shik2 = Button(frame_shik2, image = shik2_image, command = shik_user_image(2))
shik2.place(relx=0, rely=0, relwidth=1, relheight=1)

3
shik3_image = PhotoImage(file = r'C:\Users\cohenhad\code\shikShuk\dragon\dragon_n_icon.gif')
shik3_image = shik3_image.subsample(3, 3)

frame_shik3 = tk.Frame(root, bd=5, bg='#e6e600')
frame_shik3.place(relx=0.7, rely=0.45, relwidth=0.13, relheight=0.15, anchor='n')
shik3 = Button(frame_shik3, image = shik3_image, command =shik_user_image(3))
shik3.place(relx=0, rely=0, relwidth=1, relheight=1)

# ------------------------------user pick his shuk image------------------------------

frame1_shuk = tk.Frame(root, bd=5)
frame1_shuk.place(relx=0.628, rely=0.64, relwidth=1, relheight=0.08, anchor='n')
entry1_1_1 = tk.Label(frame1_shuk, text='Pick your Shuk logo:', font=4)
entry1_1_1.place(relx=0, rely=0)



# 1
shuk1_image = PhotoImage(file = r'C:\Users\cohenhad\code\shikShuk\puke\puke_icon.gif')
shuk1_image = shuk1_image.subsample(3, 3)

frame_shuk1 = tk.Frame(root, bd=5, bg='#e6e600')
frame_shuk1.place(relx=0.3, rely=0.72, relwidth=0.13, relheight=0.15, anchor='n')
shuk1 = Button(frame_shuk1, image = shuk1_image, command =shuk_user_image(1))
shuk1.place(relx=0, rely=0, relwidth=1, relheight=1)

# 2
shuk2_image = PhotoImage(file = r'C:\Users\cohenhad\code\shikShuk\puke\pukegood_icon.gif')
shuk2_image = shuk2_image.subsample(3, 3)

frame_shuk2 = tk.Frame(root, bd=5, bg='#e6e600')
frame_shuk2.place(relx=0.5, rely=0.72, relwidth=0.13, relheight=0.15, anchor='n')
shuk2 = Button(frame_shuk2, image = shuk2_image, command =shuk_user_image(2))
shuk2.place(relx=0, rely=0, relwidth=1, relheight=1)

# 3
shuk3_image = PhotoImage(file = r'C:\Users\cohenhad\code\shikShuk\puke\pukee_icon.gif')
shuk3_image = shuk3_image.subsample(3, 3)

frame_shuk3 = tk.Frame(root, bd=5, bg='#e6e600')
frame_shuk3.place(relx=0.7, rely=0.72, relwidth=0.13, relheight=0.15, anchor='n')
shuk3 = Button(frame_shuk3, image = shuk3_image, command =shuk_user_image(3))
shuk3.place(relx=0, rely=0, relwidth=1, relheight=1)

# ------------------------------submit------------------------------



frame_submit = tk.Frame(root, bd=5, bg='#e6e600')
frame_submit.place(relx=0.5, rely=0.9, relwidth=0.7, relheight=0.08, anchor='n')
frame_but = Button(frame_submit, text='Submit', command =submit_button)
frame_but.place(relx=0, rely=0, relwidth=1, relheight=1)






root.mainloop()












# target_image = test_func()
# target_image = str(input('Please enter full path to your target picture: '))
target_image = user_add_path
#need to fix it - validation
# while ' ' in target_image or target_image == None:
#     target_image = str(print('Impossible to enter path with spaces inside\nPlease try again: '))
#
# if '"' in target_image:
#     target_image = target_image.replace('"', '')
#
# user_result = str(input('Would you like to save image in a specific path?'))
# while user_result not in ['yes', 'no']:
# # while user_result != 'yes' and user_result != 'no':
#     user_result = str(input('Please answer yes or no. try again: '))
#
# if user_result == 'yes':
#     path_result = str(print('Enter a full path please..'))
#     while ' ' in path_result:
#        path_result = str(print('Impossible to enter path with spaces inside '))
#     if '"' in path_result:
#         path_result = path_result.replace('"', '')
# else:
#     desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
#     print('The ShikShuk image will wait for you on the Desktop')
#     full_path_desktop = desktop + '\\ShikShuk'
#     path_result = os.path.join(full_path_desktop)
path_result = user_save_image
imgg = Image.open(target_image)
# imgg = Image.open('orel.jpg')
w, h = imgg.size
extension = imgg.format
extension = '.{}'.format(extension)
path_result = path_result+extension

dragon = Image.open('dragon1.jpg')
puke = Image.open('corona1.jfif')

w_img = int(w/10)
h_img = int(h/10)
new_size = w_img, h_img
new_dragon = dragon.resize(new_size)
new_puke = puke.resize(new_size)

#title app
title = Image.open('title.png')
t_width = int(w/2)
t_height = int(h/10)
title_size = t_width, t_height
titleapp = title.resize(title_size)
title_location = ((int((2/100) * w)), (int((2/100) * h)))

x = int(0)
y = int((80/100)*h)
image_arr = []
image_arr.append(imgg.filename)

shik_or_shuk = input('Choose side --> Shik or Shuk')
while shik_or_shuk not in ['shik', 'shuk']:
    shik_or_shuk = str(input('Please answer shik or shuk. try again: '))
if shik_or_shuk == 'shik':
    rate = input('How good is it (choose number 1 to 5) \n5 is for fucking amazing style')
    while rate not in ['1', '2', '3', '4', '5']:
        rate = input('Please enter valid number between 1 to 5: ')

    base_image = image_arr[0]
    for i in range(int(rate)):
        if i == 0:
            x += int((5/100) * w)
        else:
            x += int(((5/100)*w)+((15/100)*w))

        area = (x, y)
        z = Image.open(base_image)
        z.paste(new_dragon, area)
        z.save("imgg{a}{b}".format(a=i+1, b=extension))
        base_image = "imgg{a}{b}".format(a=i+1, b=extension)

    final = Image.open(base_image)
    final.paste(titleapp, title_location)
    final.save(path_result)
    final.show()

else:
    rate = input('How bad is it (choose number 1 to 5) \n5 is for bad-bad-bad style')
    while rate not in ['1', '2', '3', '4', '5']:
        rate = input('Please enter valid number between 1 to 5: ')
    base_image = image_arr[0]
    for i in range(int(rate)):
        if i == 0:
            x += int((5/100) * w)
        else:
            x += int(((5/100)*w)+((15/100)*w))

        area = (x, y)
        z = Image.open(base_image)
        z.paste(new_puke, area)
        z.save("imgg{a}{b}".format(a=i+1, b=extension))
        base_image = "imgg{a}{b}".format(a=i+1, b=extension)

    final = Image.open(base_image)
    final.paste(titleapp, title_location)
    final.save(path_result)
    final.show()
