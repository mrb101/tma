// Merchant Signup form POST
$(document).on('submit', '#merchantForm', (e) => {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/m_signup/',
        data: {
            company: $('#id_company').val(),
            salutation: $('#id_salutation').val(),
            f_name: $('#id_f_name').val(),
            l_name: $('#id_l_name').val(),
            email: $('#id_email').val(),
            mobile: $('#id_mobile').val(),
            website: $('#id_website').val(),
            street: $('#id_street').val(),
            state: $('#id_state').val(),
            zip_code: $('#id_zip_code').val(),
            city: $('#id_city').val(),
            industry: $('#id_industry').val(),
            salay: $('#id_salay').val(),
            description: $('#id_description').val(),
            bank: $('#id_bank').val(),
            lead_source: $('#id_lead_source').val(),
            contact_method: $('#id_contact_method').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: (res) => {
            $('#merchantForm')[0].reset();
            const div = document.createElement('DIV');
            div.setAttribute("class", "alert alert-success");
            div.setAttribute("role", "alert");
            div.innerHTML = "Thanks! Your information has been submitted.";
            const msgDiv = document.getElementById('msg');
            msgDiv.appendChild(div);
            $('html,body').scrollTop(0);
            console.log(div);
        },
        error:(res) => {
            console.log('Error');
        },
    })
})
