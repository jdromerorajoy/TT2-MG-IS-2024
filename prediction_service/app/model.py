import torch
import os

# Cargar el modelo entrenado
model_path = os.path.join(os.path.dirname(__file__), "models", "trained_model.pkl")
model = torch.load(model_path, map_location=torch.device('cpu'), weights_only=False)

def predict_similarity(tensor_1, tensor_2):
    """Calcula la similitud entre dos conjuntos de propiedades"""
    try:
        # Predecir el score de similitud
        scores = model.predict(tensor_1, target="tail")

        # Seleccionar la puntuación de similitud con `tensor_2`
        score = scores[0, tensor_2[0][0]]  # ← Indexa el tensor para obtener el valor correcto

        # Aplicar sigmoide para obtener la probabilidad
        probabilidad = torch.sigmoid(score).item()

        return probabilidad
    except Exception as e:
        raise ValueError(f"❌ Error en la predicción: {str(e)}")