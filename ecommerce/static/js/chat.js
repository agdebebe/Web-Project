// $(function(){
// 	let chat =  {}

// 	chat.Message = (key,msg) =>{
// 		const htmlMsg = `
// 					<div class='msg'>
// 						<span> ${msg.username}|${msg.timesince} ago </span>
// 						<p>${msg.message}</p>
// 					</div>
// 				`
// 		$('#chat-messages').append(htmlMsg)
// 	}
// 	chat.fetchMessages = (data)=>{
// 		$.each(data, chat.Message)
// 	}
// 	// fetch messages //
// 	chat.Messages = () => {
// 		$('#chat-messages').html('')
// 		$.ajax({
// 			url:'/api/chat/list',
// 			method:'GET',
// 			success:(data)=>{
// 				chat.fetchMessages(data)
// 			},
// 			error:(error)=>{

// 			}

// 		})
// 	}
// 	//-------------------------------
// 	chat.interval = setInterval(chat.Messages,2000)




// })