function GenerateNames(){
    const InputText = document.getElementById(`input-textarea`);
    const OutputText = document.getElementById(`output-textarea`);

    let InputData = new FormData()
    InputData.append("input_text", InputText)

    fetch(`/generate_names`, {"method":"POST", "body":InputData})
    .then((res) => res.json())
    .then((data) => {OutputText.innerHTML = data["output_text"];});



}