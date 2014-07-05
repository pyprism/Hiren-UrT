var socket = require( "dgram" ).createSocket( "udp4" );

socket.on(
	"message",
	function ( message, requestInfo ) {
		//response that we get from the udp server
    	console.log("Message: " + message + " from " +requestInfo.address + ":" + requestInfo.port);
	}
);

socket.on(
	"error",
	function ( error ) {
	//error handling 
	socket.close(); 
	}
);
 
 
socket.on(
	"listening",
	function () {
		var address = socket.address();	 
		console.log( "socket listening " + address.address + ":" + address.port );
	 
	}
);
 
function getServerResponse(address){
    //pass it udp server address 
	socket.bind(address);
}