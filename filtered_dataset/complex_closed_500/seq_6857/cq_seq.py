import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0025, 0.07896).lineTo(0.0025, 0.07896).lineTo(0.0025, 0.08396).lineTo(-0.0025, 0.08396).lineTo(-0.0025, 0.07896).close()
solid=wp_sketch0.add(loop0).extrude(-0.00046925379642987196)
