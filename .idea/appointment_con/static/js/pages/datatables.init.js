/*
Template Name: Velzon - Admin & Dashboard Template
Author: Themesbrand
Website: https://Themesbrand.com/
Contact: Themesbrand@gmail.com
File: datatables init js
*/

document.addEventListener('DOMContentLoaded', function () {
    let table = new DataTable('#example',);
});


document.addEventListener('DOMContentLoaded', function () {
  let table = new DataTable('#scroll-vertical', {
      "scrollY":        "210px",
      "scrollCollapse": true,
      "paging":         false
    });
    
});

document.addEventListener('DOMContentLoaded', function () {
  let table = new DataTable('#scroll-horizontal', {
      "scrollX": true
    });
});

document.addEventListener('DOMContentLoaded', function () {
  let table = new DataTable('#alternative-pagination', {
      "pagingType": "full_numbers"
    });
});

$(document).ready(function() {
    var t = $('#add-rows').DataTable();
    var counter = 1;
 
    $('#addRow').on( 'click', function () {
        t.row.add( [
            counter +'.1',
            counter +'.2',
            counter +'.3',
            counter +'.4',
            counter +'.5',
            counter +'.6',
            counter +'.7',
            counter +'.8',
            counter +'.9',
            counter +'.10',
            counter +'.11',
            counter +'.12'
        ] ).draw( false );
 
        counter++;
    } );
 
    // Automatically add a first row of data
    $('#addRow').click();
});


$(document).ready(function() {
    $('#example').DataTable({
        order: [[3, 'desc']]
    });
});

//fixed header
document.addEventListener('DOMContentLoaded', function () {
  let table = new DataTable('#fixed-header', {
      "fixedHeader": true
    });
    
}); 

//modal data datables
document.addEventListener('DOMContentLoaded', function () {
  let table = new DataTable('#model-datatables', {
      responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal( {
                    header: function ( row ) {
                        var data = row.data();
                        return 'Details for '+data[0]+' '+data[1];
                    }
                } ),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
                    tableClass: 'table'
                } )
            }
        },
        order: [[1, 'asc']],
        searching: false,
        language: {
            lengthMenu: 'Sayfalarda _MENU_ kayıt göster',
            zeroRecords: 'Kayıt Bulunamadı',
            info: ' _PAGES_ sayfa arasından _PAGE_.sayfa',
            infoFiltered: '(_MAX_ Toplam Kayıt arasından filtrelendi)',
            oPaginate: {
                "sNext":     "Sonraki",
                "sPrevious": "Önceki"
            },
            sSearch:"Ara:",
        },
        columnDefs: [
            { "width": "20%" },
            { responsivePriority: 1, targets: 0 },
        ],
    });
    
}); 

//buttons exmples
document.addEventListener('DOMContentLoaded', function () {
  let table = new DataTable('#buttons-datatables', {
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'print', 'pdf'
        ]
    });
}); 

//buttons exmples
document.addEventListener('DOMContentLoaded', function () {
  let table = new DataTable('#ajax-datatables', {
        "ajax": '/static/json/datatable.json'
    });
}); 


