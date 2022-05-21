import pygame        # Setup
pygame.init()
screen = pygame.display.set_mode([1100,680])
keep_going = True

sound1 = pygame.mixer.Sound('sounds\All Star.mp3')

mus1 = pygame.mixer.music.load("sounds\Haggstrom.mp3")
pygame.mixer.music.play(-1)
pygame.init()

v1 = "В каком году вышел майнкрафт?"
v1_1 = "2009"
v1_2 = "2011" #p
v1_3 = "2008"
v1_4 = "2015"

v2 = "Сколько надо досок чтобы скрафтить верстак?"
v2_1 = "1 доска"
v2_2 = "3 доски"
v2_3 = "2 доски"
v2_4 = "4 доски" #p

v3 = "Что из списка самое крепкое?"
v3_1 = "Алмазы" #p
v3_2 = "Золото"
v3_3 = "Железо"
v3_4 = "Медь" 

v4 = "Кем станет грибная корова при ударе молнией?"
v4_1 = "Обычной коровой"
v4_2 = "Заряженой гр. коровой"
v4_3 = "Коричневой гр. коровой" #p
v4_4 = "Останется как и была"

v5 = "Кто придумал майнкрафт?"
v5_1 = "Jeb"
v5_2 = "Notch" #p
v5_3 = "Microcoft"
v5_4 = "Windows"

v6 = "С каким шансом с утопленника выпадает"
v6_1 = "8,5%" #p
v6_2 = "15,4%" 
v6_3 = "9,1%"
v6_4 = "7,5%"

v7 = "Какой моб умеет взрыватся?"
v7_1 = "Корова"
v7_2 = "Досаждатель"
v7_3 = "Крипер" #p
v7_4 = "Зиморг"

v8 = "Какого моба добавилив версии 1.18?"
v8_1 = "Светящийся спрут" #p
v8_2 = "Цветочная корова"
v8_3 = "Морская звезда"
v8_4 = "Брутальный пиглин" 

v9 = "Кого призывает вызыватель?"
v9_1 = "Ангелочков"
v9_2 = "Веечек винс"
v9_3 = "Досаждателей" #p
v9_4 = "Чаек"

v10 = "Какая еда сытнее?"
v10_1 = "Яблоко"
v10_2 = "Арбуз"
v10_3 = "Стейк"
v10_4 = "Золотая" #p

win = "Правильно!"
lose = "Неправильно!"

right = "Нажмите: RIGHT для продолжения"
f2 = "Нажмите:  F2  для след. вопроса!"
f3 = "Нажмите:  F3  для след. вопроса!"
f4 = "Нажмите:  F4  для след. вопроса!"
f5 = "Нажмите:  F5  для след. вопроса!"
f6 = "Нажмите:  F6  для след. вопроса!"
f7 = "Нажмите:  F7  для след. вопроса!"
f8 = "Нажмите:  F8  для след. вопроса!"
f9 = "Нажмите:  F9  для след. вопроса!"
f10 = "Нажмите:  F10  для след. вопроса!"
space = "Нажмите: пробел для завершения!"

pr = "Привет!"
vop = "Насколько хорошо ты знаешь майнкрафт?"
vop2 = "Пройди викторину и Узнай!"
vop3 = "Клавиши: 1,2,3,4 - выбрать 1,2,3,4 вариант ответа"
vop4 = "Нажмите:  F1  для продолжения!"

NumQ = 0 # переменная для хранения номера вопроса

pic1 = pygame.image.load("майнкрафт2.jpg")
pic2 = pygame.image.load("майнкрафт2.jpg")

