#для запуска нажать пуск справа, потом в создавшуюся консоль написать 
#pipx run streamlit run /Users/anazaharova/Desktop/диплом/ТИГР_ФИНАЛ/tigr_1-4.py
import streamlit as st
from datetime import datetime
import os
import task_data
import func
#os.chdir(os.path.dirname(__file__))  # рабочая директория


# Инициализация состояния страницы
if "current_step" not in st.session_state:
    st.session_state.current_step = 0  

if "q1_index" not in st.session_state: #added
    st.session_state.q1_index = 0 #added

if "responses" not in st.session_state:
    st.session_state.responses = {}

st.title("ТИГР: тренируемся изучать грамматику")

if st.session_state.current_step == 0:
    st.header("Добро пожаловать в тест!")
    st.write("В этом тесте вам предстоит выполнить несколько заданий.")
    if st.button("Начать"):
        st.session_state.current_step = 1
        st.rerun()
############################################################################################################################################
# Функция для создания HTML с новым дизайном
def create_task1_html(prime_text, stimulus_text, hint):
    html = f"""
    <style>
        .container {{
            display: flex;
            flex-direction: column;
            align-items: flex-start; /* Выравниваем по левому краю */
            text-align: left; /* Текст по левому краю */
            font-size: 1.2em; /* Увеличиваем шрифт */
        }}
        .example {{
            border: 2px solid #ccc;
            background-color: #f0f0f0;
            padding: 15px;
            margin: 10px 0;
            color: #666; /* Серый цвет текста */
            width: 80%;
        }}
        .task {{
            border: 2px solid orange;
            background-color: #ffebcc;
            padding: 15px;
            margin: 10px 0;
            color: black; /* Черный цвет текста */
            width: 80%;
        }}
        .hint {{
            font-style: italic;
            color: #666; /* Серый цвет текста */
        }}
    </style>
    <div class="container">
        <div class="example">
            <strong>Образец:</strong> {prime_text}
        </div>
        <div class="task">
            {stimulus_text}
            <div class="hint">{hint}</div>
        </div>
    </div>
    """
    return html

####DEBUG####
# st.session_state.current_step = 16
#############

