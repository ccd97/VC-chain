!function($) {
    "use strict";

    var Home = function() {};

    Home.prototype.toggleLoginSignUp  = function() {
      $('#login-button').css('display', 'none');
      $('#signup-a').css('display', 'none');
      $('#regester-form-div').css('display', 'none');

      $('#login-button').click(function(){
        $('#regester-form-div').css('display', 'none');
        $('#login-form-div').css('display', '');
        $('#signup-a').css('display', 'none');
        $('#login-button').css('display', 'none');
        $('#signup-button').css('display', '');
        $('#login-a').css('display', '');
      });

      $('#signup-button').click(function(){
        $('#regester-form-div').css('display', '');
        $('#login-form-div').css('display', 'none');
        $('#signup-a').css('display', '');
        $('#login-button').css('display', '');
        $('#signup-button').css('display', 'none');
        $('#login-a').css('display', 'none');
      });
    },

    Home.prototype.init = function() {
      this.toggleLoginSignUp();
    },
    //init
    $.Home = new Home, $.Home.Constructor = Home
}(window.jQuery),

//initializing
function($) {
    "use strict";
    $.Home.init();
}(window.jQuery);
