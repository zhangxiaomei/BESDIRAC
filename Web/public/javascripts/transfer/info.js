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
  // create Reader
  var reader = new Ext.data.JsonReader({
    root: 'functions',
    totalProperty: 'numRecords',
    id: 'FuncName',
    fields: ["FuncName", "ScriptName"]
  });
  // create Store
  var store = new Ext.data.Store({
    reader: reader,
    url: 'getInfoList',
    autoLoad: true,
    sortInfo: {field: 'FuncName', direction: 'DESC'}
  });
  // Create the panel
  var title = "Transfer System Info"
  var columns = [
    {header: '', 
        name: 'checkBox', 
        id: 'checkBox', 
        dataIndex: 'FuncCheckBox',
        renderer: function(value, metadata, record, rowIndex, colIndex, store) {
          return '<input id="' + record.id + '" type="checkbox" />';
        },
        hideable: false,
        fixed: true,
        menuDisabled: true
    },
    {header: 'Function', sortable: true, dataIndex: 'FuncName'},
    {header: 'Script', sortable: true, dataIndex: 'ScriptName'}
  ];

  var mainContent = new Ext.grid.GridPanel({
    store: store,
    columns: columns,
    region: 'center'
  });
  // End
  //var html = "<p>Hello</p>";
  //var mainContent = new Ext.Panel({html:html, region:'center'});
  return mainContent;
}
