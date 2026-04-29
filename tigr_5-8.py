#pipx run streamlit run /Users/anazaharova/Desktop/диплом/ТИГР_ФИНАЛ/tigr_5-8.py
import streamlit as st
from datetime import datetime
import os
import task_data
import func
import base64
import streamlit.components.v1 as components
import hashlib
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
def create_task5_html(prime_text, stimulus_text, hint, audio_base64=None, audio_answers=None, answers=None):
    
    answers_html = ""

    if answers and audio_answers:
        for i, (ans, audio) in enumerate(zip(answers, audio_answers)):
            answers_html += f"""
            <div style="
                position:relative;
                background-color:#ffebcc;
                border:2px solid orange;
                padding:15px;
                width:80%;
                margin:5px 0;
                font-size:1.2em;
            ">
                <span>{ans}</span>
                <button onclick="playAnswerAudio({i})"
                    style="
                        position:absolute;
                        top:8px;
                        right:8px;
                        font-size:18px;
                        border:none;
                        background:white;
                        border-radius:6px;
                        cursor:pointer;
                        padding:3px 6px;
                    ">
                    🔊
                </button>
                <audio id="audio_answer_{i}">
                    <source src="data:audio/mp3;base64,{audio}" type="audio/mp3">
                </audio>
            </div>
            """

    html = f"""
    <style>
        .container {{
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            text-align: left;
            font-size: 1.2em;
        }}
        .example {{
            border: 2px solid #ccc;
            background-color: #f0f0f0;
            padding: 15px;
            margin: 10px 0;
            color: #666;
            width: 80%;
        }}
        .task {{
            border: 2px solid orange;
            background-color: #ffebcc;
            padding: 15px;
            margin: 10px 0;
            color: black;
            width: 80%;
            position: relative;
        }}
        .hint {{
            font-style: italic;
            color: #666;
        }}
        .audio-btn {{
            position: absolute;
            top: 10px;
            right: 10px;
            font-size: 22px;
            cursor: pointer;
            border: none;
            background: none;
        }}
    </style>

    <div class="container">
        <div class="example">
            <strong>Образец:</strong> {prime_text}
        </div>
        <div class="task">
            {stimulus_text}
            <button class="audio-btn" onclick="playAudio()">🔊</button>
            <div class="hint">{hint}</div>
        </div>
    </div>

    <div style="margin-top:10px;">
        {answers_html}
    </div>

    <audio id="audio" autoplay>
        <source src="data:audio/mp3;base64,{audio_base64 or ''}" type="audio/mp3">
    </audio>

    <script>
        function playAudio() {{
            var audio = document.getElementById("audio");
            audio.currentTime = 0;
            audio.play();
        }}

        function playAnswerAudio(index) {{
            var audio = document.getElementById("audio_answer_" + index);
            audio.currentTime = 0;
            audio.play();
        }}
    </script>
    """

    return html
    
# Основной код для задания 5
if st.session_state.current_step == 1:  # Инструкция
    st.header("Задание 4.1")
    
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
        st.header("Тренировка задания 4.1")
        st.write("Выберите правильный глагол с опорой на предложение-образец")
        task5_test = task_data.gender_easy_test[index]

        # Создаем HTML с пустыми аудио для ответов (для макета)
        dummy_audio = [""] * len(task5_test["answers"])
        html = create_task5_html(
            task5_test["prime_text"],
            task5_test["stimulus_text"],
            task5_test["hint"],
            None,
            dummy_audio,
            task5_test["answers"]
        )
        st.components.v1.html(html, height=400)

        choice = st.radio(
            "Выберите ответ:",
            task5_test["answers"],
            key=f"q5_test_radio_{index}",
            index=None,
            horizontal=True
        )

        if choice is not None:
            st.session_state.task5_test_index += 1  # Переход к следующему стимулу
            st.rerun()

    else:
        st.header("Тренировка задания 4.1 завершена!")
        if st.button("Перейти к заданию 4.1"):
            st.session_state.current_step = 3
            st.rerun()

