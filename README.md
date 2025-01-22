# SilencerBot 9000 – Strażnik Ciszy dla Programistów

SilencerBot 9000 to zaawansowane urządzenie do monitorowania poziomu hałasu w przestrzeniach programistycznych. Gdy rozmowy przekraczają dopuszczalny poziom, bot natychmiast reaguje, wysyłając wiadomość na firmowy Discord, aby przypomnieć zespołowi o zachowaniu spokoju.

## Jak to działa?
1. **Czujnik hałasu** – Urządzenie wykorzystuje cyfrowy czujnik dźwięku podłączony do Arduino, który monitoruje poziom głośności w pomieszczeniu.
2. **Arduino jako sygnalizator** – Gdy hałas przekroczy określony próg, Arduino wysyła sygnał do komputera.
3. **Pythonowy program komunikacyjny** – Skrypt w Pythonie odbiera sygnał z Arduino i wysyła zapytanie HTTP do serwera.
4. **Serwer API (Express.js)** – Serwer API napisany w Express.js odbiera żądanie i deleguje je do Discord bota.
5. **Bot Discord** – Bot zamieszcza wiadomość na firmowym serwerze Discord, informując zespół o konieczności zachowania ciszy.

Idealne rozwiązanie dla firm, gdzie programiści lubią debatować… ale czasem zapominają, że inni próbują pracować! 🚀

