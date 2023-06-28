html_template = '''
<!DOCTYPE html>
<html>
<head>
 <title>Мій профіль/title>########
 <link 
   function addFriend() {
     var addButton = document.getElementById('addFriendButton');
     addButton.disabled = true;
     addButton.textContent = 'Очікується підтвердження';

     var friendCountElement = document.getElementById('friendCount');
     friendCountElement.textContent = parseInt(friendCountElement.textContent) + 1;
   }

   function toggleMessageButtonColor() {
     var messageButton = document.getElementById('messageButton');
     messageButton.classList.toggle('message-button-color');
   }

   function toggleOfferJobButton() {
     var offerJobButton = document.getElementById('offerJobButton');
     var addFriendButton = document.getElementById('addFriendButton');
     if (offerJobButton.style.display === 'none') {
       offerJobButton.style.display = 'block';
       addFriendButton.style.display = 'none';
     } else {
       offerJobButton.style.display = 'none';
       addFriendButton.style.display = 'block';
     }
   }

   function submitHomework() {
     var homeworkTable = document.getElementById('homeworkTable');
     var newRow = homeworkTable.insertRow();
     var taskCell = newRow.insertCell(0);
     var gradeCell = newRow.insertCell(1);
     taskCell.textContent = 'New Homework Task';
     gradeCell.textContent = 'A+';
   }
 </script>
</head>
<body>
 <div class="container">
   <h1>{name}</h1>
   {photo}
   <div class="row">
     <div class="col-md-8">
       <h2>Про мене нема шо написати</h2>
       <p>{about}</p>
     </div>
   </div>

   <h2>Список виконаних домашніх завдань</h2>
   <table id="homeworkTable" class="table">
     <thead>
       <tr>
         <th>Назва завдання 1-26</th>
         <th>Оцінка: 6</th>
       </tr>
     </thead>
     <tbody>
       {tasks}
     </tbody>
   </table>

   <h2>Досвід роботи</h2>
   <ul>
     {experience}
   </ul>

   <div class="friend-count">Friends: <span id="friendCount">{friend_count}</span></div>
   <button id="addFriendButton" onclick="addFriend()">Додати в друзі</button>
   <button id="messageButton" onclick="toggleMessageButtonColor()">Написати повідомлення</button>
   <button id="offerJobButton" onclick="toggleOfferJobButton()" style="display: none;">Запропонувати роботу</button>
   <button onclick="submitHomework()">Здати ДЗ</button>