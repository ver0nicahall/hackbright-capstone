function Listing(props) {
    return (
        <div className="listing">
            <p>{props.item_name}</p>
        </div>
    );
}

function ListingContainer() {
    const listings = [];
    for (const item of items) {
        listings.push(
            <Listing 
                item_name={item.item_name}
            />);
    }

    return (
        <div>
            {listings}
        </div>
    )
}

ReactDOM.render( <ListingContainer />, document.querySelector('#marketplace-listings'));