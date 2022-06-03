function NavBar() {
    return (
        <nav id="navbar" className="navbar navbar-style navbar-fixed-top">
            <div className="col">
                <span id="navbar-left">
                    <a href="/marketplace">Marketplace</a> | <a href="/create_listing">Create Listing</a> | <a href="/my_profile">My Profile</a> 
                </span> 
            </div> 
            <div className="col">
                <span id="navbar-right">
                    My Rentals | <a href="/my_messages">Messages</a> | <a href="/logout">Logout</a>
                </span>
            </div>
        </nav>
    )
}

ReactDOM.render(<NavBar />, document.getElementById('navbar-container'));