function validar()
{
    let texto=document.getElementById("#").value;
    if(texto=="")
    {
        document.getElementById("#").className="text-danger"
        document.getElementById("#").innerHTML="Debe ingresar el nombre";
    }
    else
    {
        document.getElementById("#").className="text-success"
        document.getElementById("#").innerHTML="Nombre correcto";
    }

}

function limpiar()
{
    document.getElementById("#").innerHTML="";
    document.getElementById("#").className=""
    document.getElementById("#").innerHTML="";
    document.getElementById("#").value="";
}

var Fn = {
	// Valida el rut con su cadena completa "XXXXXXXX-X"
	validaRut : function (rutCompleto) {
		if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test( rutCompleto ))
			return false;
		var tmp 	= rutCompleto.split('-');
		var digv	= tmp[1]; 
		var rut 	= tmp[0];
		if ( digv == 'K' ) digv = 'k' ;
		return (Fn.dv(rut) == digv );
	},
	dv : function(T){
		var M=0,S=1;
		for(;T;T=Math.floor(T/10))
			S=(S+T%10*(9-M++%6))%11;
		return S?S-1:'k';
	}
}

/* Uso de la función
alert( Fn.validaRut('11111111-1') ? 'Valido' : 'inválido');*/