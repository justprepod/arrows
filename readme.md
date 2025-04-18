# Стимфалийские птицы

Игра на 99% сделана vibe-кодингом (значения констант подбиралисть вручную, некоторые изображения взяты со стоков). Никакой архитектуры и общего плана не было. Целью было посмотреть насколько нейронка может держать контекст и обрабатывать большие файлы.

Использовались:
- ChatGPT для кода и спрайтов
- https://www.cleanpng.com и https://pixabay.com для поиска звуков (не вошли в релиз) и спрайтов
- [Yandex SpeechKit](https://yandex.cloud/ru/services/speechkit#demo) для генерации голоса

Наблюдения:
- до 200 строк можно не давать технические указания, ограничиваясь высказыванием пожеланий (не "в функции f проинициализируй переменную x", а "сделай так, чтобы количество слогов в статус-баре соответствовало выбранным словам"), про росте объёмов кода уже приходится тыкать носом в нужное место
- начиная где-то с 400 строк сказываются проблемы, вызванные сильным зацеплением кода, сказывается отсутствие архитектуры
- нейронки по прежнему плохо ориентируются в пространстве и числах, в итоге layout страницы пришлось сократить до примитивного header-body-footer
- самые большие затруднения, как ни странно, вызвала генерация аудио
    - самые лучшие многоязычные нейронки отлично работают с английским языком, но плохо справляются с русским
    - почти все нейронки не умеют произносить отдельно стоящие звуки и слоги, им нужен контекст. Надо либо оборачивать звук фразой, потом вырезать нужный фрагмент, либо использовать TTS-разметку
    - для русского языка yandexgpt рвёт всех конкурентов и даёт возможность использовать TTS разметку
- встроенный в chatgpt генератор изображений даёт возможность задать контекст и осмысленно редактировать изображения, в отличие от того же stablediffusion

Итог:
Даже по подробно расписанному ТЗ рабочий код не получается. Приходится действовать итеративно. Итеративный подход путём уточнения ТЗ работат недолго - код начинает разваливаться. Приходится давать конкретные указания по правкам, это усложняет кривость изначально сгенерированного кода. В следующий раз попробую поручить нейронке разработать архитектуру, а затем итеративно реализовывать функциональность.