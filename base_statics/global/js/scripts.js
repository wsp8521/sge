//Função que aciona a modal de deleção de registros
function modal(element){
  new bootstrap.Modal("#modalDel").show(); //acionando a modal
  var name = element.getAttribute('data-name');
  var page = element.getAttribute('data-page');
  var id = element.getAttribute('data-id'); //pegando os dados passado pelo atributo data-id
  var modalBodyContent = document.getElementById('modalBodyContent'); //elemento que rá receber a mensagem
  var deleteForm = document.getElementById('deleteForm');
 modalBodyContent.textContent = 'Tem certeza que deseja excluir o registro '+ name + '?'; //inserindo mensagem na modal
 deleteForm.action = '/'+page+'/delete/' + id ; //acionando action do form
  }

//função para esconder mensagem de sucesso
function showAndHideSuccessMessage(showTimeout = 0, hideTimeout = 1000) {
  var message = document.getElementById('successMessage');
  if (message) {
      // Mostrar a mensagem após um tempo (útil para dar tempo ao DOM de carregar)
      setTimeout(function() {
          message.classList.add('visible');  // Adiciona a classe que mostra a mensagem

          // Esconder a mensagem após o tempo definido
          setTimeout(function() {
              message.classList.remove('visible');
              message.classList.add('hidden');  // Adiciona a classe que esconde a mensagem

              // Remover o elemento após a transição de ocultar
              setTimeout(function() {
                  message.style.display = 'none';  // Esconde o elemento após a transição
              }, 500);  // Duração da transição de ocultar (0.5 segundos)
          }, hideTimeout);  // Tempo antes de iniciar o desaparecimento
      }, showTimeout);  // Tempo antes de mostrar a mensagem (normalmente 0)
  }
}

function adicionarClasse() {
        // Seleciona todos os elementos <p> dentro do formulário com id 'form-product'
        var paragrafos = document.querySelectorAll("#form-product p");
        
        // Adiciona a classe 'novaClasse' a cada parágrafo encontrado
        paragrafos.forEach(function(paragrafo) {
            paragrafo.classList.add("p");
        });
    }
    

//gráficos
function chartsSales(data_chart_Line, data_chart_bar, data_chart_Doughnut, data_chart_pie){
    document.addEventListener("DOMContentLoaded", function() { // permite interagir com o DOM da página
        var salesValue = JSON.parse(data_chart_Line); // converte os valores no formato JSON
        var salesDaiy = JSON.parse(data_chart_bar); 
        var productCategory = JSON.parse(data_chart_Doughnut); 
        var productBrand = JSON.parse(data_chart_pie); 
               
        chartLine(salesValue);
        chartBar(salesDaiy);
        chartDoughnut(productCategory);
        chartPie(productBrand)
    });
    
}

//grafico tipo linha
function chartLine(dataJson){
    var salesValue = document.getElementById('sales_value').getContext('2d');
    var charSales = new Chart(salesValue, {
        type:'line', //tipo de gráfico
        data: { //dados do grafico
            labels: dataJson.date, 
            datasets: [{
              label: 'valor de vendas',
              data: dataJson.value,
              fill: false,
              borderColor: 'rgb(75, 192, 192)',
              tension: 0.1
            }]
          },
          options: {
            scales: {
                
                y: { beginAtZero: true},
            }
        }

    })
}

//gráfico tipo barra
function chartBar(dataJson){
    var salesValue = document.getElementById('sales_deily').getContext('2d');
    var charSales = new Chart(salesValue, {
        type:'bar', //tipo de gráfico
        data: { //dados do grafico
            labels: dataJson.date, 
            datasets: [{
              label: 'valor de vendas',
              data: dataJson.value,
              fill: false,
              backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
        
              ],
              borderColor: [
                'rgb(255, 99, 132)',
              ],
              borderWidth: 1
            }]
          },
          options: {
            scales: {
                
                y: { beginAtZero: true},
            }
        }

    })
}

//gráfico tipo Doughnut
function chartDoughnut(dataJson){
  var productCategory = document.getElementById('category_product').getContext('2d');
  var chartProductCategory = new Chart(productCategory, {
      type:'doughnut', //tipo de gráfico
      data: { //dados do grafico
          labels: Object.keys(dataJson),
          datasets: [{
            data: Object.values(dataJson),
            borderWidth:1
          }]
        },
        options: {
          plugins: {
            legend: { position: 'left',},
          },
          title: {
            display: true,
            text: 'Categorias de Produtos'
        },
      }

  })
}

//gráfico tipo pizza
function chartPie(dataJson){
  var productCategory = document.getElementById('product_brand').getContext('2d');
  var chartProductCategory = new Chart(productCategory, {
      type:'pie', //tipo de gráfico
      data: { //dados do grafico
          labels: Object.keys(dataJson),
          datasets: [{
            data: Object.values(dataJson),
            borderWidth:1
          }]
        },
        options: {
          plugins: {
            legend: { position: 'right',},
          }
      }

  })
}