fon = pygame.transform.scale(pygame.image.load("fon.jpg"), (1100, 680))
fon2 = pygame.transform.scale(pygame.image.load("fon.jpg"), (1100, 680))
fon3 = pygame.transform.scale(pygame.image.load("fon.jpg"), (1100, 680))
fon4 = pygame.transform.scale(pygame.image.load("fon.jpg"), (1100, 680))
fon4 = pygame.transform.scale(pygame.image.load("fon.jpg"), (1100, 680))
fon5 = pygame.transform.scale(pygame.image.load("fon.jpg"), (1100, 680))
fon6 = pygame.transform.scale(pygame.image.load("fon.jpg"), (1100, 680))
fon7 = pygame.transform.scale(pygame.image.load("fon.jpg"), (1100, 680))
fon8 = pygame.transform.scale(pygame.image.load("fon.jpg"), (1100, 680))
fon9 = pygame.transform.scale(pygame.image.load("fon.jpg"), (1100, 680))
fon10 = pygame.transform.scale(pygame.image.load("fon.jpg"), (1100, 680))
fonkva = pygame.transform.scale(pygame.image.load("ква.jpg"), (1100, 680))
fonkva2 = pygame.transform.scale(pygame.image.load("ква.jpg"), (1100, 680))
fon_kord = pygame.transform.scale(pygame.image.load("fon_образец.jpg"), (400, 250))
ovcha = pygame.image.load("овца.gif")

timer = pygame.time.Clock()
WHITE = (255, 255, 255)
AQUA = (0,255,255)
MAGENTA = (255,0,255)
YELLOW = (255, 255, 0)
kva = (250, 330)

pygame.font.init()
font = pygame.font.SysFont("Arial Black", 70)
Hi = font.render(pr, True, YELLOW)

font2 = pygame.font.SysFont("Arial Black", 40)
Hi2 = font2.render(vop, True, YELLOW)

font3 = pygame.font.SysFont("Arial Black", 40)
Hi3 = font3.render(vop2, True, YELLOW)

font4 = pygame.font.SysFont("Arial Black", 30)
Hi4 = font4.render(vop3, True, YELLOW)

font5 = pygame.font.SysFont("Arial Black", 30)
Hi5 = font5.render(vop4, True, YELLOW)

font7 = pygame.font.SysFont("Arial Black", 30)
Hi7 = font5.render("Ответить можно только один раз.", True, YELLOW)

font8 = pygame.font.SysFont("Arial Black", 30)
Hi8 = font5.render("Варианты ответа расположены в таком порядке:", True, YELLOW)

fontby = pygame.font.SysFont("Arial Black", 70)
by = fontby.render("Поздравляю!", True, YELLOW)

fontby2 = pygame.font.SysFont("Arial Black", 40)
by2 = fontby2.render("Ты ответила правильно на", True, YELLOW)

fontby3 = pygame.font.SysFont("Arial Black", 40)
by3 = fontby3.render("из 10", True, MAGENTA)

fontby_vop = pygame.font.SysFont("Arial Black", 40)
by_vop = fontby_vop.render("вопросов!", True, YELLOW)

fontby4 = pygame.font.SysFont("Arial Black", 80)
by4 = fontby4.render("С Днём Рождения,", True, YELLOW)

fontby7 = pygame.font.SysFont("Arial Black", 45)
by7 = fontby7.render("Ну а на этом всё!", True, YELLOW)

fontby5 = pygame.font.SysFont("Arial Black", 80)
by5 = fontby5.render("Ксюша!", True, YELLOW)

fontby6 = pygame.font.SysFont("Arial Black", 60)
by6 = fontby6.render("Ты прошла Викторину!", True, YELLOW)

prav = pygame.font.SysFont("Arial Black", 350)
winner_v1 = font.render(win, True, YELLOW)

noprav = pygame.font.SysFont("Arial Black", 350)
losekva = font.render(lose, True, YELLOW)

f_a = pygame.font.SysFont("Arial Black", 30)
r_f2 = f_a.render(f2, True, YELLOW)

f_s = pygame.font.SysFont("Arial Black", 30)
r_f3 = f_s.render(f3, True, YELLOW)

f_d = pygame.font.SysFont("Arial Black", 30)
r_f4 = f_d.render(f4, True, YELLOW)

