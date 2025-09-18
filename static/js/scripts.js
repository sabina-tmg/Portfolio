document.addEventListener('DOMContentLoaded', function () {
  const messagesList = document.getElementById('messages-list');
  if (messagesList) {
    // Wait 1 minute (60000 ms) before fading out
    setTimeout(() => {
      messagesList.style.transition = 'opacity 1s ease'; // fade out duration 1 second
      messagesList.style.opacity = '0';

      // Remove from DOM after fade out completes (1s)
      setTimeout(() => messagesList.remove(), 1000);
    }, 60000); // 60000 ms = 1 minute
  }
});

/*for hidden message */

document.getElementById("openMessageBox").addEventListener("click", function(e) {
    e.preventDefault();
    document.getElementById("messageBox").style.display = "flex";
});

document.getElementById("closeMessageBox").addEventListener("click", function() {
    document.getElementById("messageBox").style.display = "none";
});

window.addEventListener("click", function(e) {
    if (e.target === document.getElementById("messageBox")) {
        document.getElementById("messageBox").style.display = "none";
    }
});
