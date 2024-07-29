from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import random

    
class ActionGreet(Action):
    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        language = tracker.get_slot("language")
        if language == "ru":
            dispatcher.utter_message(text="Привет! Здесь ты можешь найти подборку важной информации для комфортного начала жизни на Кипре!")
        if language == "en":
            dispatcher.utter_message(text="Hi there! 🖐 Here you can find a selection of important information for a comfortable start to life in Cyprus!")
        return [SlotSet("language", language)]
    
class ActionGreetSecond(Action):
    def name(self):
        return "action_greet_second"

    def run(self, dispatcher, tracker, domain):
        buttons = [
            {"title": "Документы Documents", "payload": "/section1"},
            {"title": "Set up your company", "payload": "/section2"},
            {"title": "Taxation", "payload": "/section3"}
        ]
                
        language = tracker.get_slot("language")
        if language == "ru":
            follow_up_messages = [
                "Напиши свой вопрос или выбери один из разделов.",
                "Кликни на нужный раздел или напиши вопрос.",
                "Выбери одну из кнопок или задай свой вопрос."]
            dispatcher.utter_message(text=random.choice(follow_up_messages), buttons=buttons)
        if language == "en":
            follow_up_messages = [
                "Write your question or choose one of the sections.",
                "Click on the apropriate section or write a question.",
                "Choose one of the buttons or ask your question."]
            dispatcher.utter_message(text=random.choice(follow_up_messages), buttons=buttons)
            
        return [SlotSet("language", language)]
 
class ActionRandomGreeting(Action):
    def name(self):
        return "action_random_greeting"

    def run(self, dispatcher, tracker, domain):
        language = tracker.get_slot("language")
        if language == 'ru':
            follow_up_messages = ["Привет!🖐", "Здравствуй!🖐"]
            dispatcher.utter_message(text=random.choice(follow_up_messages))
        if language == 'en':
            follow_up_messages = ["Hello!🖐"]
            dispatcher.utter_message(text=random.choice(follow_up_messages))

        return [SlotSet("language", language)]

class ActionHelp(Action):
    def name(self):
        return "action_help"
    
    def run(self, dispatcher, tracker, domain):
        language = tracker.get_slot("language")
        if language == "ru":
            dispatcher.utter_message(text="Я могу предоставить тебе полезную информацию для жизни на Кипре! Выбери один из разделов, чтобы начать или напиши свой вопрос:")
        if language == "en":
            dispatcher.utter_message(text="I can provide you with userulinformation for life in Syprus! Choose one of the sections as get started or write your own question:")

        return [SlotSet("language", language)]

class ActionNoMatch(Action):
    def name(self):
        return "action_no_match"

    def run(self, dispatcher, tracker, domain):
        language = tracker.get_slot("language")
        if language == "ru":
            follow_up_messages = [
                "К сожалению, не получилось распознать твой запрос. Попробуй сформулировать по другому.",
                "Не совсем поняли твой запрос.Напиши его по-другому, пожалуйста."]
            dispatcher.utter_message(text=random.choice(follow_up_messages))
        if language == "en":
            follow_up_messages = [
                "Unfortunately, I wasn't unable to understand your request. Try to phrase it differently.",
                "I didn't quite understand your request. Write it differently, please."]
            dispatcher.utter_message(text=random.choice(follow_up_messages))
        return [SlotSet("language", language)]
    
class ActionThanks(Action):
    def name(self):
        return "action_thanks"

    def run(self, dispatcher, tracker, domain):
        language = tracker.get_slot("language")
        if language == "ru":
            follow_up_messages_1 = [
                "Пожалуйста!",
                "Обращайтесь!"]
            dispatcher.utter_message(text=random.choice(follow_up_messages_1))
            follow_up_messages_2 = [
                "Я всегда здесь, если захочешь узнать что нибудь еще.",
                "Я тут, если хочешь прочитать другую информацию."]
            dispatcher.utter_message(text=random.choice(follow_up_messages_2))
        if language == "en":
            follow_up_messages_1 = [
                "You are welcome!",
                "Get in touch!"]
            dispatcher.utter_message(text=random.choice(follow_up_messages_1))
            follow_up_messages_2 = [
                "I'm always here if you want to know anything else.",
                "I'm here if you want to read more information."]
            dispatcher.utter_message(text=random.choice(follow_up_messages_2))
        return [SlotSet("language", language)]
    
