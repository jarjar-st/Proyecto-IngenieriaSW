var iconoCancelar = '<i class="fas fa-window-close"></i>';
var iconoEditar = '<i class="fas fa-edit"></i>';

$("#link_activar_formulario").click(function( event ) {
    event.preventDefault();
    if($("#update_div").attr("hidden")){
        showEditProfileForm();
        hideChangePasswordForm();
        activateEditProfileForm();
    }else{
        deactivateEditProfileForm();
    }
});

$("#link_cambiar_password").click(function( event ) {
    event.preventDefault();
    if($("#form-change-password").attr("hidden")){
        showChangePasswordForm();
        hideEditProfileForm();
    }else{
        showEditProfileForm();
        hideChangePasswordForm();
    }
});

function hideEditProfileForm(){
    $("#form-edit-profile").attr("hidden",true);
    if(!$("#update_div").attr("hidden")){
        $("#update_div").attr("hidden", true);
        $("#id_first_name").attr("readonly", true);
        $("#id_last_name").attr("readonly", true);
        $("#id_birth_date").attr("readonly", true);
        $("#id_phone_number").attr("readonly", true);
        $("#id_address").attr("readonly", true);
        $("#link_activar_formulario").html(iconoEditar+' Editar mi perfil');
    }
}

function showEditProfileForm(){
    $("#form-edit-profile").attr("hidden",false);
    $("#link_activar_formulario").html(iconoEditar+' Editar mi perfil');
}

function activateEditProfileForm(){
    $("#update_div").attr("hidden", false);
    $("#id_first_name").attr("readonly", false);
    $("#id_last_name").attr("readonly", false);
    $("#id_birth_date").attr("readonly", false);
    $("#id_phone_number").attr("readonly", false);
    $("#id_address").attr("readonly", false);
    $("#link_activar_formulario").html(iconoCancelar+' Cancelar editar');
}

function deactivateEditProfileForm(){
    $("#update_div").attr("hidden", true);
    $("#id_first_name").attr("readonly", true);
    $("#id_last_name").attr("readonly", true);
    $("#id_birth_date").attr("readonly", true);
    $("#id_phone_number").attr("readonly", true);
    $("#id_address").attr("readonly", true);
    $("#link_activar_formulario").html(iconoEditar+' Editar mi perfil');
}

function hideChangePasswordForm(){
    $("#form-change-password").attr("hidden",true);
    $("#link_cambiar_password").html(iconoEditar+' Cambiar contraseña');
}

function showChangePasswordForm(){
    $("#form-change-password").attr("hidden",false);
    $("#link_cambiar_password").html(iconoCancelar+' Cancelar cambio de contraseña');
}