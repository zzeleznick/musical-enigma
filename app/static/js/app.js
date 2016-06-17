class Main extends React.Component {
  render() {
    const text = this.props.text
    const name = text.toLowerCase()
    return (
      <div className = {name}>
        {text}
      </div>
    );
  }
}

ReactDOM.render(
  <Main text={"Some Text Here"} />,
  document.getElementById('main')
);
