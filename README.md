# 📊 Sample Dash Dashboard (Python)

דוגמה קטנה לדאשבורד אינטראקטיבי ב‑Python באמצעות **Dash** ו‑**Plotly**.  
הדאשבורד מציג **תרשים עמודות** מדאטה לדוגמה (DataFrame) ומריץ שרת מקומי.

---

## ✨ מה יש בפרויקט

- **`deshbord.py`**: אפליקציית Dash פשוטה עם גרף עמודות וטקסט.
- **`test.py`**: הדפסה בסיסית של `"Hello, World!"`.

---

## 🧰 דרישות מקדימות

- Python 3.9+ מומלץ
- Pip (מגיע עם Python ברוב ההתקנות)

---

## 📦 התקנה

בטרמינל, מתוך תיקיית הפרויקט:

```bash
python -m pip install --upgrade pip
pip install dash plotly pandas
```

---

## ▶️ הרצה

הרץ את הדאשבורד:

```bash
python deshbord.py
```

לאחר מכן פתח בדפדפן את:

- `http://127.0.0.1:8050`

---

## 🧪 בדיקה מהירה

```bash
python test.py
```

---

## 🗂️ מבנה תיקיות (בקצרה)

```text
.
├─ deshbord.py
├─ test.py
└─ README.md
```

---

## 🛠️ התאמות נפוצות

- **שינוי הדאטה**: ערוך את ה‑DataFrame בתוך `deshbord.py`.
- **שינוי סוג הגרף**: החלף את `px.bar(...)` בפונקציה אחרת של Plotly Express (למשל `px.line`).
- **כיבוי מצב Debug**: החלף `debug=True` ל‑`debug=False`.

---

## 🤝 תרומה

יש רעיון לשיפור?  
אפשר לפתוח Issue / Pull Request עם תיאור קצר של השינוי והסיבה.

---

## 📄 רישיון

אם תרצה, אוכל להוסיף רישיון (MIT / Apache-2.0 / GPL) ולהכניס קובץ `LICENSE` בהתאם.
