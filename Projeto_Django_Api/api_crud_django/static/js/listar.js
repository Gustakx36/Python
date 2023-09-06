async function insertItem(table, itenInserido){
    tableName = {
        'Login' : 'login',
        'Cliente' : 'cliente',
        'Endereco' : 'endereco',
        'ApiKey' : 'key'
    }[table]
    dataParams = {'ApiKey' : API_KEY}
    for(var i = 0; i < $('.paramsInput' + table).length; i++){
        dataParams[$('.paramsInput' + table)[i].id] = $('.paramsInput' + table)[i].value
    }
    const result = await $.ajax({
        url: BASE_URL + tableName,
        data: dataParams,
        dataType: 'json',
        method: 'POST',
    });
    if(result.insert){
        return window.location.href = BASE_URL + 'home/listar/' + itenInserido + '?ApiKey=' + API_KEY;
    }
    if(result.api_key_error){
        console.log('api')
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
            title: 'ApiKey incorreta!'
        })
    }
    if(!result.existeFk){
        console.log('login')
        tableName = {
            'Cliente' : 'Login',
            'Endereco' : 'Cliente'
        }[table]
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
            title: tableName + ' não existe!'
        })
    }
}

function alterPrepare(listaParams, listaColunas, listaLinhas){
    listaColunas = listaColunas.replaceAll(/[\[\]\']/g, '').split(',')
    listaColunas.splice(0, 1)
    listaLinhas = listaLinhas.replaceAll(/[\[\]\']/g, '').split(',')
    listaLinhas.splice(0, 1)
    let div = '';
    for(var i = 0; i < listaColunas.length; i++){
        div += `
        <div class="params" id="${listaParams}"></div>
        <div class="row g-3 align-items-center" style="margin-bottom: 12px;">
            <div class="col-auto" style="width: 130px;">
                <label for="inputlogin" class="col-form-label">${listaColunas[i]} :</label>
            </div>
            <div class="col-auto">
                <input type="login" id="${listaColunas[i]}" value="${listaLinhas[i].trim()}" class="form-control alterInput" style="border-color: #abaab7;" aria-describedby="passwordHelpInline">
            </div>
        </div>`;
    }
    $('#modalAlterInsert').html(div);
}

async function alterItem(){
    listaParams = $('.params')[0].id.split(',')
    table = listaParams[0]
    idItem = listaParams[1]
    itemDeletedo = listaParams[2]
    tableName = {
        'Login' : 'login',
        'Cliente' : 'cliente',
        'Endereco' : 'endereco'
    }[table]
    dataParams = {'ApiKey' : API_KEY}
    for(var i = 0; i < $('.alterInput').length; i++){
        dataParams[$('.alterInput')[i].id.replaceAll(' ', '')] = $('.alterInput')[i].value
    }
    const result = await $.ajax({
        url: BASE_URL + tableName + '/' + idItem,
        data: dataParams,
        dataType: 'json',
        method: 'POST',
    });
    if(result.update){
        window.location.href = BASE_URL + 'home/listar/' + itemDeletedo + '?ApiKey=' + API_KEY;
    }
}

async function deleteItem(table, idItem, itemDeletedo){
    tableName = {
        'Login' : 'login',
        'Cliente' : 'cliente',
        'Endereco' : 'endereco'
    }[table]
    const result = await $.ajax({
        url: BASE_URL + tableName + '/' + idItem + '?ApiKey=' + API_KEY,
        dataType: 'json',
        method: 'DELETE',
    });
    if(result.delete){
        window.location.href = BASE_URL + 'home/listar/' + itemDeletedo + '?ApiKey=' + API_KEY;
    }
}

async function gerarKey(itemKey){
    const result = await $.ajax({
        url: BASE_URL + 'key',
        dataType: 'json',
        method: 'GET',
    });
    if(result.key_gerada.api_key.length > 0){
        window.location.href = BASE_URL + 'home/listar/'+ itemKey +'?ApiKey=' + API_KEY;
    }
}
