# Life Receipts

Life Receipts is a data-analytics + AI/ML project that tracks how you spend your time each day  
and generates a **digital receipt** showing productive vs. leisure activities.  
The system provides insights, weekly badges, and improvement suggestions through a dashboard.

## Features
- Activity logging (manual entry or CSV upload)
- AI-driven productivity scoring (Random Forest + optional LSTM for pattern prediction)
- Personalized tips and weekly summary badges
- Interactive dashboards (Plotly / Streamlit)

## Tech Stack
- **Language:** Python 3.x
- **Frontend/Dashboard:** Streamlit
- **Backend/Data:** Pandas, NumPy
- **Visualization:** Plotly, Matplotlib, Seaborn
- **Machine Learning:** scikit-learn (RandomForest), TensorFlow/Keras (for LSTM)

## Project Structure
life-receipts/
- data/ # sample or synthetic datasets
- src/ # core python modules
- web/ # dashboard / web app
- notebooks/ # Jupyter notebooks for analysis
- README.md
- requirements.txt
