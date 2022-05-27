//Event handler to show edit form if user clicks edit button
editDetails = document.querySelector('#edit-details')
editButton = document.querySelector('#edit-button')
itemDetails = document.querySelector('#item-details');

//function to show edit form and hide description
function showEditForm() {
    //hide description form
    itemDetails.style.display = "none";
    //show edit form
    editDetails.style.display = "block";

}

//function to hide edit form and show description
function hideEditForm() {
    //hide edit form 
    editDetails.style.display = "none";
    itemDetails.style.display = "block";
}

editButton.addEventListener('click', showEditForm)
//Event handler to handle change submissions in description 

editForm = document.querySelector('#edit-form');
function handleEditChanges(evt) {
    evt.preventDefault();
    console.log("window.location:", window.location.pathname)

    let description = document.querySelector('#description-field').value
    let price = document.querySelector('#price-field').value
    let city = document.querySelector('#city-field').value
    let state = document.querySelector('#state-field').value
    let zipcode = document.querySelector('#zipcode-field').value

    //get form inputs 
    const formInputs = {
        description: description,
        price: price,
        city: city,
        state: state,
        zipcode: zipcode,
    }

    //get URL
    splitPath = window.location.pathname.split('/')
    itemID = splitPath[splitPath.length - 1]
    console.log('itemID: ', itemID)

    //ajax request
    fetch(`/items/${itemID}`, {
        method: 'PATCH',
        body: JSON.stringify(formInputs),
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            console.log(data["price"]);
            
            document.querySelector('#description-span').textContent = data["description"]
            document.querySelector('#price-span').textContent = data["price"]
            document.querySelector('#city-span').textContent = data["city"]
            document.querySelector('#state-span').textContent = data["state"]
            document.querySelector('#zipcode-span').textContent = data["zipcode"]

            //hide edit form again 
            hideEditForm();


        })
}

editForm.addEventListener('submit', handleEditChanges)
//Event handler show price when hover over item?
