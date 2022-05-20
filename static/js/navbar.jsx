function NavBar() {
    return (
        <div className="navbar">
            <div className="navbar-left">
                <a href="/marketplace">Marketplace</a> | <a href="/create_listing">Create Listing</a> | 
            </div> 
            <div className="navbar-right"> <a href="/my_profile">My Profile</a> |  My Account | <a href="/logout">Logout</a>
            </div>
        </div>
    )
}

ReactDOM.render(<NavBar />, document.getElementById('navbar-container'));