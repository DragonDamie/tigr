#pipx run streamlit run /Users/anazaharova/Desktop/диплом/ТИГР_ФИНАЛ/tigr_5-8.py
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
def create_task5_html(prime_text, stimulus_text, hint):
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

# Основной код для задания 5
if st.session_state.current_step == 1:  # Инструкция
    st.header("Задание 5")
    
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
            <p>Над этим предложением вы увидите предложение-образец, опираясь на которое вам нужно будет заполнить пропуск.</p>
            <p>Из двух вариантов ответа вам нужно будет выбрать подходящий и нажать на него.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Начать тренировку"):
        st.session_state.current_step = 2
        st.session_state.task5_test_index = 0  # Начинаем с первого теста
        st.rerun()

elif st.session_state.current_step == 2:  # Тренировочные стимулы
    index = st.session_state.task5_test_index
    if index < len(task_data.gender_easy_test):  # Три тренировочных стимула
        st.header("Тренировка задания 5")
        st.write("Выберите правильный глагол с опорой на предложение-образец")
        task5_test = task_data.gender_easy_test[index]

        # Создаем HTML с новым дизайном
        html = create_task5_html(task5_test["prime_text"], task5_test["stimulus_text"], task5_test["hint"])
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
        for answer in task5_test["answers"]:
            if st.button(answer, key=f"q5_test_{index}_{answer}"):
                choice = answer

        if choice is not None:
            st.session_state.task5_test_index += 1  # Переход к следующему стимулу
            st.rerun()

    else:
        st.header("Тренировка задания 5 завершена!")
        if st.button("Перейти к заданию 5"):
            st.session_state.current_step = 3
            st.rerun()

elif st.session_state.current_step == 3:  # Основная часть задания 5
    index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 5")])
    answ_co = len(task_data.gender_easy)
    if index < answ_co:
        st.header("Задание 5")
        st.write("Выберите правильный глагол с опорой на предложение-образец")
        task5 = task_data.gender_easy[index]

        # Создаем HTML с новым дизайном
        html = create_task5_html(task5["prime_text"], task5["stimulus_text"], task5["hint"])
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
        for answer in task5["answers"]:
            if st.button(answer, key=f"q5_{index}_{answer}"):
                choice = answer

        if choice is not None:
            st.session_state.responses[f"Задание 5: {task5['stimulus_text']}"] = choice
            st.rerun()

        func.skip_task(st, index, answ_co, "Задание 5: ") #пропуск задания

    else:
        st.header("Задание 5 завершено!")
        if st.button("Перейти к следующему заданию"):
            st.session_state.current_step = 4
            st.rerun()

############################################################################################################################################
# Основной код для задания 6
if st.session_state.current_step == 4:  # Инструкция
    st.header("Задание 6")

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
            <p>Вы увидите три рисунка.</p>
            <p>Под этими рисунками будут расположены кнопки, при нажатии на которые появятся три варианта ответа.</p>
            <p>Среди этих вариантов ответа вам нужно будет выбрать тот, который точнее всего опишет рисунок.</p>
            <p>Это нужно будет сделать для всех рисунков.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Начать тренировку"):
        st.session_state.current_step = 5
        st.session_state.task6_test_index = 0  # Начинаем с первого теста
        st.rerun()