if st.session_state.current_step == 1:
    st.header("Задание 1")
    st.markdown(
        """
        <style>
            .custom-text {
                font-size: 18px;  /* Размер шрифта */
                line-height: 1.6;  /* Межстрочный интервал */
                margin-bottom: 20px;  /* Отступ снизу */
            }
        </style>
        <div class="custom-text">
            <p>Вы увидите предложение с пропущенным окончанием в одном слове.</p>
            <p>Над этим предложением вы увидите предложение-образец, опираясь на которое вам нужно будет заполнить пропуск.</p>
            <p>Из двух вариантов ответа вам нужно будет выбрать подходящий и нажать на него.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Начать тренировку"):
        st.session_state.current_step = 2
        st.session_state.training_index = 0
        st.rerun()
elif st.session_state.current_step == 2:
    training_data = task_data.person_easy_test
    index = st.session_state.training_index
    
    if index < len(training_data):
        st.header("Тренировка задания 1")
        st.write("Выберите правильное окончание с опорой на предложение-образец")
        task = training_data[index]
        html = create_task1_html(task["prime_text"], task["stimulus_text"], task["hint"])
        st.components.v1.html(html, height=300)
        # Стилизация кнопок
        st.markdown(
            """
            <style>
                .stButton > button {
                    background-color: #ffebcc;
                    border: 2px solid orange;
                    padding: 10px;
                    border-radius: 5px;
                    width: 80%;
                    text-align: left; /* Текст по левому краю */
                    cursor: pointer;
                    margin: 5px 0;
                    font-size: 1.2em;
                }
                .stButton > button:hover {
                    background-color: #ffd699;
                }

            </style>
            """,
            unsafe_allow_html=True,
        )
        choice = None
        for answer in task["answers"]:
            if st.button(answer, key=f"train_{index}_{answer}"):
                choice = answer
        
        if choice is not None:
            st.session_state.training_index += 1
            st.rerun()
    else:
        st.header("Тренировка задания 1 завершена!")
        if st.button("Перейти к заданию 1"):
            st.session_state.current_step = 3
            st.session_state.responses = {}
            st.rerun()

elif st.session_state.current_step == 3:
    index = len(st.session_state.responses)
    answ_co = len(task_data.person_easy)
    if index < answ_co:
        st.header("Задание 1")
        st.write("Выберите правильное окончание с опорой на предложение-образец")

        task = task_data.person_easy[index]

        # Создаем HTML с новым дизайном
        html = create_task1_html(task["prime_text"], task["stimulus_text"], task["hint"])
        st.components.v1.html(html, height=300)

        # Стилизация кнопок
        st.markdown(
            """
            <style>
                .stButton > button {
                    background-color: #ffebcc;
                    border: 2px solid orange;
                    padding: 10px;
                    border-radius: 5px;
                    width: 80%;
                    text-align: left; /* Текст по левому краю */
                    cursor: pointer;
                    margin: 5px 0;
                    font-size: 1.2em;
                }
                .stButton > button:hover {
                    background-color: #ffd699;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Варианты ответов в виде кнопок
        choice = None
        for answer in task["answers"]:
            if st.button(answer, key=f"q1_{index}_{answer}"):
                choice = answer

        if choice is not None:
            # st.session_state.responses[task['stimulus_text']] = choice
            st.session_state.responses[f"Задание 1: {task['stimulus_text']}"] = choice
            st.rerun()

        func.skip_task(st, index, answ_co, "Задание 1: ") #пропуск задания

    else:
        st.header("Задание 1 завершено!")
        if st.button("Перейти к следующему заданию"):
            st.session_state.current_step = 4
            st.rerun()
####DEBUG####
# st.session_state.current_step = 13
#############

############################################################################################################################################
# Функция для создания HTML с новым дизайном для задания 2
def create_task2_html(stimulus_text, hint_text):
    html = f"""
    <style>
        .container {{
            display: flex;
            flex-direction: column;
            align-items: flex-start; 
            text-align: left; 
            font-size: 1.2em; 
        }}
        .task {{
            border: 2px solid orange;
            background-color: #ffebcc;
            padding: 15px;
            margin: 10px 0;
            color: black; 
            width: 80%;
        }}
        .hint {{
            font-style: italic; 
            color: #666; 
            margin-top: 10px; 
        }}
    </style>
    <div class="container">
        <div class="task">
            {stimulus_text}
            <div class="hint">{hint_text}</div>
        </div>
    </div>
    """
    return html

if st.session_state.current_step == 4:
    st.header("Задание 2")
    
    # Используем st.markdown с HTML и CSS для стилизации текста
    st.markdown(
        """
        <style>
            .custom-text {
                font-size: 18px;  /* Размер шрифта */
                line-height: 1.6;  /* Межстрочный интервал */
                margin-bottom: 20px;  /* Отступ снизу */
            }
        </style>
        <div class="custom-text">
            <p>Вы увидите предложение с пропущенным словом.</p>
            <p>Ниже будут предложены 4 варианта ответа.</p>
            <p>Из этих вариантов ответа вам нужно будет выбрать подходящий и нажать на него.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Начать тренировку задания 2"):
        st.session_state.current_step = 5
        st.session_state.task2_test_index = 0
        st.rerun()

elif st.session_state.current_step == 5:
    index = st.session_state.task2_test_index
    
    if index < len(task_data.person_middle_minus_test):
        st.header("Тренировка задания 2")
        st.write("Выберите правильный глагол")
        
        html = create_task2_html(
            task_data.person_middle_minus_test[index],
            task_data.person_middle_minus_hint_test[index]
        )
        st.components.v1.html(html, height=150)
        # Стилизация кнопок
        st.markdown(
            """
            <style>
                .stButton > button {
                    background-color: #ffebcc;
                    border: 2px solid orange;
                    padding: 10px;
                    border-radius: 5px;
                    width: 80%;
                    text-align: left; /* Текст по левому краю */
                    cursor: pointer;
                    margin: 5px 0;
                    font-size: 1.2em;
                }
                .stButton > button:hover {
                    background-color: #ffd699;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        choice = None
        for answer in task_data.person_middle_minus_opt_test[index]:
            if st.button(answer, key=f"q2t_{index}_{answer}"):
                choice = answer

        if choice is not None:
            st.session_state.task2_test_index += 1
            st.rerun()
    else:
        st.header("Тренировка задания 2 завершена!")
        if st.button("Перейти к заданию 2"):
            st.session_state.current_step = 6
            st.rerun()

elif st.session_state.current_step == 6:
    index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 2")])    
    answ = task_data.person_middle_minus
    answ_co = len(answ)
    if index < answ_co:
        st.header("Задание 2")
        st.write("Выберите правильный глагол")
        # Создаем HTML с новым дизайном
        html = create_task2_html(
            answ[index],  # Основной текст
            task_data.person_middle_minus_hint[index]  # Подсказка
        )
        st.components.v1.html(html, height=150)

        # Стилизация кнопок
        st.markdown(
            """
            <style>
                .stButton > button {
                    background-color: #ffebcc;
                    border: 2px solid orange;
                    padding: 10px;
                    border-radius: 5px;
                    width: 80%;
                    text-align: left; /* Текст по левому краю */
                    cursor: pointer;
                    margin: 5px 0;
                    font-size: 1.2em;
                }
                .stButton > button:hover {
                    background-color: #ffd699;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Варианты ответов в виде кнопок
        choice = None
        for answer in task_data.person_middle_minus_opt[index]:
            if st.button(answer, key=f"q2_{index}_{answer}"):
                choice = answer

        if choice is not None:
            st.session_state.responses[f"Задание 2: {answ[index]}"] = choice
            st.rerun()

        func.skip_task(st, index, answ_co, "Задание 2: ") #пропуск задания

    else:
        st.header("Задание 2 завершено!")
        if st.button("Перейти к следующему заданию"):
            st.session_state.current_step = 7
            st.rerun()
############################################################################################################################################
elif st.session_state.current_step == 7:
    st.header("Задание 3")
    
    # Используем st.markdown с HTML и CSS для стилизации текста
    st.markdown(
        """
        <style>
            .custom-text {
                font-size: 18px;  /* Размер шрифта */
                line-height: 1.6;  /* Межстрочный интервал */
                margin-bottom: 20px;  /* Отступ снизу */
            }
        </style>
        <div class="custom-text">
            <p>Вы увидите 6 строк, в которых нужно будет сформировать правильные предложения.</p>
            <p>Вам будет предложено начало предложения.</p>
            <p>Вам нужно будет нажать на стрелку.</p>
            <p>После нажатия на нее вы увидите 6 возможных вариантов ответа.</p>
            <p>Вам нужно будет из этих вариантов выбрать тот, который будет правильно завершать начало предложения.</p>
            <p>Сделать это нужно будет для всех предложений.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Начать тренировку"):
        st.session_state.current_step = 8
        st.session_state.task3_test_index = 0  # Инициализация индекса тренировки
        st.rerun()

elif st.session_state.current_step == 8:  
    # Тренировочная часть
    index = st.session_state.task3_test_index

    if index < len(task_data.person_middle_plus_test):
        st.header("Тренировка задания 3")
        st.write("Соедините подлежащее с правильной формой глагола")

        subjects = task_data.person_middle_plus_test[index]["subjects"]
        verbs = task_data.person_middle_plus_test[index]["verbs"]

        selected_verbs = [
            st.selectbox(f"{subject}:", [""] + verbs, key=f"test_verb_{i}_{index}") 
            for i, subject in enumerate(subjects)
        ]

        if st.button("Далее"):
            if all(selected_verbs):
                st.session_state.task3_test_index += 1
                st.rerun()
            else:
                st.warning("Выберите все глаголы перед переходом.")
    else:
        st.header("Тренировка задания 3 завершена!")
        if st.button("Перейти к заданию 3"):
            st.session_state.current_step = 9
            st.rerun()

elif st.session_state.current_step == 9:  
    # Используем task3_index для отслеживания текущего вопроса в задании 3
    index = int(len([k for k in st.session_state.responses.keys() if k.startswith("Задание 3")]) / 6)
    answ_co = len(task_data.person_middle_plus)
    if index < answ_co:
        st.header("Задание 3")
        st.write("Соедините подлежащее с правильной формой глагола")

        subjects = task_data.person_middle_plus[index]["subjects"]
        verbs = task_data.person_middle_plus[index]["verbs"]

        selected_verbs = [
            st.selectbox(f"{subject}:", [""] + verbs, key=f"verb_{i}_{index}") 
            for i, subject in enumerate(subjects)
        ]

        if st.button("Далее"):
            # Проверяем, выбраны ли все глаголы
            if all(selected_verbs):
                # Сохраняем ответы в формате "стимул-ответ" с префиксом "Задание 3:"
                for i, subject in enumerate(subjects):
                    st.session_state.responses[f"Задание 3 (итерация {index}): {subject}"] = selected_verbs[i]
                st.rerun()  # Обновляем страницу для следующего вопроса
            else:
                st.warning("Выберите все глаголы перед переходом.")

        func.skip_task(st, index * 6, answ_co * 6, "Задание 3: ") #пропуск задания
    else:
        st.header("Задание 3 завершено!")
        if st.button("Перейти к следующему заданию"):
            st.session_state.current_step = 10
            st.rerun()
############################################################################################################################################
# Функция для создания HTML с новым дизайном для задания 4
def create_task4_html(stimulus_text):
    html = f"""
    <style>
        .container {{
            display: flex;
            flex-direction: column;
            align-items: flex-start; /* Выравниваем по левому краю */
            text-align: left; /* Текст по левому краю */
            font-size: 1.2em; /* Увеличиваем шрифт */
        }}
        .task {{
            border: 2px solid orange;
            background-color: #ffebcc;
            padding: 15px;
            margin: 10px 0;
            color: black; /* Черный цвет текста */
            width: 80%;
        }}
    </style>
    <div class="container">
        <div class="task">
            {stimulus_text}
        </div>
    </div>
    """
    return html
# Основной код для задания 4
if st.session_state.current_step == 10:  # Страница с инструкциями
    st.header("Задание 4")
    
    # Используем st.markdown с HTML и CSS для стилизации текста
    st.markdown(
        """
        <style>
            .custom-text {
                font-size: 18px;  /* Размер шрифта */
                line-height: 1.6;  /* Межстрочный интервал */
                margin-bottom: 20px;  /* Отступ снизу */
            }
        </style>
        <div class="custom-text">
            <p>Вы увидите предложение с пропущенным словом.</p>
            <p>В конце предложения будет написано одно слово в скобках.</p>
            <p>Это слово нужно вставить на место пропуска, изменив его форму так, чтобы предложение после его добавления было грамматически верным.</p>
            <p>Слово должно быть в настоящем времени.</p>
            <p>Вам нужно будет напечатать это слово в окошке для ввода ответа.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Начать тренировку"):
        st.session_state.current_step = 11
        st.session_state.task4_test_index = 0
        st.rerun()

elif st.session_state.current_step == 11:  # Страница с тренировочными стимулами (3 стимула)
    index = st.session_state.task4_test_index
    
    if index < 3:  # Тренировочные стимулы (3 стимула)
        st.header("Тренировка задания 4")
        # Создаем HTML с тренировочным стимулом
        html = create_task4_html(task_data.person_complex_test[index])  # используем переменную person_complex_test для стимулов
        st.components.v1.html(html, height=150)

        # Поле для ввода ответа
        answer = st.text_input(
            f"Введите пропущенное слово (в скобках) в подходящей форме настоящего времени",
            key=f"q4_test_{index}"
        )

        if st.button("Далее") and answer:
            st.session_state.task4_test_index += 1
            st.rerun()
    
    else:  # После тренировки
        st.header("Тренировка задания 4 завершена!")
        if st.button("Перейти к заданию 4"):
            st.session_state.current_step = 12
            st.rerun()

elif st.session_state.current_step == 12:  # Основная часть задания 4 (как было в изначальном коде)
    index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 4")])
    answ_co = len(task_data.person_complex)
    if index < answ_co:
        st.header("Задание 4")
        # Создаем HTML с новым дизайном
        html = create_task4_html(task_data.person_complex[index])
        st.components.v1.html(html, height=150)

        # Поле для ввода ответа
        answer = st.text_input(
            "Напечатайте пропущенное слово (в скобках) в подходящей форме настоящего времени",
            key=f"q4_{index}"
        )

        if st.button("Далее") and answer:
            st.session_state.responses[f"Задание 4: {task_data.person_complex[index]}"] = answer
            st.rerun()
        
        func.skip_task(st, index, answ_co, "Задание 4: ") #пропуск задания
    else:
        st.header("Задание 4 завершено!")
        func.save_result(st)
