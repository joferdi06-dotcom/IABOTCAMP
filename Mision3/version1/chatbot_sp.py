# Funcion de librerias scikit-learn, esta libreria seria la que reemplaza la instalación por comandos

# Convierte texto en un vector y lo entiende en números 0 y 1
from sklearn.feature_extraction.text import CountVectorizer

# IA relación entre un texto (pregunta) y una respuesta (solución)
from sklearn.naive_bayes import MultinomialNB # Clasificador de texto

# Función de entrenamiento preguntas

def build_and_train_model(train_pairs): # Funcion para hacer el entrenamiento
    # train_pairs: lista de pares(pregunta, respuesta)
    # Ejemplo [("Hola", "!Hola"), ("adiós"), "¡Hasta luego!"]
    # separamos las preguntas y respuestas en dos listas

    quesions = [q for q, _ in train_pairs] # Construye una lista de preguntas
    answers = [a for _, a in train_pairs] # Construye una lista de respuestas
    # Creamos el vectorizado, que traducira el texto a números
    vectorizer = CountVectorizer()
    # Entrenamiento
    x = vectorizer.fit_transform(quesions) # Aqui transforma todas
    # Obtenemos una lista de respuestas umicas
    unique_answers = sorted(set(answers))
    # Crer el diccionrio con las etiquetas
    answers_to_label = {a: i for i, a in enumerate(unique_answers)}
    # Creamos una lista
    y = [answers_to_label[a] for a in answers]
    # Modelo clasificación de texto
    model = MultinomialNB()
    # Entrenar el modelo
    model.fit(x,y)
    return model, vectorizer, unique_answers

# Funcion predict_answer
def predict_answer(model, vectorizer, unique_answer, user_text):
    # Convertimos el texto a un números
    x = vectorizer.transform([user_text]) # Aqui recibe solo una, es singular
    # El modelo predice la etiqueta de la respuesta correcta
    label = model.predict(x)[0]
    return unique_answer[label]
    
 # Programa principal
if __name__ == "__main__":
    training_data = [
        ("hola", "¡Hola! ¿En qué podemos ayudarte hoy?"),
        ("buenos días", "Buenos días, gracias por contactarnos. ¿Cómo podemos asistirte?"),
        ("buenas tardes", "Buenas tardes, es un gusto atenderte. ¿Qué consulta tienes?"),
        ("buenas noches", "Buenas noches, estamos a tu disposición. ¿En qué podemos ayudarte?"),
        ("información", "Con gusto te brindamos la información que necesitas. ¿Sobre qué tema?"),
        ("soporte", "Nuestro equipo de soporte está listo para ayudarte. Cuéntanos tu inconveniente."),
        ("precio", "Con gusto te compartimos nuestros precios. ¿Qué servicio te interesa?"),
        ("gracias", "Gracias a ti por comunicarte con nosotros. ¡Que tengas un excelente día!")
        ]
    model, vectorizer, unique_answer = build_and_train_model(training_data)
    # Mostrar un mensaje inicial al usuario
    print("Chatbot supervisado listo, Escribe salir para terminar.\n")
while True:
    # Pedimos una frase al usuario
    user = input("Tú: ").strip()
    if user.lower() in {"salir", "exit", "quit", "fin"}:
        print("Bot: Hasta pronto¡")
        break
    response = predict_answer(model, vectorizer, unique_answer, user)
    print("Bot: ", response)