class ActionDoc(Action):
    def name(self):
        return "action_doc"

    def run(self, dispatcher, tracker, domain):
        buttons = [
            {"title": "Визы для въезда / Visas for entry", "payload": "/section4"},
            {"title": "Справка о несудимости / Police clearance certitlicate", "payload": "/section5"},
            {"title": "Перевод документов / Translation of documents", "payload": "/section6"},
            {"title": "Другой вопрос / Another question", "payload": "/section7"}
        ]

        language = tracker.get_slot("language")
        if language == "ru":
            message = ("Для релокации на Кипр требуется собрать пакет документов. "
                       "Список документов зависит от типа ВНЖ, который тебе нужен. "
                       "Тут есть краткая информация и ссылки на полезные ресурсы.")
            follow_up_messages = [
                "Нажми на кнопку и узнай подробнее:", 
                "Чтобы прочитать информацию, нажми на одну из кнопок:", 
                "Выбери кнопку и узнай подробности:"
            ]
        if language == "en":
            message = ("For relocation to Cyprus, you need to collect a package of documents. "
                       "The list of documents depends on the type of residence permit you need. "
                       "There is a summary and links to useful resources.")
            follow_up_messages = [
                "Click the button and find out more:", 
                "To read the information, click on one of the buttons:", 
                "Select the button and find out the details:"
            ]

        dispatcher.utter_message(text=message)
        dispatcher.utter_message(text=random.choice(follow_up_messages), buttons=buttons)
        return [SlotSet("language", language)]
    
class ActionDoc_Path1(Action):
    def name(self):
        return "action_doc_path1"

    def run(self, dispatcher, tracker, domain):
        buttons = [
            {"title": "Назад / Back", "payload": "/section8"},
            {"title": "Спасибо / Thanks", "payload": "/section9"}
        ]

        language = tracker.get_slot("language")
        if language == "ru":
            follow_up_message = ("""\n Для граждан стран Евросоюза и владельцев ВНЖ этих стран не нужна виза для въезда на Кипр.
                                    \n Граждане третьих стран могут въехать на Кипр по Шенгенской визе или оформив национальную визу Кипра.
                                    \n Чтобы найти полную информацию по визам и правилам пребывания на Кипре, вы можете перейти на сайт Миграционного департамента:
                                    \n http://www.moi.gov.cy/moi/crmd/crmd.nsf/home.en/homecnapenform#""")
        if language == "en":
            follow_up_message = ("""\n Citizens of EU countries and holders of residence permits of these countries don't need a visa to enter Cyprus.
                                    \n Third-country nationals can enter Cyprus with a Schengen visa or with a Cypriot national visa.
                                    \n To find complete information about visas and rules for staying in Cyprus, you can check the website of the Migration Department:
                                    \n http://www.moi.gov.cy/moi/crmd/crmd.nsf/home.en/homecnapenform#""")

        dispatcher.utter_message(text=follow_up_message, buttons=buttons)
        return [SlotSet("language", language)]
    
class ActionDoc_Path1_2(Action):
    def name(self):
        return "action_doc_path1_2"

    def run(self, dispatcher, tracker, domain):
        language = tracker.get_slot("language")
        if language == "ru":
            follow_up_messages = ["Хочешь узнать что-нибудь еще?",
                                  "Интересно узнать что-нибудь еще?", 
                                  "Остались еще вопросы?"]
            dispatcher.utter_message(text=random.choice(follow_up_messages))
        if language == "en":
            follow_up_messages = ["Do you want to know something else?", 
                                  "Curious to know anything else?",
                                  "Do you have mare questions?"]
            dispatcher.utter_message(text=random.choice(follow_up_messages))
        return [SlotSet("language", language)]
    
class ActionDoc_Path2(Action):
    def name(self):
        return "action_doc_path2"

    def run(self, dispatcher, tracker, domain):
        buttons = [
            {"title": "Назад / Back", "payload": "/section8"},
            {"title": "Спасибо / Thanks", "payload": "/section9"}
        ]

        language = tracker.get_slot("language")
        if language == "ru":
            follow_up_message = ("""Справка о несудимости на Кипре
                                 \n Прожив на Кипре полгода и более, можно получить кипракую справку о несудимоси.
                                 \n Справка выдаётся в главном отделении полиции в Никосим по будням до 15:00.
                                 \n Для получения справки, необходимо заполнить и подписать заявление.
                                 \n Скачать форму
                                 \n Адрес: Cyprus Police Headquarters Nicosia 1478, Cyprus
                                 \n Телефон: +357 (22) 808944
                                 \n http:www.police.gov.cy
                                 \n При себе нужно иметь копии и оригиналы загранпаспорта и РіnkSlip.""")
        if language == "en":
            follow_up_message = ("""Police clearance certificate in Cyprus
                                 \n Having lived in Cyprus for six months or more, you can get a Cypriat certificate of good conduct.
                                 \n The certificate is issued at the main police station in Nicosia on weekdays until 15:00.
                                 \n To receive a certificate, you must fill out and sign an application.
                                 \n Download form
                                 \n Address: Cyprus Police Haadquarters Nicosia 1478, Cyprus
                                 \n Phone: +357 (22) 808944
                                 \n http:www.police.gov.cy
                                 \n You need to have copies and originals of your passport and PinkSlip with you.""")

        dispatcher.utter_message(text=follow_up_message, buttons=buttons)
        return [SlotSet("language", language)]
    
