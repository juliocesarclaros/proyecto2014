$(function($){
	var socket=io();
	$("#partida").submit(function(event) {
		//enviar
		socket.emit("crearpartida",$(this).serializeArray());
		return false;
	});
	//escuchar al servidor
	socket.on("crearpartida",function(server){
		html="<ul id='partidas'>";
		for(var i=0;i<server.length;i++)
		{
			html+="<li><table>";
			html+="<tr><td>TITULO DE LA PARTIDA</td><td>"+server[i].titulo+"</td></tr>";
			html+="<tr><td>TITULO DE LA PARTIDA</td><td>"+server[i].trespuesta+"</td></tr>";
			html+="</table></li>";
			$("#container").html(html);
		}
	});
});