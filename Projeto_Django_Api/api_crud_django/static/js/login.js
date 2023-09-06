async function logar(){
    dataParams = {
        'login' : $('#typeLoginX')[0].value,
        'senha' : $('#typePasswordX')[0].value
    }
    const result = await $.ajax({
        url: BASE_URL + 'home/verify',
        data: dataParams,
        dataType: 'json',
        method: 'GET',
    });
    if(!result.existe){
        return Swal.fire({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 3000,
            timerProgressBar: true,
            didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
            },
            icon: 'error',
            title: 'Login ou Senha incorretos!'
        })
    }
    return window.location.href = BASE_URL + 'home/listar?ApiKey=' + result.ApiKey;
}