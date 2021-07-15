var submit = document.getElementById("sf-submit");
var sfForm = document.getElementById("sf-form");
var sf1 = document.getElementById("sf-1");
var sf2 = document.getElementById("sf-2");
var sf3 = document.getElementById("sf-3");
var sf4 = document.getElementById("sf-4");
var sfStep1 = document.getElementById("s-step-1");
var sfStep2 = document.getElementById("s-step-2");
var sfStep3 = document.getElementById("s-step-3");
var sfStep4 = document.getElementById("s-step-4");
var sfErrors = document.getElementById("sf-errors")
// Step 1
var categorie = document.getElementById("categorie");
var sousCategorie = document.getElementById("sous_categorie");
var sfCat = document.getElementById("sf-cat");
// Step 2
var nom = document.getElementById("nom");
var prenom = document.getElementById("prenom");
var email = document.getElementById("email");
var telephone = document.getElementById("telephone");
// Step 3
var preoccupation = document.getElementById("preocupation");
var date = document.getElementById("date");
var lieu = document.getElementById("lieu");
var description = document.getElementById("description");
var temoin = document.getElementById("temoin");
var premiere = document.getElementById("premiere");
var fichier = document.getElementById("fichier");
var recontact = document.getElementById("recontact");
var modalite = document.getElementById("modalite");
// Step 4
var confirmation = document.getElementById("confirmation");

var step = 1;

submit.addEventListener('click', function(e){
    e.preventDefault();
    if(step == 1) {
        var res = validateStep1();
        if(res[0]) {
            sf1.style.display = "none";
            sf2.style.display = "block";
            sfStep1.classList.remove("s-step-active");
            sfStep2.classList.add("s-step-active");
            sfErrors.style.display = "none";
            step = 2;
        } else {
            sfErrors.innerHTML = res[1];
            sfErrors.style.display = "block";
        }
    } else if(step == 2) {
        var res= validateStep2();
        if(res[0]) {
            sf2.style.display = "none";
            sf3.style.display = "block";
            sfStep2.classList.remove("s-step-active");
            sfStep3.classList.add("s-step-active");
            sfErrors.style.display = "none";
            step = 3;
        } else {
            var er = "<ul>";
            for(message in res[1]) {
                er += "<li>" + res[1][message] + "</li>";
            }
            er += "</ul>";
            sfErrors.innerHTML = er;
            sfErrors.style.display = "block";
        }
    } else if(step == 3) {
        var res = validateStep3();
        if(res[0]) {
            sf3.style.display = "none";
            sf4.style.display = "block";
            sfStep3.classList.remove("s-step-active");
            sfStep4.classList.add("s-step-active");
            sfErrors.style.display = "none";
            submit.innerHTML = "Valider";
            var sfRecap = sf4.getElementsByClassName("sf-recap");
            sfRecap[0].getElementsByClassName("sf-recap-text")[0].innerHTML = categorie.options[categorie.selectedIndex].text;
            if(categorie.selectedIndex == 1) {
                sfRecap[1].getElementsByClassName("sf-recap-text")[0].innerHTML = sous_categorie.options[sous_categorie.selectedIndex].text;
            } else {
                sfRecap[1].getElementsByClassName("sf-recap-text")[0].innerHTML = "NA";
            }
            sfRecap[2].getElementsByClassName("sf-recap-text")[0].innerHTML = nom.value;
            sfRecap[3].getElementsByClassName("sf-recap-text")[0].innerHTML = prenom.value;
            sfRecap[4].getElementsByClassName("sf-recap-text")[0].innerHTML = email.value;
            sfRecap[5].getElementsByClassName("sf-recap-text")[0].innerHTML = telephone.value;
            sfRecap[6].getElementsByClassName("sf-recap-text")[0].innerHTML = preoccupation.value;
            sfRecap[7].getElementsByClassName("sf-recap-text")[0].innerHTML = date.value;
            sfRecap[8].getElementsByClassName("sf-recap-text")[0].innerHTML = lieu.value;
            sfRecap[9].getElementsByClassName("sf-recap-text")[0].innerHTML = description.value;
            sfRecap[10].getElementsByClassName("sf-recap-text")[0].innerHTML = temoin.value;
            sfRecap[11].getElementsByClassName("sf-recap-text")[0].innerHTML = premiere.options[premiere.selectedIndex].text;
            sfRecap[12].getElementsByClassName("sf-recap-text")[0].innerHTML = recontact.options[recontact.selectedIndex].text;
            sfRecap[13].getElementsByClassName("sf-recap-text")[0].innerHTML = modalite.value;
            step = 4;
        } else {
            var er = "<ul>";
            for(message in res[1]) {
                er += "<li>" + res[1][message] + "</li>";
            }
            er += "</ul>";
            sfErrors.innerHTML = er;
            sfErrors.style.display = "block";
        }
    } else if(step == 4) {
        var res= validateStep4();
        console.log(res);
        if(res[0]) {
            sfForm.submit();
        } else {
            sfErrors.innerHTML = res[1];
            sfErrors.style.display = "block";
        }
    }
    window.scrollTo(0, 0);
});
// Step 1
categorie.addEventListener('change', function() {
    if(this.selectedIndex == 1) {
        sfCat.style.display = 'flex';
    } else {
        sfCat.style.display = 'none';
    }
});

function validateStep1() {
    if(categorie.selectedIndex == 0)
        return [false, ["Veuillez choisir une catégorie."]];
    return [true];
}

function validateStep2() {
    retour = true
    messages = []
    if(nom.value == "") {
        messages.push("Veuillez indiquer un nom.");
        retour = false;
    }
    if(prenom.value == "") {
        messages.push("Veuillez indiquer un prénom.");
        retour = false;
    }
    if(email.value == "") {
        // TODO : Vérification mail
        messages.push("Veuillez indiquer une adresse mail valide.");
        retour = false;
    }
    if(!retour) {
        return [false, messages];
    } else {
        return [true]
    }
}

function validateStep3() {
    retour = true;
    messages = [];
    if(preocupation.value == "") {
        messages.push("Vous devez décrire vos préocupations.");
        retour = false;
    }
    if(lieu.value == "") {
        messages.push("Vous devez préciser l'endroit où se sont déroulés les faits.");
        retour = false;
    }
    if(description.value == "") {
        messages.push("Vous devez décrire la situation ou les faits.");
        retour = false;
    }
    if(!retour){
        return [false, messages];
    } else {
        return [true];
    }
}

function validateStep4() {
    if(confirmation.checked)
        return [true];
    return [false, "Vous devez confirmer ces informations."];
}
