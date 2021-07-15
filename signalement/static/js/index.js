var btnNewSignalement = document.getElementById("new-signalement");
var nsModalOverlay = document.getElementById("ns-modal-overlay");
var nsModalDismiss = document.getElementById("ns-modal-dismiss");

btnNewSignalement.addEventListener("click", function(e) {
    e.preventDefault();
    nsModalOverlay.style.display = "block";
});
nsModalDismiss.addEventListener("click", function(e) {
    e.preventDefault();
    nsModalOverlay.style.display = "none";
});
