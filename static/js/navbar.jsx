function NavBar() {
    return (
        <div className="navbar">
            <span id="navbar-left">
                <a href="/marketplace">Marketplace</a> | <a href="/create_listing">Create Listing</a> | 
            </span> 
            <span id="navbar-right"> <a href="/my_profile">My Profile</a> |  My Account | <a href="/logout">Logout</a>
            </span>
        </div>
    )
}

ReactDOM.render(<NavBar />, document.getElementById('navbar-container'));