//Event handler to make navbar sticky

//when user scrolls, execute function to make navbar stick 
window.onscroll = function() {makeSticky()};

//get navbar
let navbarContainer = document.querySelector('#navbar-container')
//get offset position of navbar
let sticky = navbarContainer.offsetTop;

function makeSticky() {
    //when the page scrolls down
    if (window.pageYOffset >= sticky) {
        //add sticky class to navbar
        navbar.classList.add("sticky")
    } else {
        navbar.classList.remove("sticky");
    }
}

//Event handler to show edit form if user clicks edit button
let editDetails = document.querySelector('#edit-details')
let editButton = document.querySelector('#edit-button')
let noneditDetails = document.querySelector('#nonedit-details');

//function to show edit form and hide description
function showEditForm() {
    //hide description form
    noneditDetails.style.display = "none";
    //show edit form
    editDetails.style.display = "block";

}

//function to hide edit form and show description
function hideEditForm() {
    //hide edit form 
    editDetails.style.display = "none";
    noneditDetails.style.display = "block";
}

editButton.addEventListener('click', showEditForm)
//Event handler to handle change submissions in description 

editForm = document.querySelector('#edit-form');
function handleEditChanges(evt) {
    evt.preventDefault();
    console.log("window.location:", window.location.pathname)

    let itemName = document.querySelector('#item-name-field').value
    let description = document.querySelector('#description-field').value
    let price = document.querySelector('#price-field').value
    let city = document.querySelector('#city-field').value
    let state = document.querySelector('#state-field').value
    let zipcode = document.querySelector('#zipcode-field').value

    //get form inputs 
    const formInputs = {
        itemName: itemName,
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
            
            document.querySelector('#item-name-span').textContent = data["item_name"]
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
