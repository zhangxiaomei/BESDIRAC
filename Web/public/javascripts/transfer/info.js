var gMainContent = false;
var gRequestList = false;
var gFileList = false;
var gSelModel = false;

function initInfo() {
  Ext.onReady(function() {
    renderPage();
  });
}

function renderPage() {
  gMainContent = createInfoPanel();
  renderInMainViewport(gMainContent);
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
    sortInfo: {field: 'FuncName', direction: 'DESC'},
    listeners: {
      beforeload: cbStoreBeforeLoad
    }
  });
  // Create the panel
  var title = "Transfer System Info"
  var columns = [
    {header: '', 
        name: 'checkBox', 
        id: 'checkBox', 
        dataIndex: 'FuncCheckBox',
        renderer: function(value, metadata, record, rowIndex, colIndex, store) {
          var url = gURLRoot + '/' + gPageDescription.selectedSetup + '/' + record.id
          return '<a id="' + record.id + '" href="' + url + '">View</a>';
        },
        hideable: false,
        fixed: true,
        menuDisabled: true
    },
    {header: 'Function', sortable: true, dataIndex: 'FuncName'},
    {header: 'Script', sortable: true, dataIndex: 'ScriptName'}
  ];

  var topbar = [
    { handler: function(wiget, event) {
        showInfo(gRequestList);
      },
      text: 'View Selected',
      width: 150,
      tooltip: 'Click to view selected row'
    },
  ];

  var bottombar = new Ext.PagingToolbar({
    pageSize: 50,
    store: store,
    displayInfo: true,
    displayMsg: 'Displaying {0} - {1} of {2}'
  });

  var grid = new Ext.grid.GridPanel({
    store: store,
    columns: columns,
    region: 'center',
    tbar: topbar,
    bbar: bottombar,
    sm: new Ext.grid.RowSelectionModel({singleSelect:true}),
    width: '50%'
  });
  grid.getSelectionModel().on('rowselect', function(sm, rowIdx, r) {
  }
  );
  // Another grid
  var grid2 = new Ext.grid.GridPanel({
    store: store,
    columns: columns,
    region: 'east',
    width: '50%',
  });
  // End
  //var html = "<p>Hello</p>";
  var mainContent = [grid, grid2];
  gRequestList = grid;
  gFileList = grid2;
  return mainContent;
}

// helper functions
function cbStoreBeforeLoad(store, params)
{
  var sortState = store.getSortState();
  var bb = gRequestList.getBottomToolbar();
  store.baseParams = {
    'sortField': sortState.field,
    'sortDirection': sortState.direction,
    'limit': bb.pageSize,
  };
}

function showInfo( grid ) {
  var selModel = grid.getSelectionModel();
  var rec = selModel.getSelected();
  if (rec) {
    alert(rec.get('ScriptName'));
  }
}
