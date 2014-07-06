var socket = require( "dgram" ).createSocket( "udp4" );

var response = new Buffer("\377\377\377\377getstatus")
socket.on(
	"message",
	function ( message, requestInfo ) {
		//response that we get from the udp server
    	console.log("Message: " + message + " from " +requestInfo.address + ":" + requestInfo.port);
	
	 	socket.send(
            response,
            0, //offset
            response.length,
            requestInfo.port,
            requestInfo.address,
            function( error, byteLength ) {
 
                console.log( "... Sent response to " + requestInfo.address + ":" + requestInfo.port );
 
            }
        );


	}
);

socket.on(
	"error",
	function ( error ) {
	//error handling 
	console.log("Something went wrong! The error says: "+error)
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
 
function getServerResponse(host,port){
    //under construction!
    
	socket.bind(port,host);		
		
}
//testing urt server 
getServerResponse("209.190.50.170",27960)