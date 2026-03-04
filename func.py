import streamlit as st
import pandas as pd

def skip_task(st, curr_index = int, max_index = int, task_name = str):
    st.markdown(
        """
        <style>
            .st-key-skip .stButton button {
                background-color: transparent; /* Прозрачный фон */
                border: 2px solid red; /* Красная граница */
                padding: 10px 20px; /* Отступы внутри кнопки */
                border-radius: 5px; /* Скругленные углы */
                color: red; /* Цвет текста */
                cursor: pointer; /* Курсор в виде указателя */
                font-size: 14px; /* Размер текста */
                position: fixed; /* Фиксированное позиционирование */
                bottom: 20px; /* Отступ снизу */
                right: 20px; /* Отступ справа */
                z-index: 1000; /* Чтобы кнопка была поверх других элементов */
                width: auto; /* Ширина по содержимому */
                text-align: center; /* Текст по центру */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Пропустить задание", key="skip"):
        st.write(st.session_state.current_step)
        for i in range(curr_index+1, max_index+1):
            st.session_state.responses[f"{task_name}Cтимул{i}"] = 0
        # return max_index
        st.rerun()
        # if st.session_state.current_step == 3: #задание 1
    # else:
    #     return curr_index
        # st.session_state.current_step += 1

def save_result(st):
    # Поле для ввода названия файла (без значения по умолчанию)
    custom_filename = st.text_input(
        "Введите название файла для сохранения результатов (без расширения .csv):"
    )
    
    if st.button("Сохранить результаты"):
        # Проверяем, ввел ли пользователь название файла
        if not custom_filename.strip():  # Если поле пустое
            st.warning("Пожалуйста, введите название файла.")
        else:
            # Ограничиваем длину имени файла (например, 50 символов)
            custom_filename = custom_filename[:50]
            
            # Формируем имя файла с расширением .csv
            filename = f"{custom_filename}.csv"
            
            # Создаем DataFrame с результатами
            df = pd.DataFrame(list(st.session_state.responses.items()), columns=["Вопрос", "Ответ"])
            df.to_csv(filename, index=False)
            
            # Кнопка для скачивания
            with open(filename, "rb") as f:
                st.download_button(
                    label="Скачать результаты",
                    data=f,
                    file_name=filename,
                    mime="text/csv"
                )