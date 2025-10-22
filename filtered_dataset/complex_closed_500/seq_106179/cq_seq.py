import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00329, 0.00376).lineTo(0.07671, 0.07376).lineTo(0.08329, 0.06624).lineTo(0.00329, -0.00376).lineTo(-0.00329, 0.00376).close()
solid=wp_sketch0.add(loop0).extrude(-0.05256237840663725)
