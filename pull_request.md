## Как правильно внести свою лепту в Open Source проект:
1. Первое, что необходимо сделать — это создать аккаунт на GitHub (если его ещё у вас нет). Заполняйте его внимательно, так как ваш GitHub профиль — это фактически ваша визитная карточка в мире Open Source.

2. Далее следует ознакомиться с правилами участия в разработке для выбранного вами проекта. Данные правила обычно находятся в файле
**CONTRIBUTING.md**

### Отправка Pull Request

Если вы нашли GitHub Issue, которое хотели бы исправить или же создали свой собственный, то следующим вашим шагом будет отправка соответствующего Pull Request.

Опять же, для начала не забудьте ознакомиться с правилами участия в разработке для выбранного Вами проекта.
Например, вот правила для Yii.

Далее я хотел бы описать наиболее часто встречаемый процесс работы с Git и GitHub при участии в Open Source проектах **(Git Workflow)**.

Этот процесс может отличаться от проекта к проекту, да и в целом он присущ не только Open Source проектам, но и многим закрытым проектам на GitHub и BitBucket.

### Шаг 1 — Подготовка рабочего окружения

Естественно, для разработки вам надо подготовить ваше рабочее окружение. Многие Open Source проекты указывают, как именно необходимо его настроить, какие библиотеки, пакеты, инструменты, их версии и тд необходимы.

Для PHP-проектов обычно вам понадобится приблизительно такой минимальный список
Git;
PHP; (Обычно версии от 5.3+)
MySQL;
Composer.

Кроме того, часто необходим PHPUnit. Обычно он идёт в составе самого проекта и лучше использовать именно его, так как в разных версиях PHPUnit тесты могут попросту не работать и то, что работает у вас с новейшей версии, может не работать на CI сервере проекта, где библиотека более старая.

### Шаг 2 — Создаём копию (Fork) репозитория проекта

Заходим на страницу выбранного Вами проекта и нажимаем кнопку «Fork». Данная команда создаст Вашу собственную копию репозитория данного проекта.

Далее вам необходимо склонировать вашу копию репозитория.
```sh
git clone https://github.com/<Ваше-GitHub-имя>/<Название-Репозитория>.git
```

Далее вам необходимо добавить ветку upstream для проекта, которая будет ссылаться на базовый репозиторий (вариант для Yii)
```sh
cd <Локальная-Папка-Проекта>
git remote add upstream https://github.com/yiisoft/yii2.git
```

### Шаг 3 — Настроим Git

### Шаг 4 — Composer
Далее, в 99% случаев для проекта Вам придётся выполнить загрузку библиотек через Composer
```sh
cd <Локальная-Папка-Проекта>
composer install
```

### Шаг 5 — Тесты

Перед тем, как начать работу, настройте в своей любимой IDE или просто в консоли PHPUnit (реже Behat, PhpSpec и тд) для запуска и работы с тестами.

После настройки запустите тесты для проекта и проверьте что они корректно проходят.

### Шаг 6 — Работаем с кодом

Начиная работать над вашим исправлением, изначально надо создать соответствующую Git ветку, основанную на актуальном коде из базового репозитория.

Выбирайте чётко и лаконично имя ветки, которое отражало бы суть изменений.
Считается хорошей практикой включать в названии ветки номер GitHub issue.
```sh
git fetch upstream
git checkout -b 1234-helper-class-fix upstream/master
```

Теперь вы можете смело приступать к работе над кодом.
Работая, помните о следующих правилах:
Следуйте стандартам кодирования (обычно это PSR-стандарты);
Пишите юнит-тесты, чтобы доказать, что ошибка исправлена, или что новая функция на самом деле работает;
Старайтесь не нарушать обратную совместимость без крайней необходимости;
Используйте простые и логически цельные коммиты;
Пишите чёткие, ясные, полные сообщения при коммите изменений.

### Шаг 7 — Отправляем Pull Request

Пока Вы работали над кодом, в основную ветку проекта могли быть внесены другие изменения. Поэтому перед отправкой ваших изменений Вам необходимо сделать rebase Вашей ветки.
Делается это так:
```sh
git checkout <ИМЯ-ВАШЕЙ-ВЕТКИ>
git fetch upstream
git rebase upstream/master
```

Теперь вы можете отправить Ваши изменения.
```sh
git push origin <ИМЯ-ВАШЕЙ-ВЕТКИ>
```

После этого заходим в ваш репозиторий-клон проекта, в котором вы участвуете и нажимаем кнопку «New Pull Request».
И видим следующую форму:
![Comparing changes](Comparing_changes.png)
Слева необходимо выбрать ветку, в которую Вы хотите смержить изменения (обычно это master, ну а вообще это ветка, на которую вы делали rebase).
Справа — ветку с вашими изменениями.
Далее вы увидите сообщение от GitHub о том, возможно ли автоматически смержить изменения или нет.
В большинстве случаев, вы увидите Able to merge.
Если же есть конфликты, вам скорее всего придётся пересмотреть ваши изменения.

Далее нажимаем кнопку — Create Pull Request.
При заполнение имени и описания вашего Pull Request считается хорошей практикой указывать номер Issue, для которого создан ваш Pull Request.

Обычно для многих крупных проектов настроен CI сервер, часто Travis-CI.

После создания Pull Request он будет прогонять тесты, возможно какие-то инструменты для метрик и так далее. Результы его работы вы увидите в Вашем Pull Request как показано ниже:
![Pull Request](Pull_Request.png)
В случае, если тесты не будут пройдены или билд не будет собран, вы увидите красное сообщение об ошибке и по ссылку Details сможете увидите, что же именно не так. В большинстве случае вам необходимо будет исправить ваш Pull Request, чтобы все проверки проходили успешно.

### Шаг 8 — Перерабатываем Pull Request

Если с вашим Pull Request всё хорошо, то в скором времени он будет смержен кем-то из команды.
Но часто бывает, что разработчики попросят вас внести какие-то изменения.

Для этого просто возвращаемся к шагу 6 и после внесения изменений и коммита выполняем похожие команды:
```sh
git checkout <ИМЯ-ВАШЕЙ-ВЕТКИ>
git fetch upstream
git rebase upstream/master
git push origin <ИМЯ-ВАШЕЙ-ВЕТКИ>
```
### Шаг 9 — Убираемся после себя

После того, как ваш Pull Request был принят или же отвергнут, Вам необходимо удалить ветку с Вашими изменениями.
Делается это просто
```sh
git checkout master
git branch -D <ИМЯ-ВАШЕЙ-ВЕТКИ>
git push origin --delete <ИМЯ-ВАШЕЙ-ВЕТКИ>
```

Вместо последней команды также можно выполнить
```sh
git push origin :<ИМЯ-ВАШЕЙ-ВЕТКИ>
```
[Как правильно внести свою лепту в Open Source проект: простые подсказки](https://habr.com/ru/articles/275219/ "Текст был взят с ресурса habr.com")