function Marketplace() {
  const [items, setItems] = React.useState([]);

  React.useEffect(() => {
    fetch('/api/all_items')
     .then((response) => response.json())
     .then((data) => {
       setItems(data)
     })
  }, []);

  // if (items.length === 0) {
  //   return <p>Loading...</p>
  // }

  const itemsImages = []; 

  for (const item of items) {
    itemsImages.push(<div><a key={item.item_id} href={`/items/${item.item_id}`}><img src={item.item_images[0]} className="preview"/></a></div>)
  }

//event listener on change or on submit 

  return (
    <div id="app">
        <h1>Cloop Marketplace</h1>
        <div id="listings-container">
          {itemsImages}
        </div>
    </div>
  );
}
  
  ReactDOM.render(<Marketplace />, document.getElementById('marketplace-container'));