f_f = pygame.font.SysFont("Arial Black", 30)
r_f5 = f_f.render(f5, True, YELLOW)

f_g = pygame.font.SysFont("Arial Black", 30)
r_f6 = f_g.render(f6, True, YELLOW)

f_h = pygame.font.SysFont("Arial Black", 30)
r_f7 = f_h.render(f7, True, YELLOW)

f_j = pygame.font.SysFont("Arial Black", 30)
r_f8 = f_j.render(f8, True, YELLOW)

f_k = pygame.font.SysFont("Arial Black", 30)
r_f9 = f_k.render(f9, True, YELLOW)

f_l = pygame.font.SysFont("Arial Black", 30)
r_f10 = f_l.render(f10, True, YELLOW)

f_sp = pygame.font.SysFont("Arial Black", 30)
r_sp = f_sp.render(space, True, YELLOW)

f_v1 = pygame.font.SysFont("Arial Black", 50)
f_v1_1 = pygame.font.SysFont("Arial Black", 60)
f_v1_2 = pygame.font.SysFont("Arial Black", 60)
f_v1_3 = pygame.font.SysFont("Arial Black", 60)
f_v1_4 = pygame.font.SysFont("Arial Black", 60)

r_v1 = f_v1.render(v1, True, YELLOW)
r_v1_1 = f_v1_1.render(v1_1, True, YELLOW)
r_v1_2 = f_v1_2.render(v1_2, True, YELLOW)
r_v1_3 = f_v1_3.render(v1_3, True, YELLOW)
r_v1_4 = f_v1_4.render(v1_4, True, YELLOW)



f_v2 = pygame.font.SysFont("Arial Black", 40)
f_v2_1 = pygame.font.SysFont("Arial Black", 40)
f_v2_2 = pygame.font.SysFont("Arial Black", 40)
f_v2_3 = pygame.font.SysFont("Arial Black", 40)
f_v2_4 = pygame.font.SysFont("Arial Black", 40)

r_v2 = f_v2.render(v2, True, YELLOW)
r_v2_1 = f_v2_1.render(v2_1, True, YELLOW)
r_v2_2 = f_v2_2.render(v2_2, True, YELLOW)
r_v2_3 = f_v2_3.render(v2_3, True, YELLOW)
r_v2_4 = f_v2_4.render(v2_4, True, YELLOW)


f_v3 = pygame.font.SysFont("Arial Black", 50)
f_v3_1 = pygame.font.SysFont("Arial Black", 40)
f_v3_2 = pygame.font.SysFont("Arial Black", 40)
f_v3_3 = pygame.font.SysFont("Arial Black", 40)
f_v3_4 = pygame.font.SysFont("Arial Black", 40)

r_v3 = f_v3.render(v3, True, YELLOW)
r_v3_1 = f_v3_1.render(v3_1, True, YELLOW)
r_v3_2 = f_v3_2.render(v3_2, True, YELLOW)
r_v3_3 = f_v3_3.render(v3_3, True, YELLOW)
r_v3_4 = f_v3_4.render(v3_4, True, YELLOW)


f_v4 = pygame.font.SysFont("Arial Black", 38)
f_v4_1 = pygame.font.SysFont("Arial Black", 35)
f_v4_2 = pygame.font.SysFont("Arial Black", 35)
f_v4_3 = pygame.font.SysFont("Arial Black", 35)
f_v4_4 = pygame.font.SysFont("Arial Black", 35)

r_v4 = f_v4.render(v4, True, YELLOW)
r_v4_1 = f_v4_1.render(v4_1, True, YELLOW)
r_v4_2 = f_v4_2.render(v4_2, True, YELLOW)
r_v4_3 = f_v4_3.render(v4_3, True, YELLOW)
r_v4_4 = f_v4_4.render(v4_4, True, YELLOW)


f_v5 = pygame.font.SysFont("Arial Black", 50)
f_v5_1 = pygame.font.SysFont("Arial Black", 40)
f_v5_2 = pygame.font.SysFont("Arial Black", 40)
f_v5_3 = pygame.font.SysFont("Arial Black", 40)
f_v5_4 = pygame.font.SysFont("Arial Black", 40)

