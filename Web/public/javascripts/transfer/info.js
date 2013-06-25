function initInfo() {
  Ext.onReady(function() {
    renderPage();
  });
}

function renderPage() {
  var mainContent = createInfoPanel();
  renderInMainViewport([mainContent]);
}

function createInfoPanel() {
  var html = "<p>Hello</p>";
  var mainContent = new Ext.Panel({html:html, region:'center'});
  return mainContent;
}
