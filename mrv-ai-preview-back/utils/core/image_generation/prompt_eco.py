# PROMPTS ECO - Sustainable and natural MRV standard

# SMALL BEDROOM ECO
def quarto_pequeno_eco(comodo):
    return f"""
Create a photorealistic 3D image of a small bedroom ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

This room must follow the MRV ECO standard, focusing on sustainability and natural materials:

- Single beds in natural wood or bamboo, with organic cotton bedding (earthy tones, moss green).
- Wardrobes in reforested wood with natural finish, slatted doors.
- Desk in light wood with ergonomic chair in natural fibers.
- Eco-friendly decoration: plants in clay pots, paintings with natural motifs, wooden shelves.
- Walls with ecological paint in earthy tones (sage green, natural beige, light ocher).
- Low-consumption LED lighting, with natural fiber lamp.
- Certified laminate or bamboo flooring, natural fiber rug.
- Curtains in linen or raw cotton.

The environment should convey connection with nature, sustainability and well-being.
"""

# MASTER BEDROOM ECO
def quarto_casal_eco(comodo):
    return f"""
Create a realistic 3D image of a master bedroom ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ECO standard, prioritizing sustainable materials and biophilic design:

- Double bed in natural wood with rattan or bamboo headboard.
- Organic cotton bedding (natural tones: olive green, terracotta, linen).
- Wardrobe in certified wood with venetian or slatted doors.
- Plants in clay pots strategically positioned (fern, pothos, ficus).
- Walls with natural finish (reclaimed wood or mineral paint).
- Curtains in natural fabrics (linen, raw cotton, jute).
- TV panel in reforested wood.
- Maximized natural lighting, natural fiber lamps.
- Flooring in certified wood or bamboo.

The decoration should be harmonious, sustainable and connected with natural elements.
"""

# LIVING ROOM ECO
def sala_eco(comodo):
    return f"""
Create a realistic 3D image of an integrated living and dining room ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The decoration must follow the MRV ECO standard, focusing on sustainability and biophilia:

- Sofa in natural fabric (linen, cotton) or ecological leather, natural fiber cushions.
- TV rack/panel in reforested wood with natural finish.
- Dining table in solid wood with rattan or bamboo chairs.
- Natural fiber rug (jute, sisal, cotton).
- Abundant plants: palm trees, monstera, peace lily, vertical garden.
- Walls with ecological finish: mineral paint, reclaimed wood or exposed brick.
- Low-consumption LED lighting, natural fiber pendants.
- Flooring in certified wood, bamboo or ecological burned cement.
- Decoration with natural elements: straw baskets, clay pots, fiber paintings.

The environment should be welcoming, sustainable and integrated with nature.
"""

# PRIVATE AREA ECO
def area_privativa_eco(comodo):
    return f"""
Create a photorealistic 3D image of a private outdoor area ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located outside the apartment, following the MRV ECO standard.

Sustainable and natural characteristics:

- Deck in reforested wood or bamboo.
- Vertical garden with native plants and aromatic herbs.
- Table and chairs in certified wood or bamboo.
- Rainwater collection systems (decorative small reservoirs).
- Compact composter integrated into landscaping.
- Native plants in clay or wood pots.
- Solar LED lighting to save energy.
- Permeable floor or natural grass, avoiding waterproofing.
- Recycled water fountain or water mirror for microclimate.
- Sustainable decorative elements: reclaimed wood benches, recycled pots.

The environment should promote well-being, sustainability and connection with nature.
"""

# BATHROOM ECO
def banheiro_eco(comodo):
    return f"""
Create a photorealistic 3D image of a bathroom ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ECO standard, focusing on sustainability:

- Toilet with dual-flush tank (water savings).
- Sink with countertop in certified wood or natural stone.
- Shower with water recovery system and economical valve.
- Finish in recycled glass tiles or ecological ceramic.
- Flooring in certified wood (dry area) and ecological porcelain (wet area).
- Mirror with frame in reforested wood.
- Natural LED lighting, with motion sensor.
- Air-purifying plants (snake plant, peace lily).
- Bamboo accessories: towel rack, soap dispenser, laundry basket.
- Organic cotton towels, ecological cleaning products.

The environment must be functional, sustainable and with optimized air quality.
"""

# KITCHEN ECO
def cozinha_eco(comodo):
    return f"""
Create a photorealistic 3D image of a kitchen ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ECO standard, prioritizing sustainability:

- Cabinets in reforested wood with natural finish.
- Countertop in natural stone (dark granite) or certified wood.
- Energy Star appliances (efficient refrigerator, stove, microwave).
- Stainless steel sink with aerated faucet for water savings.
- Finish in recycled glass tiles or ecological tiles.
- Flooring in certified wood or sustainable porcelain.
- Vertical herb garden (basil, parsley, mint).
- Low-consumption LED lighting, with maximized natural light.
- Compact composter for organic waste.
- Sustainable utensils: bamboo, stainless steel, reusable glass.

The environment must be functional, sustainable and promote healthy eating.
"""

