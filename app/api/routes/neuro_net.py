from fastapi import APIRouter

from app.neural_network.dynamic_simple_nn import Dynamic_Simple_NN

nn_router = APIRouter(prefix="/network", tags=["neuro_net"])


@router.get("/", summary="initialize_neuro_net")
async def init():
    setup = Dynamic_Simple_NN()
    return {
        "status": "initialized",
        "inputs": setup.inputs,
        "outputs": setup.outputs,
        "biases": setup.biases,
        "weights": setup.weights,
    }


@router.post("/", summary="update_neuro_net")
async def update_neuro_net(inputs: int, outputs: int, layers: int):
    """
    Update the neural network configuration.
    """
    setup = Dynamic_Simple_NN(inputs=inputs, outputs=outputs, layers=layers)
    return {
        "status": "updated",
        "inputs": setup.inputs,
        "outputs": setup.outputs,
        "layers": setup.layers,
    }
