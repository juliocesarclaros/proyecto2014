$(function($){
	var socket=io();
	$("#partida").submit(function(event) {
		
		socket.emit("salaespera/",$(this).serializeObject());
		return false;
	});
	
	socket.on("salaespera/",function(server){
		html="";
		for (var i=0;i<server.length;i++)
		{
			
			html+="<tr><td colspan='2'><a href='/salonchat'><input type='submit' action='' value='INICIAR PARTIDA'></a></td></tr></table>";
		}
		$("#container").html(html);
	});
});