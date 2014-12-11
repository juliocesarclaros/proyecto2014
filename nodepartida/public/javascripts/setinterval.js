// var contador=10;

// function restar(){
// 	contador=contador-1;
// 	if(contador==0){
// 		acabarCuentaAtras();
// 	}
// }

// function acabarCuentaAtras(){
// 	clearInterval(temporizador);//paramos la ejecucion del metodo, indicando la variable creada al final
// 	alert("¡TIEMPO!");
// }

// var temporizador=setInterval(function(){restar()},10000); //10s = 10000ms


// JavaScript Document
$(document).ready(function(e) {
	//Si se preciona el boton damos inicio a la funcion que iniciara el progress
	$("#iniciar").click(iniciar);
});
//Iniciar llama a una funcion hilo cada segundo (1000) y le enviamos como parametro la funcion que creamos
function iniciar(){
	var jugada = setInterval(function(){hilo(jugada)}, 1000);
}
//hilo optiene el valor del progress suma su valor +1 y lo actualiza
function hilo(jugada){
	var aux=$("#barra").val()+1;
	$("#barra").val(aux);
	//actualizamos el label del progreso
	$("#lbarra").text(aux+" %");
	//Para este ejemplo detenemos el hilo cuando el valor del progress sea 5
	//Normalmente tendriamos que detener el tiempo en los 100 segundos ya que el valor maximo del progress es 100, pero podriamos modificar ese valor de acuerdo a nuestras necesidades
	if(aux==100){
		clearInterval(jugada);
		alert("Termino el tiempo");
	}
}