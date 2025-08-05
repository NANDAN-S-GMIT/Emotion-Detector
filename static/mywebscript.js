function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value.trim();
    const responseDiv = document.getElementById("system_response");
    const analyzeBtn = document.querySelector('.analyze-btn');

    // Enhanced animated loader
    responseDiv.innerHTML = `
      <div class="analyzing-loader">
        <div class="spinner"></div>
        <span class="analyzing-dots-pro"> Analyzing<span>.</span><span>.</span><span>.</span></span>
      </div>
    `;
    if (analyzeBtn) {
      analyzeBtn.disabled = true;
      analyzeBtn.classList.add('loading');
    }

    if (!textToAnalyze) {
        setTimeout(() => {
            responseDiv.innerHTML = "<span style='color:red'>Please enter text to analyze.</span>";
            if (analyzeBtn) {
              analyzeBtn.disabled = false;
              analyzeBtn.classList.remove('loading');
            }
        }, 1000);
        return;
    }

    let dotCount = 0;
    let dotInterval = setInterval(() => {
      const dots = '.'.repeat((dotCount % 3) + 1);
      const dotsHtml = `<span class='analyzing-dots-pro'>Analyzing${dots}</span>`;
      document.querySelector('.analyzing-dots-pro').innerHTML = `Analyzing${dots}`;
      dotCount++;
    }, 400);

    setTimeout(() => {
        clearInterval(dotInterval);
        let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                responseDiv.innerHTML = xhttp.responseText;
                if (analyzeBtn) {
                  analyzeBtn.disabled = false;
                  analyzeBtn.classList.remove('loading');
                }
            }
        };
        xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
        xhttp.send();
    }, 5000); // 5 seconds analyzing
}

// Add emotion buttons functionality
function setEmotionTextAndAnalyze(text) {
    document.getElementById("textToAnalyze").value = text;
    RunSentimentAnalysis();
}
