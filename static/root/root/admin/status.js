document.addEventListener("DOMContentLoaded", function() { 
    const statusSelects = document.querySelectorAll('select[name="status"]');
    
    statusSelects.forEach(select => { 
        select.addEventListener('change', function() { 
            const appointmentId = this.dataset.appointmentId;
            const newStatus = this.value;

            // دریافت توکن CSRF از input مخفی
            const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;

            fetch("/reservations/update-appointment-status/", {
                method: 'POST',
                headers: { 
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrfToken,
                },
                body: new URLSearchParams({ 
                    'appointment_id': appointmentId,
                    'status': newStatus,
                })
            })
            .then(response => response.json())
            .then(data => { 
                console.log(data); // مشاهده پاسخ سرور
                if (data.success) { 
                    alert(data.message); 
                } else { 
                    alert('خطایی رخ داده است.');
                } 
            })
            .catch(error => { 
                console.error('Error:', error);
                alert('مشکلی در ارتباط با سرور پیش آمد.');
            });
        }); 
    }); 
});
