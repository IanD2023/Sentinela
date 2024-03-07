function activelink(id){

        menus=document.getElementsByClassName("nav-link link-dark")

        for (let i=0; i < menus.length ; i++){
         
         idMenu=menus[i].id;
        // console.log(idMenu)

         if (idMenu == id){

            document.getElementById(idMenu).setAttribute("class", "nav-link link-dark active");}
        
         else {

            document.getElementById(idMenu).setAttribute("class", "nav-link link-dark");}
            
        }

        if(id == "chamadosBotao"){

            document.getElementById('botao_job').setAttribute('class','d-flex');
        }
        else{

            document.getElementById('botao_job').setAttribute('class','d-none');
        }

    }    

    activelink(document.getElementById('menu').value);

$("#botaomenu").click(
    
    function () {
    //activelink("semConexao","/semconexao")
    menus = document.getElementById('botaomenu')

    if (menus.name == '0'){
     document.getElementById('nav_bar').setAttribute("style", "margin-left:10px");
     document.getElementById('container').setAttribute("style", "margin-left:10px");
     document.getElementById('menus').setAttribute("style", "position: fixed;height: 100%;margin-left: -200px;");
     document.getElementById('div_botao').setAttribute("class", "");
     
     menus.setAttribute('name','1')
    } 
    else {

        document.getElementById('nav_bar').setAttribute("style", "margin-left:200px");
        document.getElementById('container').setAttribute("style", "margin-left:200px");
        document.getElementById('menus').setAttribute("style", "position: fixed;height: 100%;");
        document.getElementById('div_botao').setAttribute("class", "collapse navbar-collapse");
        
        menus.setAttribute('name','0') 

    }
}
)

$(".trTabela").click(function () {

    let id = $(this).attr("mac_address-id");

    let pagina = "/editar/"+id;
        
    $("#modalChamados").modal("show");
    $("#modal").load(pagina);

});   
    
$("#criar").click(function (){

    let pagina = "/criar/";
            
        
        $("#modalChamados").modal("show");
        $("#modal").load(pagina);
    })

    
    $("#criar_dispositivo").click(function (){

        let pagina = "/criar_dispositivo/";
                        
            $("#modalChamados").modal("show");
            $("#modal").load(pagina);
        })


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
    inputipo.name=("tipo"+(dispositivos).toString());
    inputId.name=("mac_id_"+(dispositivos).toString());
    inputMac.value="";
    inputId.value="";

    div.appendChild(elementoClone);
    // }
}
    })







//console.log(JSON.parse(xhr.responseText));
    