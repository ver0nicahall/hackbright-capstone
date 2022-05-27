//Listing component for the marketplace
function Listing(props) {
  return (
    <div className="listing">
      <a key={props.item.item_id} href={`/items/${props.item.item_id}`}><img className="preview" src={props.item.item_images[0]} /></a>
      <div>{props.item.item_name}</div>
    </div>
  )
}


function Marketplace() {
  const [items, setItems] = React.useState([]);
  const [term, setTerm] = React.useState('');

  //event handler to handle no items found
  function handleNoItemsFound() {
    document.querySelector("#listings-container").innerText = "ERROR: No items were found!"
  }
  
  //AJAX request to API to fetch all items 
  React.useEffect(() => {
    fetch('/api/all_items')
     .then((response) => response.json())
     .then((data) => {
       setItems(data)
     })
    .catch(() => {
      alert('Nothing was found!');
    })
  }, []);

  const itemsImages = []; 

  for (const item of items) {    
    if (item.deleted === false) {
      itemsImages.push( <Listing item={item} />)
    }
  }

//event listener on change or on submit 
  function showListings(evt) {
    evt.preventDefault();
    // alert(`you are searching for ${term}`)
    let filtered_items = []
    //filter results by search term
    //if searching by name:
    let searchType = evt.target.searchby.value;
    //if searching by name:
    if (searchType === "name") {
      for (const item of items) {
        if ((item["item_name"].includes(term))) {
          console.log(item["item_name"]);
          filtered_items.push(item);
        }
      }
    }

    if (searchType === "zipcode") {
      for (const item of items) {
        if ((item["zipcode"] === term)) {
          console.log(item["item_name"]);
          filtered_items.push(item);
        }
      }
    }
    
    //TODO: error handling (why is it returning undefined?)

    //repopulate page with filtered items 
    setItems(filtered_items)


    // if no items found 
    if (filtered_items.length === 0) {
      handleNoItemsFound();
    }
  }

  //callback function for change 
  function searchChange(evt) {
    evt.preventDefault();

    let searchTerm = evt.target.value
    setTerm(searchTerm)
    console.log(term)

  }

  return (
    <div id="app">
        <h1>Cloop Marketplace</h1>
        <form action="/" method="POST" onSubmit={showListings}>
          <input type="text" name="search-term" placeholder="Search:" onChange={searchChange}></input> <label htmlFor="Search by:"> </label>
          <select name="searchby" id="searchby">
            <option value="name">Name</option>
            <option value="zipcode">Location (Zip Code)</option>
            <option value="keyword">Keyword</option>
          </select>
          <span><input type="submit" value="Search"></input></span> 
        </form>

        <div id="listings-container">
          {itemsImages}
        </div>
    </div>
  );
}
  
  ReactDOM.render(<Marketplace />, document.getElementById('marketplace-container'));