function Listing(props) {
  return (
    <div className="listing">
      <a key={props.item.item_id} href={`/items/${props.item.item_id}`}><img class="preview" src={props.item.item_images[0]} /></a>
    </div>
  )
}

function UserProfile(props) {
  const[items, setItems] = React.useState([]);

  //fetch user's items 
  React.useEffect(() => {
    fetch(`/api/users/${props.user.user_id}/items`)
     .then((response) => response.json())
     .then((data) => {
       setItems(data)
     })
  }, []);

  const itemsImages = [];

  for (const item of items) {
    itemsImages.push( <Listing item={item} />)
  }
   

    return (
        <div id="listings-container">
          {itemsImages}
        </div>
    );
  }
  
  ReactDOM.render(<UserProfile user={user}/>, document.getElementById('user-listings'));