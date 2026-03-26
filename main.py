from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Engineering Calculator API is running!"}


# 1. Beam reaction calculator
@app.get("/beam-reaction")
def calculate_beam_reaction(load: float):
    if load < 0:
        raise HTTPException(status_code=400, detail="Load must be a positive value.")
    reaction = load / 2  # Simplified assumption for a simply supported beam
    
    return {
        "load": load,
        "reaction_per_support": reaction
    }
# 2. Stress calculator
@app.get("/stress")
def calculate_stress(force: float, area: float):
    if area <= 0:
        raise HTTPException(status_code=400, detail="Area must be greater than zero.")
    
    stress = force / area
    
    return {
        "force": force,
        "area": area,
        "stress": stress,
        "units": "N/m^2"
    }
# 3. Unit converter (kN to N)
@app.get("/convert-kN-to-N")
def convert_kN_to_N(kN: float):
    if kN < 0:
        raise HTTPException(status_code=400, detail="Kilonewtons must be a positive value.")
    return {
        "kilonewtons": kN,
        "newtons": kN * 1000
    }
# 4. Bending moment calculator
@app.get("/bending-moment")
def calculate_bending_moment(load: float, length: float):
    if length <= 0:
        raise HTTPException(status_code=400, detail="Length must be greater than zero.")
    if load < 0:
        raise HTTPException(status_code=400, detail="Load must be a positive value.")
    bending_moment = (load * length) / 4  # Simplified assumption for a simply supported beam with a central point load
    return {
        "load": load,
        "length": length,
        "bending_moment": bending_moment
    }