elif st.session_state.current_step == 3:  # Основная часть задания 5
    index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 5")])
    answ_co = len(task_data.gender_easy)
    if index < answ_co:
        st.header("Задание 4.1")
        st.write("Выберите правильный глагол с опорой на предложение-образец")
        task5 = task_data.gender_easy[index]
        audio_path = f"audio/task5/{task5['audio']}"
        
        if "last_audio" not in st.session_state:
            st.session_state.last_audio = None

        if "audio_base64" not in st.session_state:
            st.session_state.audio_base64 = None

        if st.session_state.last_audio != task5["audio"]:
            if os.path.exists(audio_path):
                with open(audio_path, "rb") as f:
                    audio_bytes = f.read()
                st.session_state.audio_base64 = base64.b64encode(audio_bytes).decode()
                st.session_state.last_audio = task5["audio"]
            else:
                st.session_state.audio_base64 = None

        audio_base64 = st.session_state.audio_base64
        audio_answers_base64 = []

        for audio_file in task5.get("audio_answers", []):
            path = f"audio/task5/{audio_file}"
            if os.path.exists(path):
                with open(path, "rb") as f:
                    audio_answers_base64.append(base64.b64encode(f.read()).decode())
            else:
                audio_answers_base64.append("")
        
        html = create_task5_html(
            task5["prime_text"],
            task5["stimulus_text"],
            task5["hint"],
            audio_base64,
            audio_answers_base64,
            task5["answers"]
        )
        st.components.v1.html(html, height=400)

        choice = st.radio(
            "Выберите ответ:",
            task5["answers"],
            key=f"q5_radio_{index}",
            index=None,
            horizontal=True
        )

        if choice is not None:
            st.session_state.responses[f"Задание 5: {task5['stimulus_text']}"] = choice
            st.rerun()

        func.skip_task(st, index, answ_co, "Задание 5: ")

    else:
        st.header("Задание 4.1 завершено!")
        if st.button("Перейти к следующему заданию"):
            st.session_state.current_step = 4
            st.rerun()

############################################################################################################################################
def transliterate(text):
    """Транслитерация русского текста для поиска аудиофайлов"""
    mapping = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
    }
    result = ''
    for char in text.lower():
        result += mapping.get(char, char)
    return result

def create_task6_audio_buttons(verbs, col_key):
    """Создает HTML с кнопками для проигрывания вариантов ответов"""
    buttons_html = ""
    script_functions = ""
    
    for i, verb in enumerate(verbs):
        audio_filename = transliterate(verb) + '.mp3'
        audio_path = f"audio/task6/{audio_filename}"
        audio_base64 = ""
        
        if os.path.exists(audio_path):
            with open(audio_path, "rb") as f:
                audio_base64 = base64.b64encode(f.read()).decode()
        
        buttons_html += f"""
        <button onclick="playAudio_{col_key}_{i}()"
            style="
                font-size:14px;
                border:2px solid #ccc;
                background:#f0f0f0;
                border-radius:6px;
                cursor:pointer;
                padding:8px 12px;
                margin:3px 0;
                width:100%;
                text-align:left;
            ">
            🔊 {verb}
        </button>
        <audio id="audio_{col_key}_{i}">
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        """
        
        script_functions += f"""
        function playAudio_{col_key}_{i}() {{
            var audio = document.getElementById("audio_{col_key}_{i}");
            audio.currentTime = 0;
            audio.play();
        }}
        """
    
    html = f"""
    <div style="margin-top:5px;">
        {buttons_html}
    </div>
    <script>
        {script_functions}
    </script>
    """
    
    return html


