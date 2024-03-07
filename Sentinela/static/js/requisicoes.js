function buscaFuncionario(id) {

    matricula=document.getElementById(id).value;
    nome=document.getElementById("nome");
    cpf=document.getElementById("cpf");
    filial=document.getElementById("filial");
    setor=document.getElementById("setor");
    retorno=document.getElementById("retorno");
    inputmac = document.getElementById("mac");

    if (matricula){
    //function scene() {
    // if (retorno == 0) {
    let url = "/buscarColaborador/" + matricula;
  
    let xhr = new XMLHttpRequest();
  
    xhr.open("GET", url, false);
  
    xhr.onreadystatechange = function () {

      resposta = xhr.responseText;

      if (xhr.status = 200){

        var dados=resposta.split('-');

        if (dados[0] == '500'){
            
            retorno.innerHTML=dados[1];
            nome.setAttribute("value","");
            cpf.setAttribute("value","");
            setor.setAttribute("value","");
            inputmac.setAttribute("disabled","disabled");
            try{
            document.getElementById("mac2").setAttribute("disabled","disabled");
            document.getElementById("mac3").setAttribute("disabled","disabled");
            }
            catch(erro){ console.log(erro);}
        }


        else if (dados[2] == "true"){

            nome.setAttribute("value",dados[0]);
            cpf.setAttribute("value",dados[1]);
            setor.setAttribute("value",dados[4]);
            retorno.innerHTML="";
            validar_nome();
        }
        else{

  //      nome.setAttribute("value",dados[0]);
//        cpf.setAttribute("value",dados[1]);
          retorno.innerHTML="Funcionário Inativo";
          nome.setAttribute("value","");
          cpf.setAttribute("value","");
          setor.setAttribute("value","");
          inputmac.setAttribute("disabled","disabled");
          try{
            document.getElementById("mac2").setAttribute("disabled","disabled");
            document.getElementById("mac3").setAttribute("disabled","disabled");
            }
            catch(erro){ console.log(erro);}
        }
       
    }
    };

    xhr.send();

    }
    // }
    // }
  }

  function buscaFuncionarioVisitante(id) {

    matricula=document.getElementById(id).value;
    nome=document.getElementById("nomeautorizador");
    cpf=document.getElementById("cpf");
    filial=document.getElementById("filial");
    setor=document.getElementById("setor");
    retorno=document.getElementById("retorno");
    inputmac = document.getElementById("mac");
    botao_salvar=document.getElementsByClassName("salvar");

    if (matricula){
    //function scene() {
    // if (retorno == 0) {
    let url = "/buscarColaborador/" + matricula;
  
    let xhr = new XMLHttpRequest();
  
    xhr.open("GET", url, false);
  
    xhr.onreadystatechange = function () {

      resposta = xhr.responseText;

      if (xhr.status = 200){

        var dados=resposta.split('-');


        if (dados[0] == '500'){

            if(dados[2]){

            nome.setAttribute("value",dados[2]);
            inputmac.removeAttribute("disabled");
            botao_salvar[0].removeAttribute("disabled");
            retorno.innerHTML="";
            try{
                document.getElementById("mac2").removeAttribute("disabled");
                document.getElementById("mac3").removeAttribute("disabled");
                }
                catch(erro){ console.log(erro);}

            return true

            }
            else{ 
            nome.setAttribute("value","");
            retorno.innerHTML=dados[1]; 
            botao_salvar[0].setAttribute("disabled","disabled");
            inputmac.setAttribute("disabled","disabled");
            try{
                document.getElementById("mac2").setAttribute("disabled","disabled");
                document.getElementById("mac3").setAttribute("disabled","disabled");
                }
                catch(erro){ console.log(erro);}
            
            return true 
        }
        }

        else if (dados[2] =="true"){

            nome.setAttribute("value",dados[0]);
            inputmac.removeAttribute("disabled");
            botao_salvar[0].removeAttribute("disabled");
            retorno.innerHTML="";
            try{
                document.getElementById("mac2").removeAttribute("disabled");
                document.getElementById("mac3").removeAttribute("disabled");
                }
                catch(erro){ console.log(erro);}

        }
        else{

  //      nome.setAttribute("value",dados[0]);
//        cpf.setAttribute("value",dados[1]);
          retorno.innerHTML="Funcionário Solicitante Inativo";
          nome.setAttribute("value","");
          botao_salvar[0].setAttribute("disabled","disabled");
          //cpf.setAttribute("value","");
          //setor.setAttribute("value","");
          inputmac.setAttribute("disabled","disabled");
          try{
            document.getElementById("mac2").setAttribute("disabled","disabled");
            document.getElementById("mac3").setAttribute("disabled","disabled");
            }
            catch(erro){ console.log(erro);}
        }
       
    }
    };

    xhr.send();
    }
    // }
    // }
  }