//prices
document.addEventListener('DOMContentLoaded', function () {
    let table = new DataTable('#prices-datatables', {
        responsive: {
            details: {
                display: DataTable.Responsive.display.modal({
                    header: function (row) {
                        var data = row.data();
                        return 'Ücret Detayları';
                    }
                }),
                renderer: DataTable.Responsive.renderer.tableAll()
            }
        },
          paging: false,
          info: false,
          searching: false,
          language: {
              lengthMenu: 'Sayfalarda _MENU_ kayıt göster',
              zeroRecords: 'Kayıt Bulunamadı',
              info: ' _PAGES_ sayfa arasından _PAGE_.sayfa',
              infoFiltered: '(_MAX_ Toplam Kayıt arasından filtrelendi)',
              oPaginate: {
                  "sNext":     "Sonraki",
                  "sPrevious": "Önceki"
              },
              sSearch:"Ara:",
          },
          columnDefs: [
              { "width": "20%" },
              { responsivePriority: 1, targets: 0 },
          ],
      });
      
  }); 

  //users
  document.addEventListener('DOMContentLoaded', function () {
    let table = new DataTable('#user-datatables', {
        responsive: {
              details: {
                  display: $.fn.dataTable.Responsive.display.modal( {
                      header: function ( row ) {
                          var data = row.data();
                          return 'Kullanıcı Detayları ';
                      }
                  } ),
                  renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
                      tableClass: 'table'
                  } )
              }
          },
          order: [[0, 'asc']],
          searching: false,
          language: {
              lengthMenu: 'Sayfalarda _MENU_ kayıt göster',
              zeroRecords: 'Kayıt Bulunamadı',
              info: ' _PAGES_ sayfa arasından _PAGE_.sayfa',
              infoFiltered: '(_MAX_ Toplam Kayıt arasından filtrelendi)',
              oPaginate: {
                  "sNext":     "Sonraki",
                  "sPrevious": "Önceki"
              },
              sSearch:"Ara:",
          },
          columnDefs: [
              { "width": "20%" },
              { responsivePriority: 1, targets: 1 },
          ],
      });
      
  }); 

   //season
   document.addEventListener('DOMContentLoaded', function () {
    let table = new DataTable('#season-datatables', {
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal( {
                    header: function ( row ) {
                        var data = row.data();
                        return ''+data[1]+' Sezonu İçin Detay';
                    }
                } ),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll()
            }
        },
        order: [[0, 'asc']],
        searching: true,
        language: {
            lengthMenu: 'Sayfalarda _MENU_ kayıt göster',
            zeroRecords: 'Kayıt Bulunamadı',
            info: ' _PAGES_ sayfa arasından _PAGE_.sayfa',
            infoFiltered: '(_MAX_ Toplam Kayıt arasından filtrelendi)',
            oPaginate: {
                "sNext":     "Sonraki",
                "sPrevious": "Önceki"
            },
            sSearch:"Ara:",
        },
        columnDefs: [
            { responsivePriority: 1, targets: 1 },
        ],
      });
      
  }); 

    //get-oil
    document.addEventListener('DOMContentLoaded', function () {
        let table = new DataTable('#getoil-datatables', {
            responsive: {
                details: {
                    display: $.fn.dataTable.Responsive.display.modal( {
                        header: function ( row ) {
                            var data = row.data();
                            return ''+data[1]+' Sezonu İçin Detay';
                        }
                    } ),
                    renderer: $.fn.dataTable.Responsive.renderer.tableAll()
                }
            },
            order: [[1, 'asc']],
            searching: false,
            language: {
                lengthMenu: 'Sayfalarda _MENU_ kayıt göster',
                zeroRecords: 'Kayıt Bulunamadı',
                info: ' _PAGES_ sayfa arasından _PAGE_.sayfa',
                infoFiltered: '(_MAX_ Toplam Kayıt arasından filtrelendi)',
                oPaginate: {
                    "sNext":     "Sonraki",
                    "sPrevious": "Önceki"
                },
                sSearch:"Ara:",
            },
            columnDefs: [
                { responsivePriority: 1, targets: 1 },
            ],
          });
          
      }); 

    //sell-oil
    document.addEventListener('DOMContentLoaded', function () {
        let table = new DataTable('#selloil-datatables-1', {
            responsive: {
                details: {
                    display: $.fn.dataTable.Responsive.display.modal( {
                        header: function ( row ) {
                            var data = row.data();
                            return ''+data[1]+' Sezonu İçin Detay';
                        }
                    } ),
                    renderer: $.fn.dataTable.Responsive.renderer.tableAll()
                }
            },
          
            searching: false,
            paging: false,
            language: {
                lengthMenu: 'Sayfalarda _MENU_ kayıt göster',
                zeroRecords: 'Kayıt Bulunamadı',
                info: ' _PAGES_ sayfa arasından _PAGE_.sayfa',
                infoFiltered: '(_MAX_ Toplam Kayıt arasından filtrelendi)',
                oPaginate: {
                    "sNext":     "Sonraki",
                    "sPrevious": "Önceki"
                },
                sSearch:"Ara:",
            },
            columnDefs: [
                { responsivePriority: 1, targets: 1 },
            ],
          });
          
      }); 

        //sell-oil
    document.addEventListener('DOMContentLoaded', function () {
        let table = new DataTable('#customer-datatables', {
            responsive: {
                details: {
                    display: $.fn.dataTable.Responsive.display.modal( {
                        header: function ( row ) {
                            var data = row.data();
                            return ''+data[0]+' İçin Detay';
                        }
                    } ),
                    renderer: $.fn.dataTable.Responsive.renderer.tableAll()
                }
            },
            order: [[2, 'asc']],
            searching: true,
            paging: true,
            language: {
                lengthMenu: 'Sayfalarda _MENU_ kayıt göster',
                zeroRecords: 'Kayıt Bulunamadı',
                info: ' _PAGES_ sayfa arasından _PAGE_.sayfa',
                infoFiltered: '(_MAX_ Toplam Kayıt arasından filtrelendi)',
                oPaginate: {
                    "sNext":     "Sonraki",
                    "sPrevious": "Önceki"
                },
                sSearch:"Ara:",
            },
            columnDefs: [
                { responsivePriority: 1, targets: 0 },
            ],
          });
          
      }); 

              //sell-oil
    document.addEventListener('DOMContentLoaded', function () {
        let table = new DataTable('#debt-datatables', {
            responsive: {
                details: {
                    display: DataTable.Responsive.display.modal({
                        header: function (row) {
                            var data = row.data();
                            return  data[0] + ' Detayları';
                        }
                    }),
                    renderer: DataTable.Responsive.renderer.tableAll()
                }
            },
            
            searching: true,
            paging: true,
            language: {
                lengthMenu: 'Sayfalarda _MENU_ kayıt göster',
                zeroRecords: 'Kayıt Bulunamadı',
                info: ' _PAGES_ sayfa arasından _PAGE_.sayfa',
                infoFiltered: '(_MAX_ Toplam Kayıt arasından filtrelendi)',
                oPaginate: {
                    "sNext":     "Sonraki",
                    "sPrevious": "Önceki"
                },
                sSearch:"Ara:",
            },
            columnDefs: [
                { responsivePriority: 1, targets: 0 },
            ],
          });
          
      }); 