class ActionDoc_Path3(Action):
    def name(self):
        return "action_doc_path3"

    def run(self, dispatcher, tracker, domain):
        buttons = [
            {"title": "Назад / Back", "payload": "/section8"},
            {"title": "Спасибо / Thanks", "payload": "/section9"}
        ]

        language = tracker.get_slot("language")
        if language == "ru":
            follow_up_message = ("""Если вам нужно сделать перевод документов, вы можете посмотреть реестр официальных переводчиков на Кипре: https://www.pie.gov.sy/enregister-ofeworn-cranslators.html""")
        if language == "en":
            follow_up_message = ("""If you need to translate documents, you can find a certified translator in the registry: https://www.pie.gov.sy/enregister-ofeworn-cranslators.html""")

        dispatcher.utter_message(text=follow_up_message, buttons=buttons)
        return [SlotSet("language", language)]
    
class ActionDoc_Path4(Action):
    def name(self):
        return "action_doc_path4"

    def run(self, dispatcher, tracker, domain):
        buttons = [
            {"title": "Назад / Back", "payload": "/section8"},
            {"title": "Спасибо / Thanks", "payload": "/section9"}
        ]

        language = tracker.get_slot("language")
        if language == "ru":
            follow_up_message = ("Что вы хотите узнать?")
        if language == "en":
            follow_up_message = ("What do you want to know?")

        dispatcher.utter_message(text=follow_up_message, buttons=buttons)
        return [SlotSet("language", language)]

class ActionCompany_Path(Action):
    def name(self):
        return "action_doc_company"

    def run(self, dispatcher, tracker, domain):
        buttons = [
            {"title": "Типы компаний / Main types of companies", "payload": "/section10"},
            {"title": "Зарегистрировать компанию / How to register a company in Cyprus", "payload": "/section11"},
            {"title": "Обязательства и платежи / Obligations and payments (Fees)", "payload": "/section12"},
            {"title": "Другой вопрос / Another question", "payload": "/section13"}]

        language = tracker.get_slot("language")
        if language == "ru":
            follow_up_message = ("Здесь бы можете найти базовую информацию о том как откры-свой бизнес на Кипре.")
        if language == "en":
            follow_up_message = ("Here you can find basic information on starting your company in Cyprus.")

        dispatcher.utter_message(text=follow_up_message, buttons=buttons)
        return [SlotSet("language", language)]
    
class ActionCompany_Path2(Action):
    def name(self):
        return "action_doc_company2"

    def run(self, dispatcher, tracker, domain):

        language = tracker.get_slot("language")
        if language == "ru":
            follow_up_message = ("Вы выбрали тему: «Тема»")
        if language == "en":
            follow_up_message = ("Your topic: «Topic»")

        dispatcher.utter_message(text=follow_up_message)
        return [SlotSet("language", language)]
    
class ActionTax_Path(Action):
    def name(self):
        return "action_doc_tax"

    def run(self, dispatcher, tracker, domain):
        buttons = [
            {"title": "Стать налоговым резидентом Кипра / How to become a tax resident in Cyprus", "payload": "/section14"},
            {"title": "Калькулятор налогообложения / Tax calculator", "payload": "/section15"},
            {"title": "Индивидуальное налогообложение / Individual taxation", "payload": "/section16"},
            {"title": "Другой вопрос / Another question", "payload": "/section17"}]

        language = tracker.get_slot("language")
        if language == "ru":
            follow_up_message = ("Понимание того, как работает налогообложение очень важно при переезде в другую страну. Мы собрали общую информацию, которая поможет начать разбираться в вопросе.")
        if language == "en":
            follow_up_message = ("Understanding taxes is very important when you arrive in a new country. Here is the starting information for you.")

        dispatcher.utter_message(text=follow_up_message, buttons=buttons)
        return [SlotSet("language", language)]