r_v5 = f_v5.render(v5, True, YELLOW)
r_v5_1 = f_v5_1.render(v5_1, True, YELLOW)
r_v5_2 = f_v5_2.render(v5_2, True, YELLOW)
r_v5_3 = f_v5_3.render(v5_3, True, YELLOW)
r_v5_4 = f_v5_4.render(v5_4, True, YELLOW)


f_v6 = pygame.font.SysFont("Arial Black", 40)
f_v62 = pygame.font.SysFont("Arial Black", 40)
f_v6_1 = pygame.font.SysFont("Arial Black", 40)
f_v6_2 = pygame.font.SysFont("Arial Black", 40)
f_v6_3 = pygame.font.SysFont("Arial Black", 40)
f_v6_4 = pygame.font.SysFont("Arial Black", 40)

r_v6 = f_v6.render(v6, True, YELLOW)
r_v62 = f_v62.render("Трезубец?", True, YELLOW)
r_v6_1 = f_v6_1.render(v6_1, True, YELLOW)
r_v6_2 = f_v6_2.render(v6_2, True, YELLOW)
r_v6_3 = f_v6_3.render(v6_3, True, YELLOW)
r_v6_4 = f_v6_4.render(v6_4, True, YELLOW)


f_v7 = pygame.font.SysFont("Arial Black", 50)
f_v7_1 = pygame.font.SysFont("Arial Black", 40)
f_v7_2 = pygame.font.SysFont("Arial Black", 40)
f_v7_3 = pygame.font.SysFont("Arial Black", 40)
f_v7_4 = pygame.font.SysFont("Arial Black", 40)

r_v7 = f_v7.render(v7, True, YELLOW)
r_v7_1 = f_v7_1.render(v7_1, True, YELLOW)
r_v7_2 = f_v7_2.render(v7_2, True, YELLOW)
r_v7_3 = f_v7_3.render(v7_3, True, YELLOW)
r_v7_4 = f_v7_4.render(v7_4, True, YELLOW)


f_v8 = pygame.font.SysFont("Arial Black", 50)
f_v8_1 = pygame.font.SysFont("Arial Black", 40)
f_v8_2 = pygame.font.SysFont("Arial Black", 40)
f_v8_3 = pygame.font.SysFont("Arial Black", 40)
f_v8_4 = pygame.font.SysFont("Arial Black", 40)

r_v8 = f_v8.render(v8, True, YELLOW)
r_v8_1 = f_v8_1.render(v8_1, True, YELLOW)
r_v8_2 = f_v8_2.render(v8_2, True, YELLOW)
r_v8_3 = f_v8_3.render(v8_3, True, YELLOW)
r_v8_4 = f_v8_4.render(v8_4, True, YELLOW)


f_v9 = pygame.font.SysFont("Arial Black", 50)
f_v9_1 = pygame.font.SysFont("Arial Black", 40)
f_v9_2 = pygame.font.SysFont("Arial Black", 40)
f_v9_3 = pygame.font.SysFont("Arial Black", 40)
f_v9_4 = pygame.font.SysFont("Arial Black", 40)

r_v9 = f_v9.render(v9, True, YELLOW)
r_v9_1 = f_v9_1.render(v9_1, True, YELLOW)
r_v9_2 = f_v9_2.render(v9_2, True, YELLOW)
r_v9_3 = f_v9_3.render(v9_3, True, YELLOW)
r_v9_4 = f_v9_4.render(v9_4, True, YELLOW)


f_v10 = pygame.font.SysFont("Arial Black", 50)
f_v10_1 = pygame.font.SysFont("Arial Black", 40)
f_v10_2 = pygame.font.SysFont("Arial Black", 40)
f_v10_3 = pygame.font.SysFont("Arial Black", 40)
f_v10_4 = pygame.font.SysFont("Arial Black", 40)
f_v10_4_2 = pygame.font.SysFont("Arial Black", 40)

