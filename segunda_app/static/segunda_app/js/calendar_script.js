document.addEventListener("DOMContentLoaded", function() {
    // Verifica se a variável global datasComCompromissos foi carregada corretamente
    if (typeof datasComCompromissos === 'undefined') {
        console.error("A variável 'datasComCompromissos' não foi definida.");
        return; // Se a variável não estiver definida, interrompe a execução
    }

    // Configura o calendário flatpickr
    flatpickr("#datepicker", {
        locale: "pt",          // Define a localização para português
        dateFormat: "d/m/Y",   // Formato de data brasileiro (dia/mês/ano)
        inline: true,          // Deixa o calendário sempre visível
        defaultDate: "today",  // Define a data atual como padrão
        firstDayOfWeek: 1,     // Define a segunda-feira como o primeiro dia da semana
        onDayCreate: function(dObj, dStr, fp, dayElem) {
            // Converte a data do dia atual do calendário para o formato ISO (YYYY-MM-DD)
            var dateStr = dayElem.dateObj.toISOString().split('T')[0];

            // Verifica se essa data está na lista de datas com compromissos
            if (datasComCompromissos.includes(dateStr)) {
                // Adiciona uma bolinha verde ao dia com compromisso
                var eventMarker = document.createElement('div');
                eventMarker.className = 'event-marker';
                dayElem.appendChild(eventMarker);
            }
        }
    });
});