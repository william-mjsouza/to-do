flatpickr("#datepicker", {
    locale: "pt",          // Define a localização para português
    dateFormat: "d/m/Y",   // Formato de data brasileiro (dia/mês/ano)
    inline: true,          // Deixa o calendário sempre visível
    defaultDate: "today",  // Define a data atual como padrão
    firstDayOfWeek: 1      // Define a segunda-feira como o primeiro dia da semana
});