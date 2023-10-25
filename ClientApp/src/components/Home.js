import React, { Component } from "react";

export class Home extends Component {
  static displayName = Home.name;

  constructor(props) {
    super(props);
    this.state = { result: null, loading: true };
    this.loadImage = this.loadImage.bind(this);
    this.predictImageGroup = this.predictImageGroup.bind(this);
  }

  componentDidMount() {}

  static renderMain(result) {
    return null;
  }

  render() {
    let contents = this.state.loading ? (
      <p>
        <em>Loading...</em>
      </p>
    ) : (
      Home.renderMain(this.state.result)
    );
    return (
      <div>
        <h1 id="tabelLabel">Cargar imagen para prediccion</h1>
        <p>Alexander Cuartas Parcial 2</p>
        <button onClick={this.predictImageGroup}>Predecir</button>
        <br></br>
        <br></br>
        <br></br>
        <form>
          <input
            id="file"
            type="file"
            accept="image/jpeg image/png imagejpg"
            onChange={this.loadImage}
          ></input>
        </form>
        {contents}
      </div>
    );
  }
  async loadImage(e) {
    this.setState({ result: { image: e.target.files[0] }, loading: false });
  }
  async predictImageGroup(e) {
    const formData = new FormData();
    formData.append("image", this.state.image);

    const response = await fetch("https://localhost:7040/predict", {
      method: "Post",
      headers: {
        "Content-Type": "application/json",
        accept: "application/json",
      },
      body: JSON.stringify(formData),
    });
    const data = await response.json();
    this.setState({
      result: { image: e.target.files[0], result: data },
      loading: false,
    });
  }
}
