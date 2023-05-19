README programu
Zapytanie Curl curl -s https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json | jq '.members[].name'
Circuit braker - inaczej bezpiecznik zapobiega wywoływaniu operacji które się nie powidą w niedziłajacej aplikacji przez co nie zwiększa się iloś problemów do rozwiazania. Możliwe jest skocentrowanie na wyszukiwaniu problemu się na rozwiązywaniu konkretnego problemu 
cascading failure - Unikanie cascading failure jest ważne ponieważ pozwala zapobiegać błędom które mogą doprowadzić do awari całej aplkacji. Gdyż błąd w jedej jej części może doprowadzić do błędów w powiązanych z nią czesciach.
greaceful degradation - Pozwala na dziłanie pewnej części aplikacji mimo problemów w inych jej częściach. Jest to ważne gdyż, aplikacja której pewna część cały czas działa i umożliwia kożystanie z niej zapewnia cały czas ruch na stronie co za tym idzie aplkacja cały czas może na siebie zarabiać.
