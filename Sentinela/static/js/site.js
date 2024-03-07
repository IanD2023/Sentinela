function activelink(id){

        menus=document.getElementById(id);
        menus.setAttribute("style","background-color:#353935;color:white");

}


function checkDevice() {
    if( navigator.userAgent.match(/Android/i)
    || navigator.userAgent.match(/webOS/i)
    || navigator.userAgent.match(/iPhone/i)
    || navigator.userAgent.match(/iPad/i)
    || navigator.userAgent.match(/iPod/i)
    || navigator.userAgent.match(/BlackBerry/i)
    || navigator.userAgent.match(/Windows Phone/i)
    ){
       return true; // está utilizando celular
     }
    else {
       return false; // não é celular
     }
}

if (checkDevice() == true){

    document.getElementById('botaoBar').setAttribute("class","shadow");
    document.getElementById('container').setAttribute("style","margin-left:10px");
    document.getElementById('menus').setAttribute("style", "position: fixed;height: 100%;margin-left: -200px;");

    document.getElementById('fecharBar').setAttribute("class", "d-flex justify-content-end h5");

}


activelink(document.getElementById('menu').value);

$(".excluir").click(function () {

    let id = $(this).attr("id");

    let pagina = "excluir/"+id;
        
    $("#modalChamados").modal("show");
    $("#modal").load(pagina);

});

$("#botaomenu").click(

    function () {

    this.name="1";
    this.class="d-none";

    document.getElementById('botaoBar').setAttribute("class", "d-none");
    document.getElementById('container').setAttribute("style", "display:none");
    document.getElementById('menus').setAttribute("style", "position: fixed;height: 100%;width:100%");
    
});

$("#fecharBar").click(

    function () {
        
        document.getElementById('container').setAttribute("style","margin-left:10px");
        document.getElementById('menus').setAttribute("style", "position: fixed;height: 100%;margin-left: -200px");
        document.getElementById('botaoBar').removeAttribute("class", "shadow");
        this.name='0';
    
    
});

function abrirModal(link){

    $("#modalChamados").modal("show");
    $("#modal").load(link);
}


function editar(id,link){

    let pagina = link+id;
        
    $("#modalChamados").modal("show");
    $("#modal").load(pagina);

}

$(".excluir").click(function () {

    let id = $(this).attr("id");

    let pagina = "excluir/"+id;
        
    $("#modalChamados").modal("show");
    $("#modal").load(pagina);

});

$("#adicionar_dispositivo").click(function (){

    var div = document.getElementById('form_editar');
    var dispositivos = document.getElementsByClassName('dispositivos').length;
    var elementoOriginal = document.getElementById('dispositivos');// elemento1

    //console.log(dispositivos+=1)

    if (dispositivos < 3){

    // for (var x = 0;x > 3; x++){

    var elementoClone = elementoOriginal.cloneNode(true);
    var inputMac=elementoClone.children[1];
    var inputId=elementoClone.children[2];
    var inputipo=elementoClone.children[5];

    inputMac.name=("mac"+(dispositivos+=1).toString());
    inputMac.id=("mac"+(dispositivos).toString());
    inputMac.removeAttribute("required");
    inputipo.name=("tipo"+(dispositivos).toString());
    inputId.name=("mac_id_"+(dispositivos).toString());
    inputMac.value="";
    inputId.value="";
    console.log(inputipo);

    div.appendChild(elementoClone);

    // }
}
    })


//Modal config

modal=document.getElementById('modalChamados');

$(document).ready(function() {

    $("#modalChamados").modal({
    backdrop: 'static',
    keyboard: false
    }); 

})

function closeModal(link){

    $("#modalChamados").modal("hide");

    window.location.href=link;
}

$(".cancelar").click(function () {

        $("#modalChamados").modal("hide");
        location.reload(); 
});


$("#criarFuncionarioModal").click(function () {

    //if ( verificacoes('validar_mac','mac') == true){
        
        document.getElementById("formFuncionario").submit();
    //}
    
});

function procurar(nome){

    buscar=document.getElementById('busca');
    buscar.value="";
    label_busca=document.getElementById('label_busca');

    buscar.placeholder=nome;
    buscar.name=nome.toLowerCase(nome);
    label_busca.innerHTML="Buscar "+nome;

}



function criaMascara() {
    
    mac = document.getElementsByName("mac1");
    mac2 = document.getElementsByName("mac2");
    mac3 = document.getElementsByName("mac3");
    mac4 = document.getElementsByName("mac");

    //novoMac = mac[0].value.replace(/([^0-9])+/g, "");

    if (mac.length > 0){

    novoMac = mac[0].value
      .replace(/[^0-9a-f]/g, "")
      .replace(/(\w{2})(\w{2})(\w{2})(\w{2})(\w{2})(\w{2})/, "$1-$2-$3-$4-$5-$6");
    mac[0].value = novoMac;

    }
    
    if (mac2.length > 0){
    novoMac2 = mac2[0].value
      .replace(/[^0-9a-f]/g, "")
      .replace(/(\w{2})(\w{2})(\w{2})(\w{2})(\w{2})(\w{2})/, "$1-$2-$3-$4-$5-$6");
    mac2[0].value = novoMac2;
    }
  
    if (mac3.length > 0){
    novoMac3 = mac3[0].value
      .replace(/[^0-9a-f]/g, "")
      .replace(/(\w{2})(\w{2})(\w{2})(\w{2})(\w{2})(\w{2})/, "$1-$2-$3-$4-$5-$6");
    mac3[0].value = novoMac3;
    }

    if (mac4.length > 0){
    novoMac4 = mac4[0].value
      .replace(/[^0-9a-f]/g, "")
      .replace(/(\w{2})(\w{2})(\w{2})(\w{2})(\w{2})(\w{2})/, "$1-$2-$3-$4-$5-$6");
    mac4[0].value = novoMac4;
    }

  }
