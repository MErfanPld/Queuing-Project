document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript loaded");

    const statusSelects = document.querySelectorAll('select[name="status"]');
    console.log(statusSelects);

    statusSelects.forEach(select => {
        select.addEventListener('change', function () {
            console.log("Status changed:", this.value);
            const appointmentId = this.dataset.appointmentId;
            const newStatus = this.value;

            const formData = new FormData();
            formData.append('appointment_id', appointmentId);
            formData.append('status', newStatus);
            formData.append('csrfmiddlewaretoken', document.querySelector('input[name=csrfmiddlewaretoken]').value);

            fetch("http://127.0.0.1:8000/reservations/update-appointment-status/", {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                console.log('Server Response:', data);
                if (data.success) {
                    alert(data.message);
                } else {
                    alert(data.message || 'خطایی رخ داده است.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('مشکلی در ارتباط با سرور پیش آمد.');
            });
        });
    });
});
