document.getElementById('predictForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const data = {
    Pregnancies: +document.getElementById('pregnancies').value,
    Glucose: +document.getElementById('glucose').value,
    BloodPressure: +document.getElementById('bp').value,
    SkinThickness: +document.getElementById('skin').value,
    Insulin: +document.getElementById('insulin').value,
    BMI: +document.getElementById('bmi').value,
    DiabetesPedigreeFunction: +document.getElementById('dpf').value,
    Age: +document.getElementById('age').value
  };

  try {
    const res = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    const result = await res.json();
    const container = document.getElementById('result-container');
    const posCard = document.getElementById('positive-card');
    const negCard = document.getElementById('negative-card');

    // Reset visibility
    posCard.style.display = 'none';
    negCard.style.display = 'none';
    container.classList.remove('hidden');

    console.log(result);

    // Show the relevant card
    if (result.prediction === "Positive") {
      posCard.style.display = 'block';
      document.getElementById('positive-prob').textContent = result.probability + "%";
    } else {
      negCard.style.display = 'block';
      document.getElementById('negative-prob').textContent = result.probability + "%";
    }

  } catch (error) {
    console.error("Prediction error:", error);
  }
});
