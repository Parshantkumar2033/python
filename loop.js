const housesForRent=async(url)=>{
  const data = await fetch(url);
  const parsedData = await data.json();
  document.querySelector('.housesForRent thead').innerHTML = 
  `<tr>
    <th scope="col">S. No.</th>
    <th scope="col">City</th>
    <th scope="col">Locality</th>
    <th scope="col">Space (BHK)</th>
    <th scope="col">Amount (Lacs)</th>
    <th scope="col">Reg. Date</th>
    <th scope="col">Contact Seller</th>
  </tr>`;
  let row = document.querySelector('.houseRent');
  parsedData.forEach((element, index)=>{
    row.innerHTML += `<tr>
                        <th scope="row">${index+1}</th>
                        <td>${element.city}</td>
                        <td>${element.locality}</td>
                        <td>${element['space (BHK)']}</td>
                        <td>${element['amount (Lacs)']}</td>
                        <td>${element.date.substring(0, 10)}</td>
                        <td>${element.prop_id}</td>
                      </tr>`;
  });
}

const houseCost=async(url)=>{
  const data = await fetch(url);
  const parsedData = await data.json();
  document.querySelector('.housesCost thead').innerHTML = 
  `<tr>
    <th scope="col">S. No.</th>
    <th scope="col">City</th>
    <th scope="col">Locality</th>
    <th scope="col">Amount (Lacs)</th>
  </tr>`;
  let row = document.querySelector('.houseCost');
  parsedData.forEach((element, index)=>{
    row.innerHTML += `<tr>
                        <th scope="row">${index+1}</th>
                        <td>${element.city}</td>
                        <td>${element.locality}</td>
                        <td>${element['amount (Lacs)']}</td>
                      </tr>`;
  });
}

const addressLocality=async(url)=>{
  const data = await fetch(url);
  const parsedData = await data.json();
  document.querySelector('.addressLocality thead').innerHTML = 
  `<tr>
    <th scope="col">S. No.</th>
    <th scope="col">City</th>
    <th scope="col">Locality</th>
    <th scope="col">Amount (Lacs)</th>
  </tr>`;
  let row = document.querySelector('.adLocality');
  parsedData.forEach((element, index)=>{
    row.innerHTML += `<tr>
                        <th scope="row">${index+1}</th>
                        <td>${element.city}</td>
                        <td>${element.locality}</td>
                        <td>${element['amount (Lacs)']}</td>
                      </tr>`;
  });
}

const agentPropSold=async(url)=>{
  const data = await fetch(url);
  const parsedData = await data.json();
  document.querySelector('.agentMostProp thead').innerHTML = 
  `<tr>
    <th scope="col">S. No.</th>
    <th scope="col">Name</th>
    <th scope="col">Total Amount</th>
  </tr>`;
  let row = document.querySelector('.agentProp');
  parsedData.forEach((element, index)=>{
    row.innerHTML += `<tr>
                        <th scope="row">${index+1}</th>
                        <td>${element.name}</td>
                        <td>${element.total_amount}</td>
                      </tr>`;
  });
}

const agentYear=async(url)=>{
  const data = await fetch(url);
  const parsedData = await data.json();
  document.querySelector('.agentPropYear thead').innerHTML = 
  `<tr>
    <th scope="col">S. No.</th>
    <th scope="col">Name</th>
    <th scope="col">Avg. Selling Price (&#8377)</th>
  </tr>`;
  let row = document.querySelector('.agentYear');
  parsedData.forEach((element, index)=>{
    row.innerHTML += `<tr>
                        <th scope="row">${index+1}</th>
                        <td>${element.agent_name}</td>
                        <td>${element.avg_selling_price.toFixed(2)}</td>
                      </tr>`;
  });
}

const expHouse=async(url)=>{
  const data = await fetch(url);
  const parsedData = await data.json();
  document.querySelector('.expHouse thead').innerHTML = 
  `<tr>
    <th scope="col">S. No.</th>
    <th scope="col">City</th>
    <th scope="col">Locality</th>
    <th scope="col">Space (BHK)</th>
    <th scope="col">Amount (Lacs)</th>
    <th scope="col">Status</th>
  </tr>`;
  let row = document.querySelector('.expensiveHouse');
  parsedData.forEach((element, index)=>{
    row.innerHTML += `<tr>
                        <th scope="row">${index+1}</th>
                        <td>${element.city}</td>
                        <td>${element.locality}</td>
                        <td>${element.status}</td>
                        <td>${element['space (BHK)']}</td>
                        <td>${element['amount (Lacs)']}</td>
                      </tr>`;
  });
}

const sqlQuery=async(url)=>{
  const data = await fetch(url);
  const parsedData = await data.json();
  const columnNames = Object.keys(parsedData[0]);
  columnNames.forEach((element)=>{
    document.querySelector('.query thead tr').innerHTML += `<th scope="col">${element}</th>`;
  });
  let row = document.querySelector('.querySql');
  parsedData.forEach((element, index)=>{
    row.innerHTML += `<tr id="row${index}"></tr>`;
    let td = document.querySelector(`#row${index}`);
    columnNames.forEach((ele)=>{
      td.innerHTML += `<td>${element[ele]}</td>`;
    });
  });
}