# Основной код для задания 6
if st.session_state.current_step == 4:  # Инструкция
    st.header("Задание 4.2")

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
        st.header("Тренировка задания 4.2")
        st.write("Соедините картинки с правильной формой глагола")
        
        # Тренировочные данные
        image_names = task_data.gender_middle_minus_test[index]
        verbs = task_data.gender_middle_minus_opt_test[index]
        verbs = [v for v in verbs if v != ""]  

        st.write("Картинки:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(f"images/{image_names[0]}", use_container_width=True)
        with col2:
            st.image(f"images/{image_names[1]}", use_container_width=True)
        with col3:
            st.image(f"images/{image_names[2]}", use_container_width=True)

        col1, col2, col3 = st.columns(3)
        index_answrs = []
        with col1:
            index_answrs.append(st.selectbox("Выберите глагол:", verbs, key=f"verb_1_{index}"))
        with col2:
            index_answrs.append(st.selectbox("Выберите глагол:", verbs, key=f"verb_2_{index}"))
        with col3:
            index_answrs.append(st.selectbox("Выберите глагол:", verbs, key=f"verb_3_{index}"))

        if st.button("Далее"):
            # Проверяем, выбраны ли все глаголы
            if len(index_answrs) == 3 and not any(item == "" for item in index_answrs):
                st.session_state.task6_test_index += 1
                st.rerun()  # Обновляем страницу для следующего стимуля

    else:
        st.header("Тренировка задания 4.2 завершена!")
        if st.button("Перейти к заданию 4.2"):
            st.session_state.current_step = 6
            st.rerun()

elif st.session_state.current_step == 6:
    index = int(len([k for k in st.session_state.responses.keys() if k.startswith("Задание 6")]) / 3)
    answ_co = len(task_data.gender_middle_minus)
    if index < answ_co:
        st.header("Задание 4.2")
        st.write("Нажмите на кнопку с глаголом, чтобы прослушать, и выберите ответ ниже.")
        
        image_names = task_data.gender_middle_minus[index]
        verbs = task_data.gender_middle_minus_opt[index]
        verbs = [v for v in verbs if v != ""]

        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.image(f"images/{image_names[0]}", use_container_width=True)
            html1 = create_task6_audio_buttons(verbs, "col1")
            st.components.v1.html(html1, height=len(verbs)*45+10)
            answer1 = st.radio("Выберите глагол:", verbs, key=f"verb_1_{index}", index=None)
            
        with col2:
            st.image(f"images/{image_names[1]}", use_container_width=True)
            html2 = create_task6_audio_buttons(verbs, "col2")
            st.components.v1.html(html2, height=len(verbs)*45+10)
            answer2 = st.radio("Выберите глагол:", verbs, key=f"verb_2_{index}", index=None)
            
        with col3:
            st.image(f"images/{image_names[2]}", use_container_width=True)
            html3 = create_task6_audio_buttons(verbs, "col3")
            st.components.v1.html(html3, height=len(verbs)*45+10)
            answer3 = st.radio("Выберите глагол:", verbs, key=f"verb_3_{index}", index=None)

        if st.button("Далее"):
            if answer1 is not None and answer2 is not None and answer3 is not None:
                st.session_state.responses[f"Задание 6: Картина {image_names[0]}"] = answer1
                st.session_state.responses[f"Задание 6: Картина {image_names[1]}"] = answer2
                st.session_state.responses[f"Задание 6: Картина {image_names[2]}"] = answer3
                st.rerun()
            else:
                st.warning("Выберите глагол для каждой картинки!")

        func.skip_task(st, index * 3, answ_co * 3, "Задание 6: ")
    else:
        st.header("Задание 4.2 завершено!")
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
    st.header("Задание 4.3")

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

    if st.button("Начать тренировку задания 4.3"):
        st.session_state.current_step = 8
        st.session_state.task7_test_index = 0  # Сбрасываем индекс тестовых стимулов
        st.rerun()

elif st.session_state.current_step == 8:
    # Получаем текущий индекс тестового стимула
    index = st.session_state.task7_test_index
    
    if index < len(task_data.gender_middle_plus_test):
        st.header("Тренировка задания 4.3")
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
                    width: auto;
                    display: inline-block;
                    text-align: left;
                    cursor: pointer;
                    margin: 5px 0;
                    font-size: 1.2em;
                }
                .stButton > button p {
                    white-space: nowrap;
                    margin: 0;
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
        st.header("Тренировка задания 4.3 завершена!")
        if st.button("Перейти к заданию 4.3"):
            st.session_state.current_step = 9
            st.rerun()

elif st.session_state.current_step == 9:
    index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 7")])    
    total_questions = len(task_data.gender_middle_plus)
    
    if index < total_questions:
        st.header("Задание 4.3")
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
                    width: auto;
                    display: inline-block;
                    text-align: left;
                    cursor: pointer;
                    margin: 5px 0;
                    font-size: 1.2em;
                }
                .stButton > button p {
                    white-space: nowrap;
                    margin: 0;
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
        st.header("Задание 4.3 завершено!")
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
    st.header("Задание 4.4")
    
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
        st.header("Тренировка задания 4.4")
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
        st.header("Тренировка задания 4.4 завершена!")
        if st.button("Перейти к основному заданию 4.4"):
            st.session_state.current_step = 12
            st.rerun()

elif st.session_state.current_step == 12:  # Задание 8 (ввод ответа)
    index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 8")])
    answ_co = len(task_data.gender_complex)
    if index < answ_co:
        st.header("Задание 4.4")
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
        st.header("Задание 4.4 завершено!")
        
        func.save_result(st)
