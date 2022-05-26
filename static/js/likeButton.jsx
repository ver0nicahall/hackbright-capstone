function LikeButton() {

    const [state, setState] = React.useState(null);

    return (
        <button onClick={() => setState(
            { liked: true }
            )}>
          Like
        </button>
      );
}

ReactDOM.render(<LikeButton />, document.querySelector("#like_button_container"));