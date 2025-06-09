from fastapi import APIRouter
form app.neural_network import NeuralNetwork

router = APIRouter(prefix="/network", tags=["neuro_net"])

@router.get("/", summary="initialize_neuro_net")
async def init():
    setup = NeuralNetwork.Dynamic_Simple_NN()
    return {"status": "initialized", "inputs": setup.inputs, "outputs": setup.outputs, "layers": setup.layers }    

@router.post("/", summary="Update Neuro Net")
async def update_neuro_net(inputs: int, outputs: int, layers: int):
    """
    Update the neural network configuration.
    """
    setup = NeuralNetwork.Dynamic_Simple_NN(inputs=inputs, outputs=outputs, layers=layers)
    return {"status": "updated", "inputs": setup.inputs, "outputs": setup.outputs, "layers": setup.layers } 