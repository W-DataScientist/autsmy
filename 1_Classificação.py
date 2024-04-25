import streamlit as st
import matplotlib.pyplot as plt

def classify_tea(sex, age, communication, social_interaction, behavior, sensory_sensitivity, specific_interests, developmental_delays, nonverbal_communication,
                 routine_preference, understanding_nonliteral, repetitive_motor_movements, sensory_issues, intense_focus, lack_of_eye_contact, emotion_comprehension,
                 social_anxiety, imaginative_play, conversation_initiation, understanding_irony, literal_rule_following, difficulty_with_changes, unusual_interests,
                 hyper_or_hypoactivity, sensory_overload, self_injurious_behaviors, emotion_recognition_difficulty, sleep_issues, exceptional_memory, tone_of_voice_difficulty):
    
    total_score = (communication + social_interaction + behavior + sensory_sensitivity + specific_interests + developmental_delays +
                   nonverbal_communication + routine_preference + understanding_nonliteral + repetitive_motor_movements + sensory_issues +
                   intense_focus + lack_of_eye_contact + emotion_comprehension + social_anxiety + imaginative_play + conversation_initiation +
                   understanding_irony + literal_rule_following + difficulty_with_changes + unusual_interests + hyper_or_hypoactivity +
                   sensory_overload + self_injurious_behaviors + emotion_recognition_difficulty + sleep_issues + exceptional_memory + tone_of_voice_difficulty)
    
    if sex == 'Masculino':
        if age < 30:
            if total_score < 20:
                return "Grau Baixo"
            elif total_score < 28:
                return "Grau Moderado"
            else:
                return "Grau Alto"
        else:
            if total_score < 20:
                return "Grau Baixo"
            elif total_score < 25:
                return "Grau Moderado"
            else:
                return "Grau Alto"
    else:  # Feminino
        if age < 30:
            if total_score < 19:
                return "Grau Baixo"
            elif total_score < 26:
                return "Grau Moderado"
            else:
                return "Grau Alto"
        else:
            if total_score < 17:
                return "Grau Baixo"
            elif total_score < 22:
                return "Grau Moderado"
            else:
                return "Grau Alto"

