html_template = '''
<!DOCTYPE html>
<html>
<head>
  <title>My profile</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
</head>
<body>
  <div class="container">
    <h1>{Pavlo}</h1>
    {photo}
    <div class="row">
      <div class="col-md-8">
        <h2>Про мене нема шо написати</h2>
        <p>{about}</p>
      </div>
    </div>

    <h2>Список виконаних домашніх завдань</h2>
    <table class="table">
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
  </div>
</body>
</html>
'''

def generate_task_table(tasks):
    table = ''
    for task, grade in tasks:
        table += f'<tr><td>{task}</td><td>{grade}</td></tr>'
    return table


def generate_experience(experience):
    items = ''
    for company in experience:
        items += f'''
        <li>
          <h4>{company['HanseGroup']}</h4>
          <p>{company['6 years']}</p>
          <p>{company['Mane manager']}</p>
          <p>{company['Building yachts']}</p>
        </li>
        '''
    return items


name = "Pavlo"
about = "Short info about me"
tasks = [("Завдання 1", "5"), ("Завдання 2", "5"), ("Завдання 3", "5")]
experience = [
    {
        "name": "HanseGroup",
        "period": "2015-2021",
        "responsibilities": "Building boats",
        "achievements": "Can fix any boats"
    }
]