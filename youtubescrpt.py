# -*- coding: utf8 -*-

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import numpy as np
import tkinter

#links = ['https://www.youtube.com/watch?v=dUM7GCLMBxQ','https://www.youtube.com/watch?v=NAyQMKsi2to','https://www.youtube.com/watch?v=qX9nf86KJ8k','https://www.youtube.com/watch?v=VfLpdsELJfU','https://www.youtube.com/watch?v=K0PuS391dsI','https://www.youtube.com/watch?v=UA3FteJn9oc','https://www.youtube.com/watch?v=66YZEptO2Zo','https://www.youtube.com/watch?v=iSYIjjW--pE',
#'https://www.youtube.com/watch?v=5ZFfT347-j0','https://www.youtube.com/watch?v=vGOvU7de3DM','https://www.youtube.com/watch?v=AFXGZBdzf-s','https://www.youtube.com/watch?v=Fa9TCNpBPBg','https://www.youtube.com/watch?v=F5t4jpezDPI','https://www.youtube.com/watch?v=plesqDCozKg','https://www.youtube.com/watch?v=BplCjZ0HZLg','https://www.youtube.com/watch?v=YEneLXIAPAs','https://www.youtube.com/watch?v=qLWeE5wiiwY','https://www.youtube.com/watch?v=KD5wYlYHj_U','https://www.youtube.com/watch?v=jCasz8Nitlw','https://www.youtube.com/watch?v=_ke6TdV2Qj0','https://www.youtube.com/watch?v=LmrzXWsV910','https://www.youtube.com/watch?v=0DHpbYBrKPs','https://www.youtube.com/watch?v=_6qZlmLrMzM','https://www.youtube.com/watch?v=mleWEDCNh8s','https://www.youtube.com/watch?v=AhipgYwSzcU','https://www.youtube.com/watch?v=joChTd_bwKk'
#,'https://www.youtube.com/watch?v=Uvx7NcZ-SWY','https://www.youtube.com/watch?v=uH-SZgFtP3k','https://www.youtube.com/watch?v=DI-GL2v0d1Y','https://www.youtube.com/watch?v=QyeTkWTRrII','https://www.youtube.com/watch?v=iBgdNphFYO8','https://www.youtube.com/watch?v=2fcsPzC_ZuI','https://www.youtube.com/watch?v=5sG5lfIjVoc','https://www.youtube.com/watch?v=auER8X-0OgU','https://www.youtube.com/watch?v=NsmoKA4Fd8w','https://www.youtube.com/watch?v=ieO_uImbSA4','https://www.youtube.com/watch?v=nRIzyJWTv5U',
#'https://www.youtube.com/watch?v=T8IIqc4QG7g','https://www.youtube.com/watch?v=953YmmFivvc','https://www.youtube.com/watch?v=rUz0iSKTLf4','https://www.youtube.com/watch?v=Q1lILNGAKwU','https://www.youtube.com/watch?v=xmDpgnBZJW4','https://www.youtube.com/watch?v=qBjlp4RLeUA','https://www.youtube.com/watch?v=-2XItBbxSto','https://www.youtube.com/watch?v=g9as2CQPy7M','https://www.youtube.com/watch?v=5h0zV_8nNko','https://www.youtube.com/watch?v=pDp5EBpJrQY','https://www.youtube.com/watch?v=zBMxVfcbli4','https://www.youtube.com/watch?v=T9t51XoCR3g','https://www.youtube.com/watch?v=HMJJ35BZK_g','https://www.youtube.com/watch?v=O18mcC_wqwc','https://www.youtube.com/watch?v=bNSqjHLb6MU','https://www.youtube.com/watch?v=EnmwIi18p5Y'
#,'https://www.youtube.com/watch?v=pAwVXWqiyA0','https://www.youtube.com/watch?v=u2tEDpjOxdg','https://www.youtube.com/watch?v=ioiS0I2WqRQ','https://www.youtube.com/watch?v=hwlroASv9ws','https://www.youtube.com/watch?v=ezXOQ2cNI74','https://www.youtube.com/watch?v=QLnbJ9Wn68o','https://www.youtube.com/watch?v=URDW6aaO3Ro','https://www.youtube.com/watch?v=Jrrf-Uy2n4I','https://www.youtube.com/watch?v=Rds8pdRCI-U','https://www.youtube.com/watch?v=sEzVn2A1lOA','https://www.youtube.com/watch?v=FRU_HZWSSlM','https://www.youtube.com/watch?v=2FjixP1nMVg','https://www.youtube.com/watch?v=bHGhoXzG4EU','https://www.youtube.com/watch?v=dUzvNkQ9qsI','https://www.youtube.com/watch?v=Rhvh13v1VzQ&','https://www.youtube.com/watch?v=LtUH-Oj2qUo','https://www.youtube.com/watch?v=5ETHy1DkhBk','https://www.youtube.com/watch?v=L0AGrHOtbj4','https://www.youtube.com/watch?v=eL7gDSLDCgU','https://www.youtube.com/watch?v=9mDh42chIhQ'
#,'https://www.youtube.com/watch?v=n3r1MUd_D0M','https://www.youtube.com/watch?v=_tUNvawSSRM','https://www.youtube.com/watch?v=H3e4eXuC51s','https://www.youtube.com/watch?v=SjJKGcsbESo','https://www.youtube.com/watch?v=4dZ-GbdtS0U','https://www.youtube.com/watch?v=y_vcOpBdc1c','https://www.youtube.com/watch?v=fsXzduunBOs','https://www.youtube.com/watch?v=y9yajPL82wQ','https://www.youtube.com/watch?v=nz35ofz6Zxo','https://www.youtube.com/watch?v=P60KKsgyWwk','https://www.youtube.com/watch?v=8XR5ZKAZzwE','https://www.youtube.com/watch?v=gHTBMTs2FZY','https://www.youtube.com/watch?v=4gwAw3yHBZA','https://www.youtube.com/watch?v=dFOCdTokhzw','https://www.youtube.com/watch?v=oa25s_6Sfn0']

