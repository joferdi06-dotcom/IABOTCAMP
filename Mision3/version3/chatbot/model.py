# Funcion de librerias scikit-learn, esta libreria seria la que reemplaza la instalación por comandos

import os
import pickle

# Convierte texto en un vector y lo entiende en números 0 y 1
from sklearn.feature_extraction.text import CountVectorizer

# IA relación entre un texto (pregunta) y una respuesta (solución)
from sklearn.naive_bayes import MultinomialNB # Clasificador de texto

MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")
ANSWERS_PATH = os.path.join(MODEL_DIR, "answers.pkl")


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
    
    # Crear carpeta para guardar el model si no existe
    os.makedirs(MODEL_DIR, exist_ok = True)

    # Guardar los objetos entrenados
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model,f)
    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer, f)
    with open(ANSWERS_PATH, "wb") as f:
        pickle.dump(unique_answers, f)
    print("🆗 Modelo Entrenado y Guardado Correctamente")

    return model, vectorizer, unique_answers

def load_model():
    """
    Docstring para load_model
    """
    if(
        os.path.exists(MODEL_PATH)
        and os.path.exists(VECTORIZER_PATH)
        and os.path.exists(ANSWERS_PATH)
    ):
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
        with open(VECTORIZER_PATH, "rb") as f:
            vectorizer = pickle.load(f)
        with open(ANSWERS_PATH, "rb") as f:
            unique_answers = pickle.load(f)
            print("📁 Modelo Cargado desde disco.")
            return model, vectorizer, unique_answers
    else:
        print("⚡ No hay modelo guardado, será necesario entrenarlo")
        return None, None,None

# Funcion predict_answer
def predict_answer(model, vectorizer, unique_answer, user_text):
    # Convertimos el texto a un números
    x = vectorizer.transform([user_text]) # Aqui recibe solo una, es singular
    # El modelo predice la etiqueta de la respuesta correcta
    label = model.predict(x)[0]
    return unique_answer[label]