def main():
    st.title("Classificação (TEA)")

    # Parâmetros
    sex = st.radio("Qual o sexo do paciente?", ("Masculino", "Feminino"))
    age = st.slider("Qual a idade do paciente?", 1, 40)
    communication = st.radio("Tem dificuldades na comunicação?", ("Sim", "Não"))
    social_interaction = st.radio("Tem dificuldades na interação social?", ("Sim", "Não"))
    behavior = st.radio("Exibe padrões repetitivos de comportamento?", ("Sim", "Não"))
    sensory_sensitivity = st.radio("É sensível a estímulos sensoriais?", ("Sim", "Não"))
    specific_interests = st.radio("Tem interesses intensos e específicos em determinados temas?", ("Sim", "Não"))
    developmental_delays = st.radio("Experimentou atrasos no desenvolvimento motor ou cognitivo na infância?", ("Sim", "Não"))
    nonverbal_communication = st.radio("Tem dificuldades em entender ou usar gestos e expressões faciais?", ("Sim", "Não"))
    routine_preference = st.radio("Prefere seguir uma rotina diária específica?", ("Sim", "Não"))
    understanding_nonliteral = st.radio("Tem dificuldade em entender sarcasmo ou expressões não literais?", ("Sim", "Não"))
    repetitive_motor_movements = st.radio("Apresenta movimentos motores repetitivos, como balançar o corpo ou bater as mãos?", ("Sim", "Não"))
    sensory_issues = st.radio("É sensível a certos alimentos ou odores?", ("Sim", "Não"))
    intense_focus = st.radio("Tende a se concentrar intensamente em objetos ou partes de objetos?", ("Sim", "Não"))
    lack_of_eye_contact = st.radio("Evita contato visual durante conversas?", ("Sim", "Não"))
    emotion_comprehension = st.radio("Tem dificuldade em entender ou expressar emoções?", ("Sim", "Não"))
    social_anxiety = st.radio("Experimenta ansiedade em situações sociais?", ("Sim", "Não"))
    imaginative_play = st.radio("Tem dificuldade em brincar de forma imaginativa ou simbólica?", ("Sim", "Não"))
    conversation_initiation = st.radio("Tem dificuldade em iniciar ou manter conversas com outras pessoas?", ("Sim", "Não"))
    understanding_irony = st.radio("Tem dificuldade em entender ironia ou expressões faciais sutis?", ("Sim", "Não"))
    literal_rule_following = st.radio("Segue regras ou instruções de forma literal?", ("Sim", "Não"))
    difficulty_with_changes = st.radio("Tem dificuldade em lidar com mudanças na rotina?", ("Sim", "Não"))
    unusual_interests = st.radio("Tem interesses incomuns ou obsessões por assuntos específicos?", ("Sim", "Não"))
    hyper_or_hypoactivity = st.radio("Apresenta hiper ou hipoatividade?", ("Sim", "Não"))
    sensory_overload = st.radio("Tem dificuldade em filtrar informações sensoriais, como ruídos de fundo?", ("Sim", "Não"))
    self_injurious_behaviors = st.radio("Tem comportamentos autolesivos?", ("Sim", "Não"))
    emotion_recognition_difficulty = st.radio("Tem dificuldade em reconhecer ou compreender emoções alheias?", ("Sim", "Não"))
    sleep_issues = st.radio("Experimenta dificuldades de sono?", ("Sim", "Não"))
    exceptional_memory = st.radio("Tem uma memória excepcional para detalhes?", ("Sim", "Não"))
    tone_of_voice_difficulty = st.radio("Tem dificuldade em entender o tom de voz das pessoas?", ("Sim", "Não"))

    # Convertendo respostas para pontuação
    sex = 1 if sex == "Masculino" else 0
    age = age
    communication = 1 if communication == "Sim" else 0
    social_interaction = 1 if social_interaction == "Sim" else 0
    behavior = 1 if behavior == "Sim" else 0
    sensory_sensitivity = 1 if sensory_sensitivity == "Sim" else 0
    specific_interests = 1 if specific_interests == "Sim" else 0
    developmental_delays = 1 if developmental_delays == "Sim" else 0
    nonverbal_communication = 1 if nonverbal_communication == "Sim" else 0
    routine_preference = 1 if routine_preference == "Sim" else 0
    understanding_nonliteral = 1 if understanding_nonliteral == "Sim" else 0
    repetitive_motor_movements = 1 if repetitive_motor_movements == "Sim" else 0
    sensory_issues = 1 if sensory_issues == "Sim" else 0
    intense_focus = 1 if intense_focus == "Sim" else 0
    lack_of_eye_contact = 1 if lack_of_eye_contact == "Sim" else 0
    emotion_comprehension = 1 if emotion_comprehension == "Sim" else 0
    social_anxiety = 1 if social_anxiety == "Sim" else 0
    imaginative_play = 1 if imaginative_play == "Sim" else 0
    conversation_initiation = 1 if conversation_initiation == "Sim" else 0
    understanding_irony = 1 if understanding_irony == "Sim" else 0
    literal_rule_following = 1 if literal_rule_following == "Sim" else 0
    difficulty_with_changes = 1 if difficulty_with_changes == "Sim" else 0
    unusual_interests = 1 if unusual_interests == "Sim" else 0
    hyper_or_hypoactivity = 1 if hyper_or_hypoactivity == "Sim" else 0
    sensory_overload = 1 if sensory_overload == "Sim" else 0
    self_injurious_behaviors = 1 if self_injurious_behaviors == "Sim" else 0
    emotion_recognition_difficulty = 1 if emotion_recognition_difficulty == "Sim" else 0
    sleep_issues = 1 if sleep_issues == "Sim" else 0
    exceptional_memory = 1 if exceptional_memory == "Sim" else 0
    tone_of_voice_difficulty = 1 if tone_of_voice_difficulty == "Sim" else 0

    if st.button("Classificar"):
        result = classify_tea(sex, age, communication, social_interaction, behavior, sensory_sensitivity, specific_interests, developmental_delays, nonverbal_communication,
                              routine_preference, understanding_nonliteral, repetitive_motor_movements, sensory_issues, intense_focus, lack_of_eye_contact,
                              emotion_comprehension, social_anxiety, imaginative_play, conversation_initiation, understanding_irony, literal_rule_following,
                              difficulty_with_changes, unusual_interests, hyper_or_hypoactivity, sensory_overload, self_injurious_behaviors,
                              emotion_recognition_difficulty, sleep_issues, exceptional_memory, tone_of_voice_difficulty)
        st.write(f"A classificação do TEA é: {result}")

        # Criar gráfico de barras
        grades = ["Grau Baixo", "Grau Moderado", "Grau Alto"]
        counts = [result.count(grade) for grade in grades]
        
        fig, ax = plt.subplots()
        ax.bar(grades, counts, color=['green', 'orange', 'red'])
        ax.set_ylabel('Pontuação')
        ax.set_title('Classificação de TEA')
        st.pyplot(fig)

if __name__ == "__main__":
    main()
