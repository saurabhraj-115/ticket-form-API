<link rel="stylesheet" href="/css/form_styles.css">
<div id="ticket_form">
<div class="title">Submit a ticket</div>

% if feedback:
    <div class="feedback">{{feedback}}</div>
% end

<form action="create_ticket"  method="post">
<ul>
  <li><input type="text" placeholder="your name"
    name="name" class="field" required></li>

    <li><input type="text" placeholder="your email"
      name="email" class="field" required></li>

  <li><input type="text" placeholder="ticket subject"
    name="subject" class="field" required></li>

  <li><textarea placeholder="what's the problem?"
    name="description" rows="6" class="field" required></textarea></li>

  
    <!-- <script>
      window.sprChatSettings = window.sprChatSettings || {};
      window.sprChatSettings = {"appId":"62b32b859d508e7d5a6be781_app_300066307","skin":"MODERN"};
  </script>
   -->
  <script>
  (function(){var t=window,e=t.sprChat,a=e&&!!e.loaded,n=document,r=function(){r.m(arguments)};r.q=[],r.m=function(t){r.q.push(t)},t.sprChat=a?e:r;var o=function(){var e=n.createElement("script");e.type="text/javascript",e.async=!0,e.src="https://prod3-live-chat.sprinklr.com/api/livechat/handshake/widget/"+t.sprChatSettings.appId,e.onerror=function(){t.sprChat.loaded=!1},e.onload=function(){t.sprChat.loaded=!0};var a=n.getElementsByTagName("script")[0];a.parentNode.insertBefore(e,a)};"function"==typeof e?a?e("update",t.sprChatSettings):o():"loading"!==n.readyState?o():n.addEventListener("DOMContentLoaded",o)})()
  </script>

<a href="./newpage">New Page</a>

<li><input type="submit" value="Submit"></li>
</ul>
</form>
</div>
