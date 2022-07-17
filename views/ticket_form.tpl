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


<li><input type="submit" value="Submit"></li>
</ul>
</form>
</div>
