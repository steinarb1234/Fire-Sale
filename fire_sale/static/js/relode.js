document.addEventListener('DOMContentLoaded', function() {
  if (window.performance && window.performance.navigation.type === window.performance.navigation.TYPE_BACK_FORWARD) {
    window.location.reload();
  }
});