# GENERIC ECO
def generico_eco(comodo):
    return f"""
Create a generic 3D image ECO for the room '{comodo['nome']}' with dimensions {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

Sustainable decoration in MRV ECO standard:
- Furniture in certified wood or bamboo
- Natural colors (earth tones, moss green, ocher)
- Native and air-purifying plants
- Low-consumption LED lighting
- Recycled and natural materials
- Environment integrated with nature
"""

# LAUNDRY ECO
def lavanderia_eco(comodo):
    return f"""
Create a photorealistic 3D image of a laundry room ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ECO standard, focusing on sustainability and efficiency:

- Washing machine and dryer side by side or stacked, with Energy Star rating (low consumption).
- Utility sink with countertop in certified wood or natural stone.
- Wall-mounted cabinets in reforested wood for detergents and ecological cleaning products.
- Retractable clothesline or wooden/bamboo drying rack on the wall.
- Finish in recycled glass tiles or ecological ceramic, easy to clean.
- Flooring in certified wood or sustainable porcelain.
- Low-consumption LED lighting with motion sensor.
- Sustainable organization: straw baskets, wooden hangers, bamboo shelves.
- Compact composter for organic waste (optional).
- Air-purifying plants (snake plant, peace lily).

The environment must be functional, sustainable and promote ecological laundry practices.
"""

# OFFICE ECO
def escritorio_eco(comodo):
    return f"""
Create a photorealistic 3D image of a home office ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

This room must follow the MRV ECO standard, prioritizing sustainable materials and well-being:

- Desk in certified wood or bamboo, with organizing drawers.
- Ergonomic chair in natural fibers or wood with organic fabric upholstery.
- Wall-mounted shelves in reforested wood for books and files.
- Desk lamp in natural fiber or wood, with low-consumption LED.
- Walls with ecological paint or natural finish (reclaimed wood, mineral paint).
- Flooring in certified wood or bamboo.
- Maximized natural lighting, curtains in linen or raw cotton.
- Air-purifying plants: fern, pothos, snake plant.
- Eco-friendly decoration: paintings with natural motifs, clay pots, straw baskets.
- Sustainable organization: recycled cardboard boxes, paper folders.

The environment should convey connection with nature, sustainability and productivity.
"""

# CLOSET ECO
def closet_eco(comodo):
    return f"""
Create a photorealistic 3D image of a walk-in closet ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ECO standard, with sustainable organization:

- Built-in wardrobes in certified wood or bamboo, with venetian or slatted doors.
- Hanging rods at different heights for clothes, in wood or recycled metal.
- Shelves for folded clothes and accessories, in natural wood.
- Simple drawers in certified wood for small items.
- Low-consumption LED lighting under shelves or central.
- Flooring in certified wood or bamboo.
- Simple mirror with frame in reforested wood.
- Sustainable organization: wooden hangers, recycled cardboard boxes, straw baskets.
- Air-purifying plants (snake plant, peace lily) in clay pots.

The environment must be functional and organized, maximizing space with sustainable materials.
"""

# SUITE ECO
def suite_eco(comodo):
    return f"""
Create a realistic 3D image of a suite ECO (master bedroom with private bathroom) with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ECO standard, prioritizing sustainable materials and biophilic design:

- Double bed in natural wood with rattan or bamboo headboard.
- Organic cotton bedding (natural tones: olive green, terracotta, linen).
- Wardrobe in certified wood with venetian or slatted doors.
- Private bathroom access visible or integrated.
- Plants in clay pots strategically positioned (fern, pothos, ficus).
- Walls with natural finish (reclaimed wood or mineral paint).
- Curtains in natural fabrics (linen, raw cotton, jute).
- TV panel in reforested wood.
- Maximized natural lighting, natural fiber lamps.
- Flooring in certified wood or bamboo.

The decoration should be harmonious, sustainable and connected with natural elements, with the convenience of an ecological private bathroom.
"""

# HALLWAY ECO
def corredor_eco(comodo):
    return f"""
Create a photorealistic 3D image of a hallway ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The environment must follow the MRV ECO standard, focusing on circulation and sustainability:

- Walls with ecological paint in natural tones (sage green, natural beige, light ocher).
- Low-consumption LED lighting (sconces or LED strips) with motion sensor.
- Flooring in certified wood, bamboo or sustainable porcelain.
- Minimalist decoration: paintings with natural motifs, simple mirror, small wooden shelf.
- Functional elements: wooden coat hooks, small console table (if space allows).
- Hanging plants or in clay pots: fern, pothos, snake plant.
- Clean and uncluttered appearance, prioritizing circulation flow.
- Natural lighting from adjacent rooms or windows, if available.

The environment should be functional and welcoming, facilitating movement between rooms with natural elements.
"""