function validar_mac() {

        nome_classe=document.getElementsByClassName("mac");
        retorno=document.getElementById("retorno");
        botao_salvar=document.getElementsByClassName("salvar");
        macs=[];
        macs_repetidos=[];

         for (var x=0; x < nome_classe.length ;x++ ){
    
            dado=nome_classe[x].value;

            if (dado != ""){

            if (macs_repetidos.indexOf((dado).toString()) < 0){
                console.log("existe");
                }
                else{
                    retorno.innerHTML="Mac já informado";
                    botao_salvar[0].setAttribute("disabled","disabled");
                    macs.push('1');
                }
        
            macs_repetidos.push(dado);

            let url = "/verificacoes/validar_mac@"+dado;
            let xhr = new XMLHttpRequest();
            xhr.open("GET", url, false);
        
            xhr.onreadystatechange = function () {
    
            resposta = xhr.responseText;
            
            if (resposta != "False"){
                
                retorno.innerHTML=resposta;
                botao_salvar[0].setAttribute("disabled","disabled");
                macs.push('1');}};
    
            xhr.send();
        }
    }

    if(macs.length < 1){

        retorno.innerHTML="";
        botao_salvar[0].removeAttribute("disabled");        
        return true;
    }
        
}

function validar_mac_existente() {

        nome_classe=document.getElementsByClassName("mac");
        retorno=document.getElementById("retorno");        
        nome=document.getElementById("nome");
        botao_salvar=document.getElementsByClassName("salvar");
        macs=[];
        macs_repetidos=[];
        
        for (var x=0; x < nome_classe.length ;x++ ){

        dado=nome_classe[x].value;
        
        if (dado != ""){

        if (macs_repetidos.indexOf((dado).toString()) < 0){
            console.log("existe");
            }
            else{
                retorno.innerHTML="Mac já informado";
                botao_salvar[0].setAttribute("disabled","disabled");
                macs.push('1');
            }
    
        macs_repetidos.push(dado);

        let url = "/verificacoes/validar_mac_existente@"+dado+"@"+nome.value;
        let xhr = new XMLHttpRequest();
        xhr.open("GET", url, false);
    
        xhr.onreadystatechange = function () {

        resposta = xhr.responseText;
        
        if (resposta != "False"){

            retorno.innerHTML=resposta;
            botao_salvar[0].setAttribute("disabled","disabled");
            macs.push('1');
            // return false
        }
        };

        xhr.send();
    }
}
         
    if(macs.length < 1){

        retorno.innerHTML="";
        botao_salvar[0].removeAttribute("disabled");

    }
        
        return macs;
}

function validar_mac_dispositivos() {

    id_dispositivo=document.getElementById("id_dispositivo").value;
    mac=document.getElementById("mac").value;
    retorno=document.getElementById("retorno");
    botao_salvar=document.getElementsByClassName("salvar");
    macs=[];


        if (mac != ""){

        let url = "/verificacoes/validar_mac_dispositivos@"+mac+"@"+id_dispositivo;
        let xhr = new XMLHttpRequest();
        xhr.open("GET", url, false);
    
        xhr.onreadystatechange = function () {

        resposta = xhr.responseText;
        
        if (resposta != "False"){
            
            retorno.innerHTML=resposta;
            botao_salvar[0].setAttribute("disabled","disabled");
            macs.push('1');}};

        xhr.send();
    }

if(macs.length < 1){

    retorno.innerHTML="";
    botao_salvar[0].removeAttribute("disabled");        
    return true;
}
    
}

function validar_nome() {

    nome=document.getElementById("nome").value;
    cpf=document.getElementById("cpf").value;
    retorno=document.getElementById("retorno");
    botao_salvar=document.getElementsByClassName("salvar");
    inputmac = document.getElementById("mac");
    macs=[];

        if (nome != "" || cpf != ""){

        let url = "/verificacoes/validar_nome@"+nome+"@"+cpf;
        let xhr = new XMLHttpRequest();
        xhr.open("GET", url, false);
    
        xhr.onreadystatechange = function () {

        resposta = xhr.responseText;
        
        if (resposta != "False"){
            
            retorno.innerHTML=resposta;
            botao_salvar[0].setAttribute("disabled","disabled");
            inputmac.setAttribute("disabled","disabled");
            try{
            document.getElementById("mac2").setAttribute("disabled","disabled");
            document.getElementById("mac3").setAttribute("disabled","disabled");
            }
            catch(erro){ console.log(erro);}
            macs.push('1');}

        else{

            retorno.innerHTML="";
            botao_salvar[0].removeAttribute("disabled");
            inputmac.removeAttribute("disabled");
            try{
            document.getElementById("mac2").removeAttribute("disabled");
            document.getElementById("mac3").removeAttribute("disabled");
            }
            catch(erro){ console.log(erro);}
        }
        };

        xhr.send();
    }


    // if(macs.length < 1 && nome != "" || cpf != ""){

    //     retorno.innerHTML="";
    //     botao_salvar[0].removeAttribute("disabled");        
    //     return true;
    // }
    
}

function validar_nome_existente() {

    nome=document.getElementById("nome").value;
    cpf=document.getElementById("cpf").value;
    retorno=document.getElementById("retorno");
    botao_salvar=document.getElementsByClassName("salvar");
    id_item=document.getElementById("cancelar").value;
    macs=[];

        if (nome != ""){

        let url = "/verificacoes/validar_nome_existente@"+nome+"@"+cpf+"@"+id_item;
        let xhr = new XMLHttpRequest();
        xhr.open("GET", url, false);
    
        xhr.onreadystatechange = function () {

        resposta = xhr.responseText;
        
        if (resposta != "False"){
            
            retorno.innerHTML=resposta;
            botao_salvar[0].setAttribute("disabled","disabled");
            macs.push('1');}};

        xhr.send();
    }

if(macs.length < 1){

    retorno.innerHTML="";
    botao_salvar[0].removeAttribute("disabled");        
    return true;
}
    
}