links = ['https://www.youtube.com/watch?v=9hJo_fx_STs','https://www.youtube.com/watch?v=AocY41hgNd4']

citates = ["Извините за опоздание, я заблудился на дороге под названием жизнь","Не бывает безвыходных ситуаций. Бывают ситуации, выход из которых тебя не устраивает","Я бы с удовольствием пригласил тебя зайти и выпить, но боюсь, что ты согласишься","Если бы мы встретились в другом месте и в другое время, мы бы стали друзьями","Никогда не сдаваться... Встать, когда все рухнуло — вот настоящая сила","Если отказаться от надежды спасти друга означает поумнеть, то я лучше навсегда останусь глупцом","Быть другим — не значит быть лучше. Иначе говоря, гвоздь, который торчит, забьют первым","Ты думаешь, что ты понял это, хотя на самом деле всего лишь думаешь, что ты понял то, о чем ты думаешь","Ничего не понимаю! Ладно, притворюсь, что понял","Очень просто сложить руки и сказать «Это невозможно»",
"Только начнешь работать, обязательно кто-нибудь разбудит","На ошибках учатся, после ошибок лечатся","Никогда не спорь с идиотом. Сначала он опустит тебя до своего уровня, а потом задавит опытом","Человек понимает ценность чего-либо только после потери этого","Сколько бы иллюзий ты ни сочинил, они никогда не заполнят дыру в твоём сердце","Знание и понимание неоднозначны","Сильнейшая боль — это когда никто не нуждается в тебе","Да, в мире шиноби те, кто не следуют приказам, считаются мусором. Но те, кто предают друзей, хуже мусора","когда у человека есть что-то, что он хочет защитить... лишь тогда сможет он стать по-настоящему сильным","Даже птицы в клетке, поумнев, пытаются открыть её своим клювом. И они не сдаются, ведь они хотят летать","Ты не идеален, но, делая ошибки, ты учишься на них. Мне кажется, настоящая сила заключается именно в этом","Впереди у нас ещё целая жизнь, а некоторые уже говорят, что у них нет времени","Домом можно называть то место, где о тебе кто-то думает","Все люди делятся на гениев и тех, кто всего добивается своим трудом",
"Нелегко обрести друга. Еще труднее потерять врага","Не думаю, что в этом мире есть что-либо совершенное само по себе. Вот почему мы тянемся к тем, кто дополняет нас","Сила веры в себя. Этой силе подвластно изменить судьбу","Это нормально, если ты плачешь, когда счастлив","Перестанешь существовать, когда исчезнешь из мыслей других","Мало сказать глупость, надо чтобы в нее поверили","Именно любовь, ненависть, счастье, страх, одиночество... все эти чувства объединяют людей воедино","Боль — это боль, как ее не назови. Разве она становится слабее от того, что ты думаешь, что она нереальна","Разве быть сильным – единственная причина жить? Признание людей можно заслужить не только силой","У тебя была мечта стать Хокаге","Если у тебя есть время бегать за мной, может, стоит больше тренироваться... А, Наруто?","азве может тот, кто не спас товарища стать Хокаге?... Ведь так, Саске?","Не того признают, кто стал Хокаге. А Хокаге становится тот, кого признают. Не забывай о своих друзьях","Выходит, ты все-таки превзошёл предыдущих Хокаге"]


