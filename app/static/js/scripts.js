function verificarSenha(){
    var valor = document.getElementById("id_senha").value;
    if (valor == '') {
        var novaSenha = gerarSenha();
        document.getElementById('id_senha').value = novaSenha
        alert("Senha gerada: " + gerarSenha());
    }
}

function gerarSenha(){
    var chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJLMNOPQRSTUVWXYZ!@#$%^&*()+?><:{}[]";
    var passwordLength = 10;
    var password = "";

    for (var i = 0; i < passwordLength; i++) {
      var randomNumber = Math.floor(Math.random() * chars.length);
      password += chars.substring(randomNumber, randomNumber + 1);
    }
    return password
}