//hide booking form if the item is yours 
function hideBooking() {

}

//event Listener for delete button 
deleteButton = document.querySelector('#delete-button');
deleteButton.addEventListener('click', handleDelete);
// function handleDelete(evt) {
//     alert('This item is going to be deleted!')
//     console.log(evt.target.value);


//     //AJAX request - set item's "deleted" property to true
//     //post request - send item id
//     fetch(`/api/items/${evt.target.value}`, {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//       })
//         .then((response) => response.json())
//         .then((responseJson) => {
//           alert(responseJson);
//         })

// }
//Show delete button if the item is yours
function showDelete() {

}

//show price when hover over item?
function showPrice() {

}