def inputbox(title, message, button_text):
    root = tkinter.Tk()
    root.title(title)
    root.resizable(False, False)

    label = tkinter.Label(text=message)
    label.pack()

    text = ''
    def on_return(e=None):
        nonlocal text
        text = textbox.get()
        root.destroy()

    textbox = tkinter.Entry(width=40)
    textbox.bind('<Return>', on_return)
    textbox.pack()
    textbox.focus_set()

    button = tkinter.Button(text=button_text, command=on_return)
    button.pack()

    root.mainloop()

    return text


def main():
    mail = inputbox("BDLYCHIIPREDMET", "Mail", "ok")
    password = inputbox("BDLYCHIIPREDMET", "Password", "ok")
    ii = int(inputbox("BDLYCHIIPREDMET", "Nomer start rolika", "ok"))
    f = open('text.txt', 'w')
    driver = webdriver.Chrome()
    driver.get("https://accounts.google.com/o/oauth2/auth?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile+email&redirect_uri=https%3a%2f%2fstackauth.com%2fauth%2foauth2%2fgoogle&state=%7b%22sid%22%3a609%2c%22st%22%3a%2259%3a3%3abbc%2c16%3a86d07744fda69598%2c10%3a1599484786%2c16%3a60c4e5d1345ba611%2c435afdebe958e0eb4b0c2ae402169d861a91711cb5f5aade5ea87fac1e75e916%22%2c%22cdl%22%3anull%2c%22cid%22%3a%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2c%22k%22%3a%22Google%22%2c%22ses%22%3a%226f22d85a2dd546fe9512f8360efad577%22%7d&response_type=code")
    login = driver.find_element_by_xpath('//*[@id="identifierId"]')
    login.send_keys(mail)
    login.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    psswrd = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    psswrd.send_keys(password)
    psswrd.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    ii = ii - 1
    while ii < 2:
        f = open('text.txt', 'w')
        driver.get(links[ii])
        f.write(str(ii)+'\t')
        f.write(str(links[ii]))
        f.write('\n')
        driver.implicitly_wait(10) #прогрузка

        first_num = driver.find_element_by_class_name("ytp-time-current").text
        end_num = driver.find_element_by_class_name("ytp-time-duration").text
        f1 = first_num.split(":")
        f2 = end_num.split(":")
        print(f1, '/', f2)
        try:
            ff = int(f1[0]) * 60 + int(f1[1])
            fff = int(f2[0]) * 3600 + int(f2[1]) * 60 + int(f2[2])
            video_len = int(fff) - int(ff) - 10
            print(ff, '2', fff)
        except:
            ff = int(f1[0]) * 60 + int(f1[1])
            fff = int(f2[0]) * 60 + int(f2[1])
            print(ff, '1', fff)
            video_len = int(fff) - int(ff) - 10        #Вычисление длительности ролика (раньше было 20, нужно проверить шоб смотрел до конца.

        target = driver.find_element_by_xpath('//*[@id="more"]/yt-formatted-string')
        target.location_once_scrolled_into_view
        driver.implicitly_wait(10)        # cкроллинг вниз и прогрузка

        comment = driver.find_element_by_xpath('//*[@id="simplebox-placeholder"]')
        comment.click()-00000000000000000000000
        comment = driver.find_element_by_xpath('//*[@id="contenteditable-root"]')
        comment.send_keys(citates[random.randint(0,35)]) #Комментирование
        comment.send_keys(Keys.CONTROL + Keys.ENTER)
        time.sleep(video_len)               #Сон до конца ролика
        #time.sleep(10)
        red = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[1]/ytd-comment-renderer/div[1]/div[3]/ytd-menu-renderer/yt-icon-button/button/yt-icon')
        red.click()
        #red = driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/iron-dropdown/div/ytd-menu-popup-renderer/paper-listbox/ytd-menu-navigation-item-renderer[1]/a')
        red = driver.find_element_by_xpath('//*[@id="items"]/ytd-menu-navigation-item-renderer[1]/a/paper-item/yt-formatted-string')
        red.click()
        red = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[1]/ytd-comment-renderer/div[2]/ytd-comment-dialog-renderer/ytd-commentbox/div/div[2]/paper-input-container/div[2]/div/div[1]/ytd-emoji-input/yt-user-mention-autosuggest-input/yt-formatted-string/div')
        red.click()
        red.send_keys(Keys.CONTROL + Keys.ENTER)
        ii+=1


main()