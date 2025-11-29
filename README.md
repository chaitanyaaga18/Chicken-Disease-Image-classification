
# 🐔 Chicken Disease Image Classification

An end-to-end deep-learning project to classify chicken diseases using images.
Built using **TensorFlow**, **Keras**, **Flask**, **Streamlit**, and a fully modular ML pipeline.

---

## 📌 Features

* ✔ Complete training, evaluation & prediction pipeline
* ✔ Transfer learning using MobileNetV2
* ✔ Streamlit UI for user-friendly predictions
* ✔ Flask API for backend deployment
* ✔ Dataset organized into train/val/test
* ✔ Artifacts saved automatically (models, logs, scores)
* ✔ Easy to run & share

---

## 📁 Project Structure

```
Chicken-disease-Image-classification/
│
├── src/
│   └── cnnClassifier/
│       ├── components/
│       ├── config/
│       ├── constants/
│       ├── entity/
│       ├── pipeline/
│       └── utils/
│
├── templates/                 # Flask HTML templates
├── artifacts/                 # Saved models, logs & outputs
├── chicken_disease_dataset/   # Dataset (not pushed to GitHub)
│
├── app.py                     # Flask app
├── streamlit_app.py           # Streamlit app
├── config.yaml
├── params.yaml
├── main.py                    # Complete ML pipeline runner
├── requirements.txt
└── README.md
```

---

## 🧪 Dataset

Your dataset must be structured like this:

```
chicken_disease_dataset/
├── train/
├── test/
└── val/
```

**Dataset Size:** ~288 MB
**Total Images:** ~8993

## 🧵 Dataset Download Link

The full Chicken Disease Dataset (train/test/val) used in this project is available here:

🔗 **Download Dataset (Google Drive)**  
https://drive.google.com/file/d/1hkjesmXM4I3mbO6ItZ-IpaN4zQcL_XWU/view?usp=sharing

Dataset Structure:
- 8,993 images  
- 5 disease classes  
- train / test / val  
- Total size: 288 MB  




## ⚙️ Installation

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/chaitanyaaga18/Chicken-Disease-Image-classification.git
cd Chicken-Disease-Image-classification
```

---

### **2️⃣ Create and activate virtual environment**

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### **3️⃣ Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

### **🔹 Run the full ML pipeline (training + evaluation)**

```bash
python main.py
```

---

### **🔹 Run Flask API**

```bash
python app.py
```

Then open:
👉 [http://127.0.0.1:8080](http://127.0.0.1:8080)

---

### **🔹 Run Streamlit App (recommended)**

```bash
streamlit run streamlit_app.py
```

Then visit:
👉 [http://localhost:8501](http://localhost:8501)

---

## 🧠 Model Details

* Architecture: **MobileNetV2 (ImageNet pretrained)**
* Image Size: **224 × 224 × 3**
* Optimizer: **Adam (lr=0.0001)**
* Loss: **Categorical Crossentropy**
* Classes: **5 chicken diseases**

---

## 📊 Evaluation Results

Example (your model output):

```
Accuracy: 97.7%
Loss: 0.079
```

---

## 🖼️ Screenshots 


* Streamlit UI screenshot

* Flask UI screenshot
* Sample predictions

---

## 👨‍💻 Author

**Chaitanya Agarwal**
GitHub: [https://github.com/chaitanyaaga18](https://github.com/chaitanyaaga18)

---

## 📜 License