r_v10 = f_v10.render(v10, True, YELLOW)
r_v10_1 = f_v10_1.render(v10_1, True, YELLOW)
r_v10_2 = f_v10_2.render(v10_2, True, YELLOW)
r_v10_3 = f_v10_3.render(v10_3, True, YELLOW)
r_v10_4 = f_v10_4.render(v10_4, True, YELLOW)
r_v10_4_2 = f_v10_4_2.render("морковка", True, YELLOW)


ky = 0
great_otvet = 0
font6 = pygame.font.SysFont("Arial Black", 40)
Hi6 = font6.render(str(great_otvet), True, MAGENTA) 
while keep_going:
    for i in pygame.event.get(): 
        if i.type == pygame.QUIT: 
            keep_going = False

        if ky == 0:
            #screen.fill(AQUA) 
            screen.blit(fonkva, (0, 0))
            #screen.blit(ovcha, (0, 0))
            screen.blit(Hi, (40, 15))
            screen.blit(Hi2, (40, 115))
            screen.blit(Hi3, (40, 165))
            screen.blit(Hi4, (40, 235))
            screen.blit(Hi5, (40, 285))
            screen.blit(fon_kord, (40, 425))
            screen.blit(Hi7, (40, 335))
            screen.blit(Hi8, (40, 380))
            #screen.blit(Hi6, (40, 360))
        elif ky == 2:
            fonkva2.blit(by, (300, 20))
            fonkva2.blit(by2, (40, 210))
            fonkva2.blit(by3, (695, 210))
            fonkva2.blit(by4, (120, 340))
            fonkva2.blit(by5, (355, 420))
            fonkva2.blit(by6, (185, 110))
            fonkva2.blit(by7, (330, 280))
            fonkva2.blit(by_vop, (830, 210))
            #screen.blit(Hi3, (40, 180))
            #screen.blit(Hi4, (40, 250))
            #screen.blit(Hi5, (40, 300))
            fonkva2.blit(Hi6, (650, 210))
            screen.blit(fonkva2, (0, 0))

     

        if i.type == pygame.KEYDOWN:
            ky = 1
            #print("keydown")
            
            # формируем фон для каждого из вопросов
            if i.key == pygame.K_F1:
                #print("F1*")
                #screen.blit(fon, (0,0))
                fon.blit(r_v1, (120, 60))
                fon.blit(r_v1_1, (50, 200))
                fon.blit(r_v1_2, (50, 500))
                fon.blit(r_v1_3, (1100 - 200, 200))
                fon.blit(r_v1_4, (1100 - 200, 500))
                screen.blit(fon, (0,0))

                NumQ = 1

            elif i.key == pygame.K_F2:
                #print("F2*")
                fon2.blit(r_v2, (22, 60))
                fon2.blit(r_v2_1, (50, 200))
                fon2.blit(r_v2_2, (50, 500))
                fon2.blit(r_v2_3, (1100 - 240, 200))
                fon2.blit(r_v2_4, (1100 - 240, 500))
                screen.blit(fon2, (0,0))

                NumQ = 2

            elif i.key == pygame.K_F3:
                #print("F3*")
                #screen.blit(fon3, (0,0))
                fon3.blit(r_v3, (120, 60))
                fon3.blit(r_v3_1, (50, 200))
                fon3.blit(r_v3_2, (50, 500))
                fon3.blit(r_v3_3, (1100 - 200, 200))
                fon3.blit(r_v3_4, (1100 - 200, 500))
                screen.blit(fon3, (0,0))

                NumQ = 3

            elif i.key == pygame.K_F4:
                #print("F4*")
                #screen.blit(fon4, (0,0))
                fon4.blit(r_v4, (35, 60))
                fon4.blit(r_v4_1, (35, 200))
                fon4.blit(r_v4_2, (35, 500))
                fon4.blit(r_v4_3, (1100 - 500, 200))
                fon4.blit(r_v4_4, (1100 - 500, 500))
                screen.blit(fon4, (0,0))                                        

                NumQ = 4

            elif i.key == pygame.K_F5:
                #print("F5*")
                fon5.blit(r_v5, (150, 60))
                fon5.blit(r_v5_1, (50, 200))
                fon5.blit(r_v5_2, (50, 500))
                fon5.blit(r_v5_3, (1100 - 250, 200))
                fon5.blit(r_v5_4, (1100 - 250, 500))
                screen.blit(fon5, (0,0))                  
                NumQ = 5

            elif i.key == pygame.K_F6:
                #print("F6*")
                fon6.blit(r_v6, (80, 40))
                fon6.blit(r_v62, (400, 110))
                fon6.blit(r_v6_1, (50, 200))
                fon6.blit(r_v6_2, (50, 500))
                fon6.blit(r_v6_3, (1100 - 200, 200))
                fon6.blit(r_v6_4, (1100 - 200, 500))
                screen.blit(fon6, (0,0))                  
                NumQ = 6

            elif i.key == pygame.K_F7:
                #print("F7*")
                fon7.blit(r_v7, (120, 60))
                fon7.blit(r_v7_1, (50, 200))
                fon7.blit(r_v7_2, (50, 500))
                fon7.blit(r_v7_3, (1100 - 200, 200))
                fon7.blit(r_v7_4, (1100 - 200, 500))
                screen.blit(fon7, (0,0))                  
                NumQ = 7

            elif i.key == pygame.K_F8:
                #print("F8*")
                fon8.blit(r_v8, (50, 60))
                fon8.blit(r_v8_1, (40, 200))
                fon8.blit(r_v8_2, (40, 500))
                fon8.blit(r_v8_3, (1100 - 460, 200))
                fon8.blit(r_v8_4, (1100 - 460, 500))
                screen.blit(fon8, (0,0))                  
                NumQ = 8

            elif i.key == pygame.K_F9:
                #print("F9*")
                fon9.blit(r_v9, (120, 60))
                fon9.blit(r_v9_1, (50, 200))
                fon9.blit(r_v9_2, (50, 500))
                fon9.blit(r_v9_3, (1100 - 350, 200))
                fon9.blit(r_v9_4, (1100 - 350, 500))
                screen.blit(fon9, (0,0))                  
                NumQ = 9

            elif i.key == pygame.K_F10:
                #print("F10*")
                fon10.blit(r_v10, (300, 60))
                fon10.blit(r_v10_1, (50, 200))
                fon10.blit(r_v10_2, (50, 500))
                fon10.blit(r_v10_3, (1100 - 300, 200))
                fon10.blit(r_v10_4, (1100 - 300, 480))
                fon10.blit(r_v10_4_2, (1100 - 315, 530))

                screen.blit(fon10, (0,0))                  
                NumQ = 10

            if ky == 0:
                screen.fill(AQUA) 
                screen.blit(Hi, (40, 20))
                screen.blit(Hi2, (40, 130))
                screen.blit(Hi3, (40, 180))
                screen.blit(Hi4, (40, 250))
                screen.blit(Hi5, (40, 300))
                screen.blit(Hi6, (40, 360))

            elif i.key == pygame.K_1:
                #print ("вопрос: " + str(NumQ) + "ответ №1")
                if NumQ == 3:    #or NumQ == 6 or NumQ == 8:
                    # это правидльные ответы
                    fon3.blit(winner_v1, (280, 350))
                    fon3.blit(r_f4, (280, 600))
                    screen.blit(fon3, (0,0))
                    great_otvet += 1
                if NumQ == 6:
                    fon6.blit(winner_v1, (280, 350))
                    fon6.blit(r_f7, (280, 600))
                    screen.blit(fon6, (0,0))
                    great_otvet += 1
                if NumQ == 8:
                    fon8.blit(winner_v1, (280, 350))
                    fon8.blit(r_f9, (280, 600))
                    screen.blit(fon8, (0,0))
                    great_otvet += 1

                elif NumQ == 1:
                    fon.blit(losekva, (280, 350))
                    fon.blit(r_f2, (280, 600))
                    screen.blit(fon, (0,0))
                elif NumQ == 2:
                    fon2.blit(losekva, (280, 350))
                    fon2.blit(r_f3, (280, 600))
                    screen.blit(fon2, (0,0))
                elif NumQ == 4:
                    fon4.blit(losekva, (280, 350))
                    fon4.blit(r_f5, (280, 600))
                    screen.blit(fon4, (0,0))
                elif NumQ == 5:
                    fon5.blit(losekva, (280, 350))
                    fon5.blit(r_f6, (280, 600))
                    screen.blit(fon5, (0,0))
                elif NumQ == 7:
                    fon7.blit(losekva, (280, 350))
                    fon7.blit(r_f8, (280, 600))
                    screen.blit(fon7, (0,0))
                elif NumQ == 9:
                    fon9.blit(losekva, (280, 350))
                    fon9.blit(r_f10, (280, 600))
                    screen.blit(fon9, (0,0))
                elif NumQ == 10:
                    fon10.blit(losekva, (280, 350))
                    fon10.blit(r_sp, (280, 600))
                    screen.blit(fon10, (0,0))

                    # а тут - неправильные
                    
                
            elif i.key == pygame.K_2:
                #print ("вопрос: " + str(NumQ) + "ответ №2")
                if NumQ == 1:                       #or NumQ == 5:
                    # это правидльные ответы
                    #screen.blit(fon, (0,0))
                    fon.blit(winner_v1, (280, 350))
                    fon.blit(r_f2, (280, 600))
                    screen.blit(fon, (0,0))
                    great_otvet += 1
                if NumQ == 5:
                    fon5.blit(winner_v1, (280, 350))
                    fon5.blit(r_f6, (280, 600))
                    screen.blit(fon5, (0,0))
                    great_otvet += 1

                elif NumQ == 2:
                    fon2.blit(losekva, (280, 350))
                    fon2.blit(r_f3, (280, 600))
                    screen.blit(fon2, (0,0))
                elif NumQ == 3:
                    fon3.blit(losekva, (280, 350))
                    fon3.blit(r_f4, (280, 600))
                    screen.blit(fon3, (0,0))
                elif NumQ == 4:
                    fon4.blit(losekva, (280, 350))
                    fon4.blit(r_f5, (280, 600))
                    screen.blit(fon4, (0,0))
                elif NumQ == 6:
                    fon6.blit(losekva, (280, 350))
                    fon6.blit(r_f7, (280, 600))
                    screen.blit(fon6, (0,0))
                elif NumQ == 7:
                    fon7.blit(losekva, (280, 350))
                    fon7.blit(r_f8, (280, 600))
                    screen.blit(fon7, (0,0))
                elif NumQ == 8:
                    fon8.blit(losekva, (280, 350))
                    fon8.blit(r_f9, (280, 600))
                    screen.blit(fon8, (0,0))
                elif NumQ == 9:
                    fon9.blit(losekva, (280, 350))
                    fon9.blit(r_f10, (280, 600))
                    screen.blit(fon9, (0,0))
                elif NumQ == 10:
                    fon10.blit(losekva, (280, 350))
                    fon10.blit(r_sp, (280, 600))
                    screen.blit(fon10, (0,0))
                #else:
                    # а тут - неправильные

  
            elif i.key == pygame.K_3: # 4  7  9
                #print ("вопрос: " + str(NumQ) + "ответ №3")
                if NumQ == 4:
                    fon4.blit(winner_v1, (280, 350))
                    fon4.blit(r_f5, (280, 600))
                    screen.blit(fon4, (0,0))
                    great_otvet += 1
                if NumQ == 7:
                    fon7.blit(winner_v1, (280, 350))
                    fon7.blit(r_f8, (280, 600))
                    screen.blit(fon7, (0,0))
                    great_otvet += 1
                if NumQ == 9:
                    fon9.blit(winner_v1, (280, 350))
                    fon9.blit(r_f10, (280, 600))
                    screen.blit(fon9, (0,0))
                    great_otvet += 1
                elif NumQ == 1:
                    fon.blit(losekva, (280, 350))
                    fon.blit(r_f2, (280, 600))
                    screen.blit(fon, (0,0))
                elif NumQ == 2:
                    fon2.blit(losekva, (280, 350))
                    fon2.blit(r_f3, (280, 600))
                    screen.blit(fon2, (0,0))
                elif NumQ == 3:
                    fon3.blit(losekva, (280, 350))
                    fon3.blit(r_f4, (280, 600))
                    screen.blit(fon3, (0,0))
                elif NumQ == 5:
                    fon5.blit(losekva, (280, 350))
                    fon5.blit(r_f6, (280, 600))
                    screen.blit(fon5, (0,0))
                elif NumQ == 6:
                    fon6.blit(losekva, (280, 350))
                    fon6.blit(r_f7, (280, 600))
                    screen.blit(fon6, (0,0))
                elif NumQ == 8:
                    fon8.blit(losekva, (280, 350))
                    fon8.blit(r_f9, (280, 600))
                    screen.blit(fon8, (0,0))
                elif NumQ == 10:
                    fon10.blit(losekva, (280, 350))
                    fon10.blit(r_sp, (280, 600))
                    screen.blit(fon10, (0,0))

            elif i.key == pygame.K_4: # 2  10
                #print ("вопрос: " + str(NumQ) + "ответ №4")
                if NumQ == 2:
                    fon2.blit(winner_v1, (280, 350))
                    fon2.blit(r_f3, (280, 600))
                    screen.blit(fon2, (0,0))
                    great_otvet += 1
                if NumQ == 10:
                    fon10.blit(winner_v1, (280, 350))
                    fon10.blit(r_sp, (280, 600))
                    screen.blit(fon10, (0,0))
                    great_otvet += 1
                    #screen.blit(Hi5, (40, 300))
                    #ky = 0
                elif NumQ == 1:
                    fon.blit(losekva, (280, 350))
                    fon.blit(r_f2, (280, 600))
                    screen.blit(fon, (0,0))
                elif NumQ == 3:
                    fon3.blit(losekva, (280, 350))
                    fon3.blit(r_f4, (280, 600))
                    screen.blit(fon3, (0,0))
                elif NumQ == 4:
                    fon4.blit(losekva, (280, 350))
                    fon4.blit(r_f5, (280, 600))
                    screen.blit(fon4, (0,0))
                elif NumQ == 5:
                    fon5.blit(losekva, (280, 350))
                    fon5.blit(r_f6, (280, 600))
                    screen.blit(fon5, (0,0))
                elif NumQ == 6:
                    fon6.blit(losekva, (280, 350))
                    fon6.blit(r_f7, (280, 600))
                    screen.blit(fon6, (0,0))
                elif NumQ == 7:
                    fon7.blit(losekva, (280, 350))
                    fon7.blit(r_f8, (280, 600))
                    screen.blit(fon7, (0,0))
                elif NumQ == 8:
                    fon8.blit(losekva, (280, 350))
                    fon8.blit(r_f9, (280, 600))
                    screen.blit(fon8, (0,0))
                elif NumQ == 9:
                    fon9.blit(losekva, (280, 350))
                    fon9.blit(r_f10, (280, 600))
                    screen.blit(fon9, (0,0))

            elif i.key == pygame.K_SPACE:
                ky = 2
                pygame.mixer.music.pause()
                sound1.play()

            Hi6 = font6.render(str(great_otvet), True, MAGENTA) 
            #print(great_otvet)
            #Hi6 = font6.render(str(great_otvet), True, MAGENTA) 
    

    pygame.display.update()
    timer.tick(60)

