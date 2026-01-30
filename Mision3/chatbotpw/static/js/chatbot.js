const chatToggle = document.getElementById("chat-toggle");
    const chatWrapper = document.getElementById("chat-wrapper");
    const chatClose = document.getElementById("chat-close");

    chatToggle.addEventListener("click", () => {
      chatWrapper.style.display = "flex";
    });

    chatClose.addEventListener("click", () => {
      chatWrapper.style.display = "none";
    });