# ENTRANCE HALL ECO
def hall_eco(comodo):
    return f"""
Create a photorealistic 3D image of an entrance hall ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The environment must follow the MRV ECO standard, focusing on functionality and sustainable welcome:

- Console table or simple bench in certified wood or bamboo.
- Mirror above the table, with frame in reforested wood.
- Coat hooks or small wooden coat rack for outerwear.
- Walls with ecological paint or natural finish (reclaimed wood, mineral paint).
- Flooring in certified wood, bamboo or sustainable porcelain.
- Low-consumption LED lighting with motion sensor (central fixture or sconces).
- Eco-friendly decoration: small plant in clay pot, painting with natural motifs, wooden key holder.
- Shoe storage: simple wooden rack or small cabinet in certified wood.
- Natural fiber rug (jute, sisal).

The environment should be functional and welcoming, creating a sustainable first impression integrated with nature.
"""

# BALCONY ECO
def sacada_eco(comodo):
    return f"""
Create a photorealistic 3D image of a balcony ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The environment must follow the MRV ECO standard, focusing on sustainability and connection with nature:

- Table and chairs in certified wood or bamboo, weather-resistant.
- Pots with native plants and aromatic herbs (basil, parsley, mint).
- Permeable floor or deck in reforested wood.
- Railing in recycled aluminum with tempered glass.
- Solar LED lighting to save energy.
- Outdoor curtain in natural fabric (linen, raw cotton) or bamboo blind.
- Sustainable decorative elements: reclaimed wood benches, recycled pots.
- Small vertical garden with native plants (optional).
- Decorative rainwater collection system (optional).

The environment should promote well-being, sustainability and connection with nature, ideal for outdoor relaxation.
"""

# GOURMET AREA ECO
def area_gourmet_eco(comodo):
    return f"""
Create a photorealistic 3D image of a gourmet area ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ECO standard, with sustainable barbecue and dining area:

- Simple barbecue or integrated barbecue in basic and sustainable finish.
- Counter or preparation table in natural stone or certified wood.
- Dining table for 4 to 6 people, in certified solid wood.
- Chairs in rattan, bamboo or certified wood, weather-resistant.
- Basic storage: simple cabinet in reforested wood for utensils.
- Flooring in certified wood, bamboo or sustainable porcelain.
- Low-consumption LED lighting (sconces or spots) with motion sensor.
- Sustainable decoration: plants in clay pots, straw baskets, natural elements.
- Vertical herb garden (basil, parsley, mint).
- Compact composter integrated into landscaping (optional).

The environment must be functional and sustainable, ideal for outdoor cooking and dining, maintaining MRV's ecological standard.
"""

# HOME OFFICE ECO
def home_office_eco(comodo):
    return f"""
Create a photorealistic 3D image of a home office ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

This room must follow the MRV ECO standard, prioritizing sustainable materials and well-being:

- Desk in certified wood or bamboo, with organizing drawers.
- Ergonomic chair in natural fibers or wood with organic fabric upholstery.
- Wall-mounted shelves in reforested wood for books, files and office supplies.
- Desk lamp in natural fiber or wood, with low-consumption LED.
- Walls with ecological paint or natural finish (reclaimed wood, mineral paint).
- Flooring in certified wood or bamboo.
- Maximized natural lighting, curtains in linen or raw cotton.
- Air-purifying plants: fern, pothos, snake plant, peace lily.
- Eco-friendly decoration: paintings with natural motifs, clay pots, straw baskets.
- Sustainable organization: recycled cardboard boxes, paper folders, wooden whiteboard.

The environment should convey connection with nature, sustainability and productivity, ideal for remote work or study.
"""

# BALCONY/VARANDA ECO
def varanda_eco(comodo):
    return f"""
Create a photorealistic 3D image of a balcony ECO with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The environment must follow the MRV ECO standard, focusing on sustainability and connection with nature:

- Table and chairs in certified wood or bamboo, weather-resistant.
- Pots with native plants and aromatic herbs (basil, parsley, mint, rosemary).
- Permeable floor or deck in reforested wood.
- Railing in recycled aluminum with tempered glass.
- Solar LED lighting to save energy.
- Outdoor curtain in natural fabric (linen, raw cotton) or bamboo blind.
- Sustainable decorative elements: reclaimed wood benches, recycled pots, straw baskets.
- Small vertical garden with native plants (optional).
- Decorative rainwater collection system (optional).

The environment should promote well-being, sustainability and connection with nature, ideal for outdoor relaxation maintaining MRV's ecological standard.
"""