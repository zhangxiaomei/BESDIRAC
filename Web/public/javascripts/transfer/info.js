var gMainContent = false;

function initInfo() {
  Ext.onReady(function() {
    renderPage();
  });
}

function renderPage() {
  gMainContent = createInfoPanel();
  renderInMainViewport([gMainContent]);
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
    { handler: function() {
        toggleAll(true)
      },
      text: 'Select all',
      width: 150,
      tooltip: 'Click to select all rows'
    },
    { handler: function() {
        toggleAll(false)
      },
      text: 'Select none',
      width: 150,
      tooltip: 'Click to unselect all rows'
    },
  ];

  var bottombar = new Ext.PagingToolbar({
    pageSize: 50,
    store: store,
    displayInfo: true,
    displayMsg: 'Displaying {0} - {1} of {2}'
  });

  var mainContent = new Ext.grid.GridPanel({
    store: store,
    columns: columns,
    region: 'center',
    tbar: topbar,
    bbar: bottombar
  });
  // End
  //var html = "<p>Hello</p>";
  //var mainContent = new Ext.Panel({html:html, region:'center'});
  return mainContent;
}

// helper functions
function toggleAll( select ) {
  var checkbox = document.getElementsByTagName('input');
  for (var i=0; i < checkbox.length; ++i) {
    if ( checkbox[i].type == 'checkbox' ) {
      checkbox[i].checked = select;
    }
  }
}

function cbStoreBeforeLoad(store, params)
{
  var sortState = store.getSortState();
  var bb = gMainContent.getBottomToolbar();
  store.baseParams = {
    'sortField': sortState.field,
    'sortDirection': sortState.direction,
    'limit': bb.pageSize,
  };
}
