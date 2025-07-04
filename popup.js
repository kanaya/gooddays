document.addEventListener('DOMContentLoaded', function() {
    const generateButton = document.getElementById('generate');
    const outputDiv = document.getElementById('output');
    const outputText = document.getElementById('output-text');
    const copyButton = document.getElementById('copy-button');

    generateButton.addEventListener('click', function() {
        const startDate = new Date(document.getElementById('startDate').value);
        const endDate = new Date(document.getElementById('endDate').value);
        const slots = document.getElementById('slots').value.split(',');
        const suffix = document.getElementById('suffix').value;
        const format = document.getElementById('format').value;
        const noholiday = document.getElementById('noholiday').checked;

        if (isNaN(startDate.getTime()) || isNaN(endDate.getTime())) {
            outputText.textContent = 'Please select valid dates';
            return;
        }

        let output = '';
        
        // Function to check if a date is a holiday
        function isHoliday(date) {
            // Simple holiday check - you might want to implement a more comprehensive holiday checker
            const holidays = [
                { month: 1, day: 1 }, // New Year's Day
                { month: 1, day: 2 }, // Bank Holiday
                { month: 1, day: 3 }, // Bank Holiday
                { month: 1, day: 10 }, // Coming of Age Day
                { month: 2, day: 11 }, // National Foundation Day
                { month: 2, day: 23 }, // The Emperor's Birthday
                { month: 3, day: 20 }, // Vernal Equinox Day
                { month: 4, day: 29 }, // Showa Day
                { month: 5, day: 3 }, // Constitution Memorial Day
                { month: 5, day: 4 }, // Greenery Day
                { month: 5, day: 5 }, // Children's Day
                { month: 7, day: 17 }, // Marine Day
                { month: 8, day: 11 }, // Mountain Day
                { month: 9, day: 18 }, // Respect for the Aged Day
                { month: 9, day: 23 }, // Autumnal Equinox Day
                { month: 10, day: 9 }, // Culture Day
                { month: 11, day: 3 }, // Culture Day
                { month: 11, day: 23 }, // Labor Thanksgiving Day
            ];

            const dateObj = new Date(date);
            const month = dateObj.getMonth() + 1;
            const day = dateObj.getDate();

            return holidays.some(holiday => holiday.month === month && holiday.day === day);
        }

        // Generate the output
        for (let date = new Date(startDate); date <= endDate; date.setDate(date.getDate() + 1)) {
            if (noholiday && isHoliday(date)) continue;
            
            const formattedDate = date.toLocaleDateString('ja-JP', {
                month: '2-digit',
                day: '2-digit',
                weekday: 'short'
            });
            
            slots.forEach(slot => {
                output += format.replace('{}', formattedDate)
                              .replace('{}', slot)
                              .replace('{}', suffix) + '\n';
            });
        }

        outputText.textContent = output;
    });

    // Add copy functionality
    copyButton.addEventListener('click', function() {
        const textToCopy = outputText.textContent;
        if (textToCopy) {
            navigator.clipboard.writeText(textToCopy)
                .then(() => {
                    copyButton.textContent = 'Copied!';
                    setTimeout(() => {
                        copyButton.textContent = 'Copy to Clipboard';
                    }, 2000);
                })
                .catch(err => {
                    console.error('Failed to copy text: ', err);
                });
        }
    });
});
