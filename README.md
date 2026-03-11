# 🤖 Pulso Inteligente — Chatbot de Salud con Tkinter

**Pulso Inteligente** es un chatbot educativo desarrollado en **Python + Tkinter** que brinda *orientación básica* sobre **síntomas, prevención y cuidados de hipertensión y diabetes**.  
No sustituye atención médica profesional; su propósito es **informar y promover hábitos saludables**.

---

## 🩺 ¿Qué hace Pulso Inteligente?

- Detecta cuando el usuario pregunta o menciona:
  - Hipertensión (presión alta)
  - Diabetes (glucosa alta)
  - Síntomas frecuentes relacionados
  - Alimentos recomendados
  - Prevención y cuidados
  - Uso responsable de medicamentos

- El bot:
  ✔️ Sugiere cuidados generales  
  ✔️ Orienta con lenguaje sencillo  
  ✔️ Recomienda alimentos saludables  
  ⚠️ Advierte sobre automedicación  
  ❌ *No receta medicamentos*

---

## 🧠 Funcionamiento de la IA (Reglas)

El chatbot **no usa redes neuronales**, sino **reglas simples basadas en palabras clave**, implementadas en `if/elif` dentro de la función:

```python
def obtener_respuesta_medica(texto):
```

Esto permite respuestas claras y controladas para un modelo educativo de salud.

## 🖥️ Interfaz Gráfica

Pulso Inteligente utiliza Tkinter para ofrecer una interfaz visual tipo chat:

- Zona de conversación con scroll
- Entrada de texto
- Botón "Enviar"
- Mensajes con colores distintivos (bot y usuario)
- Cierre automático cuando el usuario escribe adiós/salir/terminar

## 📌 Requisitos

| Herramienta | Versión recomendada                                                |
| ----------- | ------------------------------------------------------------------ |
| Python      | 3.8+                                                               |
| Librerías   | Incluidas en la instalación estándar de Python (Tkinter, datetime) |

👉 No necesitas instalar nada adicional.

## 🚀 Cómo ejecutar

Clona este repositorio:

```bash
git clone https://github.com/mtraYuriCoronado/pulso-inteligente.git
```

Entra a la carpeta del proyecto:

```bash
cd pulso-inteligente
```

Ejecuta el script:

```python
pulso-inteligente.py
```

⏳ Listo, se abrirá la ventana del chatbot.

## 📚 Ejemplos de Preguntas que Puedes Usar

Puedes escribir:

```bash
"Hola"
"¿Cuáles son síntomas de diabetes?"
"Dolor de cabeza y mareo"
"Alimentos para hipertensión"
"¿Qué medicamento tomo?"
"Adiós"
```

💡 El bot cerrará la aplicación si detecta comandos como: **adiós, salir, terminar**.

## 🛡️ Aviso de Responsabilidad

🔔 *Pulso Inteligente no sustituye la consulta médica.*

Está orientado a la educación preventiva, exclusivamente con fines informativos.

## 🛠️ Mejoras Futuras (Roadmap)

✔️ Mejorar procesamiento de lenguaje natural
✔️ Añadir base de conocimiento estructurada (JSON/BD)
✔️ Adaptar a versión web con Flask/HTML/CSS
✔️ Integrar sensores reales en el futuro (IoT)
✔️ Exportar chat o historial del usuario

## ✨ Autores

👩‍💻 Yamilet Dimas

👩‍💻 Miranda González

👩‍💻 Yomaly Nájera

👩‍💻 Gisela Salmerón

Desarrollo educativo con enfoque tecnológico en salud preventiva.

## 📄 Licencia (Sugerida)

Licencia libre MIT para difusión educativa.

## 💚 Contribuye al proyecto con ideas o mejoras

📩 ¡Toda propuesta es bienvenida!