elif st.session_state.current_step == 5:  # Тренировочные стимулы
    index = st.session_state.task6_test_index
    if index < 3:  # Три тренировочных стимула
        st.header("Тренировка задания 6")
        st.write("Соедините картинки с правильной формой глагола")
        
        # Тренировочные данные
        image_names = task_data.gender_middle_minus_test[index]
        verbs = task_data.gender_middle_minus_opt_test[index]
        index_answrs = []  # Ответы для текущего индекса

        st.write("Картинки:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(f"images/{image_names[0]}", use_container_width=True, width=300)
            index_answrs.append(st.selectbox("Выберите глагол:", verbs, key=f"verb_1_{index}"))
        with col2:
            st.image(f"images/{image_names[1]}", use_container_width=True, width=300)
            index_answrs.append(st.selectbox("Выберите глагол:", verbs, key=f"verb_2_{index}"))
        with col3:
            st.image(f"images/{image_names[2]}", use_container_width=True, width=300)
            index_answrs.append(st.selectbox("Выберите глагол:", verbs, key=f"verb_3_{index}"))

        if st.button("Далее"):
            # Проверяем, выбраны ли все глаголы
            if len(index_answrs) == 3 and not any(item == "" for item in index_answrs):
                st.session_state.task6_test_index += 1
                st.rerun()  # Обновляем страницу для следующего стимуля

    else:
        st.header("Тренировка задания 6 завершена!")
        if st.button("Перейти к заданию 6"):
            st.session_state.current_step = 6
            st.rerun()

elif st.session_state.current_step == 6:  # Основная часть задания 6
    index = int(len([k for k in st.session_state.responses.keys() if k.startswith("Задание 6")]) / 3)  # делим на 3, так как 3 варианта ответа
    answ_co = len(task_data.gender_middle_minus)
    if index < answ_co:
        st.header("Задание 6")
        st.write("Соедините картинки с правильной формой глагола")
        
        # Основные данные
        image_names = task_data.gender_middle_minus[index]
        verbs = task_data.gender_middle_minus_opt[index]
        index_answrs = []  # Ответы для текущего индекса

        st.write("Картинки:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(f"images/{image_names[0]}", use_container_width=True, width=300)
            index_answrs.append(st.selectbox("Выберите глагол:", verbs, key=f"verb_1_{index}"))
        with col2:
            st.image(f"images/{image_names[1]}", use_container_width=True, width=300)
            index_answrs.append(st.selectbox("Выберите глагол:", verbs, key=f"verb_2_{index}"))
        with col3:
            st.image(f"images/{image_names[2]}", use_container_width=True, width=300)
            index_answrs.append(st.selectbox("Выберите глагол:", verbs, key=f"verb_3_{index}"))

        if st.button("Далее"):
            # Проверяем, выбраны ли все глаголы
            if len(index_answrs) == 3 and not any(item == "" for item in index_answrs):
                # Сохраняем ответы
                for i, subject in enumerate(index_answrs):
                    st.session_state.responses[f"Задание 6: Картина {image_names[i]}"] = index_answrs[i]
                st.rerun()  # Обновляем страницу для следующего стимуля

        func.skip_task(st, index * 3, answ_co * 3, "Задание 6: ") #пропуск задания

    else:
        st.header("Задание 6 завершено!")
        if st.button("Перейти к следующему заданию"):
            st.session_state.current_step = 7
            st.rerun()

############################################################################################################################################
# Функция для создания HTML с новым дизайном для задания 7
def create_task7_html(stimulus_text):
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
    </style>
    <div class="container">
        <div class="task">
            {stimulus_text}
        </div>
    </div>
    """
    return html

# Основной код для задания 7
if st.session_state.current_step == 7:
    st.header("Задание 7")

    st.markdown(
        """
        <style>
            .custom-text {
                font-size: 18px;
                line-height: 1.6;
                margin-bottom: 20px;
            }
        </style>
        <div class="custom-text">
            <p>Вы увидите предложение с пропущенным словом.</p>
            <p>Ниже будут предложены 3 варианта ответа.</p>
            <p>Из этих вариантов ответа вам нужно будет выбрать подходящий и нажать на него.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Начать тренировку задания 7"):
        st.session_state.current_step = 8
        st.session_state.task7_test_index = 0  # Сбрасываем индекс тестовых стимулов
        st.rerun()

elif st.session_state.current_step == 8:
    # Получаем текущий индекс тестового стимула
    index = st.session_state.task7_test_index
    
    if index < len(task_data.gender_middle_plus_test):
        st.header("Тренировка задания 7")
        st.write("Выберите правильную форму глагола")
        # Отображаем тестовый стимул
        html = create_task7_html(task_data.gender_middle_plus_test[index])
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
                    text-align: left;
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
        
        # Отображаем варианты ответов
        choice = None
        for answer in task_data.gender_middle_plus_opt_test[index]:
            if st.button(answer, key=f"q7t_{index}_{answer}"):
                choice = answer
        
        # Если ответ выбран, переходим к следующему тестовому стимулу
        if choice is not None:
            st.session_state.task7_test_index += 1
            st.rerun()
    else:
        st.header("Тренировка задания 7 завершена!")
        if st.button("Перейти к заданию 7"):
            st.session_state.current_step = 9
            st.rerun()

elif st.session_state.current_step == 9:
    index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 7")])    
    total_questions = len(task_data.gender_middle_plus)
    
    if index < total_questions:
        st.header("Задание 7")
        st.write("Выберите правильную форму глагола")
        # Отображаем основной стимул
        html = create_task7_html(task_data.gender_middle_plus[index])
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
                    text-align: left;
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
        
        # Варианты ответов
        choice = None
        for answer in task_data.gender_middle_plus_opt[index]:
            if st.button(answer, key=f"q7_{index}_{answer}"):
                choice = answer
        
        if choice is not None:
            # Сохраняем ответ
            st.session_state.responses[f"Задание 7: {task_data.gender_middle_plus[index]}"] = choice
            st.rerun()
        
        # Кнопка пропуска задания
        func.skip_task(st, index, total_questions, "Задание 7: ")
    
    else:
        st.header("Задание 7 завершено!")
        if st.button("Перейти к следующему заданию"):
            st.session_state.current_step = 10
            st.rerun()
############################################################################################################################################
# Функция для создания HTML с новым дизайном для задания 8
def create_task8_html(stimulus_text):
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

# Основной код для задания 8
if st.session_state.current_step == 10:
    st.header("Задание 8")
    
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
            <p>Вы увидите предложение в с пропущенным словом.</p>
            <p>В конце предложения будет написано одно слово в скобках.</p>
            <p>Это слово нужно вставить на место пропуска, изменив его форму так, чтобы предложение после его добавления было грамматически верным.</p>
            <p>Слово должно быть в прошедшем времени.</p>
            <p>Вам нужно будет напечатать это слово в окошке для ввода ответа.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Начать тренировку"):
        st.session_state.current_step = 11
        st.session_state.task8_test_index = 0
        st.rerun()

elif st.session_state.current_step == 11:  # Страница с тренировочными стимулами (3 стимула)
    index = st.session_state.task8_test_index
    
    if index < 3:  # Тренировочные стимулы (3 стимула)
        st.header("Тренировка задания 8")
        # Создаем HTML с тренировочным стимулом
        html = create_task8_html(task_data.gender_complex_test[index])  
        st.components.v1.html(html, height=150)

        # Поле для ввода ответа
        answer = st.text_input(
            f"Напечатайте пропущенное слово (в скобках) в подходящей форме прошедшего времени",
            key=f"q8_test_{index}"
        )

        if st.button("Далее") and answer:
            st.session_state.task8_test_index += 1
            st.rerun()
    
    else:  # После тренировки
        st.header("Тренировка задания 8 завершена!")
        if st.button("Перейти к основному заданию 8"):
            st.session_state.current_step = 12
            st.rerun()

elif st.session_state.current_step == 12:  # Задание 8 (ввод ответа)
    index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 8")])
    answ_co = len(task_data.gender_complex)
    if index < answ_co:
        st.header("Задание 8")
        # Создаем HTML с новым дизайном
        html = create_task8_html(task_data.gender_complex[index])
        st.components.v1.html(html, height=150)

        # Поле для ввода ответа
        answer = st.text_input(
            "Напечатайте пропущенное слово (в скобках) в подходящей форме прошедшего времени",
            key=f"q8_{index}"
        )

        if st.button("Далее") and answer:
            st.session_state.responses[f"Задание 8: {task_data.gender_complex[index]}"] = answer
            st.rerun()

        func.skip_task(st, index, answ_co, "Задание 8: ") #пропуск задания
    else:
        st.header("Задание 8 завершено!")
        
        func.save_result(st)
