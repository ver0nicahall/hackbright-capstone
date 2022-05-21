function Listing(props) {
  return (
    <div className="listing">
      <a key={props.item.item_id} href={`/items/${props.item.item_id}`}><img class="preview" src={props.item.item_images[0]} /></a>
    </div>
  )
}

function UserProfile() {
  //fetch user's items 
  //load using react 

    return (
      <div>
      </div>
    );
  }
  
  ReactDOM.render(<UserProfile />, document.getElementById('user-div'));